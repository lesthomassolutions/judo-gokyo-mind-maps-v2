# Direction conventions and handedness review

## What is established

The source is explicitly a classic right-sided perspective. Its diagrams encode **success/attack arrows** and sometimes colored **sectors**. The inventory records screen positions, not a verified anatomical kuzushi classification. Preserve that distinction.

- Uke: the person receiving the technique.
- Tori: the person applying the technique.
- Execution side: the right-/left-handed stance selection.
- Anatomical direction: relative to uke's own front/back/left/right.
- Screen direction: where an arrow or label appears in the drawing.
- Off-balancing, attack, travel and landing directions must have separately named meanings; do not assume they are identical.

## Proposed fixed map frame — requires content review

Keep the viewer and uke orientation fixed while changing execution side. Proposal: uke faces the bottom of the map. This would preserve the source overview's apparent orientation; the content reviewer must confirm it before anatomical labels are released.

| Screen position | Proposed anatomical label |
|---|---|
| N / top | Uke's rear |
| NE / upper right | Uke's rear-left |
| E / right | Uke's left |
| SE / lower right | Uke's front-left |
| S / bottom | Uke's front |
| SW / lower left | Uke's front-right |
| W / left | Uke's right |
| NW / upper left | Uke's rear-right |

Under this fixed frame, anatomical axis labels stay in place when execution side changes. The reviewed arrows, sectors, foot/grip illustrations and appropriate option placements change. Rotating the viewer or relabeling uke's own right as left would be a different feature.

## Geometric reflection is a candidate, not validation

Reflection exchanges E/W, NE/NW and SE/SW; N/S remain unchanged. [direction-review.json](direction-review.json) preserves each source diagram and gives its geometric candidate for all 40 techniques. Every candidate is explicitly non-publishable until reviewed. Colored sectors need their own review; the candidate arrow list does not replace them.

Examples:
- O-soto-gari: source NW; geometric candidate NE. Confirm the intended uke/tori side and grips before approving either anatomical interpretation.
- Okuri-ashi-harai and Yoko-gake: source W and E. Their reflected arrow sets still contain E and W, but sequence, grips and technique illustrations are not thereby verified.
- Harai-tsurikomi-ashi: source W/SW and E/SE. Retain both sector variants instead of reducing to one direction.
- Hiza-guruma: source black arrow S while two adjacent lower sectors are highlighted. Resolve the meaning with the content reviewer; neither silently drop sectors nor add arrows.
- Tai-otoshi self-link: retain as unresolved; determine whether repeat attack, continuation or accidental navigation.

## Review preparation

[relationship-review.json](relationship-review.json) contains all 1,151 directed source/target pairs and all 1,211 source placements. Right and left statuses begin unreviewed. Repeated placements remain distinct variants. A reviewer must identify which variant is approved; approving a pair must not automatically approve every duplicate placement.

Each reviewed variant needs:
1. Meaning: continuation, counter, repeated attempt, general navigation or unsupported.
2. Initiating side and technique, uke stance/reaction, grip and footwork context.
3. Direction meaning and reference frame.
4. Follow-up side and prerequisites.
5. Evidence, reviewer, review date and exceptions, independently for right and left.

The ledgers are machine-readable records for preparing review, not operator acceptance forms. Source evidence is linked through stable IDs; do not overwrite the original inventory. Once a reviewer is identified, prepare a small first batch (O-soto-gari, Hiza-guruma, bilateral examples and Tai-otoshi self-link), agree the review approach, then continue systematically through all variants.

## Display and persistence policy proposed for V2

Right-handed is the initial selection. Persist only the selected execution side across technique navigation, reload and later visits; fall back gracefully when browser storage is unavailable. Technique names, categories and credits remain unchanged.

Unreviewed left-handed directions/options are withheld with a clear unavailable state. Preserve the selected technique and provide an explicit way to view its original right-sided map; do not silently change the user's saved stance. Display original right-sided relationships as source material, never as newly approved instruction. Deployment policy for unreviewed right-sided relationships needs a content decision.

Videos keep their true demonstration side. Never relabel a right-handed video as left-handed or flip text-containing artwork wholesale. A right-sided reference may remain accessible with its side clearly identified.

Tracked: [#1](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/1), [#3](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/3).

## Reviewer confirmed for the next step

The user has volunteered to review the judo-specific content. Begin with [the first content-review batch](FIRST-CONTENT-REVIEW.md), answering in chat. This identifies the reviewer role; it does not change any unreviewed status or approve geometric reflection candidates.
