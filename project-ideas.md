# Project ideas

## Alt text capabilities

### Summary

Wagtail already supports defining alt text for images, but we think the user experience could be improved. In particular, the _default_ user experience out of the box needs to have better support for defining alt text in the context where the image is used. Since we want to change default behavior, this will need careful backend design and implementation, considering current accessibility best practices, database modelling possibilities, and innovations in the realm of artificial intelligence to automate the creation of image descriptions.

### Expected outcomes

A revamped user experience when setting alt text in Wagtail, with clear path for site implementers to follow best practices, and a clear way to leverage AI-driven alt text automation.

### Implementation

The project will involve refining the current contextual alt text RFC, liaising with the accessibility team, and with AI experts, to first design the best possible UX, database modeling, and Django APIs. Then, implementation of those designs, and finally, testing and documentation.

### Skills

- Django
- Wagtail
- Accessibility
- Desirable: Image-to-text AI models

### Mentors

- Lead: Storm Heg https://github.com/Stormheg
- Support: Saptak Sengupta https://github.com/SaptakS

### Size

Expected size of project approximately 350 hours.

### Difficulty rating

Medium

## Low-carbon accessible project templates

### Summary

Creation of new project templates for Wagtail. We want to demonstrate how to build Wagtail websites that:

1. Have as low of a carbon footprint as possible.
2. Are accessible to as many people as possible.
3. Follow all performance and SEO best practices.

The technology stack or stacks used to achieve this are to-be-determined, though we have a bias towards static site hosting, scale-to-zero backends, and hybrid client/server rendering. We welcome proposals on a specific stack or an interest in leaving it open based on preliminary research on which stack is best suited for the task.

### Implementation

After preliminary research to review stack options and selection criteria (in particular lowest possible carbon footprint), we will start development of the project template(s). The project template(s) will be rated based on a benchmark suite to be determined with the mentor team.

### Skills

- Wagtail
- Digital sustainability
- Desirable: JAMstack, React/Next.js, 11ty, HTMX, SQLite, FaaS
- Desirable: Accessibility

### Mentors

- Lead: Thibaud Colas https://github.com/thibaudcolas
- Support: Sherry https://github.com/shyusu4

### Size

We will welcome proposals for 90 hours (one project template), 175 hours (two project templates to compare), or 350 hours (3-4 project templates explored in depth).

### Difficulty rating

Medium

### Summary

## Change page type

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

### Mentors

- Lead: TBC - Thibaud Colas https://github.com/thibaudcolas

We will supply a primary mentor and at least two secondary mentors to support the participant.

### Size

Expected size of project approximately 350 hours.

### Difficulty rating

Medium

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
