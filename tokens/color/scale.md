## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for |
| --- | --- | --- |
| `Scales/Energy` | Energy Performance Class (DPE) fills — France, classes A to G. Used by every energy component | CO2 visualisation (→ `CO2`); any general product UI colour |
| `Scales/CO2` | CO2 emission scale data visualisation fills — a sequential blue palette | Energy class labels (→ `Energy`); general data visualisation (→ `Surface/Data`) |

## Semantic usage

### Energy

*Always match the token to the actual DPE class from the listing data — never
estimate, and never choose by colour preference.*

**France is the only country in scope.** The French scale has seven classes,
A to G, and it does **not** walk the palette in order — it samples across it so
that seven classes still span green to red. `Green300`, `Yellow200`,
`Orange200`, `Red300` and `Blue100` are not part of it.

| Token | DPE class (France) |
| --- | --- |
| `Scales/Energy/Green100` | A |
| `Scales/Energy/Green200` | B |
| `Scales/Energy/Green400` | C |
| `Scales/Energy/Yellow100` | D |
| `Scales/Energy/Orange100` | E |
| `Scales/Energy/Red100` | F |
| `Scales/Energy/Red200` | G |

**Corrected 10 September 2026, against web source code.** The previous version of
this table assigned the French classes to the first seven steps of the palette
(`Green100` · `Green200` · `Green300` · `Green400` · `Yellow100` · `Yellow200` ·
`Orange100`). Five of the seven were wrong, and class G — the worst rating —
came out orange instead of red. The mapping above is the one in
`libraries/patterns/energyclassslider/src/EnergyScale.tsx`.

**Not checked against Figma.** `Energy Tag` carries 48 Figma variants that have
not been read. If they disagree with this table, raise it.

#### Other countries — legacy, not in scope

Recorded because the tokens exist, not because anything should generate with
them. This is the German and Austrian scale, nine classes, and it matches the
same source file's `ENERGY_CLASS_COLORS_DE`.

| Token | Class (DE/AT) |
| --- | --- |
| `Scales/Energy/Green200` | A+ |
| `Scales/Energy/Green300` | A |
| `Scales/Energy/Green400` | B |
| `Scales/Energy/Yellow100` | C |
| `Scales/Energy/Yellow200` | D |
| `Scales/Energy/Orange100` | E |
| `Scales/Energy/Orange200` | F |
| `Scales/Energy/Red100` | G |
| `Scales/Energy/Red200` | H |

`Scales/Energy/Blue100` and `Scales/Energy/Red300` are used by neither scale.

### CO2

*Sequential palette for CO2 emission visualisation only. Use Blue100 for the lowest emission value and Blue700 for the highest — never reverse the scale.*

| Token | When to use |
| --- | --- |
| `Scales/CO2/Blue100` | Lowest CO2 emission value in the scale |
| `Scales/CO2/Blue200–600` | Intermediate steps — assign in order, low to high |
| `Scales/CO2/Blue700` | Highest CO2 emission value in the scale |

## Tokens

### Scales — Energy (12)

*Energy Performance Class fills only. France uses seven of these twelve; see Semantic usage above.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Scales/Energy/Blue100` | `#00ADEF` | `#56B3D6` | |
| `Color/Scales/Energy/Green100` | `#078748` | `#34805A` | |
| `Color/Scales/Energy/Green200` | `#60AD2E` | `#74A565` | |
| `Color/Scales/Energy/Green300` | `#8EC120` | `#A2C8DE` | |
| `Color/Scales/Energy/Green400` | `#CBDA0F` | `#D3DD76` | |
| `Color/Scales/Energy/Orange100` | `#F1C502` | `#EACC6E` | |
| `Color/Scales/Energy/Orange200` | `#EBA902` | `#DFAF63` | |
| `Color/Scales/Energy/Red100` | `#E38102` | `#D18B55` | |
| `Color/Scales/Energy/Red200` | `#D74202` | `#BB5240` | |
| `Color/Scales/Energy/Red300` | `#C40201` | `#AD3434` | |
| `Color/Scales/Energy/Yellow100` | `#F6ED02` | `#F3F07B` | |
| `Color/Scales/Energy/Yellow200` | `#F5DF02` | `#F3E477` | |

### Scales — CO2 (7)

*CO2 emission scale visualisation only.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Scales/CO2/Blue100` | `#91D9F9` | `#B5D1E8` | |
| `Color/Scales/CO2/Blue200` | `#80BCDD` | `#9AB4CF` | |
| `Color/Scales/CO2/Blue300` | `#70A0C2` | `#7F97B5` | |
| `Color/Scales/CO2/Blue400` | `#587598` | `#5D7294` | |
| `Color/Scales/CO2/Blue500` | `#47587C` | `#4D6184` | |
| `Color/Scales/CO2/Blue600` | `#363B60` | `#3B4E73` | |
| `Color/Scales/CO2/Blue700` | `#1F1238` | `#283A61` | |
