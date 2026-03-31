# Madhvi Rathor

## About Me
I completed my graduation in bca branch Computer Science engeneering with a strong 
foundation in full-stack web development and machine learning. 
Over the past year, I have built multiple projects combining 
React/Next.js frontends with Django backends, and have hands-on 
experience integrating AI/ML models into real-world applications 
through my internship.

I discovered Wagtail while exploring Django-based CMS solutions 
and was immediately drawn to its developer-friendly architecture, 
clean API design, and active open-source community. I have spent 
the past few weeks studying the Wagtail codebase, contributing 
to bakerydemo-nextjs, and engaging with the community on Slack.

## GSoC 2026 Project
**AI-Powered Self-Explaining & Adaptive Learning Demo Platform 
for Wagtail CMS**

### Problem
The current Wagtail demo site is largely static. New developers 
can see what Wagtail produces but cannot understand how it works 
internally. There is no guided onboarding, no way to trace how 
a UI component connects to its Django template or Wagtail model, 
and no intelligent assistance to help beginners get started 
quickly. This creates a steep learning curve and slows adoption.

### My Solution

**1. Self-Explaining UI Layer**
An interactive overlay system where users can click on any 
rendered UI component and instantly see:
- Which Django template rendered it
- Which Wagtail model or StreamField powers it
- How the data flows from the database to the frontend

**2. Code-to-UI Mapping Engine**
A structured mapping system that connects every visible UI 
element to its corresponding code:
- UI Component → Django Template
- Template → Wagtail Page Model
- Model → Database fields and structure

**3. AI-Powered Explanation Engine**
Using Python NLP techniques including HuggingFace transformers 
and Scikit-learn, the engine will:
- Generate human-readable explanations of backend logic
- Summarize what each page or component does
- Convert complex Wagtail concepts into beginner-friendly language

**4. Adaptive Learning System**
A personalized onboarding module that:
- Tracks which features a user has explored
- Suggests the next most relevant feature to learn
- Provides step-by-step guided tours for different skill levels

**5. Modular Real-World Demo System**
- Blog system with rich text, images, and tags
- E-commerce product listing page
- Portfolio showcase
- Live CMS editing interface

**6. Developer Debug & Insight Mode**
- Inspecting all API calls made on a page
- Visualizing data flow between components
- Analyzing template rendering performance in real time

### Technical Architecture
| Layer | Technology |
|-------|-----------|
| Frontend | React, Next.js 14, TypeScript |
| Backend | Python, Django 4.x, Wagtail CMS |
| AI/ML | HuggingFace, Scikit-learn, Pinecone |
| Database | PostgreSQL |
| Auth | JWT Token Management |

### Timeline
| Weeks | Work |
|-------|------|
| 1-2 | Community bonding, codebase deep dive |
| 3-4 | System design, UI/UX, architecture |
| 5-6 | Core UI, self-explaining overlay layer |
| 7-8 | Code-to-UI mapping, backend integration |
| 9-10 | AI/ML engine, adaptive learning system |
| 11-12 | Testing, optimization, documentation |

**Proposal:** https://summerofcode.withgoogle.com/proposals/details/O7G2G1vQ
**Project Repo:** https://github.com/madhvirathor14/wagtail-ai-demo-platform

## Technical Skills

**Frontend**
- React.js, Next.js 14, TypeScript
- HTML5, CSS3, Tailwind CSS

**Backend**
- Python, Django 4.x, Wagtail CMS
- REST API, Django REST Framework

**AI/ML** *(Internship Experience)*
- Scikit-learn, NumPy, Pandas
- HuggingFace Transformers, NLP pipelines
- Vector databases, Semantic search

**Database & Tools**
- PostgreSQL, Git, GitHub

## Contributions to Wagtail
**PR #8 — bakerydemo-nextjs**
Fixed inconsistent image aspect ratio in PictureCard component.
https://github.com/wagtail/bakerydemo-nextjs/pull/8

## Why This Project Matters
Wagtail has a powerful architecture but new developers often 
struggle to see how everything connects. This project makes 
Wagtail's internals visible and approachable — helping grow 
the community and making Wagtail the go-to Django CMS choice.

## Why Me
During my internship, I worked extensively with Python, NumPy, 
Pandas, and Scikit-learn to build and evaluate ML models — 
giving me practical experience with the AI/ML side of this 
project. I have also been building full-stack applications 
with React, Next.js, and Django for over a year.

I genuinely care about developer experience and open-source 
contribution. I want to build something that makes Wagtail 
easier to learn for every new developer who encounters it.

## Contact
- 📧 Email: madhvirathor14@gmail.com
- 🐙 GitHub: https://github.com/madhvirathor14
- 💬 Slack: Madhvi Rathor