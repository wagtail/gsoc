# Madhvi Rathor

## About Me
I graduated in bca Computer Science student with a strong 
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
I propose building an intelligent, interactive demo platform that 
transforms the learning experience for new Wagtail developers.

**1. Self-Explaining UI Layer**  
An interactive overlay system where users can click on any 
rendered UI component and instantly see:
- Which Django template rendered it
- Which Wagtail model or StreamField powers it
- How the data flows from the database to the frontend

This makes Wagtail's architecture visible and understandable 
in real time — something no CMS demo currently offers.

**2. Code-to-UI Mapping Engine**  
A structured mapping system that connects every visible UI 
element to its corresponding code:
- UI Component → Django Template
- Template → Wagtail Page Model
- Model → Database fields and structure

Developers can visualize the full stack at a glance without 
having to dig through files manually.

**3. AI-Powered Explanation Engine**  
Using Python NLP techniques including HuggingFace transformers 
and Scikit-learn, the engine will:
- Generate human-readable explanations of backend logic
- Summarize what each page or component does
- Convert complex Wagtail concepts into beginner-friendly language
- Provide fallback template-based explanations for accuracy

**4. Adaptive Learning System**  
A personalized onboarding module that:
- Tracks which features a user has explored
- Suggests the next most relevant feature to learn
- Provides step-by-step guided tours for different skill levels:
  beginner, intermediate, and advanced

**5. Modular Real-World Demo System**  
Multiple real-world demo modules to showcase Wagtail in action:
- Blog system with rich text, images, and tags
- E-commerce product listing page
- Portfolio showcase
- Live CMS editing interface

Each module will clearly demonstrate real-world Wagtail usage 
patterns that developers can directly apply in their own projects.

**6. Developer Debug & Insight Mode**  
A toggle-based developer mode that allows:
- Inspecting all API calls made on a page
- Visualizing data flow between components
- Analyzing template rendering performance in real time

### Technical Architecture
| Layer | Technology |
|-------|-----------|
| Frontend | React, Next.js 14 (App Router), TypeScript |
| Backend | Python, Django 4.x, Wagtail CMS |
| AI/ML | HuggingFace, Scikit-learn, Pinecone |
| Database | PostgreSQL |
| Auth | JWT Token Management |
| Performance | Page load < 2s, Lighthouse score > 90 |
| Accessibility | WCAG 2.1 AA compliant |

### Timeline
| Weeks | Work |
|-------|------|
| 1-2 | Community bonding, codebase deep dive, requirement analysis |
| 3-4 | System design, UI/UX wireframes, architecture finalization |
| 5-6 | Core UI development, self-explaining overlay layer |
| 7-8 | Code-to-UI mapping engine, backend API integration |
| 9-10 | AI/ML explanation engine, adaptive learning system |
| 11-12 | Testing, performance optimization, documentation, submission |

**Proposal:** https://summerofcode.withgoogle.com/proposals/details/O7G2G1vQ  
**Project Repo:** https://github.com/madhvirathor14/wagtail-ai-demo-platform

## Technical Skills

**Frontend**
- React.js, Next.js 14 (App Router), TypeScript
- HTML5, CSS3, Tailwind CSS, Responsive Design

**Backend**
- Python 3.x, Django 4.x, Wagtail CMS
- REST API design, Django REST Framework

**AI/ML** *(Internship Experience)*
- Scikit-learn, NumPy, Pandas
- HuggingFace Transformers, NLP pipelines
- Vector databases (Pinecone), Semantic search
- Building and evaluating ML models in production

**Database & Tools**
- PostgreSQL, database schema design
- Git, GitHub, CI/CD basics

## Contributions to Wagtail

**PR #8 — bakerydemo-nextjs**  
Fixed inconsistent image aspect ratio and cropping behavior 
in the PictureCard component across location and gallery pages.
This was a real UX issue affecting how images were displayed 
across different screen sizes.  
Link: https://github.com/wagtail/bakerydemo-nextjs/pull/8

## Why This Project Matters
Every great open-source project needs great onboarding. Wagtail 
has a powerful and elegant architecture, but new developers 
often struggle to see how everything connects. This project makes 
Wagtail's internals visible, understandable, and approachable — 
which will help grow the community and make Wagtail the go-to 
choice for developers evaluating Django CMS options.

## Why Me
During my internship, I worked extensively with Python, NumPy, 
Pandas, and Scikit-learn to build and evaluate ML models — which 
gives me practical, real-world experience with the AI/ML side of 
this project. Alongside that, I have been building full-stack 
applications with React, Next.js, and Django for over a year.

What makes me confident about delivering this project is that I 
have already worked across all three layers it requires — an 
interactive React frontend, a Django/Wagtail backend, and real 
ML pipelines from my internship. I understand how these pieces 
fit together in a production environment, not just in theory.

I genuinely care about developer experience and open-source 
contribution. I want to build something that makes Wagtail 
easier to learn for every new developer who encounters it — 
and I plan to stay involved with the Wagtail community long 
after GSoC ends.

## Contact
- 📧 Email: madhvirathor14@gmail.com
- 🐙 GitHub: https://github.com/madhvirathor14
- 💬 Slack: Madhvi Rathore
