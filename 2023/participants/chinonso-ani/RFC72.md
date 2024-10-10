# RFC 72: Background Tasks

## A Reference to Wordpress
WordPress, as a content management system, is capable of performing various background tasks that help to keep your website running smoothly. Here are some examples of the background tasks that WordPress can perform:

- Scheduled Posts: WordPress allows you to schedule your blog posts to be published at a specific date and time in the future. When the time comes, WordPress will automatically publish the post for you.

- Auto-Saving Drafts: WordPress automatically saves your post as a draft as you work on it, so you don't have to worry about losing your work if something happens.

- Backing Up Data: WordPress can automatically create backups of your website's data and files, so you can restore your website to a previous state if something goes wrong.

- Cleaning Up Database: WordPress can automatically clean up your website's database by removing unnecessary data like post revisions, spam comments, and trashed items.

- Updating Plugins and Themes: WordPress can automatically update your website's plugins and themes to ensure that they are up to date and secure.

- Generating Thumbnails: WordPress can automatically generate thumbnails of your images to make them easier to display on your website.

- Sending Email Notifications: WordPress can send email notifications to you and your users about important events on your website, such as new comments, password resets, and new user registrations.

WordPress uses a built-in scheduler that runs background tasks at specific intervals or at specific times. These tasks are triggered by WordPress's cron system, which is a scheduling system that allows WordPress to run scheduled tasks even when no one is using the website. The WordPress cron system runs by default on every page load, so you don't need to set it up manually.

### The Scheduler & Cron
WordPress's built-in scheduler and cron system work together to schedule and run background tasks on your website. Here's how it works:

The WordPress Scheduler: The WordPress scheduler is a built-in feature that allows you to schedule tasks to run at specific times or intervals. You can use the scheduler to schedule tasks like publishing a post, sending an email, or backing up your website.

The WordPress Cron System: The WordPress cron system is a feature that runs scheduled tasks automatically. It works by checking the WordPress database for scheduled tasks and running them at the appropriate time. The WordPress cron system runs by default on every page load, which means that scheduled tasks will be run as long as someone visits your website or use a tool to make a web request to the wp-cron.php file.

Execution of Background Tasks: When a task is due to be executed, the WordPress Cron System triggers an HTTP request to the website, which in turn triggers the execution of the task. This HTTP request is made internally within WordPress, and it triggers the WordPress core to check for scheduled events in the database and execute any that are due.
[Link to WP Cron](https://developer.wordpress.org/plugins/cron/)

_So while you can’t be 100% sure when your task will run, you can be 100% sure that it will run eventually_

## Wagtail Thoughts
From carefully reading through RFC 72, it can be seen that 
1. Not all task need to be scheduled, some just need to be non-blocking; e.g. re-indexing pages. We would definitely want pages to be re-indexed asap as published, but in a non-blocking manner. Other tasks like sending emails also
2. Some task need to be scheduled to run at specified times.

The intended implementation is to both use asyncio and Python threads.


## Possible implementation
To implement the proposed feature of background tasks in Wagtail, you can follow these steps:

1. Create a new application that will be responsible for managing background jobs. This application should be added to the INSTALLED_APPS setting in your Django project. Note this is just during development, it would be a package, possibly in contrib

2. Define a Job model that will store information about each background task, including its status, priority, and parameters. This model should include fields such as task name, task arguments, task status, task priority, and timestamps for creation and completion. 

3. Define a backend for executing background tasks, which should be pluggable and configurable. The backend should be able to handle different types of tasks, and should have the ability to prioritize tasks based on their importance.  _This is the grey area_

4. Create a job manager class that will be responsible for creating new jobs, updating their status, and managing their execution. This manager class should include methods for creating, updating, and deleting jobs, as well as for running jobs in the background. The initial scopes is already defined in RFC 72.

5. Create a view or decorator or API endpoint that allows users to create new background jobs. This view should handle user input, create a new job instance, and pass it to the job manager for execution.

6. Implement support for different task backends, such as Redis or Django's ORM. This should allow users to choose the backend that best fits their needs, based on their scale and hosting environment.

7. Add support for scheduling tasks, which should be optional and can be enabled separately. This feature should allow users to schedule background tasks to run at specific times, using cron-like syntax.

8. Document the new feature thoroughly, including how to use it, how to configure it, and how to troubleshoot common issues.

9. Write tests to ensure that the new feature works as expected, and that it is backwards-compatible with existing code.

Release the new version of Wagtail with the background task feature, and announce it to the community.


## Further reading/ research Links
- [Python Long-Running Background Task using Threads](https://superfastpython.com/thread-long-running-background-task/)
- [Python Triggered Threads Background Task](https://superfastpython.com/thread-triggered-background-task/)
- [Book: Effective Python, 2nd Edition - Chapter 7: Concurrency and Parallelism](https://learning.oreilly.com/library/view/effective-python-90/9780134854717/ch07.xhtml#ch7)
- [Book: Fluent Python, 2nd Edition - Chapter 19. Concurrency Models in Python](https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/ch19.html)


## Other areas that this can help - Little Language models
> If content is King, the conversation is Queen - {Attribution incoming}
Large language models like ChatGPT makes the news, being trained on all or most of the available internet contents, but do we all need Large Language model for all use cases... I think not.
This is where little language model comes in. Little language model knows a lot about a little.

We already have a CMS, C = Content, so why don't we train a Little Language Model on that content, and possibly build a better chatbot than the rule based system.
This idea is still in its early stages... To be continued.



