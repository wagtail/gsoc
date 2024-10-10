# Google summer of code 2023 final project report

**Contributor**: [Aman Pandey](https://github.com/salty-ivy)

**Mentor**: [Chris Adams](https://github.com/mrchrisadams)

**Project**: [Greener coding 💚: Backend development](https://github.com/orgs/wagtail/projects/30/views/1)

**Organization**: [Wagtail](https://github.com/wagtail/wagtail)

**Original idea discussion by chris adams**: [Greener coding:Making a 'gold' reference configuration with the Wagtail bakery app](https://github.com/wagtail/wagtail/discussions/8843)

**Contributor proposal**: [Wagtail: Greener coding (GSoC 2023 Proposal)](https://docs.google.com/document/d/1u9F8Pw4TLGRBIwOt2Fofma3ER8yB9y2MEZ_-U3K9-Zg/edit)

## Description

The project aims to integrate green coding practices into Wagtail’s direction and make concrete improvements to reduce related carbon emissions also ensuring that the websites we build are environmentally friendly. We plan to do so by improving different parts of wagtail architecture like improving project templates, adopting internal template caching, extending image support and lazy loading, lighter embeds, job scheduling interface for asynchronous task processing, eco-friendly themes, and other processing-related optimisations.

**Technologies used**: django, wagtail, python

### Execution

Original Greener Coding was divided into 2 parts namely 1.**Greener coding: Frontend development** 2.**Greener coding: Backedn development**. This report consist the progress for **2. Backend development**.

We along with organization maintainers priortized certain tasks over the others that can be rolled out into wagtial's new release.

Our sustainable coding initiative diverged from conventional developmental trajectories, diverging significantly in its approach. The crux of its impact resides in pioneering research directed towards the reduction of carbon emissions. Our preliminary research during the coding phase unveiled several pathways for exploration, each meticulously prioritized based on complexity and feasibility for integration into forthcoming releases. These pathways encompass:

Integration of AVIF support into Willow: AVIF, a lightweight image format, demonstrates superior efficiency compared to its counterparts. Static site pages enriched with AVIF-encoded images exhibit substantially reduced load times and resource consumption compared to those incorporating alternative formats.

Extension of AVIF support to Wagtail: Building upon the successful integration of AVIF within Willow, we seamlessly extended this support to Wagtail. Concurrently, a concerted effort was made to foster adoption amongst fellow developers, encouraging the incorporation of this technology into their projects.

Implementation of "scale to zero" configurations for Wagtail sites: Leveraging serverless architectures such as neon.tech, we explored the concept of "scale to zero" configurations for Wagtail sites. This endeavor aimed to enhance resource efficiency by dynamically adapting server capacity to match traffic demands, thereby minimizing carbon footprint and operational costs.

Development of a Green Wagtail-specific debug toolbar: Addressing the need for developers to gauge the optimization levels and resource intensity of their sites and pages during the development phase, this debug toolbar emerges as a crucial tool. By providing insights into the optimization status of their projects, developers are empowered to make informed decisions that lead to more streamlined and resource-efficient outcomes.

## Work done

1. AVIF support for willow PR https://github.com/wagtail/Willow/pull/115
2. AVIF support for Wagtail PR https://github.com/wagtail/wagtail/pull/10657

### What's next

While we can still venture on many imporvements related to our sustaninable development but its really important for us to measure those in action to show if it actually makes any difference or not, so our next step would be to `benchmark`
these changes on a project using [Green Metric Tool](https://docs.green-coding.berlin).

1. Original benchmarking on wagtial bakerydemo by [Thibaud colas](https://github.com/thibaudcolas): [bakerydemo GOLD benchmarking](https://github.com/thibaudcolas/bakerydemo-gold-benchmark)

2. Benchmarking the impact of AVIF over other image formats: [AVIF GOLD benchmarking on demo project](https://github.com/salty-ivy/wagtail-AVIF-demo-GOLD-benchmark/tree/main)

## Blogs

1. [Wagtail's sustainability consideration page](https://wagtail--10527.org.readthedocs.build/en/10527/advanced_topics/sustainability_considerations.html)
2. [Wagtail gets bit leaner and greener](https://wagtail.org/blog/wagtail-greener-and-leaner/#:~:text=Our%20latest%20release%20focuses%20on%20improving%20performance%20and%20reducing%20Wagtail%27s%20carbon%20footprint&text=We%20designed%20Wagtail%20to%20help,work%20for%20our%20planet%20too.)
3. [Green Web Foundation helping us make wagtail greener](https://www.thegreenwebfoundation.org/news/working-with-the-wagtail-community-on-the-summer-of-code/)
