# Pranav Sharma

## Introduction

Hi, I'm Pranav Sharma, a 2nd-year CSE student from RBU, India.
I'm interested in the Demo Website Redesign project. I've been contributing to bakerydemo by setting up the project locally, building a `generate_people` management command, filing and fixing [#699 (BreadPage missing search_fields)](https://github.com/wagtail/bakerydemo/issues/699), and reporting Docker-related issues [#692](https://github.com/wagtail/bakerydemo/issues/692).

I also built AutoVault, a Wagtail CMS supercar encyclopedia, as a portfolio project to deepen my understanding of Wagtail's page models, search, and StreamField.

**GitHub:** https://github.com/Pra26nav
**LinkedIn:** https://www.linkedin.com/in/pranav-sharma-791568321

## Tasks

### Getting to know Wagtail

- [X] Read our recent posts: [Wagtail nominated for TWO CMS Critic Awards!](https://wagtail.org/blog/wagtail-nominated-for-two-cms-critic-awards/), [Open source AI we use to work on Wagtail](https://wagtail.org/blog/open-source-ai-we-use-to-work-on-wagtail/)
- [X] Sign up for [our newsletter](https://wagtail.org/newsletter/), [our YouTube channel](https://www.youtube.com/@wagtailcms), or follow us [on LinkedIn](https://www.linkedin.com/company/wagtail-cms/)
- [X] Join [our Slack community workspace](http://github.com/wagtail/wagtail/wiki/Slack)

### Google Summer of Code fundamentals

- [X] Read [Advice for People Applying for GSoC](https://developers.google.com/open-source/gsoc/help/student-advice)
- [X] Read [Guidance for GSoC Contributors using AI tooling in GSoC 2026](https://developers.google.com/open-source/gsoc/resources/ai_guidance)
- [X] Read all of Google's [contributor guide](https://google.github.io/gsocguides/student/)
- [X] Read the official [timeline](https://developers.google.com/open-source/gsoc/timeline)
- [X] Read [7 tips for applying to Google Summer of Code](https://wagtail.org/blog/7-tips-for-applying-to-google-summer-of-code/)
- [X] Introduce yourself on our [GSoC 2026: expression of interest #130](https://github.com/wagtail/gsoc/discussions/130) discussion thread

### Open source fundamentals

- [X] Read through [How to contribute to open source](https://opensource.guide/how-to-contribute/)
- [X] Read [Open source etiquette](https://developer.mozilla.org/en-US/docs/MDN/Community/Open_source_etiquette)
- [X] Make your first pull request with us! Add a new Markdown file inside `2026/participants/` with your GitHub username as the file name
- [X] Read through GitHub's [Markdown formatting documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### Demo website redesign

- [X] Pick up and address an [existing issue](https://github.com/wagtail/bakerydemo/issues) on the site — fixed [#699 BreadPage missing search_fields](https://github.com/wagtail/bakerydemo/issues/699)
- [ ] Create new content fixtures for the existing demo, which allow testing with another theme than bread
- [ ] Create a new alternative visual look for the website, with its existing content
- [ ] Write and share an AI [agent skill](https://agentskills.io/) to help with future maintenance of the project

## Research

### Resources for understanding Wagtail and the Demo Website Redesign

1. [Official Wagtail Getting Started Guide](https://docs.wagtail.org/en/stable/getting_started/index.html) — covers initial setup and project structure
2. [Official Wagtail Tutorial](https://docs.wagtail.org/en/stable/tutorial/index.html) — in-depth walkthrough of core Wagtail concepts
3. [Django Getting Started Documentation](https://docs.djangoproject.com/en/stable/intro/) — Django fundamentals up to part 7
4. [Wagtail StreamField documentation](https://docs.wagtail.org/en/stable/topics/streamfield.html) — understanding StreamField for content-heavy pages
5. [Wagtail Search documentation](https://docs.wagtail.org/en/stable/topics/search/index.html) — how search_fields and indexing work in Wagtail
6. [bakerydemo repository](https://github.com/wagtail/bakerydemo) — the project I'm contributing to directly
7. [Wagtail GitHub repo](https://github.com/wagtail/wagtail) — understanding Wagtail's implementation and design decisions

### Project idea

The Bakery Demo website redesign — I'm particularly drawn to this project because of the hands-on work I've already done in the bakerydemo codebase. I've set up the project locally via Docker, built a `generate_people` management command using Faker, fixed [#699 (BreadPage missing search_fields)], and reported Docker-related issues [#692]

To deepen my understanding of Wagtail's architecture before applying, I built **AutoVault** — an original Wagtail CMS supercar encyclopedia from scratch, covering 12 combustion-engine brands with custom page models, StreamField content, a full search implementation, a dark luxury editorial frontend, and a 52-test suite. Building AutoVault taught me exactly how content-heavy page types like `BreadPage` need to be carefully designed, including proper `search_fields`, rich StreamField bodies, and thoughtful template structure.

This direct experience with both bakerydemo and a self-built Wagtail project gives me a strong foundation to contribute meaningfully to the Demo Website Redesign — not just fixing bugs, but rethinking how the demo can better showcase real-world Wagtail capabilities.

### My project planning notes

I mapped out the current state of bakerydemo vs the proposed redesign:

**Current state:**
- HomePage, Breads, Blog, Locations, Recipes, Gallery, About, Contact
- Our People app — exists but draft/unpublished
- Press Releases app — does not exist
- Events app — does not exist
- No modern CSS system
- No programmatic content generation

**Proposed:**
- All existing sections retained and published
- New vanilla CSS system with custom properties
- Our People — published and live
- Press Releases app — new page models and views
- Events app — date-based
- `generate_content` management command using Faker
- Realistic demo content across all page types