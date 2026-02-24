# [Google Summer of Code: Wagtail Editor Guide](https://wagtail.org/blog/google-summer-of-code-wagtail-editor-guide/)

During Google Summer of Code, I worked on building a standalone website for the Wagtail Editor's guide that will make it easier for Wagtail users to find information about how to use the CMS. This is my final report for the project.

## About the project

The primary goal of my Google Summer of Code (GSoC) project was to create a standalone site for the [Wagtail’s Editor guide](https://docs.wagtail.org/en/v4.0.1/editor_manual/index.html). The current Editor’s Guide is defined in code. You need to know Markdown, Git, and Sphinx to contribute to it. Therefore, our team decided to convert this part of the technical documentation to a standalone Wagtail website. The result is a site that will make it easier for content editors to contribute their ideas. We also added translations, live search, and a feedback system. The site is built completely on Wagtail and Django.

## Links

- Live site: [https://wagtail.org/editor-guide-site](https://wagtail.org/editor-guide-site)
- GitHub: [https://github.com/wagtail/guide](https://github.com/wagtail/guide)
- Discussions: [https://github.com/wagtail/guide/discussions](https://github.com/wagtail/guide/discussions)

## Before and after

### Landing page

Here is the page users of the site would land on in the existing documentation (before, left), and in the new dedicated Guide site (after, right).

![Editor Guide landing page before-after](https://media.wagtail.org/images/Group_3.original.width-950.png)

The new Guide will make it possible to group different resources intended for users of the Wagtail content management system (CMS) in one place rather than having it mixed in with developer-focused documentation.

### Content page

Here are screenshots of a sample page as it appears to users of the site within the existing documentation site for developers (before, left), and as part of the new Guide site (after, right).

![Editor Guide editing experience before-after](https://media.wagtail.org/images/image4.original_h3jXWCq.width-950.png)

The page is much simpler, and features like search and navigation only show resources that are relevant to users of the CMS, rather than developer-focused content.

Here is what the editing experience for this same page looks like in GitHub with Markdown files (left, before), and with the new Guide site (right, after).

For people who don’t know Markdown and Git / GitHub Pull Request workflows, editing the docs was daunting. Using a CMS with rich text fields and a live preview, it’s simpler to author learning materials.

## How we did this

### Technologies

- Django, Wagtail
- Heroku
- Bootstrap

### Methodology

- [**GitHub Projects**](https://github.com/orgs/wagtail/projects/4/views/1): We used **GitHub Projects** to manage, assign, and keep track of tasks. We divided the tasks on a weekly basis.
- [**GitHub Discussions for feedback**](https://github.com/wagtail/guide/discussions): Things like design, new features etc. that needed discussion and different opinions to work on were managed using GitHub Discussions.
- **Weekly catch-ups**: We used to have 2 meetings per week. A 30 min meet on Tuesdays and a 60 min meet on Fridays. Weekly planning and assigning tasks were done in Tuesday’s meeting. Detailed discussion about any topic, bug or feature, discussing any doubts or concerns were done in Friday’s meeting.
- [**Timeline**](https://docs.google.com/spreadsheets/d/1xNA9G2w_8C3IRoeKNZZiQCTJBr7RyVGMPVIBKZVYXxQ/edit#gid=0): We prepared an initial timeline and tried to follow it as much as possible.

## Learnings

I learned several things throughout the project. I have stated some of the things I found particularly interesting or enjoyed working on.

### GitHub Actions

This was the first time I built a [GitHub CI/CD pipeline](https://github.com/wagtail/guide/actions). I knew the concept of pipelines before but I read about it in depth to properly implement it. The implementation wasn’t very large but I enjoyed working on it.

### Live search

Search is a feature in the project. It fetches and displays results in real time as a user types in the search box. I enjoyed brainstorming methods to implement it. The concept I learned and found particularly interesting was [Debounce/Throttling](https://css-tricks.com/debouncing-throttling-explained-examples/). It helped me manage the requests sent to the backend while implementing live search (see [pull request #35](https://github.com/wagtail/guide/pull/35)).

![Editor Guide live search](https://media.wagtail.org/images/image6.original_wGLcK5M.width-950.png)

## Feedback system

The users should be able to submit feedback on the website. I implemented a simple system that enables users to do the same. I got some experience tweaking Django views to handle both GET and POST requests on the same URL. During this work, I faced an issue regarding _csrf tokens_. I learned how to fetch a CSRF-token in JavaScript that can be passed in a request header to avoid an issue covered [in the Django documentation](https://docs.djangoproject.com/en/4.1/howto/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false).

For users of the site, the form is very simple:

![Editor Guide feedback form](https://media.wagtail.org/images/image3.original_nomh0y4.width-500.png)

And in the CMS, we can see all submissions:

![Editor Guide feedback submissions](https://media.wagtail.org/images/image2.original_BnezB3g.width-950.png)

## Tests

One thing that was always missing in my projects before GSOC were automated tests. I gained some very useful experience in writing tests in a Django/Wagtail project. I also got to know about a package that can determine the test coverage in a project. I added it to the GitHub CI/CD so that one can inspect the test coverage (see [pull request #45](https://github.com/wagtail/guide/pull/45) for an example).

## Thanks

Thank you for the opportunity to work on this project. I would like to thank my amazing mentors who taught me a lot and who made valuable contributions to this project.

- [Coen van Der Kamp](https://github.com/allcaps)
- [Meagen Voss](https://github.com/vossisboss)
- [Phil Dexter](https://github.com/phildexter)
- [Sage Abdullah](https://github.com/laymonage)
- [Thibaud Colas](https://github.com/thibaudcolas)

I liked to continue working on open source and am sure I’ll see you all around! 👋
