# Proposal: Create Wagtail developer onboarding tutorials

## About Wagtail

Wagtail is a popular content management system (CMS). It's built on Python by an active and engaged open source community, which has grown rapidly since Wagtail's release in 2014. Wagtail is available in over 40 languages. It is used by some of the world's best-known organizations, including NASA, Google, Mozilla, MIT, and the UK's National Health Service. Our users also include museums, universities, non-profits, governments, banks, studios, restaurants, startups and bloggers around the world.

Like Python and Django, the technologies which underpin it, Wagtail is known for its welcoming community. We have a diverse core team with representatives who are currently spread across Europe, Africa, and North America. We're keen to continue welcoming new developers as well as people who are new to programming and open source into our project so we can continue to increase the geographic and cultural diversity of the people who use Wagtail.

Wagtail has moved fast in the last few years, and we have delivered several large improvements to our editor experience and accessibility features. We have adopted a regular quarterly release cycle to minimise upgrade time while providing compelling new features and improvements with each release. Yet keeping up with these changes can be difficult without appropriate learning resources that demonstrate new features in a practical manner. With this proposal, we’re seeking to establish a strong foundation for continuous learning within the Wagtail community.

## About the project

### Our challenge

We have a lot of strong initial interest in Wagtail both from developers and business stakeholders who are looking for open source alternatives to a proprietary CMS. Around 1,000 visitors per week to Wagtail.org participate in one of the Get Started activities we offer and we have recorded at least 9000 visits to the Getting Started tutorial within the last 30 days. Yet many new people find the transition from completing our introductory tutorial to deploying their first project more difficult than it needs to be.

A lot of the in-depth tutorials and learning resources we currently have within our community are based on much older versions of Wagtail. Having learning resources that include many of the improvements and updates we have made would help more community members to learn how to use the newest versions of Wagtail and encourage them to explore using the newer features we offer. Having newer resources would also help us provide a better onboarding experience for people who participate in our initial contribution rounds for Google Summer of Code and Outreachy. In 2022, we had 266 contribution participants and we expect to support a similar number in 2023.

### Project scope

Our onboarding tutorials project will:

- Audit the existing Wagtail Get Started tutorial and create a friction log to ensure it is accessible and usable for newcomers.
- Use the friction log to update our primary tutorial and ensure it provides a strong basis for additional learning in the onboarding tutorial series.
- Review the Wagtail Bakery, an existing demo project used for teaching and testing, to determine which Wagtail features should be covered in the tutorials.
- Use the audit results to create a series of written tutorials for our documentation that teach newcomers how to build their own deployable Wagtail website using the newest version of Wagtail.
- Work with our community organisers to adapt the tutorials for open source beginners, which will support programs and workshops like Outreachy, GSoC, and Coders of Colour.
- Incorporate feedback from tutorial testers and the wider community.
- Work with the Wagtail core team to update our documentation and determine a process for maintaining the written tutorials going forward.
- Collaborate with our Developer Relations team to identify the best opportunities to share the tutorial with our community at upcoming events.

Work that is out-of-scope for this project:

- This project will not involve the creation of videos for the tutorial series.
- This project will focus on lower friction deployment options suitable for newcomers and will not cover all available options.
- This project will incorporate a relatively easy-to-learn frontend technology like Bootstrap or Tailwind CSS rather than trying to cover all potential frontend options.
- This project will not create documentation for a starter template or cookiecutter for Wagtail.

We have at least two strong potential candidates for this project who we have collaborated with on previous efforts. Thibaud Colas, a core Wagtail contributor and Wagtail consultant as well as Meagen Voss, an experienced writer and editor who currently leads content creation for Wagtail.org, have committed to supporting this project. After factoring in available project time and planned summer holidays, we anticipate this project will take 6 months to complete.

### Measuring success

Our primary measure of success will be tracking the number of users who click the link within our current Getting Started tutorial to continue their learning as well as how many users progress through the onboarding series to completion. We cannot track completion of the tutorial content directly but we can compare the number of visits to each section of the tutorial and track links to determine whether people are progressing through the material.

We plan to track two metrics: the total number of visitors to each section of the tutorial series and the percentage of visits to the final tutorial in the series relative to the initial Getting Started tutorial. Currently, there have been just over 9000 visits to the Getting Started tutorial within the past 30 days.

We would consider this documentation project a success if:

- At least 50% of visitors to the Getting Started tutorial continue on to the next tutorial in the new onboarding series.
- The final tutorial in the series receives at least 20% of the traffic of the initial Getting Started tutorial.
- 50+ open source newcomers go through the series as part of our next two outreach program participations (Outreachy December 2023, GSoC 2024).

## Timeline

The project itself will take approximately six months to complete with planned time off for holidays and other planned projects and releases factored in. Once a suitable candidate is recruited, we’ll spend at least two weeks orienting the technical writer within the Wagtail community then proceed to auditing the Getting Started tutorial, which we anticipate will take at least two weeks for full audit and revision. If we select a candidate with previous experience in our community, the initial orientation and audit period will be shorter.

The bulk of the project time will be spent outlining the required tutorials for creating a deployable Wagtail demo project and crafting documentation required for the tutorial series. We anticipate this series will take at least 4 months to complete and test with other members of the community. The number of tutorials we create will depend on the abilities and availability of the writer we collaborate with. Based on past Wagtail learning series, we believe we’ll likely need at least 6-8 tutorial sections to document the material needed for building a fully functional Wagtail website and teach relevant features.

We plan to use the final few weeks of the project period to integrate the series fully within our documentation, develop plans for maintaining the tutorial series over time, and share the new series more widely with our community.

| Month        | Action items                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| May          | Orientation                                                                                                                                             |
| June         | Audit and revise existing Get Started tutorial. Review existing demo site code and outline tutorial documentation required to teach people to build it. |
| July-October | Draft tutorial sections. Recruit testers and revise tutorial documentation accordingly.                                                                 |
| November     | Project wrap-up and promotion of new documentation within the Wagtail community.                                                                        |

## Project budget

| Budget item                                                                                                                  | Amount | Running total | Notes/justification                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | ------------- | -------------------------------------------------------------------------------------------------------------- |
| Technical writer audit and update of existing material, creating new tutorial series, and refining tutorials through testing | $5000  | $5000         |                                                                                                                |
| User testing compensation                                                                                                    | $250   | $5250         | $50 incentives for user testing participation X 5 to recruit five high-quality testers for the tutorial series |

## Additional information

Meagen Voss has several years of experience as a professional science, health, and technical communicator. She has over a decade of experience as an editor with particularly strong experience mentoring and guiding writers who learned English as a second language. She collaborated regularly with technical writers in a prior role at IBM to clarify technical documentation and adapt it into technically accurate materials for sales and marketing professionals to use in their roles.

In addition to being one of the most active contributors to our Wagtail documentation, Thibaud Colas served as a mentor for a documentation project we completed with Outreachy in 2022 to improve our Wagtail User Guide (https://guide.wagtail.org/). Under his supervision, the Outreachy intern we collaborated with conducted user research and made several substantial improvements to our guide. This was the Wagtail project’s first time working with a technical writer contributor over an extended period of time and we appreciated how well he navigated our dense documentation and created materials that helped other contributors with less technical experience get involved with our project, especially user researchers.

We are also in the process of building a contributor team to serve as Wagtail ambassadors for developer relations and outreach. This team will be our first effort to organize people who are interested in contributing communications, documentation, user research, and educational materials to the Wagtail community.

Both of our proposed administrators took part in Google Summer of Code 2022 as mentors. Thibaud Colas also mentored and administered our Outreachy internships in 2022 and 2023. Our 2022 Google Summer of Code program was our largest outreach program to date with 3 contributors steered by 12 mentors. Past participants in our contributor outreach programs have continued to collaborate and contribute to Wagtail. We are especially proud to share that two of our past participants have returned to these programs as mentors. We definitely wish to continue encouraging this trend of giving back to the community as well as fostering long-term collaborations and relationships with our contributors.
