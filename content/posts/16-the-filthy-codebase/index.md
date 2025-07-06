---
slug: lol-3
title: Lol 3
authors:
- Lucas Lira Gomes
created_date: 2024-03-22 19:30
quote: "Lol"
quote_author: Lol
category: Work
tags:
- growth
- career
draft: True
---

There are many concepts that stuck to me during my career – helping to shape my engineering ethos. One that brings back memories is of when I was reading the Pragmatic Engineer during my graduation and bumped into the Broken Window theory for the first time.

It imprinted in me the notion, simply put, that no one wants to be the first to mess up a pristine environment, but if chaos is already there, most wouldn't shy away from worsening it. In fact, I've experienced that just this Summer, when my parents were visiting me and my wife. The situation happened among our weekend walks, when my father intentionally threw a piece of paper on the sidewalk as we passed by. We were a couple of minutes away from home and I could nevertheless see a trash can close by, so I reproached him. Even more because that was not a usual practice of him – not as I was a child, so definitely not now. My father then – displaying an embarrassed countenance – picked it up from the floor, as he noticed I was bothered. After which he humorously remarked the street was, and I quote, “already filthy”.

I've seen instances of this so many times during my career as a software engineer. Poorly tested codebases, in which encompassing automated tests were a by product of perhaps a few persistent fellows, but mostly neglected. Or test suites of humungous services, which just seemed to be in a trajectory of almost bottomless execution time. As if nobody cared to increase ten seconds, when that would be likely seemed as outrageous for a test suite that used to take just a blink of an eye to execute. All part of a worry I have, which naturally transcends testing practices.

It might be just as well be all anecdotal evidence, you might counter, but nevertheless that pattern has emerged so many times, that my gut feeling cannot object to it. That said, even though I'm not of big fan of behavioral determinism, I believe that's one of the few instances when behaviorism works best.

A sheer unavoidable consequence, such as backed by automated checks of any kind (e.g., linters, formatters, type checkers), is most often than not the reasonable way to curb that sort of unwanted behavior. Yes, I believe that sometimes the best incentive you can provide, is to ensure an unavoidable penalty that normalizes the culture we want. Curiously, there is a very popular adage in Germany: “Vertrauen ist gut, Kontrolle ist besser”. Aphorism that was allegedly coined by Lenin and is close to the Russian proverb equivalent later popularized in English: "Trust, but verify".

One situation that demonstrates my enthusiasm on the matter, happened in 2016. Soon after I moved to Germany for my first role after graduation, I found out our team had no automatic test suite running as part of our deployment workflow. There were automated tests, which I could run locally, but not as an enforced part of the deployment flow. That was odd to me, since my previous experiences with open source as part and after Google Summer of Code, had me very convinced of the value of not trusting large groups to keep codebases tidy without the right incentives.

Therefore, on the day our team finally got the test suite running as part of the deployment flow, I uttered a “What a lovely day” as the tests there passed for my new pull request. To which a British coworker, who eventually to become my manager and happened to be looking through a large window contemplating the ever-present thick cloudiness of Berlin, replied humorously: “Well, we know you haven't moved here for the weather”.

So let's keep it harder for ourselves to do the wrong thing – for our good intentions are not the best enforcers.
