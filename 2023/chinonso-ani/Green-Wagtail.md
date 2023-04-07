# Greener coding: Wagtail’s climate impact
I read through this project idea, watched @mrchrisadams video from 2020, this is quite a long-tail project requiring substantive research.

## 1. Identify & Understand
- Understand the climate impact of python/django and by extension wagtail project.
This involves reading through the green coding project from a couple of sources he listed
* [From Wagtail Discussion: Greener coding - Making a 'gold' reference configuration with the Wagtail bakery app #8843](https://github.com/wagtail/wagtail/discussions/8843)
* Understanding how [Neon.tech](https://neon.tech/docs/introduction) implemented a serverless PostreSQL - is it possible to implement a serverless wagtail??? (Big weird question - a wagtail that can be deployed to lambda or something similar)
* Code optimization: this is going to be a hard one, but what can be optimized about where/how wagtail runs, is written, is deployed?


## 2. Design
I think it is important to follow a test driven approach here. To make sure we know when we have done it right. 
>What does it mean to have done right? (how would done right look like?)

GOLD - Green Open Lean Distributed
Our design must be golden. (I love this phrase, because I'm the Goldsmith.)

1. Qualitative: 
2. Quantitative: Ideas discussed [here](https://www.cloudcarbonfootprint.org/docs/methodology/) follow a qualitative measure. Provides a good startup pad.
3. Mixed
4. Performance indicators

### 2.1. Qualitative
There's not a lot of reference to qualitative stuffs and for good reason, @mrchrisadams started with 
>I hope this isn't too left-field for the discussion [here](https://github.com/wagtail/wagtail/discussions/8843) ... interest in the community in demonstrating some of the ideas using wagtail as as real world reference project

Qualitative design strategies involve conducting user surveys, interviewing stakeholders and conducting expert reviews. This mustn't be for wagtail, it could be for django or even python as a whole.
>At breaks during (python, django) meetups we could approach people with a form to be developed. Who know what we might discover? 

We could also do an online voluntary survey. Or at DjangoCon in June.

### 2.2. Quantitative
I personally love the objectivity to which @mrchrisadams approached this subject. Many quantitative design strategies have been outlined, but a good way to approach this would be to:
1. Conduct a life-cycle assessment of wagtail - this would provide a comprehensive understanding of the environmental impact of the product.
2. Analyze server resource usage: product energy consumption, carbon footprint.
3. Calculate carbon emissions (and maybe savings)
>@mrchrisadams said: He burnt through millions of VCs money trying to do this for years. 

We don't have the money or the time.

At step 2 is where we would be trying out different deployment configurations, starting with docker containers that he has already drawn out... and then others.

I was at an AWS event where they spoke about cold-starting problems with Java apps deployed as serverless - can't remember the full details, but I think this could be a close corollary

## 3. Develop
Setting up a similar test structure like the example LAMP Stack.

Implementing ideas, plans and strategies realized from the design phase.

## 4. Test
Test what was developed according to design parameters that have been set.

The wagtail bakery demo would be used for the testing using the configurations designed and deployed

The major thing we test against is performance. Hope we haven't degraded performance... if so, by how much?

## 5. Expected Output
The expected output will most likely affect how wagtail and most django/ python projects are built and deployed.

Also a report on objectivity of the output is also required to answer the question posed: 
>Are the savings worth the extra hassle compared to running it on a VPS?

A breakthrough would be highlighting how people could save more on billing if they did one more thing right - which is what we hope to discover.

A well (or better) architected wagtail might be the end result. The GOLD standard for python projects maybe 


# Schedule and milestones
TBD... this section will describe how much time to devote to each of the activities above.

