---
slug: the-low-hanging-fruits-of-technical-writing
title: The low-hanging fruits of technical writing
authors:
- Lucas Lira Gomes
created_date: 2023-02-05 19:30
quote: "What is written without effort is in general read without pleasure."
quote_author: Samuel Johnson
category: Work
tags:
- writing
---

If there is one ability I see engineers overlooking, that is writing. Perplexing as it may be, many don't realize how much eloquent writing can help advance their careers – especially at companies with mature documentation practices such as FAANG. I'd go as far as to say that it's one of the key skills, if going past your terminal IC level (i.e., senior level) is an ambition of yours.

Proper technical writing shouldn't require you to be a master writer, though. Just like in coding, there are patterns we can rely on to get somewhere between, and my aim for this article is to show you how. Expect me to share a few low-hanging fruits that you can pay more attention to, when writing that important design doc, which seems to be stuck on review hell.

Yes, allow me to reveal the ultimate truth. Being right, about an architectural choice or design, is only the beginning. You still need to present your ideas convincingly, which is a subject for another day, and to convey the information as you want it to be received. So that you don't fall short on that last one, here goes a few soft and hard things to consider.

[TOC]

## The soft things
That's what I call the common sense – rules to live by. A set of principles that will help you write better, without teaching you anything linguistic.

### Have some structure
Whenever I see an introduction section of a technical document, I get ready for three things. They are: the context, the problem, and the solution's outcome. All in this precise order. A failure in that regard, will likely mean that your reader will have to skim back and forth in your text, trying to figure out the missing information. However, just like a code full of goto expressions can be a context switch nightmare. This isn't far, either. Being predictable in technical text is good.

### Helping others to help you
If you write clear, concise and well-written text – the trifecta of writing – you will have less trouble when it comes to the long-lasting peer-review rounds. While that is still truth, I want to talk about an often overlooked aspect: the peer-review round itself. 

How many times have I seen engineers reply to a comment on their text, stating that they have explained whatever the commentor is asking in section X? That's it. They think, they already explained that well somewhere, and the commentor might not have been paying attention.

Let me tell you one truth: when I see a comment like this, I think, oh well. I'll have a look later – more likely some other day. And there it goes, another day in which you are likely blocked waiting for a response of mine, which could be prevented, if you had put the effort to summarize why my question isn't a problem. And then definitely mentioned that I can find more on section X.

Why would a reviewer behave like this? Well, because that someone has other stuff to care about. Plus, there is no downside in replying later. So, you should probably consider this dynamic, next time you make it hard for anyone else to help you. For more on the topic of getting help, there is a previous post of mine, which you might find useful: https://x8lucas8x.com/how-can-i-help-you.

### Out of breath
If there is something annoying in text, it is to be forced to stop midway in a sentence: to catch breath. Because the writer thought it was fine to amass forty-plus words together in a single phrase – often with little to no punctuation. Try reading the following sentence to have a sense of what I mean:

> The Linux Kernel started to be developed by the at the time 21-years old Linus Torvalds in the early months of the year of 1991 as a hobby that would end up being the poster child of the open-source movement and one of the most successful operating systems to date.

Let me say it once and for all. That isn't fine. You lost me – at the expense of your argument. That reminds me of those Stack Overflow's folks that reply with a very convoluted single line response, such as:

> q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

Or that proverbial academic paper verbiage, in which the text has proper punctuation in place, but chain four-plus subordinate clauses, instead of splitting them in multiple sentences. Let's see a non-academic example of the same issue:

> The solution, proposed by team A, can address solution X, provided team A finds a way to convince leadership, which might be wary to schedule it for Q1, given the CEO's push for the new design, which has been in discussion for a while.

Don't be that person. Readability trumps any of this, provided you care about your point reaching anyone else besides yourself. Readability that can be ensured by writing short and to the point phrases.

### Clarity is king
No, you can't assume I know what you mean, unless you have made me walk through your shoes – ideally through one story that grows in complexity incrementally. It isn't obvious, really. That you're meant to rely on system A or B and that's right because: 1) you have been at the company long enough to know that or 2) your team is familiar with it. So write it down.

It's not my fault, if I couldn't understand what you had to say. It might not even be your fault, either, since I might lack business or technical context to realize why something is important. But be certain it will be your fault, have you failed to make your point to the “right” people. Who are they? Think leadership planning whether your project should be on Q1's shortlist, the platform team that act as a gateway in anything X, and the security team in that effort to integrate with a third party.

### Saying more than you need
Be laconic [^1], my friend, said no one. But seriously, why say with more words that which can be said with less. Not following? Then read the following paragraph:

> In light of the time and effort you have spent and may otherwise continue to spend on dealing with their repeated requests for assistance, we can support you for the forthcoming term should the requirements be agreed.

Why write that? When you can simply write:

> We can support you.

Ha, you don't need to be so extreme and that's likely omitting relevant details, so how about: 

> Despite the effort that team X has and might still require, we can start supporting you in that, provided we agree upon some conditions.

The point is, why write that long code comment, when a better variable name would have addressed the issue? Same thing.

### Improve your vocabulary game
Please, don't be that person, who overuses a single word. There is a reason you have myriad, plethora, and cornucopia in your belt after you've spent your share of many and several. You might not know them at first, but it pays off to extend your vocabulary. That way adding nuances to your text. I know that might be hard. After all, I am a non-native speaker myself – Portuguese is my mother tongue. Despite, the secret is to make it a habit to learn new words – one a day is no big ask.

Moreover, vocabulary isn't always a matter of knowing synonyms, but rather of word choice precision. That is why every profession has jargon. Think Lawyers and their “quid pro quo”. Or us and “deadlock”. We could write a whole phrase to mean yet the same thing, but precision demands them.

### Be a reader yourself
Good writing takes yet greater reading. The more you read, the more vocabulary you collect, the better you become at writing. There is no rule here. My wife, for instance, loves romances. Anything Tolstoy, Roth, Houellebecq, Dostoevsky, Pasternak, Shakespeare is game for her. I, on the other hand, prefer to focus on anything ancient, think Plutarch for history or Sophocles for theater. Then add some philosophical works here and there, such as the ones of Seneca. Not to mention the technical reading oriented towards my craft – currently reading “The Staff Engineer's Path” by Tanya Reilly. So try finding some time. For us, reading just before bed is what works best habit-wise.

### When in Rome
I certainly won't be the first person telling you to know your audience. The reason is simple. If people cannot relate to your writing style, it will be harder for you to find a way into their minds. Politicians are doing this when they, for instance, resort to regionalisms or double down on the accent. So blend in. How can you do that in text? Well, for starters, I'd look for pieces from someone's writing you admire in either your team or organization. Then analyze its composition until you can answer what makes their writing worthy of your admiration. Those points are likely something you can also do yourself. That's it, sheer mimesis (i.e., imitation) is still a great tool for learning something or blending in.

### Be respectful
Time is a very precious resource – especially when we are talking about the time of others. So be respectful and do your due diligence, before asking someone to look into your document. Basic grammar mistakes and sloppy sentence building aren't really acceptable. It communicates you don't consider that your time is as valuable as that of your reader. So try to be mindful. You can't simply expect that the first version of anything you write is proper. Mine isn't. Yours aren't. That means you should read yourself a couple of times – sometimes even out loud. Improve what can be improved. Put some effort, really. Is this preciousness? No, do justice to your subject first. Only then you should consider sharing it.

When you do so, understand that it won't be perfect either, but good enough is good enough. Take this very article, for instance. The first time I've published it, even though I had someone proofreading it, I could still find a few things to correct. Furthermore, two days after having it published, a fellow at work asked me if I wanted feedback about the article, which of course I did want. As part of the feedback, though, there were still some grammar mistakes. Is that the end of the world? No, as long as you keep your conscience clear by knowing you've done your part – to the best of your knowledge.

### Tools of the trade
Don't shy away from using grammar checkers. It would be stubborn of you to have aid and, yet, to ignore it. In this spirit, I'd greatly recommend https://languagetool.org/ or similar alternatives (e.g., https://grammarly.com, https://hemingwayapp.com/). I've been using LanguageTool's premium plan for at least six months, since I started being more serious about blogging, and it has helped. Don't get me wrong – they're no panacea, just like linters. Bad text and code are still bad, after all. Unfortunately, there is no tool in the word that can help you with that. However, it's nice to have something suggesting you synonyms to prevent word overuse, fixing basic typos, providing you alternatives for far-fetched expressions, and so on.

## The hard things
This is grammar and style territory. Many people hate it, but just like you can't write idiomatic code without mastering a programming language's syntax, you won't be able to write elegantly without understanding its building blocks.

### Tone down on your pronouns
Oh, I understand we hate to repeat ourselves in text. Pronouns are there to prevent that, but pronouns can also make your technical piece, less precise. Pay attention to the following example:

> As a consequence of the company's positive results, a few longer-term experiments were approved by leadership. They …

When I see that personal pronoun (i.e., they), I know someone is making me have the trouble of figuring out, who or what that “they” might be. Is it about the results? Can it be about the experiments? Or is that person talking about leadership? Who knows? That will require understanding the context, which might mean having to go through a whole paragraph and then get back – until that's figured out. All that could be avoided, had the person avoided a dubious pronoun. Such as on:

> As a consequence of the company's positive results, a few longer-term experiments were approved by leadership. The results … \
> As a consequence of the company's positive results, a few longer-term experiments were approved by leadership. The experiments … \
> As a consequence of the company's positive results, a few longer-term experiments were approved by leadership. The leadership …

You don't need to reuse the precise noun (e.g., results, experiments, leadership), as the examples above. In fact, any synonym would have worked. Additionally, this doesn't mean you shouldn't use pronouns in your technical writing. The takeaway is that you should avoid them, if clarity demands. To leave to context, that which could be clear from the get go, is no way of treating your reader.  

### Images/tables/code samples too deserve names
If there is one thing that is just annoying, is to have to say something like:

> Hey, you know that second image you have on page 82, I think that …

Don't do that. If you have an image, table, or code sample in a technical document, please add a label under it, which can go like:

> Image C1.1: Diagram of the current architecture.\
> Table C2.1: Descriptive statistics of the response timings of endpoint X.\
> Code Sample C3.1: Example of how the system will be tested.

Now, your readers can just say:

> On image C1.1, you seem to …

It just facilitates communication. And that's what you want. Not to stay on the path of people trying to help you. Make it easy to be helped. That also reminds of something my professor of scientific methodology said during my graduation. It went like: If you are not going to mention your image/table/code sample in your text, don't bother adding it. And I have to agree. Worst case, just write something like:

> On Image C1.1, the architecture of the proposed solution is depicted. Essentially, …

That will prepare your readers for what is ahead, or tie with something that came before.

### Forms of adding more context
You likely know that your way to add context to a sentence isn't just through new phrases. Consider:

> GNU/Linux is a great operating system. It is open source. It has a big community behind it.

That could just have been written with a relative clause, by using commas (,), such as:

> GNU/Linux, which is open source, is a great operating system and has a big community behind it.

I believe that's clear, yet you have alternatives. The dash (–) for instance, can be of help here – not to be confounded with a hyphen (-). That same sentence could be:

> GNU/Linux, which is open source, is a great operating system – backed by a big community.

Or perhaps:

> GNU/Linux is a great operating system, which is backed by a big community – a true open-source phenomenon.

Now, the comma (,) can produce the same result, but occasionally, it is nice to see a break amidst a sea of commas.

### Enlisting things
There are many other ways of listing elements, then to just say:

> The main types of users are admins, internal support, paying clients and partners.

While this might be fine for a few elements, it can get out of hand for longer phrases, in which case I'd likely prefer a colon (:) so that it could be roughly like:

> The main types of users are four. They are: admins, internal support, paying clients and partners.

Now I know to expect only four types of users, before even getting to know them. Plus, the phrases are short and sweet. You could also have spent some Latin, as an academic would do, and thrown an id est (exhaustive list equivalent to using a colon) or exempli gratia (non-exhaustive list). Both are often referenced as acronyms – i.e., and e.g., respectively.

> The main types of users are four (i.e., admins, internal support, paying clients, and partners).

Do what you may, but don't just use bare parentheses. When I see them, the first thing I ask is: Is this exhaustive or not? So prefer to use the colon or your Latin equivalents. They are more precise.

### Conjunctions are your friends
Conjunctions, that is an ode to you. How pleasant it is that one or two words, often placed at the beginning of a sentence, can prepare you for the logical argument that is coming next. On the other hand, how frustrating it is when I have to figure that out by context. See the following example:

> Python is a powerful language. The fact that it is simple is key. Some bits of it, such as metaclasses, can be hard to grasp. Learning it as a newcomer might be discouraged. Metaclasses are used under the hood by many popular frameworks, such as sqlalchemy's model and Django's models.

Now look how much better it is when I throw a few conjunctions here and there:

> Python is a powerful language. Moreover, it is simple, however, some bits of it, such as metaclasses, can be hard to grasp. Therefore, it might be better not to focus on it as a newcomer. Even though it might be a complicated feature of Python, many popular frameworks use it under the hood, such as sqlalchemy's model and Django's models.

Do you see how “moreover” (addition relation), “however” (opposition/contrast relation), “therefore” (cause/effect/result relation) and “even though” (opposition/contrast relation) just made it clearer, what was the sort of relation those phrases had? So don't shy away from them. Ah, and please keep in mind your compound versions (e.g., neither … nor …, either … or …, not only … but also …, both … and …). Anyway, you can find more examples of conjunctions on https://www.fluentu.com/blog/english/english-conjunctions/, https://www.grammarly.com/blog/conjunctions/ and https://eslforums.com/list-of-conjunctions/. Before closing this topic, let me warn you that conjunctions for the sake of using them, isn't necessarily better – especially if they are poorly employed. See the following redacted example, which I've reviewed recently as part of a design doc:

> The only considerable cost is the cost of Service A. We were able to get the following pricing scheme from Product B and we have signed up for 3 parallel processes for now and later we will evaluate if we need more parallel processes.

The coordinating conjunction “and” (addition relation), in the aforementioned example, isn't really fulfilling its purpose. That's so the case, that removing its occurrences and keeping distinct sentences instead work just as fine. Additionally, shorter phrases end up being a plus, as can be seen on:

> The only considerable cost is the cost of Service A. We were able to get the following pricing scheme from Product B. We have signed up for 3 parallel processes for now. Later we will evaluate if we need more parallel processes.

This can be definitely improved by toning down on the use of personal pronouns (e.g., we), reordering the sentences and introducing a single adverb as a conjunction (i.e., currently). Consider:

> The only considerable cost is the cost of Service A. Currently, a plan with 3 parallel processes has been adopted, which might be reevaluated later. The following pricing schema was negotiated:

Do you see how that just feels neater?

### Have a style guide of choice
I honestly don't care if you write color or colour, as long as you stick to a version of English. That's the same attitude I have towards the indentation you choose for your C code (e.g., GNU, K&R, Allman) or the linter rules you are going to apply. The important thing is to adopt one style – to stay consistent.

Likewise, there is no such a thing as an ultimate style guide for writing. You can decide to adopt any among https://developers.google.com/style, https://learn.microsoft.com/en-us/style-guide/welcome/, https://www.chicagomanualofstyle.org/home.html, and https://www.ox.ac.uk/sites/files/oxford/media_wysiwyg/University%20of%20Oxford%20Style%20Guide.pdf – the latter being my favorite. What is indispensable, is that you adhere to one.

Those will teach you, for instance, that there are way more than just commas (,) and dots (.) out there. More importantly, they will show you when to use what and when. Familiarize yourself with your style guide now. But you can reply me:

> Lucas, I'd be too bored or don't have time to go through all this grammar mumbo jumbo.

My friend, if you can't make yourself available for going through the thirty slides of the Oxford Style Guide, you don't take yourself seriously. And if you don't, why should I?

## Conclusion

Writing is one of those skills that if you think you are good at it, that's because you don't care enough to keep growing. Like coding, it can take a whole life. You might realize you need to delve deep and get yourself a good grammar book. That might be particularly useful for native speakers, which often have a sense for what is right or wrong, but often can't put on a finger why. 

Finally, if writing ever becomes a passion, like it is for me, you might find yourself reading about how to write. Last year I've felt that need by reading “On Writing Well” by William Zinsser, which I'd greatly recommend.

[^1]: Fun fact: Laconic is an adjective that refers to Laconia. A region in Greece most known for residing Sparta – the famed war-oriented city state of Ancient Greece. Less known is however the fact that Spartans valued being “laconic”.
