# Google Summer of Code 2022

Our application for 2022 is accepted.

**Links**

- [#gsoc on Slack, open to ask us anything](https://github.com/wagtail/wagtail/wiki/Slack)
- [Documentation](http://docs.wagtail.org/)
- [Wagtail blog](https://wagtail.org/blog/)
- Our past projects: [GSoC 2022](https://github.com/wagtail/wagtail/wiki/Google-Summer-of-Code-2022), [GSoC 2021](https://github.com/wagtail/wagtail/wiki/Google-Summer-of-Code-2021)

**Table of Contents**

- [About Wagtail](#about-wagtail)
- [Contributors](#contributors)
- [Organisation admins](#organisation-admins)
- [Mentors](#mentors)
- [Project ideas](#project-ideas)
  - [Toolkit for StreamField data migrations in Wagtail](#toolkit-for-streamfield-data-migrations-in-wagtail)
  - [Make Wagtail editor guide a Wagtail website](#make-wagtail-editor-guide-a-wagtail-website)
  - [Apply new page editor UX to all of Wagtail](#apply-new-page-editor-ux-to-all-of-wagtail)
  - [Windows High Contrast mode support](#windows-high-contrast-mode-support)
- [Canceled projects (archived)](#canceled)
  - Change page type
  - RTL support for Wagtail
  - Create and select related content

# About Wagtail

Wagtail is a popular content management system. It's built on Python, by an active and engaged open source community, which has grown rapidly since Wagtail's release in 2014. Wagtail is available in over 40 languages, and used by some of the world's best-known organizations, including NASA, Google, Mozilla, MIT, and the UK's National Health Service, as well as museums, universities, non-profits, governments, banks, studios, restaurants, startups and bloggers around the world.

Like Python and Django, the technologies which underpin it, Wagtail is known for its welcoming community. We're keen to increase the geographic and cultural diversity of our core team, who are currently spread across Europe, Africa and North America. We seek to offer friendly support on Slack, StackOverflow and Github, and we encourage the community to meet in real life where possible, with recent sprints and conferences held in South Africa, Iceland, the USA, Belarus and the UK.

Wagtail has moved fast in the last few years, with particular focus on the editor experience, the refinement of APIs for headless CMS architectures and accessibility. We have adopted a regular quarterly release cycle, which aims to minimise upgrade time while providing compelling new features and improvements with each point releases. We're seeking help to deliver some of our more ambitious plans, many of which are expressed as [RFCs]. We're also open to your ideas for making Wagtail the best open source CMS for the 2020s!

# Contributors

GSoC is an activity that a contributor (participant) performs as an independent developer. Contributors get a stipend from Google.

Wagtail contributors should:

- Have a good understanding of how GSoC works. Read [Contributor advice](https://developers.google.com/open-source/gsoc/help/student-advice), [Contributor guide](https://google.github.io/gsocguides/student/) and [FAQ](https://developers.google.com/open-source/gsoc/faq).
- Have a basic familiarity with Python, Django and Git.
- Go through the [Wagtail tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html). Let us know if you encounter blockers.
- Create a [development environment](https://docs.wagtail.org/en/stable/contributing/developing.html) for working on Wagtail. There are good instructions in our [official documentation](https://docs.wagtail.org/en/stable/contributing/index.html).
- Join [Wagtail Slack](https://github.com/wagtail/wagtail/wiki/Slack) and introduce yourself on the [#gsoc](https://wagtailcms.slack.com/archives/CTL4SFX29) channel.
- Get to know the Wagtail community. Consider contributing to Wagtail already. Show that you understand how open-source projects work.
- Invest time to discover what project fits you.
- Try to contribute to the project discussion.

## Project proposal

Your proposal should:

- Have a concrete task.
- Give a solid idea of what will constitute success. You tell us.
- Present a detailed design specification.
- Give insight into who you are. If you propose something ambitious, convince us that you are up to the task.
- Give insight into your previous projects and experience.
- Tell us about your experience with Python/Django/Wagtail.
- Provide a schedule, including a detailed work breakdown and major milestones.
- Contain your motivation and curriculum vitae.

Here is an example of [an accepted proposal](https://gist.github.com/chrismedrela/82cbda8d2a78a280a129).

Note:

- The project ideas below are starting points for your submission, but aren’t enough by themselves. You’ll need to come up with a more complete project plan, and use your own words.
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

Contribution guidelines:

- The [code of conduct](https://github.com/wagtail/wagtail/blob/main/CODE_OF_CONDUCT.md) applies to all contributors.
- The [contribution guidelines](https://docs.wagtail.org/en/latest/contributing/index.html#) apply to all contributions.

## Improve your chances of being accepted

The best thing you can do to improve your chances of being accepted as a Wagtail GSoC contributor is to start contributing now. Make yourself known to the community for your contributions. Try to contribute to an area related to your proposal. When the time comes to evaluate applications, you will be a known individual.

We're looking for candidates who can demonstrate that they can engage in the Wagtail project. We're here to help, but we can't watch you every step of the way. We need to see motivation from you. Your activities before the submissions process are the best way to demonstrate this.

# Organisation admins

Dawn Wages and Thibaud Colas are Wagtail organisation admins. They oversee mentors, contributors, and are the point of contact for Google.

To contact Dawn and Thibaud, direct message them on [Slack](https://github.com/wagtail/wagtail/wiki/Slack) @dawn and @Thibaud.

# Mentors

If you're interested in mentoring -- supervising a contributor in work on Wagtail-related activities -- let us know by direct messaging the [organisation admins](#organisation-admins).

---

# Project ideas

Most RFCs are suitable GSoC projects https://github.com/wagtail/rfcs/pulls?q=is%3Apr+label%3AActive+

## Toolkit for StreamField data migrations in Wagtail

For project questions or comments, use [GSoC 2022: Toolkit for StreamField data migrations in Wagtail #8156](https://github.com/wagtail/wagtail/discussions/8156).

### Summary

Wagtail provides a field type for semi-freeform data, StreamField, which uses a JSON representation to store "blocks" of data. While flexible for editors, a pain point for developers has been writing data migrations when changes are made to the block definitions, due to its nested format. This project aims to provide a set of reusable utilities to allow Wagtail implementors to easily generate data migrations for changes to StreamField block structure. It could be extended to cover another common pain point when updating stored data: dealing with live and draft revisions.

### Expected outcomes

Create a package which provides utilities for easily updating StreamFields within data migrations.

### Implementation

- Investigate the existing problems when making a change to StreamField structure
- Set up a new Python package
- Create utilities for recursing through different types of StreamField structure, recognising blocks, and making changes
- Create a set of functions to make appropriate changes for the most common data migration use cases (eg adding a new block with required value, changing the type of a block, or moving a block to within a StructBlock)
- Add documentation for the new library
- Extension: add utilities for updating both the live and draft versions of pages

### Skills

Django, Python.

### Mentors

- Lead: Jacob Topp-Mugglestone https://github.com/jacobtoppm
- Support: Karl Hobley https://github.com/kaedroho
- Support 2: Josh Munn https://github.com/jams2

### Size

175 hours (basic version), but could be extended to deal with more migration types, and to make dealing with live and draft revisions easier.

### Difficulty

Medium

## Make Wagtail editor guide a Wagtail Website

For project questions or comments, use [GSoC 2022: Editor's Guide - Separate Repo or Website #7824](https://github.com/wagtail/wagtail/discussions/7824).

> Final report: [Google Summer of Code: Wagtail Editor Guide](https://wagtail.org/gsoc-2022-editor-guide/)

### Summary

- The goal is to [pull out the existing editor's guide](https://github.com/wagtail/wagtail/discussions/7824) from static documentation to a Wagtail website that can be translated, built upon and even used to generate custom guides for more complex usages of Wagtail.
- The current guide is part of the Wagtail technical documentation - [Using Wagtail: an Editor's guide](https://docs.wagtail.org/en/stable/editor_manual/index.html).
- The audience of the main technical documentation (those who are building with Wagtail) is very different to the audience of the editor's guide (those who are using the editor to edit content, manage permissions, non-technical users).

### Expected outcomes

A dedicated User Guide website with content editors as targeted audience.

### Implementation

- Prepare a Wagtail project
  - Using the [Wagtail cookiecutter package](https://github.com/wagtail/cookiecutter-wagtail-package)
  - Pull out the existing RST/MD files into a stand-alone Wagtail website, starting with the [Wagtail project cookiecutter](https://github.com/wagtail/cookiecutter-wagtail-package)
  - Break up the existing content and screenshots into Django views and URLs so that the content can be used in translation tools such as transifex, the output should be a static HTML/CSS/JS bundle. This could use some of the Wagtail primitives for page editing but it does not have to.
- Improve the guide
  - Target specific audiences
  - Make translatable, possibly using individual template parts to 'hold' the translatable content using Transifex (translation of content is not in scope)
  - Make it version-able (so that older versions of the Wagtail editor's can be available)
  - Potentially rework content to be less nested or easier to read through, see [Firefox's How do I Wagtail](https://foundation.mozilla.org/en/docs/how-do-i-wagtail/) for inspiration
- Make the guide maintainable (extended goal)
  - Automatic screenshots
  - Accept contributions from non-technical users, this can either be a documented reference to where each content is located in Github or more advanced such as a hosted version of Wagtail that outputs changes to submit to Github
  - Set up a nightly CI that runs against Wagtail master
  - Add a feedback option (measure happiness), this itself could submit issues to Github or email
- Make it extendable (extended goal)
  - The website will be open source. Add an option to download a snapshot of the content.

### Skills

- Python
- Django
- Translations - speaking a second language would be helpful
- Static site building (with Django or Node tooling)

### Mentors

- Lead: Phil Dexter https://github.com/phildexter
- Support: Coen van der Kamp https://github.com/allcaps
- Support: Meagen Voss https://github.com/vossisboss
- Support: Thibaud Colas https://github.com/thibaudcolas

We will supply a primary mentor and at least two secondary mentors to support the participant.

### Size

Expected size of project 175 hours.

### Difficulty rating

Medium

## Apply new page editor UX to all of Wagtail

For project questions or comments, use [GSoC 2022: Apply new page editor UX to all of Wagtail #8158](https://github.com/wagtail/wagtail/discussions/8158).

### Summary

This project idea is a follow-up to Wagtail’s [Page editor 2022](https://github.com/wagtail/wagtail/discussions/7739) project, as part of which we are modernizing Wagtail’s page editor. This redesign focuses on the page editor, incorporating long-awaited UX improvements, accessibility fixes, and new features. We now want to roll out similar improvements to other parts of Wagtail.

### Expected outcomes

Consistent UX throughout the whole of Wagtail, using our modern visual language, powered by a design system. Long-standing accessibility issues are fixed, and Wagtail is well on its way to [WCAG 2.1 AA](https://github.com/wagtail/wagtail/projects/5) conformance.

### Implementation

1. Review the page editor redesign.
2. Plan for application of the new UX & particular UI components to other parts of Wagtail.
3. Liaise with our [UI](https://github.com/wagtail/wagtail/wiki/UI-team) and [accessibility](https://github.com/wagtail/wagtail/wiki/Accessibility-team) teams.
4. Update our UI build and testing tools to sustain this work.
5. Roll out UI improvements either component-by-component, or view-by-view.

### Skills

- Accessibility
- HTML, CSS, SVG
- JavaScript, TypeScript
- React
- UI development tooling
- UI testing

### Mentors

- Lead: LB Johnston https://github.com/lb-
- Support: Helen Chapman https://github.com/helenb
- Support: Thibaud Colas https://github.com/thibaudcolas

### Size

175 or 350 hours depending on candidate proposal

### Difficulty rating

Medium.

## Windows High Contrast mode support

For project questions or comments, use [GSoC 2022: Windows High Contrast mode support #8193](https://github.com/wagtail/wagtail/discussions/8193).

### Summary

Roll out Windows High Contrast mode (also known as Contrast Themes) support to all of Wagtail. This is a continuation of [existing work](https://wagtail.org/blog/state-of-wagtail-accessibility/) from Wagtail’s accessibility team.

### Expected outcomes

The whole of the Wagtail administration interface will work as well as possible for users of Windows High Contrast mode. Wagtail’s UI development methodology now takes it into account for future features, in a sustainable way.

### Implementation

We’re wondering if we should consider general theme-ability as part of this – delivering not just High Contrast mode but also potentially a dark theme for Wagtail, potentially custom color theming capabilities. Aside from this decision, we can already:

1. Review how the admin UI works currently in High Contrast mode.
2. Research how leading projects are doing this.
3. Update our contributor documentation with appropriate guidelines.
4. Update our tooling to make it easier to support and test those types of changes.
5. Roll out fixes & improvements to existing UI components.

We are expecting the types of changes needed to be simple once identified, but there is an important planning element here to make sure we do the most sensible changes, at the appropriate level of abstraction.
We also want to make sure any changes for WHCM support are made in a way that works for future development.

### Skills

- Accessibility
- HTML, CSS, SVG
- JavaScript
- UI development tooling

### Mentors

- Lead: Jane Hughes https://github.com/janehughes
- Support: Scott Cranfill https://github.com/Scotchester
- Support 2: Thibaud Colas https://github.com/thibaudcolas

### Size

175 hours

### Difficulty rating

Medium

---

# Canceled

<details>

<summary>Click to expand</summary>

## Change page type

### Motivation for cancellation

This project is canceled because:

1. Too complex.
2. There are too many Wagtail internals involved.
3. Many third-party packages will break.
4. There are no mentors available

The core-team suggests to develop a third-party package first.

### Summary

Make it possible for a content editor to change the content type of a page.

This is an often requested feature, but is technically hard to implement.

### Expected outcomes

A user interface and backend logic to allow switching page type.

### Implementation

Here is a very rough, high-level idea for what the user experience could look like:

1. Select "change page type" action on a page
2. Choose new page type from a list (borrowed from the New Page type selection screen)
3. New "visual data migration" UI appears showing original page's fields on left (more condensed than standard edit view) and new page's fields on right
   - _(this is where the major front-end complexity is)_
4. Fields with same name and type automatically have data copied over to new page
5. Fields that have no match are highlighted on the left to prompt user to manually copy that data over to a field on the right (or acknowledge that that data will be lost)
6. Once satisfied with the data in the new page model on the right, click the done/save/go/whatever button at the bottom to execute the behind the scenes magic needed to change the type
   - _(and this is where the major back-end complexity is)_
   - Would be good to store a copy of the changed page in some archive location, so it can be restored in case of emergency

There is obviously a lot of complexity not touched on here, especially on the back end, but this outlines what I think would be a good workflow for users.

This should likely be initially developed as a standalone package before determining if it makes sense to bring it into core.

### Skills

- Django
- Wagtail
- Django Tree

## RTL support for Wagtail

This project is canceled because:

1. Wagtail is working on a new page editor. The work clashes with this project.
2. Wagtail core-team and mentors find other projects more important.

### Summary

Wagtail’s administration interface currently has poor support for right-to-left languages, such as Arabic and Hebrew. We have been wanting to fix this for a while ([#1240](https://github.com/wagtail/wagtail/issues/1240)), and now have a great opportunity to do so with [CSS logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties).

### Expected outcomes

The Wagtail UI supports Arabic, Hebrew, and other right-to-left languages.

### Implementation

We want to refactor Wagtail’s stylesheets to use CSS logical properties, Flexbox, and Grid layout, so the styles can be written agnostic to the writing direction of the language – browsers would then automatically display the correct end-user layout based on the target language.

### Skills

HTML and CSS. Bonus: user experience, visual design, Django.

### Mentors

- Lead: Thibaud Colas https://github.com/thibaudcolas
- Support: Coen van der Kamp https://github.com/allcaps
- Support 2: TBC

We will supply a primary mentor and at least two secondary mentors to support the participant.

### Size

Expected size of project approximately 350 hours.

### Difficulty rating

Medium

## Create and select related content

### Motivation for cancellation

This project is canceled because:

- Too many of the pieces --it would depend on-- are in flux.

For project questions or comments, use [GSoC 2022: Create and select related content #8157](https://github.com/wagtail/wagtail/discussions/8157).

### Summary

**Django**

Django has a way to select related content AND create, update and delete related content _without leaving the current form_. It does this by opening new windows.

See this video illustrating the differences between Django and Wagtail related objects.

https://user-images.githubusercontent.com/1969342/158978211-db1a7dda-12cb-4bc5-84e9-2efccf53fdfd.mp4

A select field in Django has a create (plus), edit (pencil) and delete (red cross). It opens a new window that allows performing CRUD actions.

Also, Django raw id field has a search loop. It opens a chooser in a new window. It re-uses the model admin list view. Advantages are:

- Enables custom list fields, search and filter.
- Pagination.
- With a lot of content, you don't have to render all select options in the current form. Boosting performance.

**Wagtail**

Creating related content in Wagtail involves tedious and annoying steps:

1. You need to navigate away from the current form (losing your work).
2. Create the related object.
3. Go back to the initial form and recreate all content.

Forms with many fields have the chance of losing a lot of work. There is also a chance that the user is required to repeat steps 1-3 a couple of times. There might be multiple required related object fields.

The current Wagtail snippet chooser opens a modal. The modal:

- Does support content selection
- Does not support CRUD actions
- Does not re-use the list view (like Django does). Customisation of list fields, search, and filter is hard/impossible.
- Wagtail has no `raw_id_fields`.

### Expected outcomes

This GSOC project is about related object selection and CRUD in Wagtail:

- Create a chooser window that re-uses the ModelAdmin list view.
- Create related object CRUD views. They open in a new window.
- Respect user permissions on the related objects.
- Make nested related object CRUD (multiple windows) possible.
- Introduce RAW id field.

### Skills

- Django
- Wagtail
- HTML/CSS/JS

### Mentors

- Lead: TBC – Coen van der Kamp https://github.com/allcaps
- Support: TBC
- Support 2: TBC

### Size

Expected size of project 175 hours.

### Difficulty rating

Medium
