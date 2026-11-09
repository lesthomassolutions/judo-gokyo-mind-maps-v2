# GitHub Pages publishing — 9 November 2026

The owner authorized GitHub Pages publication of V2. The latest application/text changes are already committed. The original repository and website must remain untouched.

## Prepared

.github/workflows/pages.yml is a manually triggered workflow. It checks the 17 preservation/perspective tests and publishes only web/, excluding planning documents, review records, tools and local QA artifacts. The application uses relative assets and is suitable for a repository subpath. Actions versions were checked against the official actions repositories when preparing this workflow.

The workflow has not been dispatched because Pages is unavailable for the current private repository on the account's plan. No site has been published.

## Observed blocker

The V2 Settings → Pages screen says: “Upgrade or make this repository public to enable Pages.” The repository is private and has_pages is false. No plan, billing or visibility change has been made.

Choose one route before deployment:
- Keep private V2 tracking and publish only the website in a separate public repository.
- Keep V2 private and have the owner upgrade to a GitHub plan supporting Pages from private repositories.
- Explicitly authorize making V2 public, including its history, issues and planning material.

After the chosen route is available, select GitHub Actions as the Pages source, run the prepared workflow, inspect the completed deployment and verify the live site. Keep repository visibility separate from the visibility of the published website.

Planned URL if publishing directly from V2: https://lesthomassolutions.github.io/judo-gokyo-mind-maps-v2/ — not live/verified yet.
