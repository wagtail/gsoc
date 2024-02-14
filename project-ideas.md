# Project ideas

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

- Lead: Thibaud Colas https://github.com/thibaudcolas
- Support: Coen van der Kamp https://github.com/allcaps

We will supply a primary mentor and at least two secondary mentors to support the participant.

### Size

Expected size of project approximately 350 hours.

### Difficulty rating

Medium

## Create and select related content

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

### Size

Expected size of project 175 hours.

### Difficulty rating

Medium

## Enhanced file manager

### Summary 

TBD

### Implementation

TBD

### Skills

TBD

### Mentors

TBD

### Aims

TBD


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
