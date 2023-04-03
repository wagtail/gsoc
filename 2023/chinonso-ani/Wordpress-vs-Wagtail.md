# Out-of-the-box, Page Builder & Themes/ Templates proposal for GSOC 2023
Create a low-code/ no-code solution for techies and more importantly non-techies to use Wagtail, without necessarily having to contact a developer.

## Table of content
1. Abstract
2.  `out-of-the-box` app
2. `wagtail-pagebuilder` app
3. Schedule and milestones
4. About me
5. Start with why?

# 1. Abstract
Wagtail does not work out-of-the-box, from a non-technical user point-of-view. 
>Out-of-the-box refers to the immediate usability of a new software package. In the case of wagtail, it is after it has been downloaded from Github or PyPi.

This ruins [the first 30 minutes](https://wagtail.org/wagtail-vision/) of a non-technical user initial experience. A smooth set-up process is not configured for that non-technical user, _who may be the one of the influencers of which CMS a company adopts (see Extra 1 below)_. This non-technical user wants to try it out, by themselves. In trying it out by themselves, they don't want to call in a Developer just yet, they want to work it out by themselves in 10-20mins. The rise of low-code/no-code solutions and DIY tools in other sectors/ industries are the drivers. 

Because [the first 30 minutes](https://wagtail.org/wagtail-vision/) may not go so great, they never get to see the awesome page for [Editors, to get their best work done](https://wagtail.org/wagtail-vision/)

Further more, Wagtail has no page-builder solution, similar to what is available on other CMS solutions. 
>Page-builder refers to tools that allow non-technical users to create web pages by providing a visual interface with pre-built element (like the StreamField) for defining the entire web page content - including navigation menu, headers and footers.

To change the default demo bakery theme/template, you must have some coding experience. Hence, before any wagtail solution can be deployed, a developer needs to be brought in by default.

Two apps are being proposed here. `wagtail-out-of-the-box` and `wagtail-pagebuilder`

A page builder solution `wagtail-pagebuilder` is useful for creating simple websites quickly, which would simply allow one to build out a page similar using blocks to compose and edit a full page. And to change the theme/ template of the website without having to know how to code.

The `wagtail-out-of-the-box` is a packager and distributor, configuration management for Wagtail deployment for mostly the non-technnical user. Think about `wagtail-out-of-the-box` as a non-technical cookie cutter version, an installer for the wagtail cms on any host. It would configure environment variables, database, write and optimize the configurations needed to setup wagtail. 

Wagtail can work out-of-the-box for all - It simply means, this user either pulls in the docker image or uploads the wagtail cms to their host and it works. After a 1-3 step installation/ configuration management process.

 As a [future-proof solution](https://wagtail.org/about-wagtail/) wagtail needs to be beginner proof or maybe even fool proof. In business/ marketing speak:
 >Increasing the appeal of wagtail to a wider audience and not just technical people (developers). This may also be coined as going *mainstream*

 All these are done, without sacrificing flexibility and customization and performance.

 # 2. The `wagtail-out-of-the-box` package
 ## 2.1 Brief history
 In a good number of conversations with [@Thibaud](https://github.com/thibaudcolas), we've been hovering on some usecases of AI in wagtail. And I really like the idea of Little Language Models (LLMs) of which Wagtail CMS can sufficiently benefit from. Little unlike Large Language Models (think ChatGPT) are more specific domain knowledge areas application of AI. And then it hit me... 
 >Wagtail should be able to install itself once commanded to do so. On any server, on any host.


 In researching about [Greening Wagtail](https://github.com/wagtail/wagtail/discussions/8843) I realized we might hit and come up with some good ideas, but they might just end up as recommendations on our _how to setup wagtail_ page, because people (and developers) would by default setup apps, the way they've always done it, simply because it is what they're familiar with. Driving adoption of a new deployment pattern, without providing for how people can easily orchestrate might be too much of a learning curve.

 I just thought to myself, what if there's way for people to just get to test and see a way of setting up the app, that might be different that could lead to an optimized wagtail, efficient codebase, and a Greener Planet, and by extension, help them optimize the rest of their own python code base, further saving the World.
 >Wagtail can save the world, one developer at a time

 Super users (developers) can obviously turn that off, we're not trying to lock anyone in.

 ## 2.2 Out-of-the-box
 Download wagtail from docker hub or from PyPi and Wagtail is able to set itself up. This involves a lot of discoveries to be made about the environment and setup and write those configuration to file or environment variables. The things the `wagtail-out-of-the-box` package would take care of include
 1. Installing a reverse proxy - Nginx or Apache (and others)
 2. Setting up Wagtail app and the `uWSGI Application Server`
 3. Installing and configuring the Database - Postgres or MySQL (and others)
 4. Running migrations and other django management commands to create superuser, etc...

 ## 2.3 The Goal
 First, is to have an opinionated way to setup Wagtail for first-time users, using wagtail alone (not within other django apps). If using within other django apps, then 
`wagtail-out-of-the-box` would not be needed, since you've already got all that setup.

This would serve people who want to quickly try out Wagtail on any hosting (or free tier) service.

## 2.4 Benefits
An Awesome [first 30 minutes](https://wagtail.org/wagtail-vision/) of a non-technical user initial experience with Wagtail. 

If we achieve some awesome nirvana with [Greening Wagtail](https://github.com/wagtail/wagtail/discussions/8843) project, then we can pass on our learnings with the above.

# 3. `wagtail-pagebuilder` app
A Page Builder & Themes application for Wagtail: Bring Wagtail to the Next billion users
>Big question: What would you have, if you took the the success of Wordpress as a CMS, the drive to headless systems and the rise of low-code/no-code tools?

## 3.1 Business Case
Wagtail's primary focus and rightly so... has been to provide a powerful and flexible platform for developers to build custom content-driven websites and applications.

According to [DjangoCMS](https://www.django-cms.org/en/blog/2021/02/03/django-cms-vs-wagtail-which-cms-is-best-for-your-website/) Wagtail is a CMS framework and not a CMS. As it is designed for developers vs being designed for everyone. This is obviously because it doesn't just work out-of-the-box as described above for non-technical users. This is a strategic decision to make.

With [Traleor CMS](https://youtu.be/IQY0dzo2Wzg) you can deploy Wagtail, which is a very good thing.

First, let's understand what really drove the adoption of wordpress, amongst many things it was this: 
>The ability to easily switch between themes or modify templates using PHP code or drag-and-drop tools 

Having been a PHP developer, who also built his own CMS (which looked like codeigniter) and having done numerous research over the last 4 weeks, this is the singular success factor I could thread.

You would also find the same corollary with Operating Systems, especially Ubuntu vs other Linux distros... User friendliness to the end-users and not just User-friendliness to the developers, has been the major cause of the runaway success. As more non-technical people try it out, they want to get more technical people in to build some more out of it.

## 3.2 The Idea
The ability for non-technical users to change the theme/ template of the wagtail frontend, without having to write any code or even interact with it. Think about it as how we can change the skin of the default django-admin (this is already being done, we are just adapting that idea to the Wagtail public facing frontend) and then more...

The more here includes providing building blocks, similar to what is already available in Wagtail StreamFields, but that would also manage dynamic content, the navigation menu, footer, header and every other part of the app. 

Note this would also mean, any developer can create a theme/ template and that theme/ template can be applied to the site and adopts its look and feel, Also that the role of the Wagtail organization would then be to have a marketplace for Wagtail themes and templates, and if we go down the future proof of this idea... packages as installable plugins.

The  `wagtail-pagebuilder` app would provide a WYSIWYG block form interface (the initial version is not supposed to be too complex), so that other interested developers can build upon it an create better theme/ template editors like [What you have here from Wordpress](https://kubiobuilder.com/)

## 3.3 The Goal
Inherent technical decision have so far limited the flexibility and use of Wagtail especially for non-technical users. Our goal is to make a cms for power users and one for the low-code/ no-code community. Ideally for my Grandma to write about her Grand children, that she can easily setup by herself.

The Longtail of this goal is that wagtail can become a _future proof_ Digital Experience Platform (DXP). See more about DXP below.

## 3.4 The Benefit
There are a lot of benefits. It provides a delightsome [first 30 minutes](https://wagtail.org/wagtail-vision/) of a non-technical user initial experience with the platform. Plus even if a developer is tasked to do the job, he gets it done within a shorter time-frame.

It increases the reuseabilility of themes and templates across the Wagtail community. And by extension, [a new freedom](https://ma.tt/2014/01/four-freedoms/)
>In this co-evolution of society and technology, what it means to be truly “free” ... is shaped by the products we live on. The “free” doesn’t have to do with price, as you’re still free to charge for your software, but with freedom to create.

Freedom from needing a developer to hold your hand through your Wagtail journey. You're truly free as a bird _wagtail_.


## 3.5 Organizational Impact
Changes the role of Wagtail as an organization to a larger community manager and the need for [Developer Relations](https://wagtail.org/blog/wagtails-new-developer-relations-team/) 
* The Wagtail company earns profits or commission on every purchase of these paid themes and templates through its platform
* The Wagtail company gets to profile wagtail dev jobs [like this](https://jobs.wordpress.net/)

## 3.6 Community Impact
A wagtail developer as a job role.
* Wagtail developers are able to earn money from building Wagtail Themes and Templates
* Wagtail developers are able to earn money from building plugins
* A WagSpace where beginners in Python can build Wagtail themes and templates

## 3.7 Future prospect
### 3.7.1 Digital Experience Platform (Headless)
Example of DXPs are Sitecore, Adobe Experience Manager

A digital experience platform (DXP) is a software platform that enables organizations to manage and deliver consistent, personalized, and engaging experiences across a wide range of digital channels, including websites, mobile apps, social media, and more. A DXP typically includes a range of features and capabilities, such as content management, personalization, analytics, and marketing automation.

The move to headless, is a step in the right direction. However these subtle [trends show DXP](https://drewl.com/blog/wordpress-dxp/) might be the path larger organizations are headed, and also many small businesses. Especially for empowering departments of an organization who want to use wagtail to build up their internal intranet self service to have more than just a blog-like page.

### 3.7.2 An AI first CMS
The first CMS to allow the use of simple AI tools and tooling, for example the Little Language Models (the inital AI thought... yeah  😘). Because no CMS has a way to learn from its own content or what people are consuming/ creating. Or from the questions people are asking... Do you see where this is going... yeah... [future-proof 🚀](https://wagtail.org/about-wagtail/)

# 4. Technical Stuff
A simple implementation path.
From the start of GSOC - May 29, I'll be writing my Dissertation whilst working on this Parttime. After July, I'll have time to work on this full time.

## 4.1 `wagtail-out-of-the-box` app
This is centered around the DevOps and deployment path of Wagtail.
In my head, this involves using Ansible (which is python) to orchestrate the deployment of wagtail and manage the configuration, but also building a UI layer for inputs to be made.

### 4.1.1 Schedule and Milestones: From Week 1-6  - `wagtail-out-of-the-box` app
These thought are adapted from my research on [Greening Wagtail](https://github.com/wagtail/wagtail/discussions/8843) project. It can be the basis upon which the GOLD of Wagtail is further developed from and improved.

## 4.2 `wagtail-pagebuilder` app
Learning from the way django admin is setup to allow different skins to be applied (learning from django), plus the way Wordpress templates are setup (learning for Wordpress) I would suggest a PageField and ThemeModel leading to more robust and faster templating and theming system.

### 4.2.1 Schedule and Milestones: From Week 7-16 weeks - `wagtail-pagebuilder` app
The full schedule would be developed inline with the mentor's guidance and guidelines.

## 4.3 Research
The goal is to find out why the templating system of Wordpress, DjangoCMS and others was designed and work the way it is and what is the impact. It is about benchmarking the world's best, and finding out the dos and don'ts
* Review relevant existing algorithms, and methods for designing and architecting templating and deployment systems.
* Critically evaluate the requirements of a performance optimized templating and deployment system in and for django/ wagtail.

## 4.4 Develop and Test
* Design and implement a solution a Wagtail deployment and templating solution that is tailored to the specific needs of the CMS.
* Test and evaluate the performance and reliability of the proposed solution.
* Provide recommendations for developers and end-users on how best to use the solution and how it can be improved in future versions.
* Provide documentation for hosting companies (Developer Relations to act on this)
* Provide documentation for developers and end-users


# Extra 1: Choosing a CMS
_This section was written with help of ChatGPT_
The decision of which CMS (Content Management System) to adopt in a company can be made by different individuals or teams depending on the organization's size and structure.

In smaller companies, the decision may be made by the owner or a small group of executives responsible for technology and marketing. In larger organizations, a dedicated IT department or a team responsible for digital marketing may be in charge of selecting and implementing a CMS.

Other stakeholders that may have a say in the decision-making process include content creators, editors, as they will be the ones using the CMS on a regular basis and need to ensure that it meets their needs.

Ultimately, the decision of which CMS to adopt should be based on the company's requirements, budget, and strategic goals, and should involve a thorough evaluation of different options and consultation with relevant stakeholders.

## What non-technical evaluators seeks
1. Ease of Use: Non-technical evaluators may prioritize a CMS that is easy to use and intuitive. They may look for a CMS that allows content creators to easily create, edit, and publish content without needing extensive technical knowledge.

2. Content Management Capabilities: Non-technical evaluators may look for a CMS that allows them to manage different types of content, such as text, images, and videos. They may also look for a CMS that allows them to easily organize and categorize content for easy retrieval.

3. Customization Options: Non-technical evaluators may want a CMS that allows them to customize the look and feel of their website without needing extensive coding skills. They may look for a CMS that offers templates and themes that can be easily customized.

4. Scalability: Non-technical evaluators may consider a CMS that can grow with their organization over time. They may look for a CMS that can handle larger volumes of content or support additional features and functionality as their needs evolve.

5. Integration with other tools: Non-technical evaluators may want a CMS that can integrate with other tools they use, such as social media platforms, analytics tools, or marketing automation software. They may look for a CMS that has a robust set of APIs or supports integrations with popular third-party tools.

6. Cost: Non-technical evaluators may need to consider the cost of a CMS, including any licensing fees, ongoing maintenance costs, or fees for additional features and functionality. They may look for a CMS that offers a good balance of affordability and functionality.

7. Support and Training: Non-technical evaluators may also want a CMS that offers good support and training resources, including documentation, tutorials, and customer support. They may look for a CMS vendor that offers responsive customer support and provides training resources to help users get up to speed quickly.