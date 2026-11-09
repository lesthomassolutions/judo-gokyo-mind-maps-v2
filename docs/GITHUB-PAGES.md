# GitHub Pages — published 9 November 2026

Live website: https://lesthomassolutions.github.io/judo-gokyo-mind-maps-v2/

The owner authorized publication, changed V2 from private to public, and the public visibility was confirmed before deployment. The original repository and original hosted site remain untouched.

## Deployment evidence

- Successful workflow: https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/actions/runs/42628205473
- Deployed commit: a1e9637d6f4eb10d8dfca3a3d63e5c4759c572ac (contains the latest introduction and help edits).
- All 17 automated checks passed before publication.
- Source: GitHub Actions; workflow .github/workflows/pages.yml. Only web/ is uploaded as the website artifact. Planning documents, local QA and build tools are excluded from the website artifact; the repository itself is public.

## Live browser verification

The HTTPS introduction loads with the requested two-part introduction and dated perspective note. The latest How to use paragraphs are present. Navigation to the overview and Tai-otoshi works, SVG assets load, Left-handed selection persists through reload, repeated Tai-otoshi remains available, and the list heading reads List of 15 directional attack options. Returning to Right-handed restores the original presentation.

Embedded Tai-otoshi and Ko-uchi-gari videos were observed playing on the live site. The earlier local-file Error 153 was not reproduced for these hosted videos. Closing the dialog removes the iframe; no browser console errors were observed. This spot check does not claim all forty videos were exhaustively played.

Full print and broader assistive-technology acceptance remain separate outstanding checks.

## Publishing future committed updates

Open Actions → Publish V2 to GitHub Pages → Run workflow, choose main, and run it. The workflow is manual; committing alone does not deploy a new version. Wait for success and verify the live site. No billing plan change or custom domain was configured.

## Resolved initial restriction

GitHub initially blocked Pages while V2 was private on the account’s plan. The owner made V2 public; Pages was then configured to use GitHub Actions. No changes were made to the original project’s Pages settings.
