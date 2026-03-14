# Aviral Sapra

## Profiles

| Platform | Link |
|---|---|
| GitHub | [AviraL0013](https://github.com/AviraL0013) |
| LinkedIn | [aviral0013](https://linkedin.com/in/aviral0013) |
| Email | aviralsapra13@gmail.com |

## Introduction

Hey everyone! I'm Aviral, a 3rd-year IT student at ABV-IIITM Gwalior, India.

I do full-stack dev (React, Node.js, Python, JavaScript) and have been building stuff for a while now. I'm exploring Wagtail for GSoC 2026, specifically the Starter Kit Upgrade project. I set up the news-template fresh on Windows, went through the codebase properly, and have been contributing fixes as I find issues.

## Tasks

### Getting to know Wagtail
- [x] Read recent blog posts
- [x] Sign up for newsletter / socials
- [x] Join Slack

### GSoC Fundamentals
- [x] Read Advice for People Applying for GSoC
- [x] Read Google's contributor guide
- [x] Read official timeline
- [x] Read Wagtail's 7 tips
- [x] Post intro on discussion thread #130

### Open Source Fundamentals
- [x] Make first pull request (this file!)
- [x] Add Markdown table with profile links
- [x] Add Tasks section (this!)

### Learning & Research
- [x] Add Research section
- [x] Write and publish a blog post - [I Used Wagtail to Organize My Notes About Wagtail](https://wagtail.hashnode.dev/from-wagtail-user-to-wagtail-contributor)

### Django & Wagtail
- [ ] Complete Django tutorial (parts 1–7)
- [ ] Complete Wagtail "Your first Wagtail site" tutorial

### Starter Kit Upgrade - Project Tasks
- [x] Set up a new project with the starter kit (Windows, fresh scaffold)
- [x] Review the contents of the starter kit and publish a blog post

## Contributions

PRs related to this work:

- https://github.com/wagtail/news-template/pull/90 - Fix 30 npm vulnerabilities on fresh install
- https://github.com/wagtail/news-template/pull/91 - Fix Tailwind CSS deprecation warnings on every build
- https://github.com/wagtail/news-template/pull/92 - Fix contact form error messages not rendering

## Research

### Starter Kit Upgrade

I set up the news-template fresh on Windows and went through the whole codebase.
Key findings:

- Fresh install shows 30 npm vulnerabilities before writing a single line of code
- 8 manual steps across two package managers before seeing a homepage
- Wagtail silently downgrades from 7.3 to 6.4 due to stale version pins
- The admin ships with Lorem ipsum everywhere fake author, no images, no date
- ArticlePage StreamField only has 3 block types (Section, Statistics, CTA)
- Wagtail features like autosave, live preview, drag-and-drop are not showcased
- No CI, no Dependabot, no automated tests maintenance is fully manual

Key resources:

- [Wagtail News Template](https://github.com/wagtail/news-template) - studied structure and limitations
- [GSoC 2026 Project Ideas](https://github.com/wagtail/gsoc/blob/main/project-ideas.md)  - scope of Starter Kit Upgrade
- [Wagtail Getting Started Tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)
- [Wagtail Blog: New Starter Kit](https://wagtail.org/blog/new-starter-kit-for-wagtail-cms/)
- [Q&A Discussion #134](https://github.com/wagtail/gsoc/discussions/134) -  maintainer feedback on project direction