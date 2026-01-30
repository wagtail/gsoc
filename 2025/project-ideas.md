# Project ideas

## Multilingual support overhaul

### Summary

Wagtail is close to being compatible with strict [Content Security Policies](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP). With one final push, we can get fundamental features all compatible with CSPs, document support, and treat any gaps as bugs.

For more information, see:

- [CSP compatibility issues #1288](https://github.com/wagtail/wagtail/issues/1288)
- [A list of widgets breaking strict Content-Security-Policy (CSP) directives #7053](https://github.com/wagtail/wagtail/issues/7053)
- [Wagtail Stimulus Adoption Schedule (2022-25) 🎛️](https://docs.google.com/spreadsheets/d/1LdrXlj8OeCWy3B_moYZ-ynhfZZtFVHPahG9GFoT-XBs/edit).

### Expected outcomes

- Addressing any remaining CSP issues in Wagtail.
- Providing official recommendations for compatible CSP settings.
- Ensuring essential functionality works with a strict CSP.
- Documenting or backlogging all CSP-related issues.
- Adding a strict CSP to wagtail.org.

### Implementation

This will require reviewing existing issues and technical discovery work to devise a plan for addressing them. Understanding options in [django-csp](https://github.com/mozilla/django-csp), and possibly trialing any changes with [core Django CSP support](https://github.com/django/django/pull/18215).

The changes required will be a mix of front-end and backend work, and require expertise with security fundamentals to understand what is needed.

### Skills

- Django
- JavaScript
- Security headers
- CSP
- Cross-site scripting
- Technical writing

### Mentors

- Lead: TBC - Sage Abdullah
- Support: TBC
- Support: TBC

### Size

Expected size of project approximately 350 hours.

### Difficulty rating

High

## Grid-aware websites

### Summary

We want to trial the [grid-aware websites](https://wagtail.org/blog/reflections-on-grid-aware-websites/) concept on a real Wagtail project: the [wagtail.org website](https://wagtail.org/). This will involve understanding what grid awareness means for websites, how to implement it with Wagtail, and how to measure the website’s energy use depending on different adaptations.

### Expected outcomes

- A grid-aware version of the wagtail.org website.
- A blog post explaining the process and outcomes.
- A report on energy use of different website front-end and back-end components.
- A set of recommendations for other Wagtail websites to become grid-aware.

### Implementation

This is highly dependent on the outcome of the ongoing grid-aware websites project, which is currently under way. More information will be available in March 2025.

### Skills

- JavaScript
- Django
- Cloudflare workers
- Digital sustainability
- Performance auditing

### Mentors

- Lead: Thibaud Colas
- Support: TBC
- Support: TBC

### Size

Expected size of project approximately 350 hours.

### Difficulty rating

High

## Project proposal: your own idea

You can also propose your own idea. Your proposal should:

- Have a concrete task.
- Give a solid idea of what will constitute success. You tell us.
- Present a detailed design specification.
- Give insight into who you are. If you propose something ambitious, convince us that you are up to the task.
- Give insight into your previous projects and experience.
- Tell us about your experience with Python/Django/Wagtail.
- Provide a schedule, including a detailed work breakdown and major milestones.
- Contain your motivation and curriculum vitae.

Here is an example of [an accepted proposal](https://gist.github.com/chrismedrela/82cbda8d2a78a280a129) on Django.

Note:

- The project ideas above are starting points for your submission, but aren’t enough by themselves. You’ll need to come up with a more complete project plan, and use your own words.
- Do not feel limited to the project ideas below.
- If you have a project idea not listed, please direct message the [organisation admins](#organisation-admins). They can test the project eligibility and pair you with a mentor for initial feedback.

Project proposals should fall into one of three categories:

- Work on Wagtail itself. The core product.
- Work on tools to support Wagtail. Example: Editor guide as a Wagtail website.
- Wagtail third-party libraries. Example: [Wagtail Live](https://github.com/wagtail/wagtail-live) is a GSOC 2021 project.

The project you propose should be:

- Something useful for the Wagtail project
- A single well-scoped project
- Achievable within the time of GSoC
- And something the core developers can help mentor you on.

## Template: project idea title

### Summary

### Expected outcomes

### Implementation

### Skills

### Mentors

- Lead: TBC
- Support: TBC

### Size

Expected size of project approximately 350 hours.

### Difficulty rating

Low / Medium / High
