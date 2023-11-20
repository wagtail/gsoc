# GSoD 2023: Wagtail technical writer agreement

## Scope of work

In one sentence: create a series of written tutorials for our documentation that teach newcomers how to build their own deployable Wagtail website using the newest version of Wagtail, based on the bakerydemo website.

Full scope:

- Audit the existing Wagtail Get Started tutorial and create a friction log to ensure it is accessible and usable for newcomers.
- Use the friction log to update our primary tutorial and ensure it provides a strong basis for additional learning in the onboarding tutorial series.
- Review the Wagtail Bakery, an existing demo project used for teaching and testing, to determine which Wagtail features should be covered in the tutorials.
- Use the audit results to create a series of written tutorials for our documentation that teach newcomers how to build their own deployable Wagtail website using the newest version of Wagtail.
- Work with our community organisers to adapt the tutorials for open source beginners, which will support programs and workshops like Outreachy, GSoC, and Coders of Colour.
- Incorporate feedback from tutorial testers and the wider community.
- Work with the Wagtail core team to update our documentation and determine a process for maintaining the written tutorials going forward.
- Collaborate with our Developer Relations team to identify the best opportunities to share the tutorial with our community at upcoming events.

Out of scope:

- This project will not involve the creation of videos for the tutorial series.
- This project will focus on lower friction deployment options suitable for newcomers and will not cover all available options.
- This project will incorporate a relatively easy-to-learn frontend technology like Bootstrap or Tailwind CSS rather than trying to cover all potential frontend options.
- This project will not create documentation for a starter template or cookiecutter for Wagtail.

## Deliverables

We expect deliverables across 3 thematic areas, delivered sequentially as most deliverables inform later work.

### Audit of the existing tutorial

- Friction log for existing [Your first Wagtail site tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html), in Google Docs.
- Pull request with content updates to [Your first Wagtail site tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html), directly in Wagtail repository in Markdown
- List of Wagtail [bakerydemo](https://github.com/wagtail/bakerydemo) website features to cover in new tutorials, in Google Docs.

### New tutorial series

- Outline for new tutorial series in Google Docs, including all illustrations and expected code snippets.
- Pull requests with content updates directly in the Wagtail repository in Markdown.

### Tutorial refinements

- Core team documentation on how to maintain tutorials, in Markdown in GitHub wiki.
- Tutorial feedback survey (draft in Google Docs, final survey in Google Forms)
- 5x feedback sessions with community organisers to review tutorials.
- Pull requests with tutorial content updates directly in the Wagtail repository in Markdown.

## Proposed timeline

This is a tentative timeline drafted in accordance with the [official GSoD timeline](https://developers.google.com/season-of-docs/docs/timeline), and project commitments from mentors and the technical writer, based on a schedule of 20 work hours per week for the writer, and 5h of support per week from mentors.

- Monday May 8, 2023 –Monday June 12, 2023
  - 5h – Project kickoff meeting with stakeholders
  - 5h – Technical writer induction
  - 5h – Project methodology refinements
  - 65h – Completion of the **Audit of the existing tutorial** deliverables.
- Monday June 12, 2023 – Monday July 10, 2023
  - 80h – **New tutorial series** – exact milestones TBC by project team
- Monday July 10, 2023 – Monday August 7, 2023
  - 80h – **New tutorial series** – exact milestones TBC by project team
- Monday August 7, 2023 – Monday September 4, 2023
  - 65h – **Tutorial refinements** – exact milestones TBC by project team
  - 15h – Final project report
- Monday September 4, 2023 – Monday October 2, 2023
  - Buffer if needed – exact milestones TBC by project team
- Monday October 2, 2023 – Monday October 30, 2023
  - Buffer if needed – exact milestones TBC by project team

Within this proposed timeline, both the mentors and the technical writer will convene to schedule up to 30 days away from the projects for each participant (for holidays or any other planned leave). Those days off can be taken as a single block or spread out, at the discretion of the participants. The actual project timeline will then shift accordingly.

## Licensing & copyright

- For changes to the existing Your first Wagtail site tutorial, the work will use Wagtail’s existing[ BSD 3-clause licence](https://github.com/wagtail/wagtail/blob/main/LICENSE#LL1C1-L1C1), with copyright retained by the writer.
- Any changes to the bakerydemo project will use the existing BSD 3-clause licence, with copyright retained by the writer.
- All other work, including the new tutorials, will be made available under a [CC0 public domain dedication](https://creativecommons.org/share-your-work/public-domain/cc0/), opting out of copyright.

## Methodology & revisions

We expect all work to be delivered either as Google Docs documents or GitHub pull requests with Markdown file changes, depending on the needs of the task.

Those formats will also be what we use to structure feedback from mentors and other community stakeholders.

As a standard, we expect all deliverables to follow a minimum number of iterations:

Draft outline, followed by feedback on the outline

First draft of the content, followed by feedback

Second draft as needed, followed by feedback

Final version

For the new tutorials, we expect to need up to 10 rounds of drafts and feedback.

## Communication & project management

The project will be run fully remotely, with chat communications via Wagtail’s Slack in a private channel, and occasional video call meetings.

We expect the writer and mentors to be available for up to two 1h-meetings per week (exact schedule to be agreed by the team), at times compatible with attendance from US east coast / Europe work hours (13:00 to 17:00 UTC).

The team will follow agile / scrum methodologies – in particular,

- Breaking down high-level project goals into smaller tasks
- Scheduling work as 2-week sprints, with sprint planning to refine the tasks and estimate the work needed.
- Sprint demos / review sessions with stakeholders
- Daily standup via group message Slack updates

For all communications, the technical writer must follow Wagtail’s [code of conduct](https://github.com/wagtail/wagtail/blob/main/CODE_OF_CONDUCT.md).

### Project participants

Project mentors Meagen Voss and Thibaud Colas will oversee the project and support the technical writer. They act on behalf of the Wagtail organisation, and can get other Wagtail stakeholders involved at their discretion as needed.

There are two scenarios where the project team could change and we expect the project to otherwise continue as planned:

- In case of disagreements in the project team, we will nominate another Wagtail core team member otherwise not involved with the project to moderate.
- In case one of the mentors has to permanently drop out from the project, the Wagtail organisation will find a replacement so project activities can continue as planned.

And three scenarios where team changes would result in the immediate termination of the project:

- In case both mentors have to drop out and no replacement mentor is found.
- In case the technical writer has to permanently drop out of the project.
- In case the project mentors deem the project isn’t running satisfactorily, they reserve the right to immediately terminate the project and release the technical writer from their obligations.

In those scenarios, the technical writer can invoice for any agreed completed deliverable, as well for any in-progress deliverable as a pro-rata of the current rate of completion, to be calculated by the project team.

## Compensation

The project budget is USD 5000, to be paid according to the following split of three payments tied to specific deliverables:

$1000 – Completion of the **Audit of the existing tutorial**

$1000 – Completion of half of the **New tutorial series**

$3000 – Completion of second half of **New tutorial series**, and **Tutorial refinements**

Payments are conditioned on the work being completed in accordance with the Scope of work and Deliverables as defined in this document. Payments will be made with Wagtail’s [OpenCollective account](https://opencollective.com/wagtail), by Wagtail’s fiscal host Open Source Collective, on behalf of the Wagtail core team.

Payments will be in USD, with each party responsible for their respective fees: any payment origination fees covered by Wagtail, any payment reception fees covered by the payee. Any currency conversion is the responsibility of the payee.

Payments will be made in accordance with [expense payment options](https://docs.opencollective.com/help/expenses-and-getting-paid/expenses) supported by Open Collective and Open Source Collective. At the time of writing this is PayPal or bank transfer for countries supported by Wise. Which payment option to use is left at the discretion of the payee and mentors, to be decided based on expected fees and convenience to the payee.

Payment dates will be dependent on availability of funds received from Google Season of Docs, according to their [Grants for organisations](https://developers.google.com/season-of-docs/docs/org-payments) guidance. In particular:

- The first and second payments won’t be possible until mid to late June 2023, at which point Wagtail will receive $2000 from GSoD (40% of $5000 project budget).
- The third (final) payment won’t be possible until mid to late December 2023, at which point Wagtail receives the final $3000 from GSoD (60% of project budget).

### Invoices

To receive payment, the payee must provide an invoice according to the [guidance from Open Collective](https://docs.opencollective.com/help/expenses-and-getting-paid/submitting-expenses#invoices) and [from Open Source Collective](https://docs.oscollective.org/how-it-works/basics/invoice-and-reimbursement-examples).. Here is an excerpt of important terms:

- Must have a description of the work done, and the amount of time (normally in hours) spent on work or time covered (normally in months).
- The payee must include their billing address.
- The payee's name must match the billing contact.

Regarding descriptions: Invoices need a clear description of services rendered and provide sufficient detail to make it clear what the collective is paying for. This is because this description may be checked by our accountant for compliance. That means that someone with no knowledge of your project, and only a limited knowledge of open source, should be able to understand what was done from the description.

For this project, descriptions and amounts of work can be based directly on deliverables as defined in the technical writer agreement.

Invoices can be submitted and will be approved as soon as the project team considers the deliverable to have been completed. Payments will be possible as soon as Wagtail receives its funding from Google Season of Docs (40% in June 2023, 60% in December 2023).
