# Bakerydemo Maintenance Skill for AI Agents

This skill was written from real contributor experience working on bakerydemo (February–March 2026) and from Wagtail experience since December 2025.Follow these guidelines to contribute correctly and avoid common mistakes.


## 1. Project Organization & Architecture

When asked to navigate the repository, use this mental map

**Core Settings:** `bakerydemo/settings/`
Use `base.py` for global settings.

**Wagtail Apps — one responsibility each:**

| App | Purpose |
|---|---|
| `base` | Homepage, shared blocks, forms, gallery |
| `blog` | Blog pages and index |
| `breads` | Bread models, ingredients, countries |
| `locations` | Store locations, operating hours |
| `people` | Authors, staff |
| `search` | Search logic and results |

**Templates:** `bakerydemo/templates/`

**Key file to understand first:**
`bakerydemo/base/fixtures/bakerydemo.json`
This is the entire demo database in JSON form.
Every page, image, ingredient lives here.
Handle it carefully (see Section 5).

---

## 2. Wagtail Model Best Practices

### Always Add content_panels

The most common Django→Wagtail mistake.
Without it, fields exist in database but are
completely invisible in Wagtail admin.
```python
#  This looks fine but editors can't see the fields
class PersonPage(Page):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

#  Using this the  fields  are visible in admin
class PersonPage(Page):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
    ]
```

### Image Fields

Never hardcode the image model string.
```python
from wagtail.images import get_image_model_string

# Wrong Approach
image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
)

# Correct Approach
image = models.ForeignKey(
    get_image_model_string(),
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
)
```

### ManyToMany Relationships
```python
# The code below  breaks Wagtail revision system
ingredients = models.ManyToManyField(...)

# Use the following code instead of the above
ingredients = ParentalManyToManyField(...)
```

### Page Queries
```python
# Django 
PersonPage.objects.filter(live=True)

#  Wagtail specific
PersonPage.objects.live()

#  Get children of specific index page
self.get_children().type(PersonPage).live()

#  Avoid N+1 queries at scale
BlogPage.objects.live().select_related('owner')
```

### Time & Dates
```python
#  timezone naive
from datetime import datetime
now = datetime.now()

# timezone aware
from django.utils import timezone
now = timezone.localtime()
```
Use the timezone aware one

### get_context() for Pagination
```python
def get_context(self, request):
    context = super().get_context(request)
    people = (
        self.get_children()
        .type(PersonPage)
        .live()
        .order_by('last_name')
    )
    paginator = Paginator(people, 20)
    context['people'] = paginator.get_page(
        request.GET.get('page', 1)
    )
    return context
```

---

## 3. StreamField & Templates

### StreamField
```python
body = StreamField(
    BaseStreamBlock(),
    blank=True,
    use_json_field=True
)
```

### Images in Templates
```html
<!--  Wrong -->
<img src="{{ image.url }}" alt="{{ image.title }}">

<!--Corr ect — responsive rendering -->
{% load wagtailimages_tags %}
{% picture image format-{avif,webp,jpeg} fill-300x200 %}

<!-- Decorative images -->
{% image image fill-300x200 alt="" %}
```

### Heading Hierarchy

Never skip heading levels. Skipping h1→h3
violates WCAG and breaks screen readers.
```html
<!--  Wrong — skips h2 -->
<h1>Search results</h1>
<h3 class="listing-card__title">Result</h3>

<!-- Correct -->
<h1>Search results</h1>
<h2 class="listing-card__title">Result</h2>
```

---

## 4. Code Quality & Formatting

Never suggest submitting a PR if make lint fails
```bash
# Format everything automatically
make format

# Check without changing files
make lint

# Format fixture file specifically
npx prettier --write \
  bakerydemo/base/fixtures/bakerydemo.json
```

### Commit Message Format
```
fix: resolve timezone-naive datetime in location models
feat: add PersonPage and PersonIndexPage models
docs: update contributing instructions
```

---

## 5. Fixture Management

This is where most new contributors go wrong.

### What is the Fixture?

`bakerydemo/base/fixtures/bakerydemo.json` is a
snapshot of the entire demo database. When someone
clones the project fresh, this file populates
their database via:
```bash
python manage.py load_initial_data
```

### For Small Changes (Recommended)

Edit `bakerydemo.json` directly in VS Code
using Find & Replace (Ctrl+H).
Then immediately format:
```bash
npx prettier --write \
  bakerydemo/base/fixtures/bakerydemo.json
```

Check the diff is small:
```bash
git diff --stat \
  bakerydemo/base/fixtures/bakerydemo.json
```

### For Large Changes
```bash
python manage.py dumpdata \
  --natural-foreign --indent 2 \
  -e auth.permission \
  -e contenttypes \
  -e wagtailcore.GroupCollectionPermission \
  -e wagtailimages.rendition \
  -e sessions \
  -e wagtailsearch.indexentry \
  -e wagtailsearch.sqliteftsindexentry \
  -e wagtailcore.referenceindex \
  -e wagtailcore.pagesubscription \
  -e wagtailcore.workflowcontenttype \
  -e wagtailadmin.editingsession \
  > bakerydemo/base/fixtures/bakerydemo.json

npx prettier --write \
  bakerydemo/base/fixtures/bakerydemo.json
```

### Always Publish Before Exporting

Unpublished pages don't appear in dumpdata.
Save draft ≠ Published.
Always click Publish before running dumpdata.

---

## 6. Windows-Specific Guide

*This section comes from painful firsthand
experience — not documentation.*

### The Problem

Running `dumpdata` on Windows without proper
encoding settings silently adds:
- UTF-8 BOM characters at file start
- CRLF line endings instead of LF
- Result: 20,000+ line diffs for tiny changes
- Result: PR gets rejected immediately

This happened to me twice before finding the fix.

### The Fix

Always use **Git Bash** (never PowerShell):
```bash
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1
python manage.py dumpdata ...
```

### Verify Before Committing
```bash
# Should show ONLY your intended changes
# Thousands of lines = something went wrong
git diff bakerydemo/base/fixtures/bakerydemo.json
```

### Files to Never Commit
```
db.sqlite3    → your local database
.env          → your secret keys
```

---

## 7. Testing

Use `WagtailPageTestCase` not plain `TestCase`.
```python
from wagtail.test.utils import WagtailPageTestCase

class PersonPageTest(WagtailPageTestCase):
    def test_can_create_at(self):
        self.assertCanCreateAt(
            PersonIndexPage,
            PersonPage
        )

    def test_renders(self):
        response = self.client.get('/people/')
        self.assertEqual(response.status_code, 200)
```

---

## 8. Accessibility Checklist
```
[ ] Heading levels sequential (h1→h2→h3)
[ ] All images have descriptive alt text
[ ] All interactive elements have aria-labels
[ ] Lighthouse score 90+
[ ] axe DevTools — zero violations
[ ] NVDA screen reader — content readable
```

---

## 9. PR Checklist
```
[ ] make lint will pass on my changes
[ ] Fixture diff is minimal and focused
[ ] db.sqlite3 is not included
[ ] .env is not included
[ ] Pages are published before dumpdata runs
[ ] Tests are included for new functionality
```

---

## 10. Useful Commands Reference
```bash
# Fresh database setup
python manage.py migrate
python manage.py load_initial_data
python manage.py runserver

# Fix Windows encoding (run before dumpdata)
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1

# Check fixture changes
git diff --stat \
  bakerydemo/base/fixtures/bakerydemo.json

# Format everything
make format

# Run tests
python manage.py test
```

---

## Resources

- Wagtail docs: https://docs.wagtail.org
- bakerydemo: https://github.com/wagtail/bakerydemo
- Redesign plan: https://github.com/wagtail/bakerydemo/issues/566
- Contributing guide: CONTRIBUTING.md in repo
