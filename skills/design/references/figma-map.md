<!-- Generated from `figma/*.json` on 2026-10-06 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

# Figma names and keys

Joins each design-system name a spec uses to the Figma key that places it. Generated from the `figma/*.json` registries.

**This file never decides which component or token to use.** `components-rules-ai.md` and the token rulesets decide that. This file only finds, in Figma, a name that was already chosen.

**The spec keeps the design-system name.** A key or a node ID never appears in a spec.

## Libraries

| Tier | Figma library name |
| --- | --- |
| foundations | `0. GSL Foundations Library` |
| components | `2. GSL Components Library` |
| patterns | `3. GSL Patterns Library` |
| experiences | `4. GSL Experiences Library` |

## How to read a key

| Kind | What the key is | How to import it |
| --- | --- | --- |
| Component with variants | The **component set** key | `figma.importComponentSetByKeyAsync(key)`, then pick the variant. If it throws *not found*, try `figma.importComponentByKeyAsync(key)` — the key is then a single component |
| Icon | The **component set** key. **Proved 14 September 2026**: `importComponentByKeyAsync` throws *not found* on these keys | `figma.importComponentSetByKeyAsync(key)` |
| Colour, spacing, radius, border width | A **variable** key | `figma.variables.importVariableByKeyAsync(key)`, then bind it |
| Text style, shadow | A **style** key | `figma.importStyleByKeyAsync(key)` |

## Components

**Pattern 2** means the component has an exposed inner slot. Set the slot's own properties on the nested instance, found by its main component key in **Exposed slots** — never through the parent's properties.

| Name | Library | Key | Node ID | Pattern | Variants |
| --- | --- | --- | --- | --- | --- |
| `Accordion` | components | `12bad17c5323ed7d55361e6e9a7d159dcd1179d5` | `11:136048` | Pattern 1 | 16 |
| `Action Menu` | components | `598c5fcb9e0f4d78a5de1d9806eb2f24505564a5` | `2305:32561` | Pattern 2 | 2 |
| `Alert` | components | `6fe94d63e6cfed7576d199dedf7823f55c04b368` | — | Pattern 1 | 3 |
| `Autocomplete` | components | `b6e4071d5ce0ee97677d54e7b2e9b16afcbbb31d` | `2305:20096` | Pattern 2 | 24 |
| `Avatar` | components | `dcc57df93537a70ccc49221904d31bac911fdcc8` | `11:146259` | Pattern 1 | 103 |
| `Badge` | components | `ac3a83569347cde8300494ded82054462631b717` | — | Pattern 1 | 28 |
| `Badge Store` | components | `6b982317e899bc992539ae6872cd4d5762b20898` | — | Pattern 1 | 24 |
| `Brand Logo` | components | `c2dc9ceeed9f550a1bbed6f3cdc223c8eed103c4` | — | Pattern 1 | 136 |
| `Button` | components | `97d227b9a0714f73ddf4679c1354f5430437b7e6` | — | Pattern 1 | 828 |
| `Button Bar` | components | `5c33d2af24a9dbde936a50062d17071f29d8dba7` | — | Pattern 1 | 12 |
| `Button Card` | components | `2506f62749f9b4d09a216c1747a840bb61dee025` | — | Pattern 1 | 8 |
| `Button Card Group` | components | `df93c1020e8504e5cd6d0e54b528cac9b0d5aeaa` | — | Pattern 1 | 2 |
| `Button Group` | components | `d8f3e47638fc1b4641ec2b86596dd1abbb8557ee` | `11:9567` | Pattern 2 | 8 |
| `Card` | components | `cc742e4501a43a1d2a414295a816dbbd5ae7a55d` | `11:154743` | Pattern 2 | 12 |
| `Carousel` | components | `25b22c21b862d6d200032566aff03af0d848f63f` | — | Pattern 1 | 48 |
| `Cell Content` | components | `71b1f5176db52eb12c7744a0df8c4096655ac6f4` | `18359:17763` | Pattern 2 | 33 |
| `Checkbox` | components | `d492baa47ceea8f55da76b1d87b24cae798b4ca6` | — | Pattern 1 | 144 |
| `Checkbox Group` | components | `ccf4d111c1474025d9db50029bbb674ae29e51ea` | `12217:2024` | Pattern 2 | 2 |
| `Chip` | components | `17017457df5974938d57279d546c130c35785f5b` | `11:10848` | Pattern 1 | 15 |
| `Chip Group` | components | `0bc58367303e8375707c680133043f5ce5e601cc` | `11:10915` | Pattern 1 | 3 |
| `Coachmark` | components | `d1274e9f9474365783926ee5330e10f93b96a1af` | `13450:129981` | Pattern 2 | 12 |
| `Content Placeholder` | components | `08ba36d263c9777d4616a752d6e9a90f3ccae666` | `11:178535` | Pattern 1 | 1 |
| `Counter Field` | components | `ba7744261bff406e4d223b44520be3c22653b476` | — | Pattern 1 | 6 |
| `Divider` | components | `4686de8c81968ab25756ab8579b639f27d2741ba` | — | — | — |
| `Dropdown` | components | `a5f4fb28f1a8011a07b7594d08fee6c8f06830d7` | — | Pattern 1 | 48 |
| `Energy Tag` | components | `0e8d81cb86d1bcfd8958ceb7e4b8a307f72b63c6` | — | Pattern 1 | 48 |
| `Feedback Messages` | components | `2d943c51f0e7a4268e8c71cf883d175b4020051d` | — | Pattern 1 | 48 |
| `Feedback Thumb Buttons` | components | `decb36a7b8253a10d39ff95d6b1fb219c248e45f` | — | Pattern 1 | 2 |
| `Floating Button Group` | components | `0a2029ea677294b495b29cce28aa05b486a8dbd5` | `10515:15403` | Pattern 2 | 4 |
| `Home Indicator` | components | `e1504d5c1604c910b2634885863052b0110b3497` | `11:219584` | Pattern 1 | 2 |
| `Image Ratio` | components | `62e174674262222335bd7a283d84f3562373e686` | — | Pattern 1 | 11 |
| `Image Slider` | components | `03574118c855a279e89ce1058e78c2f4fc3a20ef` | `11:180906` | Pattern 2 | 56 |
| `Link` | components | `098d8d7a3716325411b867819f11cf9516e99bdb` | — | Pattern 1 | 32 |
| `Loading State` | components | `16200c0f1ec608b4d98156b737247c6b25b4364b` | `11:118473` | Pattern 2 | 4 |
| `Modal Bottom Sheet` | components | `0a89fa775a98ad098bd0f3fb7c3909d98eb8b53b` | `11:88040` | Pattern 2 | 21 |
| `Modal Bottom Sheet Menu` | components | `187aaabd41d7dd86c92f64a4a4c9a96ea2cf9661` | — | Pattern 1 | 3 |
| `Navigation Bar (App)` | components | `9f1d1113ba20d149f079e9bdf448e3342f6f77ba` | `11:75015` | Pattern 2 | 18 |
| `Pagination` | components | `c966f537d3d1078c6b56ae334ab4b8787ed222ff` | — | Pattern 1 | 6 |
| `Pop-up` | components | `0f5f4bb87d371a7645657384a67790759ea9c080` | — | Pattern 1 | 12 |
| `Programmatic Ads` | components | `07d79452fda22931da85fd5bfbe7c55e83e81a46` | — | Pattern 1 | 7 |
| `Progress Bar` | components | `f2cfae994502792dc220e9eb7c3239e0447a3e71` | — | — | — |
| `Progress Circle` | components | `bbd8122bd86b0374ffe71a971a9412fe424bedec` | — | Pattern 1 | 6 |
| `Radio Button Group` | components | `e751c0a41ef12cb59856926f1541dda87aa65473` | `11:49124` | Pattern 2 | 2 |
| `Rating` | components | `b55038542f08df6aa93e710627169d826063fca7` | `11:182570` | Pattern 2 | 4 |
| `Score Tag` | components | `538501c2e78d510683508ab5dc7ba42fd67ae83f` | — | Pattern 1 | 4 |
| `Segmented Control` | components | `9bcb3d3bd94a59c955ecdf32eb33254e019b52f5` | — | Pattern 1 | 2 |
| `Select Card Group` | components | `763f4df3a87828c0b7d30c5f42fe4410da9ff4db` | `11:50242` | Pattern 2 | 28 |
| `Slider` | components | `3fcda02d3b65e7e89bad1946253166b9fc2f3cb5` | `11083:4586` | Pattern 2 | 18 |
| `Snackbar` | components | `4cde9dbb04d9a342757faf991ad4f4c45111191e` | — | Pattern 1 | 24 |
| `State Message` | components | `7c94cec95f0a93ea9e2b5a0b2affd963bcf7b189` | — | Pattern 1 | 5 |
| `Status Bar` | components | `7a7c90730cc1928f21d4746ee959d03cab7d8691` | `13894:42307` | Pattern 1 | 7 |
| `Tab Bar` | components | `29ac52250ffa7869a62d1676c325d2a6253b0a68` | `13608:2423` | — | 3 |
| `Tabs` | components | `858ec7e6439fc613f65335a73673b35642871d8c` | `11:70520` | Pattern 2 | 6 |
| `Tag` | components | `09014a9e7e7dd6c36ea324ddd2a3fb33352f6cbb` | — | Pattern 1 | 28 |
| `Text Area` | components | `e7eb3dae754a4c1d58a1ba4664caf40d336a631d` | `11:58267` | Pattern 2 | 32 |
| `Text Button` | components | `4c5f262e38bee4fcb987e6ecba58ddc3c9ae4907` | — | Pattern 1 | 168 |
| `Text Field` | components | `f1c414ce0cf481118654da95ac073a068ad64a52` | — | Pattern 1 | 32 |
| `Toggle` | components | `519ddc073a8e4915f0ff15bbf91e540cda569d0a` | `13721:45244` | Pattern 2 | 6 |
| `Toggle Group` | components | `647bbde284358907b5d86fed222002ce2b8b7815` | `13721:44144` | — | — |
| `Tooltip` | components | `676c5edfb96b9595c8e7a4f8d6c1c850dc964c03` | — | Pattern 1 | 12 |
| `Webview` | components | `30acfbc11ab09d96732738747d478cf72c023185` | — | Pattern 1 | 7 |
| `Bar graph` | patterns | `804bf697ee740b385a530af149c8399ae5d980b9` | `2782:7613` | Pattern 2 | 2 |
| `Breadcrumb` | patterns | `09c6f2f0f7e42eb813530c544578f940f7692800` | `20:79283` | Pattern 1 | 3 |
| `Burger menu` | patterns | `1441ae904fca5422489654112cf2eae951511ac6` | `2213:93218` | Pattern 1 | 4 |
| `Burger menu (profil)` | patterns | `14e3da3a77641ad18114325386e3a264526c0a21` | `2213:94048` | Pattern 1 | 4 |
| `Date Field` | patterns | `97765b8a2b46548f2e6c04396aa81b060674faba` | `2893:66432` | Pattern 1 | 32 |
| `Date Picker` | patterns | `f41432798da2e1317d65b412e8a9bc29cbf8e4a8` | `2893:66973` | Pattern 1 | 5 |
| `Donut chart` | patterns | `1e38854162ca35f39c5c905e74cbc861e98f978f` | `2782:13319` | Pattern 2 | 1 |
| `Feedback Bar` | patterns | `0c888b5591b12a8d39ae7a0a42e664df7fae3689` | `21:31125` | Pattern 2 | 4 |
| `Filter bar` | patterns | `f0c6967f99c19d0ccd04f9f7794e519b732c4daf` | `2240:119077` | Pattern 2 | 8 |
| `Filter button` | patterns | `ff5f98edefbd2933e0b2da3335158a03ebc63b2a` | `2240:119093` | Pattern 1 | 96 |
| `Filter dropdown container` | patterns | `b70401e806bf4ccdf4a09173ff6fc97f05a26175` | `2867:982` | Pattern 1 | 1 |
| `Footer` | patterns | `69882bc9ec9270cec2eb046c8be4ddb7a5585be3` | `20:100245` | Pattern 1 | 30 |
| `Info State` | patterns | `239da48acaf21a51157d2e25657e0b5397cc9d27` | `2240:119466` | Pattern 2 | 3 |
| `KPI` | patterns | `16e4d980776106384ed729c205b0d697ac3227ee` | `2782:15102` | Pattern 2 | 2 |
| `Line chart` | patterns | `d27843e26ea7b70a46f91b9881e50f0de672bdfb` | `4546:54628` | Pattern 2 | 1 |
| `Media Upload` | patterns | `d77fc0f7c3b61b9e0447bca80f8fdfdedc223d39` | `20:40224` | Pattern 2 | 41 |
| `Mega menus` | patterns | `1ef51d29de3ebbaa73a3a7a9245c63213316779d` | `20:58328` | Pattern 1 | 96 |
| `Menus` | patterns | `acbd5a28268c0f85727efba97e87685f3e047c51` | `2213:91126` | Pattern 1 | 7 |
| `Navigation bar` | patterns | `30c1505a2842dec214a0784dadf554f53def6acb` | `3138:71933` | Pattern 1 | 1 |
| `Top Bar` | patterns | `9f7041c981cc4f727eb8967bbfad950861c44f30` | `20:110524` | Pattern 2 | 26 |
| `Wizard` | patterns | `db53c9b6a314015cf875fef38f223a0200185445` | `20:114293` | Pattern 2 | 2 |
| `Estimation card` | experiences | `3310e65968e47868187272bd273ad44dee77caee` | `2290:9345` | Pattern 2 | 16 |
| `Floor selection` | experiences | `9d2169bae769953bda3e9468e0f4aa33bdb1ed43` | `2610:13989` | Pattern 1 | 6 |
| `Listing Card` | experiences | `8df4cda2a41c3a4a527f69850ff42228a5d6cf2b` | `5:9439` | Pattern 2 | 79 |
| `Listing summary` | experiences | `b1cd9e88a5bbaf26ed634da16b48b70febd2acb2` | `5:9663` | Pattern 2 | 2 |
| `Map Polygon` | experiences | `8b4224f8d304a24cdd868d5bf5fa3a24ca3cc42f` | `5764:29960` | Pattern 1 | 2 |
| `Map Polygon backdrop` | experiences | `3e3467acafc2d790441901bd225f8136f58d3774` | `5764:30072` | Pattern 1 | 5 |
| `Map template` | experiences | `052a62aaec09c43a06249149772e79f6ac0c693b` | `5747:16555` | Pattern 2 | 27 |
| `Phone Number Field` | experiences | `d4f66a893de558ea18533458cc8983c78373afdc` | `3696:7931` | Pattern 2 | 52 |
| `Table` | experiences | `015ab049385f127e67df93e93e0cbc132dc7648e` | `6978:1218` | Pattern 1 | 12 |
| `mapPinsV2_IWT` | experiences | `8b64dd3ad38e44b082a8f72445a2490d8b54fdc4` | `8664:56808` | Pattern 1 | 162 |
| `mapPinsV2_SL` | experiences | `0dfc1ca2bbfd5bb71a163e0bdcb2f6197ed6f95a` | `8664:56162` | Pattern 1 | 162 |
| `Brand App Icons` | foundations | — | — | — | — |
| `Brand Logo` | foundations | `2655d153bd252a3c88303624379d23607cd06452` | `12021:46184` | Pattern 1 | 136 |
| `Favicon` | foundations | `4af3812b174f7cdcd21d08c3d2efb672753ade79` | `59238:827` | Pattern 1 | — |
| `Flag` | foundations | `8b56249f0c81c1e6f02831769e81c7e4e2e0c0f7` | `56977:25` | Pattern 1 | 11 |
| `Image Ratio` | foundations | `00f0402e71cd2bd1850a3a72aad81e521ec0d4f5` | `8864:28304` | Pattern 1 | 11 |

**Names in The inventory with no Figma key here:** none. Find one of these by name in its library, and report that it had no key.

### Exposed slots

| Parent | Exposed as | Nested component | Nested key |
| --- | --- | --- | --- |
| `Action Menu` | `Button` | `.button_type` | `39ec5df9e09ae20dd0935fd83a63131ed08e53b6` |
| `Action Menu` | `Menu` | `.action_list` | `c39f4b9182537a7aada94b15d086c17d17d6a8c5` |
| `Autocomplete` | `.base_rows` | `.base_rows` | `317e92e3a28d47093cd5870536444f9fb826d5d5` |
| `Autocomplete` | `.base_rows` | `.base_rows` | `d1e675a6bec7050770fc0d38029fc35669a30e96` |
| `Autocomplete` | `Icon Trailing` | `.icon_button` | `a5e460c768eb3fd8e77a1160303d97a80e3adb87` |
| `Autocomplete` | `.base_rows` | `.base_rows` | `8008c96baf4ea548fa15aa6cd499f92773c9665d` |
| `Autocomplete` | `.base_rows` | `.base_rows` | `0d5eed6f923d948802dd874aa05a82a4ac5af2b8` |
| `Button Group` | `1. Button group item`, `2. Button group item`, `3. Button group item`, `4. Button group item`, `5. Button group item`, `6. Button group item`, `7. Button group item`, `8. Button group item`, `9. Button group item` | `.base_button_group` | `610028119393f730e51b26f4157cbbd0d0a37bf7` |
| `Card` | `Content placeholder` | `Content placeholder` | `08ba36d263c9777d4616a752d6e9a90f3ccae666` |
| `Cell Content` | `Placeholder Left` | `.placeholder left` | `d7ba36d47a5c5fe30aed4e528aa89bea3c6407d4` |
| `Checkbox Group` | `Header form` | `.header_form` | `2fd26bdf7fa1968e9a1ad3155f546011e2914095` |
| `Checkbox Group` | `Checkboxes` | `.checkboxes - Vertical` | `f4d13671058cf9ff3ff424095da3e0f8a6c66464` |
| `Checkbox Group` | `Checkboxes` | `.checkboxes - Horizontal` | `11846eb9f1222d6f339e29a9a4676c6ed483489c` |
| `Coachmark` | `.coachmarkContent` | `.coachmarkContent` | `f4c76f4315a71bea094951f31af601e8f8e918b7` |
| `Coachmark` | `.header` | `.header` | `b8f80d92b81a5f56ce921c1c582bddf1a9d7f6b9` |
| `Floating Button Group` | `Floating button group item 1`, `Floating button group item 2`, `Floating button group item 3` | `.base_floating_button_group` | `b9aaa162a6692c74086f1816300cf8a502a3bf11` |
| `Image Slider` | `.views_tags` | `.views_tags` | `5fb0ebae560337353144400237e16cdbede14cf6` |
| `Loading State` | `Spinner` | `.spinner` | `75f1078261365b7cde865570d3258dbf93260f1e` |
| `Loading State` | `Variable tag` | `.Alerts - Tag` | `c84b651f8180623d36117aff529ba67a170779a7` |
| `Loading State` | `Spinner` | `.spinner` | `675ca56b2f71288b3d75ce2ed7ef338b11c3faf3` |
| `Modal Bottom Sheet` | `Content placeholder` | `.content_all platform_default` | `cea39abc78468f5f18d4be24320cc27ecf634f2f` |
| `Modal Bottom Sheet` | `Text Button` | `Text Button` | `4b1fc65d1dbade02183151109b16fb9329609ed1` |
| `Modal Bottom Sheet` | `Content Placeholder` | `.content_phone_fullscreen` | `eb27e8455c2d1fad2e8181aaae8ad6d0f6fe931a` |
| `Modal Bottom Sheet` | `Content Placeholder` | `.content_desktop_fullscreen` | `579c0a3a77a2265b7de29919f7bdb8f3caa22c35` |
| `Modal Bottom Sheet` | `Text Button` | `Text Button` | `d4582c7925ba7246d9a4ec29cc8ffb93f5478330` |
| `Modal Bottom Sheet` | `Content Placeholder` | `.content_tablet_fullscreen` | `90779dd3755ed6b1b0e06788c50e71ce9db4c6bd` |
| `Modal Bottom Sheet` | `Content Placeholder` | `.content_all platform_default` | `c0a4605fa994eebad46f17ffa9710bc9acbc189d` |
| `Navigation Bar (App)` | `.base_tab` | `.base_tab` | `36302a1b4180474b0457d5fd2d92c5df07c9fe80` |
| `Navigation Bar (App)` | `.base_tab` | `.base_tab` | `09a3487ea5ac71493c2a8d21ba9066e0727ce8c7` |
| `Navigation Bar (App)` | `.base_tab` | `.base_tab` | `c12564561fbdefe186deb0f6b8e3ea0ca7f6db70` |
| `Radio Button Group` | `Header form` | `.header_form` | `2fd26bdf7fa1968e9a1ad3155f546011e2914095` |
| `Radio Button Group` | `Radio` | `.radio - Vertical` | `04b9b0c3175e3d113a646cae2e17231e27fc9ca0` |
| `Radio Button Group` | `Radio` | `.Horizontal` | `ed09c6b4a00b3f2b3e07286680d276e7c4e63ed0` |
| `Rating` | `Star 1`, `Star 2`, `Star 3` | `.star` | `65eefa8eb5eb8104299cb451f3b16cd90cba6109` |
| `Rating` | `Star 4` | `.star` | `a1298a5d39ac54eac385c5ca07dcb84fb3e0f9de` |
| `Rating` | `Star 5` | `.star` | `03fb8315fbc5773977c2938de63adc0a7fbed6ed` |
| `Rating` | `.rating` | `.rating` | `214b8968f4fc4026d98ce0b65c7f7f66e90cfea8` |
| `Select Card Group` | `.content select card` | `.content select card` | `a21124e029a2bb1abd7c4f14a28e18cfa163faaa` |
| `Slider` | `.header_slider` | `.header_slider` | `944a1ac9a96992532ff1f19539176626f223ff62` |
| `Slider` | `.header form` | `.header_form` | `10ffb513884b5e0e56cba53a53131f9e50b57e10` |
| `Slider` | `Icon Trailing` | `.icon_button` | `a5e460c768eb3fd8e77a1160303d97a80e3adb87` |
| `Tabs` | `.base_tabs` | `.base_tabs` | `62c072302c8131d0ea5ad4b1fc028d19f008c0e3` |
| `Tabs` | `tab_02`, `tab_01` | `.item_tabs` | `7e2be3e3a260b29971e79170dd52a9dfefa51788` |
| `Tabs` | `tab_03`, `tab_04`, `tab_05`, `tab_06`, `tab_02` | `.item_tabs` | `16393e22861ff0ee7e3489e6db9a0081b731ba63` |
| `Tabs` | `.base_tabs` | `.base_tabs` | `a858a8754112474ce6c414643536d43084e851ab` |
| `Tabs` | `Button` | `.button_type` | `39ec5df9e09ae20dd0935fd83a63131ed08e53b6` |
| `Tabs` | `Menu` | `.action_list` | `c39f4b9182537a7aada94b15d086c17d17d6a8c5` |
| `Text Area` | `Header` | `.header_form` | `2fd26bdf7fa1968e9a1ad3155f546011e2914095` |
| `Text Area` | `.State message + counter` | `.State message + counter` | `4a926312b99553f950cc0bc5fd32bd02a7a581b3` |
| `Toggle` | `.states` | `.states` | `ae1d03a9644dd1b70a359927fb508db0df02863d` |
| `Toggle` | `.side` | `.side` | `ef20341e7bb67ca41ed1bf1b5c7a5b01ce65a0b5` |
| `Toggle` | `.content` | `.content` | `b7bc59fcebeb4a67eb9a4bf7d61f661264ff7bca` |
| `Toggle` | `.toggle` | `.toggle` | `49385c47d52b0ae76838a589a6809c577eb9f813` |
| `Toggle` | `.toggle` | `.toggle` | `83761b2a8e1e6e5aaee3670c4a1d7c874d20eaae` |
| `Toggle` | `.toggle` | `.toggle` | `c2eb7b284011f07982972b3a5306a96d3fe475b4` |
| `Toggle` | `.toggle` | `.toggle` | `ef090bd8efc4fbe68a406c1c444f39c98ced33cf` |
| `Toggle` | `.toggle` | `.toggle` | `9cbdd6a0918503654551d19f3924787a27776ba6` |
| `Toggle` | `.toggle` | `.toggle` | `570c43466a1284925e0a4976f4bc52648ab7d37a` |
| `Bar graph` | `.Header` | `.Header` | `ca3902f3b109f4a4786f9132835806c45a53e042` |
| `Bar graph` | `Filters` | `.filters` | `86191dc25127a3e7f764b8ffb804061f13aeebf4` |
| `Bar graph` | `state_message` | `state_message` | `a2901bf826e653d60ad67c9079424d4b630016d6` |
| `Bar graph` | `.Bar graph vertical` | `.Bar graph vertical` | `776ec1935132f70e3e7ecd9c3945819861c29a1a` |
| `Bar graph` | `.Bar chart horizontal ` | `.Bar chart horizontal ` | `b6adaf3fbffbab977a514a8e00cc048523afe24d` |
| `Donut chart` | `.Header` | `.Header` | `332239b3ca48614e11ac092aec30ac2835435dc0` |
| `Donut chart` | `state_message` | `state_message` | `a2901bf826e653d60ad67c9079424d4b630016d6` |
| `Donut chart` | `.Donut chart` | `.Donut chart` | `c7d73dd441f4b5956be9aea050a80c9b9e7dc7f5` |
| `Feedback Bar` | `.base_button_group` | `.base_button_group` | `ae5436847d1178b6218ddcd92eddd91156be5c13` |
| `Feedback Bar` | `.base_button_group` | `.base_button_group` | `de94fa8f7a9bab4395a5422c641fb0ab629e471c` |
| `Feedback Bar` | `Feedback` | `.vertical_feedback` | `384ce001a7ab17b8c39b373823e5205eeb621d99` |
| `Filter bar` | `filter_01` | `Filter button` | `caa6e85ffc1dcd733432a46d244265d426ead708` |
| `Filter bar` | `filter_02`, `filter_03`, `filter_04`, `filter_05`, `filter_06` | `Filter button` | `06ad2ae997c2d503bff32f7b1f31ac9fd0c357c6` |
| `Filter bar` | `filter_01` | `Filter button` | `385f282b38b843c81dc53271adb20846c1bbf7ef` |
| `Filter bar` | `filter_02`, `filter_03`, `filter_04`, `filter_05`, `filter_06` | `Filter button` | `9266cea7b29ec58688adc09289701c0aa5f3f99c` |
| `Info State` | `.Content` | `.Content` | `e897eeda698213a5799260b247e0970049768393` |
| `KPI` | `state_message` | `state_message` | `a2901bf826e653d60ad67c9079424d4b630016d6` |
| `Line chart` | `Header` | `.Header` | `ca3902f3b109f4a4786f9132835806c45a53e042` |
| `Line chart` | `Filters` | `.filters` | `86191dc25127a3e7f764b8ffb804061f13aeebf4` |
| `Line chart` | `Grid` | `.Grid` | `8eb0fd6e00aa0d474f68547436ec866fabb1865b` |
| `Line chart` | `.Line chart data` | `.Line chart data` | `298246e1c92a16bb15890e75baedc1f1f2ee45b1` |
| `Line chart` | `Legend` | `.Legend` | `c8b3a1d00cbde6dd8516a049097a2d3ae6afaf60` |
| `Media Upload` | `Header` | `.Header form` | `9ce3a0b7e7fcc2dadd9f7cb4da63bfe2802bf5c5` |
| `Media Upload` | `.upload_content` | `.upload_content` | `6905dedb2b59301bf94540cc59a3539aa8b1bc8c` |
| `Media Upload` | `.spinner` | `.spinner` | `17f500baaba19e295fca5796c967293ec0c7ffd7` |
| `Media Upload` | `Floating Button` | `.floating_button` | `154a4df80355d166170d41c211a8f9c667cd92e8` |
| `Top Bar` | `Text Button` | `Text Button` | `d4582c7925ba7246d9a4ec29cc8ffb93f5478330` |
| `Top Bar` | `Text Button` | `Text Button` | `4b1fc65d1dbade02183151109b16fb9329609ed1` |
| `Wizard` | `Top line`, `Bottom line` | `.lineWizard` | `42e5a1d316155fc952bfebebb7a5c2eedcd0c416` |
| `Wizard` | `Bottom line`, `Top line` | `.lineWizard` | `70f5c65f9fb8ffbd28974d513fa349cc377b66f0` |
| `Wizard` | `Bottom line`, `Top line` | `.lineWizard` | `7b4d38b552b84d9191ec1150ccfaf961d8c96c2c` |
| `Wizard` | `Bottom line`, `Top line` | `.lineWizard` | `1ea5c06606aba6c20f9dc2557ecce6a11d619747` |
| `Estimation card` | `Variable tag` | `.Alerts - Tag` | `c525fa12205af7bd64d3652e9acd532a85edb753` |
| `Estimation card` | `.price_range` | `.price_range` | `c4b5ac9c95eb32724df440540dccf0a817b542ff` |
| `Estimation card` | `.confidence_indicator` | `.confidence_indicator` | `acbacf0676b9ce90d650633f26e9c355d9895445` |
| `Estimation card` | `Tabs` | `Tabs` | `a117f1a7e7c8eb2a97233ecd65e377db067b0d62` |
| `Estimation card` | `.base_tabs` | `.base_tabs` | `57fa777316d317e5ab9518c7c9337571b0b3356f` |
| `Estimation card` | `.item_tabs` | `.item_tabs` | `049773c80f1054b86d09fffcb904e5800682cb44` |
| `Estimation card` | `.estimation_details` | `.estimation_details` | `d49a9d02fef420f21d6058793ba989ad6efdef21` |
| `Estimation card` | `.estimation_feedback_module` | `.estimation_feedback_module` | `c3a21fc5b4946f67ef51e36648d87fc2467b00dd` |
| `Listing Card` | `T`, `a`, `g`, `s`, ` `, `l`, `i`, `s`, `t` | `.listing_tags_list` | `8e806e91f54e265e2fee654770236c65dbf2bd94` |
| `Listing Card` | `P`, `r`, `i`, `c`, `e`, ` `, `t`, `a`, `g` | `.listing_price_tag` | `a996befb8fc11dccab52e997e2bda4e91da9cec8` |
| `Listing Card` | `A`, `c`, `t`, `i`, `o`, `n`, `s` | `.listing_actions` | `6335f9d832d9d10440f80c791f0cb12da07ae3dd` |
| `Listing Card` | `T`, `i`, `t`, `l`, `e` | `.listing_title` | `0256e229500b2d3c16f0db3fbf482437ced660f0` |
| `Listing Card` | `P`, `r`, `o`, `p`, `e`, `r`, `t`, `y`, ` `, `f`, `e`, `a`, `t`, `u`, `r`, `e`, `s` | `.listing_property_features` | `7833c95d116e771761fd55c49a072168742b7cf2` |
| `Listing Card` | `P`, `r`, `o`, `p`, `e`, `r`, `t`, `y`, ` `, `l`, `o`, `c`, `a`, `t`, `i`, `o`, `n` | `.listing_property_location` | `d94d85f277b2d50a066743275da4a5e2961eb941` |
| `Listing summary` | `T`, `a`, `g`, `s`, ` `, `l`, `i`, `s`, `t` | `.listing_tags_list` | `8e806e91f54e265e2fee654770236c65dbf2bd94` |
| `Listing summary` | `P`, `r`, `i`, `c`, `e`, ` `, `t`, `a`, `g` | `.listing_price_tag` | `a996befb8fc11dccab52e997e2bda4e91da9cec8` |
| `Listing summary` | `A`, `c`, `t`, `i`, `o`, `n`, `s` | `.listing_actions` | `6335f9d832d9d10440f80c791f0cb12da07ae3dd` |
| `Listing summary` | `T`, `i`, `t`, `l`, `e` | `.listing_title` | `0256e229500b2d3c16f0db3fbf482437ced660f0` |
| `Listing summary` | `P`, `r`, `o`, `p`, `e`, `r`, `t`, `y`, ` `, `f`, `e`, `a`, `t`, `u`, `r`, `e`, `s` | `.listing_property_features` | `7833c95d116e771761fd55c49a072168742b7cf2` |
| `Listing summary` | `P`, `r`, `o`, `p`, `e`, `r`, `t`, `y`, ` `, `l`, `o`, `c`, `a`, `t`, `i`, `o`, `n` | `.listing_property_location` | `d94d85f277b2d50a066743275da4a5e2961eb941` |
| `Listing summary` | `H`, `e`, `l`, `p`, `e`, `r`, ` `, `t`, `e`, `x`, `t` | `.listing_helper_text` | `25b0494e982187d46750ba4aa92db3272f39b9b7` |
| `Listing summary` | `T`, `h`, `u`, `m`, `b`, `n`, `a`, `i`, `l` | `.listing_summary_thumbnail` | — |
| `Map template` | `.Button 1`, `.Button 2` | `❌ .base_floating_button_group (outdated)` | `3b93c2dbc2c84caec586330319d2d74c628ce3c7` |
| `Map template` | `Image Slider placeholder` | `Image Slider` | `9672fc4b24d4516179f66e6f0f1aec8d2f23b0b2` |
| `Map template` | `.views_tags` | `.views_tags` | `5fb0ebae560337353144400237e16cdbede14cf6` |
| `Map template` | `Tags list` | `.listing_tags_list` | `17b3d558f50061ea6a52ed679c191c5e9933a853` |
| `Map template` | `Tag` | `Tag` | `e514a0494aadcb8a83b0810c1f687acbd8974769` |
| `Map template` | `Actions` | `.listing_actions` | `dc01119ec25e7ef5e44e55aaee67a7e9cfaef570` |
| `Map template` | `Property features` | `.listing_property_features` | `411cdbbd586f7bb281863d9602569e9a32ed1227` |
| `Map template` | `Property location` | `.listing_property_location` | `ee2dca7224a92c3b74b2e4c64a2e0143d588fad5` |
| `Phone Number Field` | `.header_form` | `.header_form` | `86d03bf35f009ae492fde88f6580d8649432f592` |
| `Phone Number Field` | `Icon Trailing` | `.icon_button` | `a5e460c768eb3fd8e77a1160303d97a80e3adb87` |

## Tokens

**A colour in a spec may omit the leading `Color/`.** `Content/Default/Default` in a spec is `Color/Content/Default/Default` here. Every other kind is written the same in both.

**Never write a raw value where a token exists.** Bind the variable or apply the style, so a brand or theme switch still works.

### Border Width

_Collection: `1 - Primitive`._

| Figma name | Key |
| --- | --- |
| `Border Width/None` | `a7e549dabf6bd3f14a0e30cdb5a86be42cf1eb4c` |
| `Border Width/1` | `785b62f4706d4656fad3b5dde0967ed4c0520705` |
| `Border Width/2` | `725c8f53e7c43c0266b43190648f0f5869577d85` |

### Breakpoint

_Collection: `4 - Breakpoint`._

| Figma name | Key |
| --- | --- |
| `Breakpoint/Width` | `51eb4cf284703d6d016b5abe52d7605f4362d130` |
| `Breakpoint/Min width` | `e22ad820d50b88080e29ae6d4e5b182fa5212781` |
| `Breakpoint/Max width` | `5da37bd78e3c6f812ca7fed2b65b710cc64cfdfc` |
| `Breakpoint/Height` | `2d5437568123431d36f59c1d2837959e3db4bc40` |
| `Breakpoint/Min height` | `ae2a8bdd825f16c88b4fe108e3a94dd8cb292cf6` |

### Colors

_Collection: `3 - Brand`._

| Figma name | Key |
| --- | --- |
| `Color/Background/Backdrop/Default` | `da6d9419308c1527d981b4e69f43f4fc633cd5cc` |
| `Color/Background/Constant/Black` | `70d9d5b90d394a5bdee81243e7f75d9134dec8d6` |
| `Color/Background/Constant/White` | `dd457be76b8bab36462be21fed10ca63cc3fd34f` |
| `Color/Background/Default` | `4eac340e9bcc67cea2c77566887b954804530fbf` |
| `Color/Background/Light` | `e65d75db8124824e1915e2f86860627bc0d0c6ff` |
| `Color/Background/Subdued` | `d82880ead1694a54e503a6611c86dda53cfe1488` |
| `Color/Border/Accent/Light/Default` | `eb9cb384e41aaffba0748c2dc22cfef344986716` |
| `Color/Border/Active/Default` | `62225e744db054adb1685f9740a5c85c927297a3` |
| `Color/Border/Active/Pressed` | `b8cf233ad8705552c2c064c3fa33749fdd70bd69` |
| `Color/Border/Constant/Black` | `790ead15f17fb45b6eac7bb23fb83fdb5ebd3851` |
| `Color/Border/Constant/White` | `58ce5eaf37261d2fdd03df22229941fac1b1bd25` |
| `Color/Border/Default-Inverted/Default` | `2c55756240d76531a559784c36ce9af173d1f11c` |
| `Color/Border/Default/Default` | `7adf6436ec398ac4808d3763edd10104e7cd218f` |
| `Color/Border/Disabled` | `ddb4f8bac0bf5505daf2a1c1ab0e10c063106771` |
| `Color/Border/Focus` | `8319faef36e02dd0908e9d0c8b13356769b5b73a` |
| `Color/Border/Interactive/Default` | `84951a1161d8fe09adc041cfa680940c98c40d55` |
| `Color/Border/Interactive/Hover` | `7277efce9c9cc54887e05fc0926e778777a53a86` |
| `Color/Border/Interactive/Pressed` | `c37f7948c3265671d6a31f9106dfbd236e95cd9c` |
| `Color/Border/Light/Default` | `ff93acff44522d41bb717cdd2a85a71bc28df798` |
| `Color/Border/On-Primary/Default` | `26041b09dff01bc11002dd11f90442f887bf7e88` |
| `Color/Border/On-Primary/Disabled` | `12fa3261491984309874d507141779b99815629c` |
| `Color/Border/On-Secondary/Default` | `0ef9ee94b07c3a4bd4951488c8d72fe29b8c579f` |
| `Color/Border/On-Secondary/Disabled` | `d39d5574bd01049857c10d79110778699f362729` |
| `Color/Border/Status/Error/Default` | `697b343e7cb7864cb8154944784aa70c79cb442c` |
| `Color/Border/Status/Error/Hover` | `426fcc39e9f684f85e7c5ab0a747c03c7510e680` |
| `Color/Border/Status/Error/Pressed` | `d3b42442360fa3a364cbdbba640cad96778234ea` |
| `Color/Border/Status/Information/Default` | `daafc4279088483c30977667b20d6d8def806e62` |
| `Color/Border/Status/Success/Default` | `24f3fe665c2bf890433adab9b334ccf2795a7232` |
| `Color/Border/Status/Warning/Default` | `9e2ab16e57dedf80d2bf340a7ff03d43e52909c1` |
| `Color/Border/Subdued/Default` | `b05f64048fb68730aef2b3b5b556d10622d65379` |
| `Color/Border/Surface/Default` | `ea0e19126bba3f4ee09efd855f6276c1298b1aba` |
| `Color/Border/Transparent/Default` | `55685b45e005d80d414b595066349a7630ac4c9d` |
| `Color/Border/Transparent/Strong/Default` | `d1a4895bfd77ee84d6eaa1f9cf287342dbe32ad2` |
| `Color/Content/Active/Default` | `a2e9554b9ec7710af12d673e9dd6420bdd1c1187` |
| `Color/Content/Active/Pressed` | `eb62f4e4228a962e04d64ba9a1bac73e18f70316` |
| `Color/Content/Constant/Black/Default` | `c26f5ca622f93b326f52d5eef72be5d1dac270c3` |
| `Color/Content/Constant/White/Default` | `04dd7dffbc5dfd654f67428ae41e686c2c7ba4e6` |
| `Color/Content/Constant/White/onDark/Default` | `cb38cd4979ebb68e062458faa7c5125c58fb2570` |
| `Color/Content/Default/Default` | `0854358864fce820ac440cc2b40690f7068c7ad5` |
| `Color/Content/Default/Inverted/Default` | `9a46d0db7222ee4276dae63a8a7cc20cf6491fb3` |
| `Color/Content/Default/Inverted/Hover` | `bf518a5dc909c0f541ab208452b91cadde59d6ed` |
| `Color/Content/Default/Inverted/Pressed` | `a5d7f71ad3bc6f4ff8d08de7e69ff1f7b8fbb392` |
| `Color/Content/Disabled` | `35ebc445b843854e2aea6622f8d0ce205fdc0d5a` |
| `Color/Content/Interactive/Default` | `7c09ac632338ac266a88e2e5dc0b1ce94422f290` |
| `Color/Content/Interactive/Hover` | `e02d5a9dd7e32c52a1b145ef4c45f15ca25cc465` |
| `Color/Content/Interactive/Inverted/Default` | `c86ec11d375052ef8bfa4bc0d4398b1aa67c9d02` |
| `Color/Content/Interactive/Inverted/Hover` | `e538cfd942a5d23ae3ce45ee745f97473b6414c0` |
| `Color/Content/Interactive/Inverted/Pressed` | `6c2dd9c771a7e097bd418672dc720c6669182615` |
| `Color/Content/Interactive/Pressed` | `d334ed7f6d25eb719cd1205eec02c06d04fb3c7d` |
| `Color/Content/Light/Default` | `b727824e8e6855aaee9e9095ff0c0a40d672bb32` |
| `Color/Content/On-Brand/Disabled` | `9650d622c81b1a0b3c59b22faf2bf25b4354c819` |
| `Color/Content/On-Primary/Default` | `e864b265e1879da7aca54e205d4a05679d79a5c5` |
| `Color/Content/On-Primary/Disabled` | `d393208fdd193e0b78f50297d90116d51fdc69b5` |
| `Color/Content/On-Primary/Hover` | `12f2f2d20e5502ec15b7bf10034770ecc345ea4b` |
| `Color/Content/On-Primary/Pressed` | `77beeb0e3cdcc3ae85023ba58eccaf0f99731d81` |
| `Color/Content/On-Secondary/Default` | `5ae3a5df2edbffdf1228d35ce0cdb3c35115739b` |
| `Color/Content/On-Secondary/Disabled` | `08333827cce1d6e7c63c83844b4242e638b506cc` |
| `Color/Content/On-Secondary/Hover` | `5c31a4278fd290f428548906faad2c2c0d8dd5ae` |
| `Color/Content/On-Secondary/Pressed` | `ce54894870e6d5bcf82f4c3e9220da6ac931b416` |
| `Color/Content/Score/Bronze` | `c7bd78a960a0a546779ae136f209e1fdd5832f9e` |
| `Color/Content/Score/Diamond` | `5ba61517e3c8797494fbda596dd80c68b746b23d` |
| `Color/Content/Score/Gold` | `903aa6296aa4f30c154cfdfd296e85813c9ee583` |
| `Color/Content/Score/Silver` | `798a426215c4e5c44a2dec7bfd4d429223853cdf` |
| `Color/Content/Status/Error-Strong/Default` | `c03ddab87679282b5ce23494af3ab09755b73e97` |
| `Color/Content/Status/Error/Default` | `01cf994bedf5cb6e2280a01df8231d92a5caff48` |
| `Color/Content/Status/Error/Hover` | `b7cb5ce10f33dbbdc702c325b0954ad139885ba6` |
| `Color/Content/Status/Error/Inverted/Default` | `1afe50427815c871bdf6bd78b0cac522b3a4d5f7` |
| `Color/Content/Status/Error/Pressed` | `a77cef316046cad6b28448bc1f0d07a72c6b2501` |
| `Color/Content/Status/Information-Strong/Default` | `3dc3cf495e3c99ec9b54cea4d1aa767587e9174a` |
| `Color/Content/Status/Information/Default` | `b1eb81935f21885659148f5b31372b9273e30c03` |
| `Color/Content/Status/Information/Inverted/Default` | `ed0ad48362266b4e376638b00de5f600305558b9` |
| `Color/Content/Status/Success-Strong/Default` | `3ba82fc81747336a62751eda10f6457606e997c2` |
| `Color/Content/Status/Success/Default` | `5e9245298f1d1499729b6644853f5c6064a76771` |
| `Color/Content/Status/Success/Inverted/Default` | `22cdc983d5246adcf018675279520ea152922f38` |
| `Color/Content/Status/Warning-Strong/Default` | `b562556be9951503952ccd6a67faa23fdde21ab3` |
| `Color/Content/Status/Warning/Default` | `b1b4a70906eb6135df9a308cea953f62e0733590` |
| `Color/Content/Status/Warning/Inverted/Default` | `6017996ffdc7ec65e8eeffd4250114c5c8143e7c` |
| `Color/Content/Subdued/Default` | `93bdf3b8fd98fc7c46bf3c78f9a0dc7d44bebe25` |
| `Color/Native/Android/Ripple` | `1b92bca8c15c845c21638606135e1065437ec0ec` |
| `Color/Native/Android/Ripple-Inverted` | `90fa91c6cb8f38a2f477e28ca36e7a83c02d9a42` |
| `Color/Native/Mobile/Background/Splashscreen` | `05338df7822f5574e90cdcd8055289cd7b67eae1` |
| `Color/Scales/CO2/Blue100` | `098f200cb2094a4c872abd5df6f64c0c8ab7a9f5` |
| `Color/Scales/CO2/Blue200` | `6cc261991b06686f83fc3c044a36da230d840e7e` |
| `Color/Scales/CO2/Blue300` | `4a4717310cefb6440121cda5907a0c4479032918` |
| `Color/Scales/CO2/Blue400` | `a640f181b0e11b5c9a7b8ae7dd8706847988539b` |
| `Color/Scales/CO2/Blue500` | `e26514092cffa64c07b6f055a6a69a42ee1b2cc0` |
| `Color/Scales/CO2/Blue600` | `a54e209b58062c17116daa910040da528dadb9e3` |
| `Color/Scales/CO2/Blue700` | `e2d9df982ffe26f38f1883b7b2f1c2af2a2429b8` |
| `Color/Scales/Energy/Blue100` | `03b1aac16bd8c1327af006f9d382b1db6b1dd524` |
| `Color/Scales/Energy/Green100` | `48733a9f52b6bac4ee5f4682782a792586644a40` |
| `Color/Scales/Energy/Green200` | `506f6119a633ebcfface644125e22949d9db4557` |
| `Color/Scales/Energy/Green300` | `e46304f360bc62fdfd28345a9cd23145b683c742` |
| `Color/Scales/Energy/Green400` | `616773dcb0ef077f0df0c18c6e1138d291a36379` |
| `Color/Scales/Energy/Orange100` | `7caca8e6243e60ccde0e97954cf0dc94c42af4d3` |
| `Color/Scales/Energy/Orange200` | `4048500ce0dcd50e4e24e23d630cec2cea10bad7` |
| `Color/Scales/Energy/Red100` | `1bef7a7ebe8c87b67fd2acbf4f2055936b7a9a5c` |
| `Color/Scales/Energy/Red200` | `752384509b1d13c3b15ddd4950809822aff34015` |
| `Color/Scales/Energy/Red300` | `5bab21b985294e0c92bcffe74e1d4466f1582af4` |
| `Color/Scales/Energy/Yellow100` | `80d038d2aefd65f57403ef4f52cf02a14fd3f7b7` |
| `Color/Scales/Energy/Yellow200` | `5ea22365a43b2ba89b27773dab509e485d6364a0` |
| `Color/Surface/Accent/Light/Default` | `5ad61abb84223eaa4a5eeee8ea9e589be0ca7ea8` |
| `Color/Surface/Active/Default` | `30e544e0144e1d00da1630ca523672415a386f11` |
| `Color/Surface/Active/Hover` | `658079ae4b107d8604774a7feed55ef3d1955bc3` |
| `Color/Surface/Active/Pressed` | `d08f1866f05985c6b217c2657d347c78ed50f169` |
| `Color/Surface/Brand/Primary/Default` | `9cbb1e6130f6fdd46dd69af4124c5216904ce6b7` |
| `Color/Surface/Brand/Primary/Hover` | `e549dcbd208d03a96dbe283c29b116982922df86` |
| `Color/Surface/Brand/Primary/Pressed` | `df09519433f2ae2584bbc3b2626aef092943bc23` |
| `Color/Surface/Brand/Secondary/Default` | `a1c559e6993194e70e85778bba7c7315af63704f` |
| `Color/Surface/Constant/Black/Default` | `28a5cb811eb92506f7343a465a6b54f79c03723e` |
| `Color/Surface/Constant/Black/Hover` | `dbbd24fcfe90aa9d2a9e0a176bdf2e54726048f2` |
| `Color/Surface/Constant/Black/Pressed` | `118121bbb5dedbfb5ba522d7da5712288603437b` |
| `Color/Surface/Constant/Black/Transparent/Strong/Default` | `a38cf31f89b3e52e2fbbebe7a47478a65c76123c` |
| `Color/Surface/Constant/Black/Transparent/Strong/Hover` | `44505f4a88ee317c9744986cfe791d99983d8251` |
| `Color/Surface/Constant/Black/Transparent/Strong/Pressed` | `88fd8ced777e35a51e2ec1bb2053fe6373f24187` |
| `Color/Surface/Constant/Black/Transparent/Subdued/Default` | `fe52568f5b6c94f87a75070db1fe611f83cf3ffb` |
| `Color/Surface/Constant/Black/Transparent/Subdued/Hover` | `88e51b3ef347ae7fe56d1f53c3f0284e4f7a60f7` |
| `Color/Surface/Constant/Black/Transparent/Subdued/Pressed` | `e2ab04e8d85f6e0e5c8afe39214d88933377807b` |
| `Color/Surface/Constant/White/Default` | `bee50cf9935dd56dfff3cbe6d562c550ba3dfe63` |
| `Color/Surface/Constant/White/Disabled` | `2a6545f7dc4c92bff52c33ed50fefc1fe16f2999` |
| `Color/Surface/Constant/White/Hover` | `798142dcdb90c8ee8a2f0f16df461c47f1a7a20d` |
| `Color/Surface/Constant/White/Pressed` | `3cc07cdcd9404c0056fc28c7e3b8678acf587025` |
| `Color/Surface/Dark/Default` | `fb3b7e6b779c0fcad19967f3c1520a7c629ef6a1` |
| `Color/Surface/Data/Categorical/1` | `45bc13a6d84a15c968bf3640d4181f895303b07f` |
| `Color/Surface/Data/Categorical/2` | `7686d995b6b4cfa629357229fe6571e781121b90` |
| `Color/Surface/Data/Categorical/3` | `ae266413377c4a3629db76ab3773c17bd95de4fd` |
| `Color/Surface/Data/Categorical/4` | `b82a0b77e489a896f6f4e8b1c2e42fd9e8a7ad4a` |
| `Color/Surface/Data/Categorical/5` | `6e43d8c5cd7a09922f96c1b4f9fcde6d2b6b88c6` |
| `Color/Surface/Data/Categorical/Disabled` | `963e69b000b2e4582990dc28e2f0230b76a9090a` |
| `Color/Surface/Data/Diverging/1` | `a7e1a2d648e108fd470cbd0aefd70af099e54c91` |
| `Color/Surface/Data/Diverging/2` | `61c28475f40165e10bfa36368d50d97e22023dc1` |
| `Color/Surface/Data/Diverging/3` | `9412f8a95a8a7a2d1a4d1193f5d8e9021dca3b77` |
| `Color/Surface/Data/Diverging/4` | `15565aa1f386df8437618c4da0e4f44038c2499a` |
| `Color/Surface/Data/Diverging/5` | `8fe0f4ee956afed8f6626d92a6a8e91bb7697d40` |
| `Color/Surface/Data/Diverging/6` | `07c41e1bb06f5ba73f47f0096a64919fdfb680f8` |
| `Color/Surface/Data/Diverging/7` | `68731c83682da1e5003744cf486b8502a3e20e22` |
| `Color/Surface/Data/Diverging/8` | `a3063ef1f4690b76b3a226d19d883dd41bddb7ae` |
| `Color/Surface/Data/Sequential/1` | `8da696712fe24d1ba4e4a32514f49f7e2e47e17a` |
| `Color/Surface/Data/Sequential/2` | `30dfe89a5ce126353c98997f246e0a635f35be01` |
| `Color/Surface/Data/Sequential/3` | `4408edcd3924588eb4ddbe179c87c293aaaff697` |
| `Color/Surface/Data/Sequential/4` | `3f3e44e79e35df3a0f602978af6dd290361afe20` |
| `Color/Surface/Data/Sequential/5` | `1334613edcafafa645626d5e82bfbbd69806b6e0` |
| `Color/Surface/Data/Sequential/6` | `e3b7108934979faa9d13b9d8c02d098f9861ab74` |
| `Color/Surface/Data/Sequential/7` | `5c0bab5ed4e0fa16727e687e35329a629e1b59d1` |
| `Color/Surface/Data/Sequential/8` | `dc1ff1e3b6ea8d2a3502ae0e725fb965123fdb97` |
| `Color/Surface/Decorative/Red/Default` | `5ec66541074517f1363e9f70a6c1cc8da7be4d07` |
| `Color/Surface/Decorative/Yellow/Default` | `ab0a9036ef8225b66d8798119a5e9d9042946f96` |
| `Color/Surface/Default/Default` | `6732082edbf214765f54350a7d871dad46c5c579` |
| `Color/Surface/Default/Hover` | `26b265a9fc7f8fae391a5f16032ae1bc15b2021f` |
| `Color/Surface/Default/Inverted/Default` | `be2dfb76076349018a6bdb21adea06597592746a` |
| `Color/Surface/Default/Pressed` | `532de70f9bbd5c3ac2244464947407b914ad8855` |
| `Color/Surface/Disabled` | `0ed6328027ae359333d0be2f0fbc0e25e0df24cb` |
| `Color/Surface/Interactive/Hover` | `856efb015a92e5c76fdd9e8c1cc911962fa67afe` |
| `Color/Surface/Interactive/Pressed` | `dd91bdb2b70a2020d262d239c5cb408bc00873c7` |
| `Color/Surface/Interactive/Selected/Default` | `851ff9438ef4af1436b74527d47343b1996aefb6` |
| `Color/Surface/Interactive/Selected/Hover` | `27b7775e9f30cf6fad2f2ffce774f71bc7cb8e7f` |
| `Color/Surface/Interactive/Selected/Pressed` | `09fb32c574205409a3db0a4da764292517c1dab1` |
| `Color/Surface/Light/Default` | `1d1c83418b550c3f9c502cbf7efadb5ac6c83ff9` |
| `Color/Surface/Light/Hover` | `11a69c9099b4cafc731e2e32ff4de315da5f85f4` |
| `Color/Surface/Light/Pressed` | `290436fc93701a1206d8dda628111f6ec53e3f70` |
| `Color/Surface/Light/Transparent/Default` | `f4bb564fdda21c346c36f012916c78e7cd62ab69` |
| `Color/Surface/Light/Transparent/Hover` | `ceac964d2500b0193136180791391c6671e7d56d` |
| `Color/Surface/Light/Transparent/Pressed` | `1deb1c2f0e7353283aeed8c3af9f617202be30b9` |
| `Color/Surface/On-Brand/Disabled` | `65e9d1b574fc531fc6db36ebc3eb0576060a450d` |
| `Color/Surface/On-Brand/Hover` | `a17e0e622916613ff0c54dd03c52bc5d8611ddd9` |
| `Color/Surface/On-Brand/Pressed` | `fc0aae3313ba66c90156a54a3421cf849fdf9ce7` |
| `Color/Surface/On-Primary/Transparent/Hover` | `75a3e83774d7005e04986aa9136f85b0b7b417b1` |
| `Color/Surface/On-Primary/Transparent/Pressed` | `76e8affd9bf964e3e9fe906a13fd46db61e3a6c0` |
| `Color/Surface/On-Secondary/Transparent/Hover` | `703cddb93a9994a891a7e1e58986cb4227eecd0b` |
| `Color/Surface/On-Secondary/Transparent/Pressed` | `9bdbcdac792a44768cb0a7f962a95acd3fade0de` |
| `Color/Surface/Score/Bronze` | `c62a54eed8ae2b668186e6e0d6a51ee8c0807a98` |
| `Color/Surface/Score/Diamond` | `7ae765b2f8350e22d3d6516541cee78941a14a63` |
| `Color/Surface/Score/Gold` | `9c6051b3ae9d2bc8a03cc8456aed9f4c8c25eb8b` |
| `Color/Surface/Score/Silver` | `572e9dbc13660cac0d69c04c85bd372ba7fa231c` |
| `Color/Surface/Status/Error-Strong/Default` | `5333c5e78d44a2e2599e587a8899a48dc9bd8fd0` |
| `Color/Surface/Status/Error-Strong/Hover` | `41d36e2efb520e2f630a3481fe7cae39d702c325` |
| `Color/Surface/Status/Error-Strong/Pressed` | `8ff6593bae73d6d7454b355c3de87d59fd282d11` |
| `Color/Surface/Status/Error/Default` | `c410e10f6fd9b0949b57f0f4bd8ad481a110e35e` |
| `Color/Surface/Status/Error/Hover` | `e015964447a018ae6fce6b0b5c50f342a67dcaed` |
| `Color/Surface/Status/Error/Pressed` | `58ff0243b608d8d3224a3805efdeef51e2be1f62` |
| `Color/Surface/Status/Information-Strong/Default` | `3b9f3bdb7a9d7f1012cb7b817a0d3299038f81f3` |
| `Color/Surface/Status/Information-Strong/Hover` | `f3d48885de33917d60612ca39e14ec55c7130e22` |
| `Color/Surface/Status/Information-Strong/Pressed` | `9aede5b25f67777ecfb86ec853d7cf286a3a2201` |
| `Color/Surface/Status/Information/Default` | `c5ca5cbc608f6442f9c671acd29c551a61b7cb09` |
| `Color/Surface/Status/Success-Strong/Default` | `747e44d7f2655b9da8ebfe456d7bcb1d5162c392` |
| `Color/Surface/Status/Success-Strong/Hover` | `40a6c8b715fa280eed4cc73dc9870a901f8eb29c` |
| `Color/Surface/Status/Success-Strong/Pressed` | `f12d060de6ec2e5f03b516c18284a7f0937aef74` |
| `Color/Surface/Status/Success/Default` | `3af915373b6faf3b942499cbfed89238805fa976` |
| `Color/Surface/Status/Warning-Strong/Default` | `c4d35c6cc22cbcdb4b470d5964d93d01d2e7303b` |
| `Color/Surface/Status/Warning-Strong/Hover` | `4bc716d72fce6f3b584d5a7c7d1786313fcf9540` |
| `Color/Surface/Status/Warning-Strong/Pressed` | `22a021d2d516dd0ad64d9f97f36f64814be71d48` |
| `Color/Surface/Status/Warning/Default` | `bc0b240c62da741c9a09835e0cb637d78a9611fb` |
| `Color/Surface/Subdued/Default` | `5e36ed6041b63a7374f10beb6a51b8aad95cc8bb` |
| `Color/Surface/Subdued/Hover` | `8553be44223b6baec4afd9b555fb618359df8fe4` |
| `Color/Surface/Subdued/Pressed` | `0ec3d81d9868a2dc27bb9207c5c8b4f9430e3e21` |
| `Color/Surface/Transparent-Inverted/Hover` | `510c58772dab4292abf93d512980c9ad67186363` |
| `Color/Surface/Transparent-Inverted/Pressed` | `545400187f75230e7faeecc8f52bd5e9d92a8f05` |
| `Color/Surface/Transparent/Default` | `653f9264e5fa92e48e75daf46868dd8af1c131f6` |
| `Color/Surface/Transparent/Hover` | `d0db9a6dea162d9c19b56f359d8d921a113e49cb` |
| `Color/Surface/Transparent/Pressed` | `9996f242aaa929f667cfe84a8e43aee6ae14a228` |
| `Color/Symbol/Brand/Dark` | `21ba83eeb75598454c78ad765d0f27a9626ec825` |
| `Color/Symbol/Brand/Light` | `982de57e4120691b5130ab0b3c86b722c10d66f6` |
| `Color/Symbol/Brand/Primary/Default` | `f2b4756a373256f31f61b917bf51915ef08eede6` |
| `Color/Symbol/Brand/Primary/Subdued` | `c3a00db3bf50da89cdc340fc57fca8b6f7d5b273` |
| `Color/Symbol/Brand/Secondary/Default` | `1d751b88f4c931a41f6e9794d8103cde2e240a99` |
| `Color/Symbol/Disabled/100` | `e70fcdecdb44bc7989261bd8793e8b9d2e81400a` |
| `Color/Symbol/Disabled/200` | `d75e4913f710a281425b4341acb496a8ccb6a744` |
| `Color/Symbol/Disabled/300` | `1c920dc95d9ab96282eb2e9d16c3e68f556ac012` |
| `Color/Symbol/Disabled/400` | `b3b4372b71f1c5bc3fe046814c97b3a696de3b3b` |
| `Color/Symbol/Disabled/500` | `af4a495bbea37fe2d29f6356269ebca46ac6296f` |
| `Color/Symbol/SkinColors/Skin100` | `413882edc87b6590a55c9bb200ce3357a9156daa` |
| `Color/Symbol/SkinColors/Skin1000` | `b803b3bff6a2fc1d06c42656215e4af813fded85` |
| `Color/Symbol/SkinColors/Skin1100` | `68d226587adbdd6d4e40eb6ebc5d672c4172e42f` |
| `Color/Symbol/SkinColors/Skin1200` | `c0a543bfca4f170af9f5a8302d41c89f89833621` |
| `Color/Symbol/SkinColors/Skin200` | `3f3805041e79c3dfc4ff2d6fa9dcd4a1ee207ea8` |
| `Color/Symbol/SkinColors/Skin300` | `5de67e20d402b846a8d335d24aba3a52c9a35f52` |
| `Color/Symbol/SkinColors/Skin400` | `20796bba8cb2643c739cccc455b29afbe3a683a3` |
| `Color/Symbol/SkinColors/Skin500` | `49ce3f1394b3b4b8fd572dd157625478d64f39fc` |
| `Color/Symbol/SkinColors/Skin600` | `9812488e2d0bd40989f80df113dba39a4fa739f9` |
| `Color/Symbol/SkinColors/Skin700` | `f4e1337c931d2988cf3a074a188c7fdcbb62f80d` |
| `Color/Symbol/SkinColors/Skin800` | `d3e594cc1b29af5870153fb87eeb77444da0b201` |
| `Color/Symbol/SkinColors/Skin900` | `535f780056823837467c4560864c45b49959c791` |

### Effect Styles

_Collection: `Local Effect Styles`._

| Figma name | Key |
| --- | --- |
| `4` | `06d9b2e38beebe438c3b7c3873633e702968470b` |
| `8` | `d2a883aefbd67e2c80e241a1860455e40235eeca` |
| `16` | `8c4be1bb6f1da244dcd303008316ea976ea285d1` |
| `24` | `fe48ff33f6286761a5713fe57bca282abee9c277` |
| `32` | `220166c457414a62cd0063c3321ff76f85a9095f` |

### Grid

_Collection: `4 - Breakpoint`._

| Figma name | Key |
| --- | --- |
| `Grid/Count` | `fea97e80d309b81cace2809a92f51d5f96e2d489` |
| `Grid/Margin` | `9a19f2019f901cbc49038c2836708075e45433a7` |
| `Grid/Gutter` | `d6dc7e5b0579386af0f457fa70fb8c5aa045a988` |
| `Grid/Width` | `744dde398da0db0f1f41c9a473375cd74376eeb9` |

### Radius

_Collection: `1 - Primitive`._

| Figma name | Key |
| --- | --- |
| `Radius/None` | `f4f46e6301fe8bb158e1d35f1fb314e8952c9d8b` |
| `Radius/4` | `efc754c7546a2da77c11c02c237258adf0ba455e` |
| `Radius/8` | `8bda4f1e08b45a1651366c92813e3c26e5fca972` |
| `Radius/16` | `7b02828789d88fcb0f6f40c54deac21229f026c3` |
| `Radius/Rounded` | `e80abfc6d65630ed45274dafe84ff67d1b392c09` |

### Spacing

_Collection: `1 - Primitive`._

| Figma name | Key |
| --- | --- |
| `Spacing/None` | `a1ee036310acf38f531ca1289803b68645944809` |
| `Spacing/2` | `ed00651ddc065df6bc19e76eea78af0846ed745a` |
| `Spacing/4` | `1f35405fce3b25352702d9c4472fa0e9dbf41cb1` |
| `Spacing/6` | `f8020b7827b8f884668fb6eae0953ce29c9939d2` |
| `Spacing/8` | `e60e6fbb1d833c2c5664442b90fed44329f7ce51` |
| `Spacing/12` | `6f0ae2702c91efc85c13a63e779d31556997935f` |
| `Spacing/16` | `d815abf38d2145bcda9d128aa30492eea15441d4` |
| `Spacing/20` | `4fe4028d5805abc592ff04844d80b5b8b9d54e4a` |
| `Spacing/24` | `f419a5c920dd6f7a921d05368f395adc2e737791` |
| `Spacing/32` | `60d633d48a30eeb2351dba9d55238c50955b4b02` |
| `Spacing/40` | `364667b98e340ac51ed53d817122809a4db8f467` |
| `Spacing/48` | `8062f52a3be02061fceba141231b4a612e804a38` |
| `Spacing/56` | `f37eb1e083891d0362cad06261d0674b06a95fb5` |
| `Spacing/64` | `bfa43f12c773536e2a271ad2a0468522b4e30ce2` |
| `Spacing/80` | `17561db325acb89f51714d70bca7da1d3dd6ec86` |
| `Spacing/128` | `766e1518992a8d5f235727598ffa645023d72296` |
| `Spacing/256` | `16b6039064f73d1d7380d6bc825a6adfa1511085` |

### Text Styles

_Collection: `Local Text Styles`._

| Figma name | Key |
| --- | --- |
| `display/57/bold` | `4420d5fb6c7b47bec643f608812ce2929885f7cc` |
| `display/57/regular` | `368b860add4cd884e0aabe07b358c6512f9f0671` |
| `display/45/bold` | `102e5802f2abf3206b3d0ffa680159d831371129` |
| `display/45/regular` | `c305462ad07a8b09ac319ada6da7393b58b8d789` |
| `display/36/bold` | `ee99c52c28959aba1b7e172ca15d8e94b38e7470` |
| `display/36/regular` | `73f1504205c521b0aec6688af629f83515b1ca01` |
| `headline/32/bold` | `9ffc6cee8a3b99cf12bcbc1967ef7bfbc570287a` |
| `headline/32/regular` | `bbf593d615454ba109c3abb3785d05314585c879` |
| `headline/28/bold` | `03eced552c7d05b89eaeb0512b5462b2827509ef` |
| `headline/28/regular` | `90d4bbe06a306c0e35d48b4e14cdc9ee54211b0d` |
| `headline/24/bold` | `45f89e4f82303d1d99c9df0f7ca94a0888f218f3` |
| `headline/24/regular` | `85bc4fa6cd664c53c30b9e73e59316d000d3e225` |
| `headline/22/bold` | `b71ef7a3780091a975db2b647847a545f86d24d8` |
| `headline/22/regular` | `24971146d530a9221a6bce4168f41bf4e42c6842` |
| `headline/20/bold` | `e9bc7570b4078d17f24d32d779b78b451dde83cb` |
| `headline/20/regular` | `73f1ac865191acce20c7bf32d65bfaf2c79a98e9` |
| `body/16/bold` | `5036cf6b29b5de23032b8479a7d85c201e0cfba3` |
| `body/16/bold underlined` | `b18ed6c1852037f70c774a55e4a58edd2d59a16b` |
| `body/16/regular` | `d0c0779eb5fd562dbf6f3d81c8080e9dec952f1b` |
| `body/16/regular underlined` | `67f07d00b5ecc0959f9679a6b12b629eecc48f28` |
| `body/14/bold` | `74245d0a41fd8e6d03783ffd5e69feca0587f30e` |
| `body/14/bold underlined` | `dc40e1d202bd8c35a57e7250f7f7141ed37476aa` |
| `body/14/regular` | `30cc49cf67aded410c4f1c4a45733c47205cfa0a` |
| `body/14/regular underlined` | `1dab83886ed68cfce9f7297a563ea77167c53ad6` |
| `body/12/bold` | `937dfad1023259ce1966dd807f124b617e3f6024` |
| `body/12/bold underlined` | `84c1e13c347c0385c914ef0ff276e8e8ef270064` |
| `body/12/regular` | `5faa7d33ac12b8e45964b94df31613de58e1ac60` |
| `body/12/regular underlined` | `4a2071ffd7c7634342852afaeca7d88d4113c518` |
| `body/11/bold` | `d70c22fe367840fa2062275767c4cb0bc06b2116` |
| `body/11/bold underlined` | `d5687802f9711c2f185c7f99b992f51f4f876e9e` |
| `body/11/regular` | `b16be1ec0c6c7f35f1016710b0974d68d178a660` |
| `body/11/regular underlined` | `e45e1d7a22e7889cd0567961acd885bdbf447c18` |

## Icons

Every icon key is a component set key. Set `Filled`, `Circle` and `Square` only when the spec asks: all three default to `Off`.

| Name | Category | Key |
| --- | --- | --- |
| `minus` | Action & Settings | `018449f978efe7489f72290c0ab020e63908e54c` |
| `plus` | Action & Settings | `88abf40e254b41f0fa6cdbd7be2fccc59227a3d8` |
| `gear` | Action & Settings | `a2b63fb37d01e456fbae2e24807181a1ee373c2c` |
| `filter` | Action & Settings | `a8e84b32222e6ddc23ba1e9524c96a0792442002` |
| `filter-sliders` | Action & Settings | `4e9685734e951fab3b13992c8bd0003bfe1f8540` |
| `bars-sort` | Action & Settings | `4e14ca6e5f05e49d46eaf2928851a602fb646b98` |
| `list` | Action & Settings | `07800e23e68bec7a2cfa571ed53103fd81a1265b` |
| `list-check` | Action & Settings | `0defdd3fd45334597e457d129db223d904a9ca76` |
| `sort-down` | Action & Settings | `d1206697ba26bc1e51644f843bea140b470a1a62` |
| `sort-up` | Action & Settings | `80d96e54dfa56adecfce6e66a7c911c58d816c65` |
| `dot` | Action & Settings | `f75931a69a42c3ccbdd3641fd6590f810a3b3603` |
| `ellipse` | Action & Settings | `8d66ac66755854c44cc1c68983f7bd821b5b28ae` |
| `magnifying-glass` | Action & Settings | `33e207d248cfde25ea1bd70a29314250b7612594` |
| `magnifying-glass-plus` | Action & Settings | `9b6b29e3892390c6f1bf1d3cd033fdc3ce54b491` |
| `magnifying-glass-minus` | Action & Settings | `cbe01dd4e0d791fa095055d96ab817559a082027` |
| `maginifying-glass-spark` | Action & Settings | `fff7a0875757e8ab3d8a55b302b2c9807614a6ed` |
| `eye` | Action & Settings | `7dd53e0740a3e9a4913114de20cd4ff526a79f66` |
| `eye slash` | Action & Settings | `f7a6e005704d61b093ec83be4c0e954dd657f675` |
| `link` | Action & Settings | `a35db86f03da7bf28999500b6fb3fdd5bd82692b` |
| `unlink` | Action & Settings | `0676e95181f91b8e429ef48d9aee81dd5547ffa0` |
| `share` | Action & Settings | `ddb333a124d55f0c38c66f431368932860399e34` |
| `download` | Action & Settings | `fc62e9348963f26780805381fd161b76446e4589` |
| `upload` | Action & Settings | `415fc25d1c37809cc8f670a027e7c7f4f68188ae` |
| `reply` | Action & Settings | `706dafc98240dd6ce50cdd72630e62146f07836f` |
| `forward` | Action & Settings | `13ef115166d61f4d5f80cbe99a1bd760a231753c` |
| `Save` | Action & Settings | `fc78640138f7e52ea3538e7d29e378f38e904497` |
| `cloud-arrow-down` | Action & Settings | `06daceff1dd3f0904194bed4672b2cc74c08ca50` |
| `bookmark` | Action & Settings | `55bac3638b75875080eadc6215270f957fb19992` |
| `push-pin` | Action & Settings | `60e8ecd8361474cef9353cd95126d6c184af2dd6` |
| `play` | Action & Settings | `b2ff251ca5a79a94f783c432921a7c8a713204d2` |
| `sound` | Action & Settings | `e0615fa201a9d2cfba2aca3f1e5ddbf9933c5d1f` |
| `forward-step` | Action & Settings | `929d2ba6b57ed962b5fb9611e9c8636fa0681e59` |
| `backward-step` | Action & Settings | `5deea0ec244b0378dc7f1e023b06836b4cbc70ef` |
| `pause` | Action & Settings | `78b20b82e0a287f5b33fd03edcd5ee29e12c9c26` |
| `resize` | Action & Settings | `945cd19ef6770f668c6aa3e08f5613d4d1872f2c` |
| `ban` | Action & Settings | `a785b36c1ad9e74a6a5364aced1ab837f6156756` |
| `circle-dashed` | Action & Settings | `cc5bf76c53f0ea2446c4b1edec155a4e43476f79` |
| `bookmark-slash` | Action & Settings | `bc527e064aeeaf7ae45b877b9a729d238f096f56` |
| `bolt-square` | Action & Settings | `419909f520e1b25887ecae2f2c2b6061a6d8df3a` |
| `radio-button` | Action & Settings | `e268f82c13786112ced54dbedb6d6e5b3663f4bd` |
| `heart` | Alert & Feedback | `6ae4c99ce5538a469445dc62a455be582b489241` |
| `star` | Alert & Feedback | `3235b492c4ea26e93712081d5722cb6d23d0b15a` |
| `thumbs-up` | Alert & Feedback | `78a11e542074bceb52d458eeaf6f025e4556368f` |
| `thumbs-down` | Alert & Feedback | `5fd89a5cee86c015d6f2dd9b51b7cee0efc3c1c5` |
| `bell` | Alert & Feedback | `559ce6c4ae9094ba0e39350e0f23a4a20cf6c4a2` |
| `bell-slash` | Alert & Feedback | `e298b54400b00ce575baf17b22c65384af2389be` |
| `check` | Alert & Feedback | `6b2b85ee7bf7769f67c1af609b9b49b08c50fc22` |
| `info` | Alert & Feedback | `3daf5ac6038e34878dab7bc2ff73a5fea3abfb06` |
| `exclamation` | Alert & Feedback | `69851955f8cc42a4985b3c404be483b84d2bfb89` |
| `loader` | Alert & Feedback | `a36232a98763f5c5d70281e3b43e535e59a8d82a` |
| `question` | Alert & Feedback | `f8cbd6ad0c477946cf9b1560eae5f78061d7bae3` |
| `hourglass-half` | Alert & Feedback | `0b08a476dddea119cf0c7bef94f9d8a6e554d9fb` |
| `flag` | Alert & Feedback | `a7db35d0ccc5e0ee3ee27118c3c5502e8e85ed14` |
| `shield` | Alert & Feedback | `e0ec104f72f183751f2019ea41273e5b6744d921` |
| `shield-check` | Alert & Feedback | `5c77f7daa05bc3108d5f444ba1c6c10bfdcdf9d4` |
| `shield-xmark` | Alert & Feedback | `3b73cbcb1aaec2f1a92ec5986f268fb4c35c0ca7` |
| `alert-on` | Alert & Feedback | `adfa209c755a891f3ba5c8638975bcc11353c316` |
| `double-check` | Alert & Feedback | `38ae1667b2abb90b8235de3a5247d35318bae1c9` |
| `light-bulb` | Alert & Feedback | `13d3c443476bf6dbf5abe1ec4627e39d31c60b2f` |
| `youtube` | Brands | `2250a5b7ce26110987015dc8810c90194d40e3ac` |
| `linkedin` | Brands | `96d8f6ccd0b7fd5113cfd6dfc3f3b578fd29312b` |
| `twitter` | Brands | `a4723b05175a7e0779879efa734fcb39db33db02` |
| `facebook` | Brands | `eeb1a9aaebf11510ea6c6656463baf911c1284a0` |
| `messenger` | Brands | `02347c7b7da465e11a5636a8880d8e1fc64d74f1` |
| `google-plus` | Brands | `641649c3365f4190fd97982bb754d9bf9ef9404c` |
| `google` | Brands | `316c9636c2c7f3027e70c0c015e467c8ba88e4e4` |
| `instagram` | Brands | `4e710dcdc03bd7b0a0ff75f452251af4020b5fdf` |
| `apple` | Brands | `5256b6270dc5d8f853955101dab046cc76536e70` |
| `android` | Brands | `b13cfecad847c23b2bfdd2d4af376a68284228d1` |
| `windows` | Brands | `b230232625a45c90c30b9b21dbb5df0e1da533b5` |
| `whatsapp` | Brands | `aa4d947b9ff65fef4ca7ddc8f758144d182572a4` |
| `xing` | Brands | `4433957b033b7a27d99c436029751f09a10d0028` |
| `pinterest` | Brands | `d94545454490579164bc129c9ef0c1b020d0afff` |
| `cc-stripe` | Brands | `d46bee3781e44acdee56e02e2a1acdb9a2ed9fd8` |
| `cc-amex` | Brands | `f3325d239f000557895c8ca873dd28ab17149850` |
| `cc-discover` | Brands | `7ca1de1743c6a663b4691b60307aa86ed86f7efa` |
| `cc-paypal` | Brands | `ca8b35c77a38c1b26e6c2b5eccf49f46ee247f12` |
| `cc-mastercard` | Brands | `4a192199ef04c7cbd746a6f9c3679220ac8be7f1` |
| `cc-amazon-pay` | Brands | `bd73834c632491bd0af6b6562f3702cdf86536aa` |
| `cc-jcb` | Brands | `e2053accacf0c894065fdb7f775314edbf4b335b` |
| `cc-visa` | Brands | `1e46d9bc9421b33ea7df41e01f4e714a1d1553c5` |
| `cc-diners-club` | Brands | `db8cda63a082a500460a52904c47fcba8abac734` |
| `cc-apple-pay` | Brands | `4bba8695c376edc01c34ad4fb1d14ce0a105f6e6` |
| `tiktok` | Brands | `75559e1bbcd6ac580bf6c2085e66d524999ffb98` |
| `google-play-store` | Brands | `bd29118f2417414d33f3bc5e0f815040465ebe12` |
| `chevron-up` | Navigation & Menu | `fc174c6ae1552a0dca231447bdb3fa7e5d2f066c` |
| `chevron-down` | Navigation & Menu | `cf2c5e8a3ae5c79b9eff4dfce448e3d6639e6cc3` |
| `chevron-right` | Navigation & Menu | `4882d97797b66efd8db441d3b236dee904e4b33a` |
| `chevron-left` | Navigation & Menu | `f8fc19f9ec803daec318758c742deffee18f09bc` |
| `double-chevron-right` | Navigation & Menu | `d9c5ff9b9ce0dbfa1527b8fd357f8f84938b9027` |
| `double-chevron-left` | Navigation & Menu | `b6346386c9e4287ee42dd6648d2c7706ee73c9e4` |
| `double-chevron-left-right` | Navigation & Menu | `834962523bfe0bf9e5fb1838bd392099d87d5e58` |
| `double-chevron-up-down` | Navigation & Menu | `adb6ae605b94087bd65c9b0ff489087e5b4719d5` |
| `double-chevron-up` | Navigation & Menu | `cdc99b0b42aaf7a11b3974ac89e2aa35a81b95cc` |
| `arrow-left` | Navigation & Menu | `09366b55b3733696cf6ca485aac8afd3291ef2d7` |
| `arrow-right` | Navigation & Menu | `faccf2a60c7cf7ba15d0ee98bef14b4bd315f385` |
| `arrow-up` | Navigation & Menu | `ca6f11d61696e4d542ea06f2d99670f4aa26db5d` |
| `arrow-down` | Navigation & Menu | `efead516fd05d37e054a5959e63ce9c3fe63c8ad` |
| `arrow-up-right` | Navigation & Menu | `36097f38485b22852c271afad19dc9cfdd9fce90` |
| `arrow-up-left` | Navigation & Menu | `a91f79668251950eea2e8198dea16167beb22dff` |
| `arrow-down-right` | Navigation & Menu | `29ffb603f3a6ea2e04d93580f377c3951ad486a4` |
| `arrow-down-left` | Navigation & Menu | `d79894d77b2fa4cfbc461e1b6a7d29b2f1243b31` |
| `arrow-maximise` | Navigation & Menu | `167170d505bce9629b7c697e4d8718794b5c426a` |
| `arrow-minimise` | Navigation & Menu | `54cffb779fac1f966507057362833fa8b53b9e66` |
| `change` | Navigation & Menu | `1639de1609ddbc69de6c0ddfbe4c7830d90cb84e` |
| `rotate` | Navigation & Menu | `6ac26c40c5edc35464085e42c7ac2d259373f979` |
| `rotate-right` | Navigation & Menu | `0d468c906ab2530709a5b1a1da221f6ed597ded9` |
| `rotate-left` | Navigation & Menu | `596d0244776fcc4d2c20ad3544209dd94d37fb5e` |
| `history` | Navigation & Menu | `6235492fd343cf339e124dea7dd8dd5d0c5293c3` |
| `external-link` | Navigation & Menu | `8e3a199846e10c4ee49ab74acc624213d83b5a2f` |
| `logout` | Navigation & Menu | `580d91ea4dd8ab699f4e9d91d05ee31528f7322f` |
| `expand` | Navigation & Menu | `825d30e0502546e393b95e9aeb5f317e12d8721b` |
| `compress` | Navigation & Menu | `0b4a55878a11468b7c8d0f5a6c62c8a47fcddc97` |
| `grid` | Navigation & Menu | `f599e99df01bd3852987e60045ded2c3901f4b62` |
| `menu` | Navigation & Menu | `a076368d4cd370f423dc9354d5d502042323efe2` |
| `equals` | Navigation & Menu | `5f31c48ae381c61fb397be67d1a23848a766e259` |
| `ellipsis` | Navigation & Menu | `a22240cca9f328fba81c319076d585dc7dd15d0d` |
| `ellipsis-vertical` | Navigation & Menu | `dfbd4e2cfb58d4479b767145023454a12078b193` |
| `grip-dots-vertical` | Navigation & Menu | `e5e4678df16c455962da81d76b060cc0b1f3480f` |
| `close` | Navigation & Menu | `529627af1ce7d5743cb1179817048c6d71b4f917` |
| `caret-left` | Navigation & Menu | `09b2371da965635ddaa8b8ecc785c03e9733ac77` |
| `caret-down` | Navigation & Menu | `0b8374bed753a62766142fdc2d7a2d23f382b77d` |
| `caret-right` | Navigation & Menu | `297f1303962d9d678df18fce9dbfdf430d9f4fb6` |
| `caret-up` | Navigation & Menu | `545e19fa16d5282707d9943b22685e7a98a26e08` |
| `cursor` | Navigation & Menu | `3fc7191ce34b80c00f2b7bf8fad41834373d71be` |
| `hand-pointer` | Navigation & Menu | `a2c1050be4a9be4a9d32f2cc0bea97f57999bbc4` |
| `rotate-right-image` | Navigation & Menu | `1ce830f6719799e2ae5fc6790f04ae009d16ffe4` |
| `rotate-left-image` | Navigation & Menu | `ce4682dcb1e15fca6f0f85c835217c61cb7eb9c4` |
| `user` | Users & People | `475bd1ca7267d8f40552e07294880a03dc7e6d7a` |
| `user-group` | Users & People | `2175dec3aaaa0481cde12d6617905ea5272e75f0` |
| `user-tie` | Users & People | `d30740035d782343b81180d380e350a86653f78c` |
| `user-police` | Users & People | `97cb95592c71ef4158cc7f5c1c2ae47d02c165cb` |
| `face-meh` | Users & People | `5113e3c79fbe68560154161c880f194416f55025` |
| `face-smile` | Users & People | `ad6d4e26fe99aea458fe91844c0859fd695d4f73` |
| `face-frown` | Users & People | `3881a9d0708de6c264baf99cab641496c71c7116` |
| `face-grin-hearts-light` | Users & People | `958965646d73057fa77ebc6c711c6a9b379ee0d4` |
| `face-sunglasses-light` | Users & People | `6139a667747c845e7a02fa6754350f5a9a900fe1` |
| `user-plus` | Users & People | `f71f4bd289d638cfa77996251439a3fc500377ed` |
| `baby` | Users & People | `40353d8fcb84e0743633b87be3757bb32373d9b3` |
| `family` | Users & People | `80debc0c08066725c726782a6b4a29d8435ccce4` |
| `criminal` | Users & People | `c5100433b5b09af8504445f27456e3b719b2ae5b` |
| `handshake` | Users & People | `51a55b1f3863af7cad2dfc0c5179c5f7339149f6` |
| `wheelchair` | Users & People | `e6e86c7faa1e1fb1058fd16a0f3ae9bc3decfc93` |
| `receptionist` | Users & People | `f33d97eb0b26ff6291fd792ac15431dda47a0264` |
| `hands-holding-heart` | Users & People | `7f4fc5e94f6349d24f4bbdf298e7c1a9331c2a60` |
| `custodian` | Users & People | `61c87a2551c03f7a21d74f3341f3fbfa05ce5db7` |
| `unhappy-face` | Users & People | `6828b8b5e45942028f6106fa3f56395e10c6ff27` |
| `user-minus` | Users & People | `2c3ac506da88612a252cb7996213b8c07b4b50e5` |
| `assistance` | Users & People | `53c0f912d8763ce9644b48ff71d9c84522ff0d34` |
| `user-slash` | Users & People | `89f30ed99aee5c3bc40e27b43a66c39c66f497f7` |
| `person-circle` | Users & People | `ee17c8326f4004bdfcc8e6b1984bb0296c508f8a` |
| `location-dot` | Map | `afba5dde61f10ab80e0f678db106d4145591c050` |
| `location-plus` | Map | `6d4f4d912a18ef4bac9d0b307e53961bce3d3d08` |
| `location-slash` | Map | `0103d31599adb86311dbb37a9dc4710d12bd3beb` |
| `location-circle` | Map | `a279680bcb91c6617aac84946b7efbc5c5522372` |
| `route` | Map | `fc449a6c1e42ee9b5d87d76b8674faa799b65e96` |
| `map-location-dot` | Map | `28c3919f3f042ce03870d1de506250099692bb0b` |
| `location-arrow` | Map | `dd898889aa275e5dc641dd97f5161f64d8afed8f` |
| `map` | Map | `ae37ddaaa52cecb8e22be54f0773d6022113d0e9` |
| `compass` | Map | `4b451abf5bdf60b98b617cd232a28fd2bcf48f5a` |
| `street-view` | Map | `4925646fa802c00227ac99c20e5c82f4b4fae828` |
| `crosshairs-simple` | Map | `19a1fbb6a0543efbc27d9831598411e6d12683ea` |
| `earth` | Map | `b061c33bc3b3c5ea8ee2c7210390e34eb876dfa7` |
| `magnifying-glass-location` | Map | `a4d2957dc7327f7932d37772db3bb8d267b17148` |
| `signs-post` | Map | `ccc70f40c4cf11fad5950b799076c78156668f37` |
| `three-dimensional` | Map | `4b432adafed28f4e06567d834a8505ccfe550a22` |
| `location-Xmark` | Map | `1cbe5609101dc46ad8aaff338ecd4b36c33435d0` |
| `two-dimensional` | Map | `b4abc2799184b2e4992301679c729f4aa10cbcea` |
| `map-compass` | Map | `0e2e5235a4b1242157e9f1883d879b78433a5686` |
| `map-france` | Map | `f5041fbb05d4a2268956cf7c3b6eb247dcbc4b0b` |
| `RER-paris` | Transportation | `17a48b5378870fc255598a239fa520a215b3f8c2` |
| `shoe-prints` | Transportation | `da06e39454366346e8dd703a8969d7e1597b98e6` |
| `walking` | Transportation | `d3f698e486a08fa9f22dcba4dc058ba83ed4cd14` |
| `bicycle` | Transportation | `2fa9b87f4cccd74eebc87e8d11883949dcb7dbd8` |
| `biking` | Transportation | `2ca7f131df9faa777f1bf93c04564db3e9001c09` |
| `tram` | Transportation | `30eb04321e663bdf01bf6d9327613ac410bd6dfc` |
| `car` | Transportation | `f658f318e408d532405418d5344efece8f5dcd1a` |
| `taxi` | Transportation | `7bd3c6cc8203a7e9aa8e63312b3566afb929254e` |
| `bus` | Transportation | `4effc85fafd8a7e7fae623367e5232cd6f20bbb7` |
| `subway` | Transportation | `84aae394a0926614301059615e89196f00c947a8` |
| `train` | Transportation | `b9eb5e4002cfac26a11e9ac2aa650c7a05d95c96` |
| `cable-car` | Transportation | `e60ef5b9f5878bc2b82f218a2cecb76943089c36` |
| `truck` | Transportation | `38324c30a78edb68115dbaf95e3e4dd29f746360` |
| `plane` | Transportation | `4be5b6680357e0beebfb646785efbffdb4a042f4` |
| `ship` | Transportation | `3a6ae180c7e0523b7c1752658cae1f411490f6f9` |
| `tractor` | Transportation | `86609641b92578fde632efaad56f3085f5dd7891` |
| `charging-station` | Transportation | `417b2e6f4080e0182ffd523bc3213a8c0e26602a` |
| `gas-station` | Transportation | `7a00ab9eb8f13083ed52d73944670dce6e15736f` |
| `drone` | Transportation | `fd6617ad62063974c40df164f5267936cc5a2291` |
| `desktop` | Device & Communication | `794003798945dec0e116e86f2326e68580a2f5f0` |
| `computer` | Device & Communication | `0608260eb9794d579948b16861e4b585f8559632` |
| `print` | Device & Communication | `d0daa29360e27777b5e8854e5d537608eb5f073e` |
| `router` | Device & Communication | `395d553acfcc113f56359c1fc4c79109c8601ce2` |
| `presentation-screen` | Device & Communication | `c6539d8e825037902046441ee9f4862ece8e1ebb` |
| `floppy-disk` | Device & Communication | `1f40917ba06edb3098cb2895ec1364d4c59c8dc2` |
| `camera` | Device & Communication | `bff637a288100c340043dbdd44eb1a47313026f2` |
| `mobile` | Device & Communication | `1324c50efe224e6f2f63c136647b95d2a107bf3d` |
| `wifi` | Device & Communication | `22b6910c09f954e96b9c612bebc27a5aa49a6fbb` |
| `phone-volume` | Device & Communication | `3435315c96c10de610c7957a25e27fa83561f700` |
| `wifi-slash` | Device & Communication | `dc0a68c7ea48e4b2ae93024a014702c6ce7904a6` |
| `phone` | Device & Communication | `232b6dc1723776347092a327fd4fc367ea07a8c0` |
| `phone-missed` | Device & Communication | `79b307acf75d212f893ec26759542f66a80143d6` |
| `at` | Device & Communication | `bf974e0ef66c00717f6f0dc8a184b7cd24255106` |
| `envelope` | Device & Communication | `2ce96c4b2b29518a13bfaed58fdf4442c96d4430` |
| `envelope-open` | Device & Communication | `ce57b7ac0d655e782e4dc490bbfd2756044a5856` |
| `inbox-in` | Device & Communication | `efb7edb2a80951526f69911bce737cdb6e6a410b` |
| `comments` | Device & Communication | `996bb3121e709b8466e9add770443bc88e2b9c8b` |
| `comment` | Device & Communication | `70f04a7b92a44fdf0eedc04d5e88396e4fbf6555` |
| `message` | Device & Communication | `6a67d3fcb83ee78091b4905240c691127f63b465` |
| `comment-dots` | Device & Communication | `1fca518746e4d057175566a83a1c94f99bd79c4e` |
| `paper-plane` | Device & Communication | `a1835c162bd7c6dada3ba81572724f6af2261c34` |
| `microphone` | Device & Communication | `835155ed89d0a4651baf49b24e349c989a4b70f9` |
| `microphone-slash` | Device & Communication | `1e719b8924af6763fc3bdbacf4c79eeb97acf4f9` |
| `megaphone` | Device & Communication | `2f406595fd5782c332000e244ba9704524c43894` |
| `mailbox` | Device & Communication | `058bb73c6df00fea92a75c52aac98ffba6a1ab0f` |
| `envelopes-bulk` | Device & Communication | `9dbd4ccedbe8a6c9ba851af9e9971096188f095c` |
| `phone-plus` | Device & Communication | `8fc97d51cc4f820292ffde1d5979c7841b1f8428` |
| `tv-retro` | Device & Communication | `1cf846cfb3ea714d43713fc239ca0db63510b9c4` |
| `no-phone` | Device & Communication | `7e557d5ffda9cf07e30939045b8465c54bdacd8e` |
| `paper-plane-flat` | Device & Communication | `d4aa5153aa6792ae28894c757a8f791636d82d85` |
| `fax` | Device & Communication | `1da1cc28febfdc3abf13c4aa76112cf087dfb6ee` |
| `virtual-staging` | Device & Communication | `4cf0f3a5a85c19645bdc64ad95545cc10a3cf598` |
| `scanner` | Device & Communication | `9877159276175444ebf561ab7c94fceb16be45b6` |
| `layer-group` | Editor | `d6f728ade000937565cba44498faa646229485c9` |
| `crop-simple` | Editor | `165f485d4812ceb828b62da1660b0861133e55fc` |
| `pen` | Editor | `f46d8758b66785e28c3810f23bd73c25d370009f` |
| `pen-line` | Editor | `220bafc8938ab5cf83518207342c895aed3a60ce` |
| `eye-dropper` | Editor | `f20c359c58d076ee31b7e1640e86024726c8a453` |
| `trash-can` | Editor | `9903d47d09db00d3bfb49f79ce0566bc768eea5a` |
| `trash-can-xmark` | Editor | `1d5c4d11d97eb977ca5f9e9ae91bedbd7727e6c3` |
| `lock` | Editor | `40950d5b7c4c49f0d2d4d50690dc31bbb3f1cddc` |
| `compass-drafting` | Editor | `d97fbca4055e58542370adfc02305c0998af6c5d` |
| `sitemap` | Editor | `09949b28c61013b6275880050e9b7ddbb382caa5` |
| `circle-half-stroke` | Editor | `b47eb23311a78bf1f07fba9555c439a461b935c7` |
| `lock-open` | Editor | `0efbc3220789cdf43646f0a771d5138be12e70d4` |
| `ai` | Editor | `042f44b137288c4ccd17ae1f044dd7bcb2a5da4e` |
| `smart fill` | Editor | `dc1ae7188a174e3f4a49d927b18ebc8f3e567d5d` |
| `smart edit` | Editor | `d507cc0bb37aafd2480dd7feecec500582919d9d` |
| `smart search` | Editor | `91ae1c6aa2e8af9fefff44c8fcc904d3ccd93f97` |
| `two-three-dimensional-draw` | Editor | `95bcd67f8ba8bd4f649b3f1747cbb247887f0551` |
| `camera-professional` | Editor | `b02ec15609053bf449b944cdd83046abfa441026` |
| `image ai` | Editor | `8b44a66a5fd311fcc35e8f5db09c92c6f3b68deb` |
| `language` | Editor | `5e07a5a06ebf40d355270b77214940a5114b63d1` |
| `book-open` | Document & Content | `b570978973e874d5d665b3a067ef06632a2dee07` |
| `notebook` | Document & Content | `0f14744067393fbe0325487ad68d441b1118a51a` |
| `file-lines` | Document & Content | `7bf9008a7a50af453a7eefd580f3f6cf975faf23` |
| `file-check` | Document & Content | `04a8cc4ca4ec6b25ab4ee7478cd5782f5c1ccef2` |
| `file-certificate` | Document & Content | `c8291c94408059917171802f8504b430f4811210` |
| `file-signature` | Document & Content | `0455dadba026ae5031cc6ff9614d77757f3bc955` |
| `file-plus` | Document & Content | `63381a881e9b5bfe965399e6e7a8629a78bfb675` |
| `file-circle-info` | Document & Content | `84c9ad5ed70e322e0cba838ef071ee728f321371` |
| `file-circle-xmark` | Document & Content | `d107742cc146da57ca8a177de320594c3fed3940` |
| `file-arrow-down` | Document & Content | `68d487cf9f3115bdcc78b1b09acb7ceeabc9ac4e` |
| `file-arrow-up` | Document & Content | `795d4821b80cadefb1cf6992e5c9c6ffb6896e16` |
| `file-pdf` | Document & Content | `58562ecf3b458d6652f1d79a24e733f576f1059f` |
| `file-image` | Document & Content | `f5091bb53b2ef9ffa171f56f6c255ab0d41cd9e0` |
| `image` | Document & Content | `c6b19c10ed467f6c74ade8890178d21385b414a5` |
| `clapperboard-play` | Document & Content | `a9973db5a9cdbe068f5b1ae772b2dce7a0e20205` |
| `folder-open` | Document & Content | `23b7b8ec4e397a4588bf6710f8e1027f3bc35cff` |
| `music` | Document & Content | `4afa724d2427ad656d8c0851377835fe0f4f90f4` |
| `newspaper` | Document & Content | `bedb2f9eb94c13b82f28e37d31ce3f51bac30478` |
| `copy` | Document & Content | `c15c754e105d7fac934023d2cfe6fd8da5c851e0` |
| `box-archive` | Document & Content | `ae33d3c1c05527eea834d5e897541ae99c9b1206` |
| `clock` | Document & Content | `8204f615a8b69b4e1e39725c8669a50a86462cd5` |
| `calendar-days` | Document & Content | `513a5806e8d5da06c6e36968ae15d38fd89f87ac` |
| `calendar` | Document & Content | `054bf6df9f8cef4484531a11d917f05561ee438b` |
| `calendar-star` | Document & Content | `08d7c6785e7c0c474e22a6123e0c0a92e30cef9c` |
| `One` | Document & Content | `39885ea98caa822cc4bb230afa72ff6a57012de8` |
| `Two` | Document & Content | `2b43a85de9e7b62985efe7ca648d5ed7acfefd07` |
| `file-magnifying-glass` | Document & Content | `d41394cde623988a15d65cbbe9ee78675a8b244e` |
| `Three` | Document & Content | `3c1551d17f863288801c2d3218ce16de0fb2455b` |
| `no-image` | Document & Content | `154f0fd1188d5f091212fb2d14685dcba85e85f6` |
| `no-file` | Document & Content | `1bc790de5e100a52d694b39be7d265516743a28f` |
| `three-dimensional-view` | Document & Content | `338c0604431bcc40998e7b4ce4b5a19363772c6f` |
| `unarchive` | Document & Content | `e19a05b159dc2aef9bf0a225ffa1190296b3eada` |
| `paper-clip-vertical` | Document & Content | `eda51e70e467ebc0631aa9ceb16c14122191b07c` |
| `paper-clip` | Document & Content | `da80e65a57d234634528667ef232c02ca187860c` |
| `file-globe` | Document & Content | `462cf3c935ce2b100aba5fce4ed68ad2b4e7d24f` |
| `file-cdd` | Document & Content | `9ba1f20f6a7d226f96089b6190d96e86fa166225` |
| `file-cdi` | Document & Content | `ac1686bf0e2fab8ea6d7111ed3527a50e5c914bf` |
| `coins` | Finance | `b2287c37807192d753ac1fa02b51cec61b09cce4` |
| `hand-holding-dollar` | Finance | `06ed421fca9235849f2c220d5a852d2e55aa9e04` |
| `address-card` | Finance | `e553ca97b8b723001522166034f258dd765efd22` |
| `piggy-bank` | Finance | `3241a5210f110a5a6d3f39d39138a5cfecf87910` |
| `credit-card` | Finance | `8af837fb9e92c4c8aa5792aef98aa3de9c2c3758` |
| `wallet` | Finance | `0d71afb4eabe7c048f1939d786fc68e19d9916df` |
| `money-check-dollar-pen` | Finance | `2babf9c6e0a55c2337453d285d699100adde13a6` |
| `comment-dollar` | Finance | `34f57ed2ceff48380ade7b08fb16127411f13589` |
| `euro-sign` | Finance | `3436e8c5d4cb4b83f579c86cf732023f1a8aed33` |
| `chart-line-up` | Finance | `054c8e743cded5abb544c45626e88d03fc9a49f4` |
| `chart-line-down` | Finance | `c43c84ccd5d6d64cb78e5470bd6b1c91a2b8b9e3` |
| `tag` | Finance | `790476311586840274537c0730f14a902f0a18d8` |
| `calculator` | Finance | `bd629e0929f17f230a9ca7bb904cd89605d1633d` |
| `percent` | Finance | `a1d6147213b20e39c9e18024882c47a25df91c8e` |
| `magnifying-glass-dollar` | Finance | `51ea191c6e16bea3f0345548ccaa33f4b803d41f` |
| `zero-percent` | Finance | `18cf08a1ab8630eb6992b9680f7da425777556c8` |
| `baguette` | Nature & Food | `21d05c3edac6262760ec617cbeefbfa024ccd12e` |
| `mug-tea` | Nature & Food | `cd8674f9d28643ed9a6f9a97e99342cc30d984df` |
| `apple` | Nature & Food | `6319aca03a0e2a129df867f610b51e1eb285e0cb` |
| `coffee-pot` | Nature & Food | `983c3ddb776a353b93f6449645af03fa6dffbddb` |
| `mug-hot` | Nature & Food | `b8d9a921789d002a1774933dca379152ea1208f6` |
| `cocktail` | Nature & Food | `202822e7d6069d56401e407db1b1595ee37b4919` |
| `ice-cream` | Nature & Food | `7789165d74ff6909c095e2740c3901a518b45290` |
| `croissant` | Nature & Food | `4d55c302520cdad1117d7a2e57268e3d078a6ac7` |
| `drumstick` | Nature & Food | `fd7bc11d5bab097bd03d2989e714bf7323c0af17` |
| `utensils` | Nature & Food | `e203336b9fedda130fa24458cc9196fbb59a0da4` |
| `mountain-sun` | Nature & Food | `34c107050628b76207c820e769081843f496ec00` |
| `paw` | Nature & Food | `7470b72a33be835c46b33c553c7616fc82e08b64` |
| `droplet` | Nature & Food | `d03103242392f8ddae7f28ee193b9254435f50b4` |
| `fire` | Nature & Food | `7b8689e8f30c9b8960f077feec4d3a196418ba0e` |
| `snowflake` | Nature & Food | `99b1afa5e2cc1358787d1ece20aee8fa176542cf` |
| `sun-haze` | Nature & Food | `3ddfe868a2c0717c2df1dd3df252634f94158cfe` |
| `leaf` | Nature & Food | `5f3dfd6a1f89436cf7f4bdb50a022c316de68642` |
| `spa` | Nature & Food | `2983b031d10916f0b5a95da8efbd075051b9c9c0` |
| `trees` | Nature & Food | `0467399157de6de596da7044e325360fbab5ea5d` |
| `bench-tree` | Nature & Food | `469d3fc411f8a7f95240b5b3f733da348ded0511` |
| `sea-view` | Nature & Food | `a1a078d0d3dfb5ff76e0befe39b282409a85be70` |
| `lake-view` | Nature & Food | `febd96173ddc19942a219f45a426c26eb8246b90` |
| `tractor-tree` | Nature & Food | `9bd3be8d3b92bc6922724250deaaddd657cb2530` |
| `basketball` | Lifestyle | `6ac49362c1d536e4ab13e29869052bac5d38ebd0` |
| `tennis-ball` | Lifestyle | `5b99bc8a6fdcd576ca2ae9c1d83948ef5497e406` |
| `table-tennis` | Lifestyle | `7b6925471c853d12c2c3e9f5e72f6a060f1b3a29` |
| `dumbbell` | Lifestyle | `cfe210721a273794d9c075838c8c153b3d784a91` |
| `water-ladder` | Lifestyle | `f761f522c42d9ef6214528a4a7f463bc0cc2e7e1` |
| `person-swimming` | Lifestyle | `1c27db6e2bede55daf53179b2169d1e1fec9f32e` |
| `puzzle-piece` | Lifestyle | `27f6bd8459f1c9244faa54db44d5a83be7b177e5` |
| `chess` | Lifestyle | `7f17367980bbb22d72b55308e6949369de78e538` |
| `pump-soap` | Lifestyle | `7ef964a9f4371bda936ae85d6f0bbb9a93896182` |
| `cart-shopping` | Lifestyle | `4e5fcb7092c97e9a8fb83d12e6979b756c15e091` |
| `umbrella-beach` | Lifestyle | `98dd6387d78db6f07983e5cef7cabcfc345d4097` |
| `masks-theater` | Lifestyle | `fb13e0fdcabea95820222a37a3c368479e7a592a` |
| `ticket` | Lifestyle | `979834d37a22bb8a95a59ced3f73f96acbb2b853` |
| `film` | Lifestyle | `89b3df33dbf62b723c9ba5b116f469cf01fbe82b` |
| `briefcase-medical` | Lifestyle | `444526ae2673e4f15da0beda78a7e04bb543d72b` |
| `house-medical` | Lifestyle | `c7dd3e237a4df61f9851d6a31ce72b8609ba548a` |
| `stethoscope` | Lifestyle | `de8ab331723aced97b5193adad3e077e60a918f3` |
| `scissors` | Lifestyle | `2cddaa572064a20542b97b8a4ac260095767f641` |
| `smoking` | Lifestyle | `0509aaf3a536571cbce795e4d440c2dae817cf1d` |
| `gem` | Lifestyle | `381af11ca195ada15dd0f5e9999448be33a6ac66` |
| `podium` | Lifestyle | `92d28bcad318873cf7dea68f6d9fea1314270246` |
| `backpack` | Lifestyle | `c5788c0a90f97ea475f63541559222e303d0dcdb` |
| `briefcase` | Lifestyle | `b4d0e61978cdb921a2272ec1e66fdf77e961ae8d` |
| `suitcase` | Lifestyle | `164e7fc9ae62042d5fd3f6c094845a47eae8ef5b` |
| `graduation-cap` | Lifestyle | `ebd8092d1be1183b164f7c6d817ac9ca2a1d1603` |
| `construction-site-helmet` | Lifestyle | `02315fa8ea3966032425ec976f0ac786d0064a97` |
| `monkey` | Lifestyle | `d4cc95aa3a799e136d061f93427323e08adeed15` |
| `movie` | Lifestyle | `e8b994f5a42978629ab617064257ef668b846c47` |
| `medal` | Lifestyle | `4b56f590560a0e37ff779b6d4850d6706c4491ef` |
| `trophy` | Lifestyle | `ddf71d8ce6cd0dc1ccfc6f61a1a4a7599fc44f40` |
| `teddy-bear` | Lifestyle | `45f7a1e60e3f1e3e1c69d22c849269f16fbbf542` |
| `towel` | Lifestyle | `6668415e14446588653130e42e38227ca84a3e0a` |
| `plate-cutlery` | Lifestyle | `8479897c0e7d970a0e3fe789f2a0b697e5a92c41` |
| `loveseat` | Furnitures | `e6f21cc64d42ac6ffc982b939aa455faa0f92f51` |
| `bed-front` | Furnitures | `4886c7bb5b7b59b9e41ae287b4e17e19cdee3a9c` |
| `chair-office` | Furnitures | `5ae071f856ec5161377bb46e731264da9e1de753` |
| `faucet-drip` | Furnitures | `427edd7222bb4340e3d5d71db352958ea6f1d775` |
| `bath` | Furnitures | `37aa295561276bd656a3b92e7a6c201293e6abab` |
| `vacuum` | Furnitures | `7834df07e84bc7cdd6a9f4c46fae679d5a01a5a6` |
| `microwave` | Furnitures | `49fe98f5e53e4e950f20b1571b8bd60a10e0661a` |
| `refrigerator` | Furnitures | `3d4d2c0140d4ae71e1a0f8f91fa7c98a9cdd85af` |
| `washing-machine` | Furnitures | `de218db12ba44962614c9b0cc3b7f825802b624c` |
| `pan-frying` | Furnitures | `59ec2762fcdf368fbfdba9449b0a5deceaf2d658` |
| `air-conditioner` | Furnitures | `a8e015c0e972a92381e4ed84c83881a423320ac6` |
| `baby-carriage` | Furnitures | `ea3d93314672bac3351142c27c0c8b19094dbc5a` |
| `umbrella` | Furnitures | `7a8de5f9bf30a7abef0704700c786e0c3cebe30c` |
| `toilet` | Furnitures | `9845e5331f6238cc32950e41d09659bee302a952` |
| `lightbulb` | Furnitures | `e9fbaab698c44cff1bc04a41437fd1668734ed88` |
| `temperature-list` | Furnitures | `de6fa475296ef2dc581a2c130e4a4c19cf734bdd` |
| `sprinkler-ceiling` | Furnitures | `8d37550c4583e75e492863e6f6fc005543cf65ce` |
| `camera-cctv` | Furnitures | `d8b60f108b2b267be8e444185a6b8248e8ae7890` |
| `paint-roller` | Furnitures | `2a36b336f11b40f4a03ee664f7a8d79c9cf239a2` |
| `hammer` | Furnitures | `090c5f696f0cf4f6ae75908f36d2b0c316e0e6d7` |
| `ruler-triangle` | Furnitures | `1331c84d7e1cf5f442f20455b84feb7871ce72ca` |
| `shower` | Furnitures | `d4b421076610fd6bbbb2368f5615e324f1e633af` |
| `bell-concierge` | Furnitures | `2e4d641661f5c03450a60b0034bd7d3745e53d03` |
| `door-closed` | Furnitures | `70223858bcb2f3702c22f6974623765152c8339a` |
| `door-open` | Furnitures | `94c6835cb334b87439cd92af97e5edf5aa031dd7` |
| `fireplace` | Furnitures | `226add7d387cd070d51a0364fd3a8c339262511c` |
| `gauge` | Furnitures | `600b9161627ab416f787c2cafcec6afbf4a943e6` |
| `box-taped` | Furnitures | `562576b9d632e25f8e253c3107c44e7b0c6f3857` |
| `elevator` | Furnitures | `b71fdda5f81a2328e753e4c06d6a9bc5fc8cc4aa` |
| `person-dolly` | Furnitures | `41d5e88eab441194252158c220f166ed42bd1970` |
| `power` | Furnitures | `2fe34f2729bc89b8e81fbb0f49ea53abff4e961b` |
| `unfurnished` | Furnitures | `d629a1127b5e97308261fabcc381c33906210c34` |
| `dishwasher` | Furnitures | `0961a467a2fe05a938ffa05ec03232cb0f61dd84` |
| `square-h` | Place & Property | `c458afa99568c358b7232a826e74fbfe730ab0d0` |
| `circle-parking` | Place & Property | `72a3a1e3fc9f811422468fa52878b3223537e827` |
| `store` | Place & Property | `c7f4cad64e371866911454829dc15e6d394708ea` |
| `shop` | Place & Property | `f1fb5cf18b6050a487cb8f443d33db04c9bd6954` |
| `hotel` | Place & Property | `9c9fdcf831b1c56574abad24e8531f8d93ce6ddf` |
| `tree-city` | Place & Property | `a8c39753dd0439a03d382a608f8f2f566ba65451` |
| `landmark-flag` | Place & Property | `153e87585e62641eb0b5cd1ba8201497f894214c` |
| `warehouse-full` | Place & Property | `094eb25ffa537c9956c35e61305a413976e208da` |
| `landmark` | Place & Property | `d46b935b415b105879ea0b52e7e4bd30014dcdba` |
| `roller-coaster` | Place & Property | `733a878a51a93ef973741343b45a275e2f0a5391` |
| `house-tree` | Place & Property | `28ef6688842849c81ac23ec346a1e50f01004cf5` |
| `house-building` | Place & Property | `34b598f117abb67b9dd526860aaea9945b58cbc3` |
| `building` | Place & Property | `b5282adbbfe3a2b6dd3df6505378d258f50733de` |
| `city` | Place & Property | `147baf135b4e418ad6f12396f3799deb3fb010f9` |
| `campground` | Place & Property | `a2867dbf1783ba813ff7df30cf89c9b1150d42d9` |
| `light-emergency-on` | Place & Property | `2871cd66817fccc33d68c023c41cecd35cf68f1a` |
| `fort` | Place & Property | `586cb7dd9bcf3d72a2966a8f5223fef23a0adf0a` |
| `school` | Place & Property | `7f928cd2bba720de0f57b023fb854c1c4d3367d1` |
| `playground` | Place & Property | `507f86766dd28491c5d95b54fea11647c3bac083` |
| `soccer` | Place & Property | `71ef094c681118064b26ddd559f3696ad79b017f` |
| `floor-plan` | Place & Property | `ebb23d51762aedd3605e5724c925943971ec2ba8` |
| `balcony` | Place & Property | `770378b18f369c25fc58bfdff159778894a77213` |
| `window-frame` | Place & Property | `a6a4cef7e8eb249f14f663fb2e01f68a706c788e` |
| `terrace` | Place & Property | `4e05415116a449786b3e03e102385de840da3f13` |
| `attic` | Place & Property | `f3b507255362b22f9a7886e9ff0d94dfd610cd3e` |
| `bidet` | Place & Property | `c96ae9abf850f8310b5d1d7d52b605e0f0598575` |
| `underground-car` | Place & Property | `1449d4036f1101918acd0a73900fbb84dbaa593f` |
| `duplex-car` | Place & Property | `ce646e935b24b3175559cdeccb3074084d58235a` |
| `loggia` | Place & Property | `2c505445c03a121d56b37123baa1ba5790a5746e` |
| `pantry` | Place & Property | `d974b5a99cf45988b9d47917e05db1f590ed290c` |
| `hot-tub-person` | Place & Property | `b8e0b509cb0d736f7df755b0d8bff0dff25480a7` |
| `urinal` | Place & Property | `a982e8bac5bf0af1797a1cf133f06f1ccfc0f7e0` |
| `stairs` | Place & Property | `e953b3d4b4284c858bccf4a5552f843d1df905a6` |
| `basement` | Place & Property | `0762fdaf3761c3cde45931b271c5d1fc7990578a` |
| `cellar` | Place & Property | `98f757da40e8d2f36830747ea43038f2d7f843bf` |
| `industry` | Place & Property | `224ad8ffabe1cfb6ff1d57471d13ad297027be69` |
| `plot-space` | Place & Property | `a1e9b3b91aef7265cad83e8a34843ee71860229d` |
| `property-insurance` | Place & Property | `ced9666ba89ae8303818f203349efae86bc57982` |
| `house-staging` | Place & Property | `4848f2084ba1252d6212da6837e9e19e612c38b6` |
| `house-building-off` | Place & Property | `8fed00f7ea2122181c7353cd8427d304caa58a96` |
| `garage-car` | Place & Property | `91608001a4c80a1f89799a9a4525fb7e59fdd2b2` |
| `load-dock` | Place & Property | `1f0f7b605a749c1e17741746b35d27a59d802355` |
| `RDC` | Place & Property | `87aaf2aeb1e28ccfb50e1b5d2a3ce47a827036af` |
| `key` | Real Estate | `578b0398475d900afac1ae01902173379a1fd27b` |
| `key-skeleton` | Real Estate | `7c6330cdb3ee06bb27ca3a002dfa5065be8c50cc` |
| `gavel` | Real Estate | `6674610d2e9836e81f239e21b79a23a429be4c6e` |
| `scale-balanced` | Real Estate | `5d34709e32fe3f65574027217737a3d3582e5eb9` |
| `award` | Real Estate | `c4bc8a0970c1339c591ba3cacb04554f48f309fe` |
| `sign-hanging` | Real Estate | `f269855c00364b263ae7641f732d46c98b22ef37` |
| `magnet` | Real Estate | `8384d6126e7b23256b71f0403a8a68c5ded1ac95` |
| `digital-lock` | Real Estate | `7cc0b3bcab4c1af22d5c01c24ba9e978d418ad78` |
| `agency` | Real Estate | `9c27df173a8a9ee4fee4b5eba831f36af3070d49` |
| `sold-property` | Real Estate | `74d049559f54a104b0490a978630bb1cf0ec334d` |
| `three-six-zero-view` | Real Estate | `76fd105e77530094270ffbb108b466bfd33d3766` |
| `house-money` | Real Estate | `1c1f670476e917e1da116e5a5505db8c8acebcef` |
| `house-insurance` | Real Estate | `46bf50bb750ea4a6b048f1899e35423be68e3499` |
| `house-key` | Real Estate | `5b22f7038f2630ff49ba4490d32fa0d76c98aca1` |
| `house-search` | Real Estate | `08af66bf59925b3724ad001fd53313749d7ccfe3` |
| `magnifying-bars` | Real Estate | `1f45285f0a958dccf32d74a1c15ec0261fd97917` |
| `magnet-diagonal` | Real Estate | `7f5a9333445c23151184e112b8c6bba22eb8b316` |
| `square-meter` | Real Estate | `d7f19d8b4b977910aafa5d863b5e992e7f447576` |
| `frame` | Home | `555dbac12fe0a48515fdc44b9d2872916372da54` |
| `ruler-combined` | Home | `725105ea770abc3a0164b05c097eed6157977c55` |
| `block-brick` | Home | `5f5ef59aee4cb8b64137152f253b2ffaee93dc4a` |
| `house` | Home | `9b7ad754383328078e5311f4bed5b3d4e92eefc4` |
| `house-user` | Home | `9ab47c19855f28a7519f7ca434303678be059375` |
| `house-chimney-heart` | Home | `80131332f0ac5083dc4646ef6fe52c05dfbb9dd5` |
| `house-day` | Home | `ab7db1ebeb3a7f5770f0a3c4a56f0e12435b96f5` |
| `house-circle-check` | Home | `c6dbfcc8d76c22fe8c8e61ec8bb853798647dc78` |
| `listing-deleted` | Home | `126a13e860e404857825176db270c34b55abe5c5` |
