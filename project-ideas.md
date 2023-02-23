## Project ideas

### RFC 72: Background workers

#### Summary

See [RFC 72: Background workers](https://github.com/RealOrangeOne/wagtail-rfcs/blob/wagtail-background-workers/text/072-background-workers.md)

Wagtail currently doesn't have a first-party solution for long-running tasks. Other CMSs in the ecosystem such as WordPress and Drupal have background workers, allowing them to push tasks into the background to be processed at a later date, without requiring the end user to wait for them to occur.

One of the key goals for this project is removing the requirement for the user to wait for tasks they don't need to.

#### Background

Some tasks done as part of certain Wagtail requests don't need to block the user, and could instead be pushed to the background, improving the perceived responsiveness of the application. Having a first-party solution would also remove the need for downstream users to build a background worker pipeline themselves.

A prime example of this kind of improvement is re-indexing pages. Currently, when a user publishes a page, the "Publish" action also re-indexes the page, which slows down the request unnecessarily. The user doesn't need to wait for the indexes to be updated, meaning they could continue with whatever they need to do next faster. By moving tasks into the background, it also means longer tasks don't tie up the application server, meaning it should be able to handle more editor traffic.

Other CMSs such as WordPress and Drupal have background workers to accelerate these kinds of non-blocking tasks. These APIs allow both for the tools themselves to push tasks to the background, but also for users to submit tasks themselves.

#### Requirements

- Wagtail's background tasks should be opt-in, and Wagtail should function as it does now without it.
- Users should be able to choose from either running a persistent background process, or periodic execution with cron
- Users should have multiple options for task backends, depending on their scale and hosting environment. By default, Redis and Django's ORM should be supported.
- Users should be able to easily add their own tasks to be executed, whether through Wagtail hooks or entirely manually.
- Tasks should be able to specify a priority, so they can be executed sooner, regardless of when they were submitted.
- Users should need to neither know nor care about the specific implementation details. This includes both the implementation details, and which backend is being used (mostly applicable to library authors)

#### Implementation plan

- Create the basic plumbing and base classes required
- Implement ImmediateBackend
- Enable creating wagtail hooks as tasks
- Implement an ORM backend
- Begin migrating background-compatible bits of Wagtail to tasks
- Documentation
- Initial release?
- Complete migrating background-compatible bits of Wagtail to tasks

#### Skills

- Python
- Django
- Performance
- DevOps

#### Mentors

Final list TBC

- Lead: TBC Jake Howard https://github.com/RealOrangeOne
- Support: TBC either Thibaud, Sage, or other core team member

#### Size

175 hours

#### Difficulty rating

Medium

### Greener coding: Wagtail’s climate impact

#### Summary

We’re starting to have a better understanding of the [climate impact of Wagtail](https://github.com/wagtail/wagtail/discussions/8843) as a CMS, and how we can reduce it. We want to integrate our findings into Wagtail’s direction, and make concrete improvements to the project to reduce related carbon emissions.

#### Expected outcomes

The climate impact of Wagtail sites will be measurable with agreed-upon methodologies, and we will do so on a regular basis. By the end of the project, we will have released a number of energy efficiency improvements reducing the impact of Wagtail sites (image optimisation, better caching, scale-to-zero setup).

#### Implementation

We’re wondering if we should consider greater theme-ability as part of this – delivering not just a dark theme but also potentially support for lots of different themes ("dark high contrast", "light high c0ontrast"). Aside from this decision, we can already:

1. Research how leading CMS projects are doing this.
2. Produce a report on the climate impact of Wagtail sites at this point in time.
3. Update our tooling to make it easier to evaluate energy efficiency on a regular basis.
4. Plan 5-10 sustainability-related changes to Wagtail
5. Implement 3-5 of these changes

#### Skills

This project is suitable with a wide range of skillsets, we can adjust tasks accordingly.

- Python
- Django
- Performance
- DevOps

#### Mentors

Mentoring line-up TBC between Chris, Thibaud, Sage, performance team members

- Lead: TBC
- Support: TBC

#### Size

175 hours

#### Difficulty rating

Medium

### Project proposal

You can also propose your own idea. Your proposal should:

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
