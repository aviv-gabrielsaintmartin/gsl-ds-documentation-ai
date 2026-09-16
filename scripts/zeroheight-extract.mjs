/**
 * Extract one Zeroheight component page into blocks + local images.
 *
 * Usage:  node scripts/zeroheight-extract.mjs <page-url> <out-dir>
 *
 * Why a browser at all: the page is client-rendered, so curl returns an empty
 * shell. Why scrolling: images load only once they enter the viewport, and the
 * page scrolls inside `.page--wrapper`, not the window — scrolling the window
 * silently yields a page with two images on it.
 *
 * Everything is scoped to the editor content container, so nav logos, sidebar
 * thumbnails and the styleguide's own chrome never reach the output.
 *
 * Writes <out-dir>/blocks.json and <out-dir>/images/<hash>.png, and prints a
 * count of what it found against what it saved. Never writes into components/.
 *
 * Needs puppeteer-core and a local Chrome. See scripts/README.md.
 */
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';

const require_ = createRequire(import.meta.url);
const puppeteer = require_('puppeteer-core');

const CHROME = process.env.CHROME_PATH
  || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const [url, outDir] = process.argv.slice(2);
if (!url || !outDir) {
  console.error('usage: node scripts/zeroheight-extract.mjs <page-url> <out-dir>');
  process.exit(2);
}

const CONTENT = '[class*="EditorContentStyled"]';
const SCROLLER = '.page--wrapper';

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: 'new',
  args: ['--no-sandbox', '--disable-gpu'],
});
const page = await browser.newPage();
await page.setViewport({ width: 1600, height: 1200 });
await page.goto(url, { waitUntil: 'networkidle2', timeout: 120000 });

// Scroll the real scroll container to the bottom, so every lazy image loads.
for (let i = 0; i < 500; i++) {
  const atEnd = await page.evaluate((sel) => {
    const el = document.querySelector(sel) || document.scrollingElement;
    el.scrollTop += el.clientHeight * 0.7;
    return el.scrollTop + el.clientHeight >= el.scrollHeight - 5;
  }, SCROLLER);
  await new Promise((r) => setTimeout(r, 300));
  if (atEnd) break;
}
await new Promise((r) => setTimeout(r, 3000));

const result = await page.evaluate((contentSel) => {
  // The page carries two content containers: a short intro, then the body.
  // Walk both, in document order — taking only the first loses the whole doc.
  const roots = [...document.querySelectorAll(contentSel)];
  if (!roots.length) return { error: 'content container not found' };

  const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
  const hashOf = (u) => (u || '').split('?')[0].split('/').pop();

  const imageOf = (img) => ({
    hash: hashOf(img.currentSrc || img.src),
    url: img.currentSrc || img.src,
    name: clean(img.getAttribute('alt')),
  });

  const linksIn = (el) => [...el.querySelectorAll('a[href]')]
    .map((a) => ({ text: clean(a.textContent), href: a.href }))
    .filter((l) => l.text);

  const blocks = [];
  const seen = new Set();

  const walk = (node) => {
    if (node.nodeType !== 1 || seen.has(node)) return;
    const cls = (node.className || '').toString();
    const tag = node.tagName.toLowerCase();

    // A gallery of design uploads: each item carries its own name.
    if (cls.includes('sketch-block-view') || node.dataset.testid === 'design-uploads-block') {
      const items = [...node.querySelectorAll('[data-testid="design-upload-item"]')]
        .map((it) => {
          const img = it.querySelector('img');
          if (!img) return null;
          const named = it.querySelector('[data-testid="design-upload-item-name"]');
          const o = imageOf(img);
          if (named && clean(named.textContent)) o.name = clean(named.textContent);
          return o;
        }).filter(Boolean);
      if (items.length) blocks.push({ type: 'gallery', items });
      node.querySelectorAll('*').forEach((d) => seen.add(d));
      seen.add(node);
      return;
    }

    // A do/don't block. Its container alternates image section, text section —
    // the label ("Do", "Don't", "Caution") and the caption live in the text
    // section that FOLLOWS each image, never inside the image's own box.
    if (cls.includes('DosAndDonts') || node.dataset.testid === 'dos-and-donts-block') {
      const container = node.querySelector('[class*="DosAndDontsContainerStyled"]') || node;
      const items = [];
      const kids = [...container.children];
      kids.forEach((kid, i) => {
        const kcls = (kid.className || '').toString();
        if (!kcls.includes('ImageSection')) return;
        const img = kid.querySelector('img');
        if (!img) return;
        const text = kids.slice(i + 1).find((k) =>
          (k.className || '').toString().includes('TextSection'));
        const desc = text && text.querySelector('[class*="Description"]');
        let label = '';
        if (text) {
          const first = [...text.children].find((c) => clean(c.textContent));
          label = first && first !== desc ? clean(first.textContent) : '';
        }
        items.push({ ...imageOf(img), label, caption: clean(desc && desc.textContent) });
      });
      if (items.length) blocks.push({ type: 'dosdonts', items });
      node.querySelectorAll('*').forEach((d) => seen.add(d));
      seen.add(node);
      return;
    }

    if (tag === 'table') {
      const rows = [...node.querySelectorAll('tr')].map((tr) =>
        [...tr.querySelectorAll('td,th')].map((td) => {
          const img = td.querySelector('img');
          return {
            text: clean(td.textContent),
            links: linksIn(td),
            image: img ? imageOf(img) : null,
          };
        }));
      if (rows.length) blocks.push({ type: 'table', rows });
      node.querySelectorAll('*').forEach((d) => seen.add(d));
      seen.add(node);
      return;
    }

    if (/^h[1-6]$/.test(tag) || cls.includes('zheditor-heading')) {
      const level = /^h([1-6])$/.test(tag) ? Number(tag[1]) : 3;
      const text = clean(node.textContent);
      if (text) blocks.push({ type: 'heading', level, text });
      node.querySelectorAll('*').forEach((d) => seen.add(d));
      seen.add(node);
      return;
    }

    if (tag === 'img') {
      blocks.push({ type: 'image', ...imageOf(node) });
      seen.add(node);
      return;
    }

    if (tag === 'li') {
      const text = clean(node.textContent);
      if (text) blocks.push({ type: 'listitem', text, links: linksIn(node) });
      node.querySelectorAll('*').forEach((d) => seen.add(d));
      seen.add(node);
      return;
    }

    if (tag === 'hr') { blocks.push({ type: 'rule' }); seen.add(node); return; }

    if (tag === 'p' || cls.includes('zheditor-p')) {
      const img = node.querySelector('img');
      if (img) { blocks.push({ type: 'image', ...imageOf(img) }); }
      const text = clean(node.textContent);
      if (text) blocks.push({ type: 'paragraph', text, links: linksIn(node) });
      node.querySelectorAll('*').forEach((d) => seen.add(d));
      seen.add(node);
      return;
    }

    [...node.children].forEach(walk);
  };

  roots.forEach((root) => [...root.children].forEach(walk));

  // Every image inside the content area, so the writer can prove none was lost.
  const all = roots.flatMap((root) => [...root.querySelectorAll('img')])
    .map(imageOf)
    .filter((i) => /zeroheight-uploads|\/uploads\//.test(i.url));

  return { blocks, allImages: all, title: clean(document.title) };
}, CONTENT);

await browser.close();

if (result.error) { console.error(result.error); process.exit(1); }

fs.mkdirSync(path.join(outDir, 'images'), { recursive: true });

// Download every content image, keyed by its hash — the filename this repo uses.
const wanted = new Map();
for (const i of result.allImages) wanted.set(i.hash, i);
for (const b of result.blocks) {
  for (const i of (b.items || [])) wanted.set(i.hash, i);
  if (b.type === 'image') wanted.set(b.hash, b);
  for (const row of (b.rows || [])) for (const c of row) if (c.image) wanted.set(c.image.hash, c.image);
}

let saved = 0, failed = [];
for (const [hash, img] of wanted) {
  const file = path.join(outDir, 'images', hash.endsWith('.png') ? hash : `${hash}.png`);
  try {
    const res = await fetch(img.url);
    if (!res.ok) { failed.push(`${hash} HTTP ${res.status}`); continue; }
    fs.writeFileSync(file, Buffer.from(await res.arrayBuffer()));
    saved++;
  } catch (e) { failed.push(`${hash} ${e.message}`); }
}

fs.writeFileSync(path.join(outDir, 'blocks.json'),
  JSON.stringify({ url, title: result.title, blocks: result.blocks }, null, 1));

const counts = {};
for (const b of result.blocks) counts[b.type] = (counts[b.type] || 0) + 1;
console.log(`blocks: ${result.blocks.length}`, counts);
console.log(`images found: ${wanted.size} | downloaded: ${saved} | failed: ${failed.length}`);
if (failed.length) { console.log('FAILED:'); failed.forEach((f) => console.log('  ' + f)); process.exitCode = 1; }
