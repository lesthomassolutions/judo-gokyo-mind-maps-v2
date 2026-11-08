# Reference-checked content correction proposal

Prepared 8 November 2026. Original repository and website remain unchanged. This is a correction specification for future V2 content, not an edit to the original artwork or site.

## Exact changes

| ID | Original location | Correction for V2 | Reason |
|---|---|---|---|
| C1 | ashi_waza.htm | Remove Sumi-otoshi, Yoko-otoshi and Soto-makikomi from the Ashi-waza filter | Te-waza; Yoko-sutemi-waza; Yoko-sutemi-waza respectively |
| C2 | koshi_waza.htm | Remove O-soto-guruma from the Koshi-waza filter | Ashi-waza |
| C3 | yoko_sutemi_waza.htm | Include Yoko-otoshi | Yoko-sutemi-waza |
| C4 | sutemi_waza.htm | Include Yoko-otoshi | Sacrifice classification |
| C5 | tachi_waza.htm | Remove Yoko-otoshi and Soto-makikomi from Tachi-waza | Both are sacrifice techniques |
| C6 | Files/Image/o_soto_gari_i.gif | Correct its classification caption from Koshi-waza to Ashi-waza | Artwork and classification disagree |
| C7 | Files/Image/ushiro_goshi_i.gif | Correct its classification caption from Ashi-waza to Koshi-waza | Artwork and classification disagree |

Ten individual membership/caption edits across seven original locations. Do not modify the old files. Future V2 must display the corrected classification as live readable text and must not display contradictory raster captions. Retaining a corrected text label next to an incorrect image caption is insufficient. Resolve the image caption separately while preserving the technique illustration and provenance.

Evidence: [Kodokan classification and revised 1920 Gokyo](https://kdkjudo.org/en/techniques/names-of-judo-techniques/), checked 8 November 2026. The evidence establishes taxonomy; it does not validate combination mechanics.

## Complete baseline

[classification-proposal.json](classification-proposal.json) lists all 40 proposed technique classifications and parent categories, preserving original category and illustration values separately. Expected totals: Te 6; Koshi 9; Ashi 14; Ma-sutemi 3; Yoko-sutemi 8. Tachi 29; Sutemi 11. All five Gokyo groups remain eight each.

Keep source identifiers and existing aliases, including spacing variants, so old links and searches resolve. Do not merge Yoko-gake with Yoko-otoshi because both source translations say Side Drop. Translation normalization requires a separate reviewed decision.

Tracked work: [#2](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/2). Proposed corrections are ready; no implementation or image changes have been made.
