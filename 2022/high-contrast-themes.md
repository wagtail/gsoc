# [Gsoc-2022-Final-submission Anuja Raj Verma | Wagtail | High Contrast Themes](https://github.com/anujaraj/Gsoc-2022-Final-submission/blob/main/Report.md)

## Introduction

The Google Summer of Code programme has been a great and fun learning experience for me over the past months. The project is aimed at improving the accessibility of Wagtail through the lens of high contrast themes in windows.

---

The project had two major parts</br>

- Resolving existing high contrast issues mainly in the Wagtail admin:</br>
  Most of the contrast and accessibility issues were present in Wagtail’s styleguide. The issues had to be dealt with in all the themes of the Windows contrast themes to improve accessibility of the Admin for all its users</br>

- Accessibility tests and reporting new issues :</br>
  We can divide the tests into two categories: automated and manual. The manual accessibility tests were mostly performed using Chrome developer tools and Windows 11 contrast themes.</br>
  The Automated testing was performed using pa11y.

#### What is Wagtail ?

Wagtail is a free and open-source content management system (CMS) written in Python. It is popular among websites using the Django framework.</br>

#### What is Windows High Contrast and why is it needed</br>

Windows High Contrast mode ensures a customised user interface that renders data according to the requirements of the user. Though to some users working without WHCM is a better option, many face visual disabilities and as a result, find the UI difficult to navigate. Therefore, to allow all users a satisfactory admin interface, we must ensure WHCM is supported throughout the admin.

## Work Summary

### Fixed prior issues mentioned in the audits in the UI components, Admin interface, and Wagtail Style Guide, which are described below: 

##### Issue #1: 

High-contrast mode: buttons with .disabled class look active in high-contrast mode - To resolve this issue, I added a PR that added a @media query in forced-colors for the disabled buttons with certain CSS styles to enable a better disabled look.

##### Issue #2: 

Progress Bar not visible in Windows High Contrast Mode- To resolve this issue, system colours were added to the components

### Fixing issues discovered during the GSOC coding period are mentioned below:

##### Issue #3: 

The check mark is not visible inside the checkbox in the users section of the Admin in Windows High Contrast Mode - I used media query, forced color: active, and system colours to solve the problem.

##### Issue #4: 

The icons in the Styleguide, in contrast, themes were overridden by forced colors, which removed the icon’s original meaning - To achieve the desired result, I commented the media query for forced-colors over the icons. The query was added when chrome was having a bug due to which an override on icons using fill (a css property) was required. Since the bug is removed, we would want to remove the override too

##### Issue #5: 

The boxes(help,critical message, and warning boxes) inside the Styleguide were styled oddly, giving visual traffic to the eyes in Windows High Contrast Mode  -To resolve this issue, I added three types of borders to the three kinds of boxes and removed any colour from the texts or borders. This provides a distinct look as well as more visual clarity to the viewer in Windows High Contrast Mode.Along with border styling, the issue pertaining to text inside the first box (help box) in lighter modes of high contrast earlier was not visible.

##### Issue #6: 

In Windows High Contrast Mode/Forced Colors Mode, Styleguide’s dialogue component lacks a backdrop, thus making it hard to understand where the component is- To resolve this, borders were added to the modal box using forced colours and system colors.

##### Issue #7: 

In Windows High Contrast Mode/Forced Colors Mode,tooltip-style "More" dropdowns are missing a border or outline, so it’s hard to tell where the dropdown is - To resolve this I added a transparent border to the component, making it visible only in the contrast themes.

### Fixed Linting issues- Linting the changes while making changes on the frontend is important to reflect changes in the browser. 

##### Issue #8:

While running npm run lint:format in Windows, a certain error popped up due to some incorrect format of how it was written as a script inside the packages. This was corrected by changing the format of how it was written, particularly for Windows users.

### Other changes that were not merged

##### Issue #9:

In Windows High Contrast Mode,the field inside the login/password reset form styles of the admin, are invisible - To correct this my suggested change was to add an invisible border around the field boxes or add a media query with system colors for borders. Since this issue was already resolved by correcting the design of the form, my PR wasnt merged.

##### Issue #10:

In Windows High Contrast Mode, in the tooltip-style "More" dropdowns, the tooltip was rendered as a square - To resolve this issue, I tried the following approaches:

- Use [clip-path : polygon](https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path) - It would provide the desired shape shape of an arrow.
- Use `forced-color-adjust: none` - Since we didnt want to loose the true form of Windows High Contrast using this was erradicated.

##### Issue #11:

In the admin's info side panel, a few buttons displayed, are in "link" style - To work this out, I had to look into the following aspects:

- The component used a CSS utility framework [Tailwind](https://tailwindcss.com/)
- Understanding its basic syntax helped in resolving the issue. I added a CSS over the media query using tailwind classes to produce the required outcome
- Since the issue was not just related to this component and was a part of a whole button and anchor class in the website, we decided to freeze this PR and instead added an issue as follows (https://github.com/wagtail/wagtail/issues/9078)

### Accessibility Testing 

The accessibility testing was done in two parts, one being manual and the other being automated using pa11y. For most parts of the project, we conducted manual testing using Windows Contrast themes and Chromedeveloper tools</br>
Working with Pa11y-For trying automated testing, we preferred Pa11y. Since most automated tests were already performed by my mentor Thibaud in his github repository, (https://github.com/thibaudcolas/wagtail-tooling/blob/main/accessibility/pa11y-test.js) I mostly worked with Wagtail’s Bakery Demo website for testing pa11y. I conducted automated testing on its few pages and found bugs as shown in the below screenshots:</br>
![Screenshot-1](https://user-images.githubusercontent.com/52713215/188315836-d1d189b2-c6f7-4d2a-89ee-3506c62aab10.png)

![Screenshot (193)](https://user-images.githubusercontent.com/52713215/188315844-89b75032-1d75-45a8-962e-1b55cb7d76af.png)

The above issues were reported in the issues of wagtail’s bakery demo repository under the following link : </br>
https://github.com/wagtail/bakerydemo/issues/356<br></br>

## Pull Requests

---

### Merged pull requests before GSoC period

- https://github.com/wagtail/wagtail/pull/8238

### Merged Pull requests during GSoc period

- https://github.com/wagtail/wagtail/pull/8909 </br>
- https://github.com/wagtail/wagtail/pull/8719 </br>
- https://github.com/wagtail/wagtail/pull/8718 </br>
- https://github.com/wagtail/wagtail/pull/8852 </br>
- https://github.com/wagtail/wagtail/pull/8853 </br>
- https://github.com/wagtail/wagtail/pull/8874 </br>
- https://github.com/wagtail/wagtail/pull/8897 </br>
- https://github.com/wagtail/wagtail/pull/8729 </br>

## Important Links

---

- [Documentation](https://docs.wagtail.org/en/stable/) </br>
- [Blog Post About GSoC journey](https://wagtail.org/blog/google-summer-of-code-high-contrast-themes/) </br>
- [Project Github Board](https://github.com/orgs/wagtail/projects/5/)</br>

## Future Aspects

I intend to improve this project and also use it as a starting point for anyone who would be interested in contributing to it further. A few of the improvements and new features could be the following:</br>
Performing Automated Pa11y testing over the Wagtail’s Bakery Demo Admin interface</br>
Fixes following a Pa11y audit of the bakery site</br>
Extending the contrast improvements to Wagtail’s Bakery Demo site

## Remarks

I had a fun and learning experience while working under Wagtail. I was afraid of asking questions initially, which I overcame to some extent on the whole journey. I loved the Wagtail community, and I got guidance and help whenever I got stuck. I would like to especially thank my mentors, Jane, Thibaud, and Scott, for helping and guiding me throughout the process. I also would like to thank Lb for helping me get comfortable with the open source community during the application period.
