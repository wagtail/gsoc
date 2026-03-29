# Mayank Gupta 

## Introduction
Hi everyone, I’m a Django backend developer with experience in building scalable web applications using Django, REST APIs, and modern frontend tools.

I’m particularly interested in improving developer experience in Wagtail, especially around starter kits and onboarding, where I can make meaningful contributions while learning from the community.
## Links

| Platform | Link |
|----------|------|
| GitHub | https://github.com/Manny2706 |
| LinkedIn | https://www.linkedin.com/in/mayank-gupta-869a94327 |
| My Website | https://mayankgupta-five-lac.vercel.app/ |

## Tasks

### Getting to know Wagtail

- [x] Read our recent posts: [Wagtail nominated for TWO CMS Critic Awards! 🏆](https://wagtail.org/blog/wagtail-nominated-for-two-cms-critic-awards/) (give us a vote!), [Open source AI we use to work on Wagtail](https://wagtail.org/blog/open-source-ai-we-use-to-work-on-wagtail/)
- [x] Sign up for [our newsletter](https://wagtail.org/newsletter/), [our YouTube channel](https://www.youtube.com/@wagtailcms), or follow us [on LinkedIn](https://www.linkedin.com/company/wagtail-cms/), [on Bluesky](https://bsky.app/profile/wagtail.org), or [on Mastodon](https://fosstodon.org/@wagtail)
- [x] Join [our Slack community workspace](http://github.com/wagtail/wagtail/wiki/Slack).

### Google Summer of Code fundamentals

- [x] Read [Advice for People Applying for GSoC](https://developers.google.com/open-source/gsoc/help/student-advice).
- [x] Read [Guidance for GSoC Contributors using AI tooling in GSoC 2026](https://developers.google.com/open-source/gsoc/resources/ai_guidance)
- [x] Read all of Google's [contributor guide](https://google.github.io/gsocguides/student/)
- [x] Read the official [timeline](https://developers.google.com/open-source/gsoc/timeline) and add the most important dates as reminders on your calendar.
- [x] Read our own [7 tips for applying to Google Summer of Code](https://wagtail.org/blog/7-tips-for-applying-to-google-summer-of-code/)
- [x] Introduce yourself on our [GSoC 2026: expression of interest #130](https://github.com/wagtail/gsoc/discussions/130) discussion thread. Keep it short and sweet!

### Open source fundamentals

This checklist helps you demonstrate your understanding of how people use GitHub to collaborate.

- [x] Read through [How to contribute to open source](https://opensource.guide/how-to-contribute/)
- [x] Read [Open source etiquette](https://developer.mozilla.org/en-US/docs/MDN/Community/Open_source_etiquette)
- [x] Make your first pull request with us! Add a new Markdown file inside `2026/participants/` with your GitHub username as the file name. Add the introduction you posted earlier. Submit this to our project as a pull request.
- [x] Read through GitHub's [Markdown formatting documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [x] Now make another pull request to your own README file, adding a Markdown table with links to:
  - [x] Your GitHub profile
  - [ ] Your Mastodon profile if any
  - [ ] Your Bluesky profile if any
  - [ ] Your X profile if any
  - [x] Your LinkedIn profile if any
  - [ ] Your personal website
- [x] Update your pull request to add a new `## Tasks` section to your participant file, and copy-paste our contributor guide's checklists into it, marking each item as completed while you progress.

To stand out as an applicant,

- [x] Help others with their pull requests 
- [x] Demonstrate good awareness of open source etiquette when creating your pull requests (for example, adding an appropriate title and description).

### Learning and research

- [x] Create a new `## Research` section in your personal file inside `2026/participants/`, with a list of links to the resources you've found most useful so far in trying to understand Wagtail as a project and the specific GSoC project idea you're interested in.
- [x] Write a short blog post describing something you've learned recently, and share it with us. The post must be in English, include at least one image, be less than 500 words, and score a Grade 6 or lower on <https://hemingwayapp.com/>. The post has to be posted on a publicly-available platform (Dev.to, Hashnode, Medium, your own website). Link to it from your participant file in this repository.

### Django and Wagtail fundamentals

Here, we recommend you to go through two tutorials to demonstrate your understanding of Django and Wagtail. Submit the code from both projects by adding links to GitHub repositories in your participant file inside `2026/participants/`.

- [x] Go through Django's [Getting started documentation and tutorial](https://docs.djangoproject.com/en/stable/intro/), until part 7.
- [x] Go through Wagtail's Getting started tutorial: [Your first Wagtail site](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)

### Starter kit upgrade

> View the [project idea: Starter kit upgrade](https://github.com/wagtail/gsoc/blob/main/project-ideas.md#starter-kit-upgrade).

- [x] Set up a new project with [the starter kit](https://github.com/wagtail/news-template).
- [x] Set up a new project template / starter kit, with technology choices and demo content of your own choosing. Examples: htmx; Astro; fully static deployment; hosting in PythonAnywhere; portfolio template; photography website.
- [x] Review the contents of the starter kit, and publish a blog post explaining your understanding of its value, as well as might be missing from it.
- [x] Write and share an AI [agent skill](https://agentskills.io/) to help with future maintenance of the project.
- Built a custom starter kit prototype exploring improvements in onboarding and developer experience:
  https://github.com/Manny2706/starterkit-newtemplate-wagtail

## Contributions

To better understand the Wagtail News Template and its real-world challenges, I have actively contributed through multiple pull requests:

- **PR #72 (Merged):** Improved template flexibility by removing a hardcoded project name, making the starter kit more reusable.
- **PR #73 (Open):** Fixed a frontend layout issue causing horizontal scrolling in the homepage hero section.
- **PR #108 (Open):** Added missing frontend templates for `InternalLinkBlock` and `ExternalLinkBlock`, improving consistency and usability of StreamField components.
- **PR #68 (Closed):** Identified a pagination issue caused by missing imports. Although closed as a duplicate, it helped me understand issue tracking and collaboration workflow.

Through these contributions, I have gained familiarity with Wagtail's codebase, template structure, and contribution process, and I am continuing to actively contribute and improve my understanding.


I am also actively exploring open issues and looking for opportunities to contribute further to the project.
## Blog

Improving the Wagtail Starter Kit: My Journey Building a Modern Developer-Friendly Template  
🔗 https://wagtaila-mayank.hashnode.dev/improving-the-wagtail-starter-kit-my-journey-building-a-modern-developer-friendly-template
## Research

- Explored the Wagtail Starter Kit architecture and identified onboarding friction due to multi-step setup and lack of automation.
- Analyzed dependency management issues causing unintended downgrades of Wagtail and Django versions.
- Investigated frontend tooling and found security vulnerabilities (via npm audit) due to outdated dependencies.
- Identified missing or inconsistent frontend templates for StreamField blocks, impacting usability.
- Studied migration from legacy `ModelAdmin` to modern `SnippetViewSet` and `PageListingViewSet` in Wagtail 7.0.
- Evaluated the role of meaningful demo content (`demo.json`) in improving developer onboarding experience.
- Explored CI/CD integration using GitHub Actions to ensure reproducible environments and maintainability.