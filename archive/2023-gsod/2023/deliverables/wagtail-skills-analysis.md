# Wagtail skills analysis

This is an analysis of the broad competencies required to build a site with Wagtail as a developer. We compare the skills required in two scenarios:

1. To build and understand Wagtail’s official ["Your first Wagtail site" tutorial](https://docs.wagtail.org/en/latest/getting_started/tutorial.html).
2. To build Wagtail’s official demo site, [bakerydemo](https://github.com/wagtail/bakerydemo).

## Gap analysis – before tutorial project

The goal of the new tutorial series is to bridge the gap in knowledge between those two projects. We want someone new to Wagtail to have didactic information available to learn how to build a “real-world” website like the bakerydemo.

For all competencies present across _Your first Wagtail site_ and _bakerydemo_, here is a summary of whether they are included in one project or the other.

- We track 109 competencies in total, across 14 broad areas
- 62 items marked "🚧" are missing in the tutorial, and might be a gap to address.
- 3 items marked "❓" are missing in the bakerydemo

| Competency                                 | "First site" | "bakerydemo" |
| ------------------------------------------ | ------------ | ------------ |
| **Terminal usage**                         | Yes          | Yes          |
| ❓ Command prompts                         | Yes          | No           |
| Basic terminal commands                    | Yes          | Yes          |
| 🚧 Environment variables                   | No           | Yes          |
| **Python**                                 | Yes          | Yes          |
| Basic syntax                               | Yes          | Yes          |
| Virtual environments                       | Yes          | Yes          |
| pip and packages                           | Yes          | Yes          |
| 🚧 Environment-specific requirements files | No           | Yes          |
| **Django**                                 | Yes          | Yes          |
| 🚧 Project apps structure                  | No           | Yes          |
| Django settings                            | Yes          | Yes          |
| 🚧 django-dotenv                           | No           | Yes          |
| 🚧 DJANGO_SETTINGS_MODULE                  | No           | Yes          |
| 🚧 Email backends                          | No           | Yes          |
| Management commands                        | Yes          | Yes          |
| 🚧 Custom management commands              | No           | Yes          |
| Migrations basics                          | Yes          | Yes          |
| **Django Models**                          | Yes          | Yes          |
| Model fields                               | Yes          | Yes          |
| Django ORM / QuerySet basics               | Yes          | Yes          |
| 🚧 Choice fields                           | No           | Yes          |
| 🚧 Mixins                                  | No           | Yes          |
| Forms                                      | Yes          | Yes          |
| Form widget overrides                      | Yes          | Yes          |
| 🚧 Fixtures                                | No           | Yes          |
| 🚧 Django Debug Toolbar                    | No           | Yes          |
| 🚧 Paginator                               | No           | Yes          |
| **Django Templates**                       | Yes          | Yes          |
| Basic syntax                               | Yes          | Yes          |
| Templates inheritance                      | Yes          | Yes          |
| Built-in template tags                     | Yes          | Yes          |
| 🚧 Custom template tags                    | No           | Yes          |
| 🚧 Django Views                            | No           | Yes          |
| 🚧 Error views                             | No           | Yes          |
| 🚧 Messages                                | No           | Yes          |
| **Production infrastructure**              | Yes          | Yes          |
| 🚧 Storage backends                        | No           | Yes          |
| 🚧 uWSGI                                   | No           | Yes          |
| **Wagtail Models**                         | Yes          | Yes          |
| Wagtail user interface                     | Yes          | Yes          |
| Built-in fields                            | Yes          | Yes          |
| 🚧 Rich text                               | No           | Yes          |
| 🚧 Wagtail StreamField                     | No           | Yes          |
| 🚧 Reusable block definitions              | No           | Yes          |
| 🚧 Base block types                        | No           | Yes          |
| 🚧 Block templates                         | No           | Yes          |
| 🚧 Structural block types                  | No           | Yes          |
| 🚧 Combining blocks                        | No           | Yes          |
| 🚧 TableBlock                              | No           | Yes          |
| 🚧 TypedTableBlock                         | No           | Yes          |
| InlinePanel                                | Yes          | Yes          |
| 🚧 Basic definitions                       | No           | Yes          |
| 🚧 Item count constraints                  | No           | Yes          |
| 🚧 **Content panels**                      | No           | Yes          |
| 🚧 FieldPanel                              | No           | Yes          |
| 🚧 MultiFieldPanel and FieldRowPanel       | No           | Yes          |
| 🚧 Block count constraints                 | No           | Yes          |
| **Wagtail Pages**                          | Yes          | Yes          |
| Page models basics                         | Yes          | Yes          |
| Page QuerySet API                          | Yes          | Yes          |
| Page tree structure                        | Yes          | Yes          |
| 🚧 parent_page_types                       | No           | Yes          |
| 🚧 subpage_types                           | No           | Yes          |
| specific vs. base page data                | Yes          | Yes          |
| get_context customisations                 | Yes          | Yes          |
| ParentalKey and ParentalManyToManyField    | Yes          | Yes          |
| 🚧 Page ForeignKey                         | No           | Yes          |
| **Search**                                 | Yes          | Yes          |
| Search indexing basics                     | Yes          | Yes          |
| 🚧 Filter fields                           | No           | Yes          |
| 🚧 Autocomplete fields                     | No           | Yes          |
| 🚧 Search promotion                        | No           | Yes          |
| **Images**                                 | Yes          | Yes          |
| Image fields                               | Yes          | Yes          |
| Images in templates                        | Yes          | Yes          |
| **Content management**                     | Yes          | Yes          |
| Tagging                                    | Yes          | Yes          |
| Tag fields                                 | Yes          | Yes          |
| ❓ Page slugs                              | Yes          | No           |
| ❓ Published vs. draft content             | Yes          | No           |
| **Relational Databases**                   | Yes          | Yes          |
| Database basics                            | Yes          | Yes          |
| Foreign keys                               | Yes          | Yes          |
| Many-to-many relationships                 | Yes          | Yes          |
| 🚧 Site object                             | No           | Yes          |
| 🚧 Sitemap                                 | No           | Yes          |
| 🚧 REST API                                | No           | Yes          |
| 🚧 Pages API                               | No           | Yes          |
| 🚧 Documents API                           | No           | Yes          |
| 🚧 Images API                              | No           | Yes          |
| 🚧 Wagtail hooks                           | No           | Yes          |
| 🚧 register_icons                          | No           | Yes          |
| 🚧 Accessibility checker                   | No           | Yes          |
| 🚧 Wagtail forms                           | No           | Yes          |
| 🚧 FormField API                           | No           | Yes          |
| 🚧 Email forms                             | No           | Yes          |
| **Snippets**                               | Yes          | Yes          |
| 🚧 Draft and live snippets                 | No           | Yes          |
| 🚧 Revisions                               | No           | Yes          |
| 🚧 Previews with templates, modes, context | No           | Yes          |
| 🚧 Translations                            | No           | Yes          |
| 🚧 Documents                               | No           | Yes          |
| 🚧 Embeds                                  | No           | Yes          |
| 🚧 **Site front-end**                      | Yes          | Yes          |
| 🚧 Site search                             | No           | Yes          |
| 🚧 SEO in templates                        | No           | Yes          |
| 🚧 Pagination                              | No           | Yes          |

## Gap analysis – with new tutorial

Of 62 gaps identified at the beginning,

- ✅: 29 have been addressed with the new tutorial series.
- 🏁: 13 have been left unaddressed explicitly, in the interest of reducing the tutorial’s complexity.
- ⌛: 6 have been earmarked as "quick win" iterative improvements to deliver as a follow-up to this project.
- ❓: 16 have been left unaddressed pending further discussion.

| Competency                                 | Gap before | Gap after |
| ------------------------------------------ | ---------- | --------- |
| **Terminal usage**                         | No         |           |
| Command prompts                            | No         |           |
| Basic terminal commands                    | No         |           |
| ✅ Environment variables                   | Yes        | No        |
| **Python**                                 | No         |           |
| Basic syntax                               | No         |           |
| Virtual environments                       | No         |           |
| pip and packages                           | No         |           |
| ❓ Environment-specific requirements files | Yes        | Yes       |
| **Django**                                 | No         |           |
| ✅ Project apps structure                  | Yes        | No        |
| Django settings                            | No         |           |
| 🏁 django-dotenv                           | Yes        | Yes       |
| ✅ DJANGO_SETTINGS_MODULE                  | Yes        | No        |
| ❓ Email backends                          | Yes        | Yes       |
| Management commands                        | No         |           |
| 🏁 Custom management commands              | Yes        | Yes       |
| Migrations basics                          | No         |           |
| **Django Models**                          | No         |           |
| Model fields                               | No         |           |
| Django ORM / QuerySet basics               | No         |           |
| ✅ Choice fields                           | Yes        | No        |
| ✅ Mixins                                  | Yes        | No        |
| Forms                                      | No         |           |
| Form widget overrides                      | No         |           |
| ❓ Fixtures                                | Yes        | Yes       |
| ⌛ Django Debug Toolbar                    | Yes        | Yes       |
| ✅ Paginator                               | Yes        | No        |
| **Django Templates**                       | No         |           |
| Basic syntax                               | No         |           |
| Templates inheritance                      | No         |           |
| Built-in template tags                     | No         |           |
| ✅ Custom template tags                    | Yes        | No        |
| ✅ Django Views                            | Yes        | No        |
| ❓ Error views                             | Yes        | Yes       |
| 🏁 Messages                                | Yes        | Yes       |
| **Production infrastructure**              | No         |           |
| ✅ Storage backends                        | Yes        | No        |
| ✅ uWSGI                                   | Yes        | No        |
| **Wagtail Models**                         | No         |           |
| Wagtail user interface                     | No         |           |
| Built-in fields                            | No         |           |
| ✅ Rich text                               | Yes        | No        |
| ✅ Wagtail StreamField                     | Yes        | No        |
| ✅ Reusable block definitions              | Yes        | No        |
| ✅ Base block types                        | Yes        | No        |
| ✅ Block templates                         | Yes        | No        |
| ✅ Structural block types                  | Yes        | No        |
| ✅ Combining blocks                        | Yes        | No        |
| 🏁 TableBlock                              | Yes        | Yes       |
| 🏁 TypedTableBlock                         | Yes        | Yes       |
| InlinePanel                                | No         |           |
| ❓ Basic definitions                       | Yes        | Yes       |
| ❓ Item count constraints                  | Yes        | Yes       |
| ✅ **Content panels**                      | Yes        | No        |
| ✅ FieldPanel                              | Yes        | No        |
| ✅ MultiFieldPanel and FieldRowPanel       | Yes        | No        |
| ❓ Block count constraints                 | Yes        | Yes       |
| **Wagtail Pages**                          | No         |           |
| Page models basics                         | No         |           |
| Page QuerySet API                          | No         |           |
| Page tree structure                        | No         |           |
| ⌛ parent_page_types                       | Yes        | TODO      |
| ⌛ subpage_types                           | Yes        | TODO      |
| specific vs. base page data                | No         |           |
| get_context customisations                 | No         |           |
| ParentalKey and ParentalManyToManyField    | No         |           |
| ✅ Page ForeignKey                         | Yes        | No        |
| **Search**                                 | No         |           |
| Search indexing basics                     | No         |           |
| ❓ Filter fields                           | Yes        | Yes       |
| ✅ Autocomplete fields                     | Yes        | No        |
| ❓ Search promotion                        | Yes        | Yes       |
| **Images**                                 | No         |           |
| Image fields                               | No         |           |
| Images in templates                        | No         |           |
| **Content management**                     | No         |           |
| Tagging                                    | No         |           |
| Tag fields                                 | No         |           |
| Page slugs                                 | No         |           |
| Published vs. draft content                | No         |           |
| **Relational Databases**                   | No         |           |
| Database basics                            | No         |           |
| Foreign keys                               | No         |           |
| Many-to-many relationships                 | No         |           |
| ❓ Site object                             | Yes        | Yes       |
| ⌛ Sitemap                                 | Yes        | TODO      |
| 🏁 REST API                                | Yes        | Yes       |
| 🏁 Pages API                               | Yes        | Yes       |
| 🏁 Documents API                           | Yes        | Yes       |
| 🏁 Images API                              | Yes        | Yes       |
| ⌛ Wagtail hooks                           | Yes        | TODO      |
| 🏁 register_icons                          | Yes        | Yes       |
| ⌛ Accessibility checker                   | Yes        | Yes       |
| ✅ Wagtail forms                           | Yes        | No        |
| ✅ FormField API                           | Yes        | No        |
| ❓ Email forms                             | Yes        | Yes       |
| **Snippets**                               | No         |           |
| 🏁 Draft and live snippets                 | Yes        | Yes       |
| 🏁 Revisions                               | Yes        | Yes       |
| 🏁 Previews with templates, modes, context | Yes        | Yes       |
| ❓ Translations                            | Yes        | Yes       |
| ✅ Documents                               | Yes        | No        |
| ❓ Embeds                                  | Yes        | Yes       |
| ✅ **Site front-end**                      | No         | No        |
| ✅ Site search                             | Yes        | No        |
| ✅ SEO in templates                        | Yes        | No        |
| ✅ Pagination                              | Yes        | No        |
