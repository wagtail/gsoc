# [Open source internship: UX Unification](https://wagtail.org/blog/open-source-internship-ux-unification/)

I contributed over 50 pull requests to Wagtail this summer through the UX Unification project. Here, I'll tell you more about the project and the improvements I contributed.

![GSoC UX Unification - Dashboard 4.0](https://media.wagtail.org/images/image11.original.width-900.png)

## About the project

I'm Paarth Agarwal, a seasoned open-source developer pursuing my undergrad degree at the Indian Institute of Technology (BHU), Varanasi. The Wagtail community selected me to work on the UX Unification of Wagtail, alongside other Google Summer of Code projects.

My project, UX Unification of the Wagtail CMS, primarily involved applying the new Page Editor redesign to large swaths of Wagtail and making the CMS more accessible.

During the project, I applied shared templates across the whole CMS, worked with the Python backend, modified existing components and functions, created new ones, and added components to the Wagtail pattern library for smoother testing. I also did some heavy unit testing with Jest and Python Testing. As a result, we ended up making Wagtail more maintainable and accessible than ever before.

## The team behind the project

The team for the UX Unification project included myself as well as LB (Ben) Johnston from Virgin Australia as the lead mentor and Helen Chapman and Thibaud Colas from Torchbox as supporting mentors. This is my description of our coding journey!

![GSoC UX Unification - Zoom call screenshot. Thibaud in the top left, Paarth in the top right, LB in the bottom left, Helen in the bottom right. All smiles](https://media.wagtail.org/images/Screenshot_90_modified.original.width-950.png)

## My major wins

- I'm now number 21 in the list of [top contributors to Wagtail](https://github.com/wagtail/wagtail/graphs/contributors), even though I only started contributing this year. I contributed over 55 pull requests (PRs), 59 commits, and 25 resolved issues to the main Wagtail repository.
- Out of all the redesign work, the sign-in page was my favourite one because it's the first page that the user sees while using Wagtail, and the new design is really beautiful.
- I’ve written many tests and added components to the Wagtail pattern library (which uses Storybook).
- I replaced hard-coded components with shared templates using Django templating, which will continue to make development easier for future contributors.
- Two of the oldest issues I closed were from 2017 - [Delete buttons have inconsistent styling #3823](https://github.com/wagtail/wagtail/issues/3823) & 2016 - [Visual design of login screen #2309](https://github.com/wagtail/wagtail/issues/2309)
- I resurrected two old PRs, modified them, and prepared them to be merged - [Add functionality to reorder pages with keyboard #5785](https://github.com/wagtail/wagtail/pull/5785) & [Support twitter previews in Draftail embeds #5176](https://github.com/wagtail/wagtail/issues/5176).
- Other than the main repository, I contributed to other Wagtail repositories, which took my PR count up to 73!

## Major visual changes that I made

### Sign in page before

![GSoC UX Unification - Sign in 3.0](https://media.wagtail.org/images/image8.original_asoNWpc.width-500.png)

### Sign in page after

![GSoC UX Unification - Sign in 4.0](https://media.wagtail.org/images/image1.original_JxnEiUW.width-500.png)

### Dashboard page before

![GSoC UX Unification - Dashboard 3.0](https://media.wagtail.org/images/image12.original.width-500.png)

### Dashboard page after

![GSoC UX Unification - Dashboard 4.0](https://media.wagtail.org/images/image11.original.width-500.png)

### Page listing before

![GSoC UX Unification - Page listing 3.0](https://media.wagtail.org/images/image9.original.width-500.png)

### Page listing after

![GSoC UX Unification - Page listing 4.0](https://media.wagtail.org/images/image6_D9kmPDG.original.width-500.png)

### Form submissions listing before

![GSoC UX Unification - Form submission listing 3.0](https://media.wagtail.org/images/image2_V7K3LTf.original.width-500.png)

### Form submissions listing after

![GSoC UX Unification - Form submission listing 4.0](https://media.wagtail.org/images/image10.original.width-500.png)

### Buttons

Coming in Wagtail 4.1

![GSoC UX Unification - Buttons 3.0](https://media.wagtail.org/images/image4_x6lWDaL.original.width-500.png)

![GSoC UX Unification - Buttons 4.0](https://media.wagtail.org/images/image7.original_0cTHBhf.width-500.png)

### Technologies I used

- Django, React
- Jest Unit Testing
- Python Unit Testing
- Pattern Library (Storybook)
- SAAS, BEM Classes, IT CSS
- Tailwind
- Python Backend

## How I got here

The most precise answer for how I got involved in Wagtail is that I hitchhiked to Wagtail and started contributing to it like crazy! I started contributing to open source during Hacktoberfest 2021. Since then, I’ve been involved with many organisations like [Circuitverse](https://github.com/CircuitVerse) and [Purr Data](https://agraef.github.io/purr-data/) until I found Wagtail in March. I was astonished when I got to know more about Wagtail. Everything felt perfect. Wagtail has a fantastic community on Slack filled with awesome folks, well-described issues and a near-perfect CI! What made me stick to it is its tradition of adding people’s names to the contributor's list no matter how small you think your contribution is. This kind of appreciation is uplifting, and it became part of my initial motivation to go above and beyond while working on my project.

One of the most memorable moments during the pre-coding period was when my mentor LB told me I was doing well and asked me if I needed any review or help with my proposal. By the end of the pre-coding period, I made 25 PRs in 5 Wagtail repositories. One of the repositories I’ve worked on was “stylelint-config-wagtail” and I basically wrote rules for the Wagtail CI.

Since then:

![Harry Potter meme about linting in Pull Requests](https://media.wagtail.org/images/image3.original.width-500.jpg)

## The coding period

After my project was selected to be sponsored by Torchbox, my mentors congratulated me, and we started moving ahead with the project. LB put up a GitHub Projects board and helped refine my proposed plan. He also set meeting times at everyone’s convenience, which was hard since we all live in different time zones across India, Australia, and the UK. Thanks to his organisation skills, we never lost sight of our goals. I was also invited to be a part of the UI team, which I gladly accepted. We held weekly meetings, i.e. two 1.5-hour meetings with me and LB as participants called mentoring sessions and two 40 mins long stand-ups with all four of us. In stand-ups, we used to decide on broader goals and discuss our approaches, and in the mentoring meeting, LB and I would go through issues thoroughly. In the middle of the coding period, I moved to college to take classes in person instead of online mode.

Looking back, I can say that starting with anything new was challenging because Wagtail’s codebase is large. I would get comfortable with a few files in some directory, and suddenly there was a shift to a new directory that caused some friction. I was afraid of writing unit tests and was hesitant about backend work. The only reason I overcame all that was my mentors’ support and their confidence in my ability to _figure it out along the way._ I was so proud when I wrote my first unit test by myself, and seeing my PRs getting bigger has been satisfying. Thibaud even made a tweet [celebrating the merging of my 50th PR](https://twitter.com/WagtailCMS/status/1547949511737192449) in Wagtail!

These were perhaps my most productive summers. I got to learn Django better, learned Jest, Python Unit testing and Storybook (Pattern Library), which were utterly unknown to me. I became more proficient with GitHub, Linux commands and VSCode. I also had the chance to learn about Tailwind and BEM Classes and their importance for a long-lived project. Other than that, I moved to college to attend classes in person for the first time since COVID. Managing college and development together was challenging, but we made it work.

I consider myself lucky because a key thing about my project is that it was large and touched almost every part of Wagtail, due to which I got to interact with practically the whole Wagtail team either through PR reviews, discussion on issues, UI team meetings or through entire team meetings. Above anything else, I wish to sustain our connection with each other and do some fun projects again!

## What’s next

For the UX unification project, a list of pending issues has been added to UI that are up for grabs: [UI up-for-grabs (github.com)](https://github.com/orgs/wagtail/projects/6/views/8)

As for what's next for me, I’ll continue to walk my developer path, keep working with Wagtail, and maybe get another opportunity to work with Torchbox. Some recent things on my bucket list are to apply to other similar open source programs as well as practice [competitive programming](https://www.hackerearth.com/getstarted-competitive-programming/), data structures and algorithms. I also want to organise a dev-talk on Wagtail soon at my college.

## Conclusion

I’m grateful to Torchbox as well as my mentors Thibaud, LB and Helen for giving me this opportunity and for everything they’ve done for me in the past couple of months. I'm also grateful to LB's employer Virgin Australia for giving him paid time to mentor me. Over this time, I’ve gone through considerable changes in my life, and I can say that life is mostly about filling up the void in yourself. Good or bad, the experiences we share fill a void we all have inside of us. So keep filling it, and you'll enrich your life and the lives of others too.

If you want to keep following my journey through open source, I’m [@AgarwalPaarth](https://twitter.com/AgarwalPaarth) on Twitter, and will next be mentoring [Outreachy participants with Wagtail](https://wagtail.org/blog/outreachy-welcoming-new-contributors-to-open-source/).

## Links

- Live site: [https://wagtaildemo-nightly.herokuapp.com/admin/](https://wagtaildemo-nightly.herokuapp.com/admin/)
- GitHub: [wagtail/wagtail: A Django content management system focused on flexibility and user experience (github.com)](https://github.com/wagtail/wagtail)
- Discussions:[UX Unification · Discussion #8158 · wagtail/wagtail (github.com)](https://github.com/wagtail/wagtail/discussions/8158)
- Project Board: [🎨 UX Unification (github.com)](https://github.com/orgs/wagtail/projects/3)
- List of PRs: [https://github.com/wagtail/wagtail/pulls/PaarthAgarwal](https://github.com/wagtail/wagtail/pulls/PaarthAgarwal)
