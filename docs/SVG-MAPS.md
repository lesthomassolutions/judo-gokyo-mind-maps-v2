# SVG map reconstruction

The app uses 41 clean SVG diagrams in web/maps: the shared overview plus 40 technique-specific diagrams. Interactive attack links remain HTML overlays using the original geometry, targets and duplicates. Directional diagrams contain no embedded bitmap, foreign object or external image dependency. Technique illustration panels are unchanged GIF originals and will still pixelate if enlarged.

scripts/recreate-maps.py derives each map's palette and black/grey arrow states from its own original GIF and rebuilds the geometric diagram. It preserves the eight sectors and all source exceptions, including Hiza-guruma, Tai-otoshi and Harai-tsurikomi-ashi. The manifest records the source asset, SVG path, intrinsic dimensions, center, sector colors and clockwise arrow states starting at north. The SVGs are ordinary editable text files.

Python, Pillow, NumPy and OpenCV are only needed to regenerate SVGs; they are not runtime website dependencies. Install Pillow and opencv-python-headless in a development environment, then run python scripts/recreate-maps.py. The optional local .tools directory is ignored. Run npm test and npm run build:preview after regeneration. The local server sends SVG with image/svg+xml.

The source GIFs remain unchanged. Geometric reconstruction removes raster edge noise; fonts and antialiasing differ. Comparison is of meaning and placement, not identical pixels. Browser comparison covered all 41 diagram pairs; arrow-set and special-sector regressions are automated. Full print acceptance remains pending.

Resources now retain the original grouping: Resources → Kodokan Judo, Jigoro Kano → Yungwirth Judo Academy / Judo Info / Judo CAJA / Mercuryu Judo, followed by the other original credits. OpenElement, Paint.NET and the complete Various others including subsection are removed from rendered content, while historical source/inventory remain intact.

Phase 2 update: smooth outlined feet now replace the traced polygon indicators in the overview, as requested by the owner. scripts/build-left-review.mjs creates separate geometric review candidates with shapes reflected and text retained upright. These remain explicitly unapproved for left-handed combinations. See PHASE-2-STATUS.md.

Current Phase 2: the owner has confirmed that no exceptions are needed for the maps' centerline mirror rule. Active left-handed links, success areas and repeats now follow that rule. The legacy maps-left-review folder name is an internal asset path, not a pending-approval status. Media-side review and remaining print/accessibility checks are described in PHASE-2-STATUS.md.
