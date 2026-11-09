# Phase 2 build — 9 November 2026

Phase 2 is active at the owner's request. The owner initially asked for review diagrams, then confirmed the governing rule: “There are no exceptions, the map techniques are mirrored down the center”, with 12 and 6 o’clock unchanged, 11 exchanging with 1, 10 with 2, 9 with 3, and so on. The active left-handed maps now follow that explicit confirmation.

## Implemented

- Introduction spacing: removed empty quotation blocks and trailing blank breaks, retaining all substantive text. The Begin button follows the Harold Moore attribution with normal spacing.
- Uke's feet: smooth outlined SVG curves for heels, arches and toes, retaining original placement and orientation. Both perspectives include the improved shapes.
- Accessible Right-handed / Left-handed selector. First visit defaults to Right-handed. Selection persists between navigation and reloads using browser local storage. Unavailable storage retains a working session selection and displays a brief status; invalid saved data defaults to Right-handed. Selecting Right-handed resets the choice.
- All 41 distinct diagrams, including all 40 techniques, have left-handed SVG versions. Shapes, arrows and success areas reflect through the vertical centerline through Uke. Labels remain readable, with their boxes reflected rather than their text reversed. Intrinsic diagram proportions, including Harai-tsurikomi-ashi, are retained.
- All source technique links and success hotspots now work in either perspective. Original attack placements, duplicates, self-links and loops remain intact. The reflection rule is owner-confirmed, not an assumption that every combination mirrors identically. No left-handed exceptions were supplied because the owner explicitly confirmed none.
- Original videos and technique illustration panels remain unchanged; their demonstration side is explicitly identified as not reviewed for left-handed use. No pixel image or embedded writing is flipped.
- Perspective is stated in the page subtitle, including print content. Technique identity and browser history remain stable when changing perspective.

## Review the build

Regenerate with npm run build:preview, or open the supplied Judo-Mind-Maps-Preview.html. Select Perspective in the header. Click attack options, repeat Tai-otoshi, follow Success to the existing unfinished Ne-waza section, and change back to compare the original. The per-technique decision record is planning/phase2-review.json.

## Verification

All 17 automated checks pass: the original 40 techniques and 1,211 attack placements, groups/categories, loops, media associations and special dimensions; genuine SVG artwork and original arrow/sector states; saved stance default/read/write/reset/failure behavior; readable text in all 41 left versions; vertical-axis SVG reflection; smooth feet in both versions.

Browser checks covered introduction spacing, enlarged smooth feet, initial Right-handed default, left selection persisting through reload, mirrored overview links with unchanged targets/text/vertical coordinates, left-handed Tai-otoshi repetition, Success to Ne-waza and return, restoration of right-handed links, and the distinct Harai-tsurikomi-ashi map with both mirrored success hotspots. Phone layout was checked at 390 × 844. No console errors were observed.

The SVG reflection axis is taken from Uke's center, rather than assuming every source GIF was centered perfectly in its file. Text and hotspot anchors use the same axis. Right-handed baseline page records retain their original geometry and media values; only reflection metadata is added.

Full print output, broader screen-reader acceptance and browser-restart persistence have not been separately exercised. Persistence logic and reload behavior have been checked. The standalone embeds all images; external videos/resources need internet. Local-file YouTube embedding can encounter Error 153. No source video IDs have changed.

V2 is now public following the owner’s visibility change and publication authorization. The website was published on 9 November 2026; see GITHUB-PAGES.md for deployment evidence. The original repository/site remain untouched.
