---
title: "Confirmed Email Privacy Hole at Orkut"
slug: "confirmed_email"
url: "/2004/02/confirmed_email.html"
tags:
  - "Security"
  - "Social Software"
  - "Web/Tech"
  - "orkut"
  - "social software"
  - "social networking"
  - "privacy"
  - "email"
  - "hole"
  - "feedback"
  - "beta"
date: "2004-02-01T17:12:22-07:00"
---
<p>Another Orkut user and I have confirmed a privacy hole in Orkut whenever you send a message to someone via Orkut.</p>
<p>For instance, whenever I send a message to anyone in the system that is forwarded by email, in the message headers it will read:</p>
<blockquote><pre>
From: "Christopher Allen" &lt;member@orkut.com&gt;
Reply-To: "Christopher Allen" &lt;christophera@alacritymanagement.com>;</pre></blockquote>
<p>When someone reads the message in their email software, the "From:" line will be my name but the fake email of &lt;member@orkut.com&gt; -- however, when you reply to it, it will use my real email address. This appears to happen whether or not I have my privacy settings to reveal my email address. For instance, I can set it so that no one (not friends, not friends of friends, only myself) can see my email address, but the address will still be revealed when I send an email</p>
<p>I had reported what I thought was a security flaw when you emailed to "friends of friends" a couple of days ago, but I was mistaken, as I reported in my blog <a href="/2004/01/insecurity_at_o.html">Insecurity at Orkut</a>.  However, as I didn't want risk "crying wolf" this time, so my friend and I triple checked this and have confirmed this privacy flaw.</p>
<p><s>They only way that I know of to avoid this is in your prefences to set that all of your messages should be sent to you via the web, not email.</s> [Updated: I was wrong, there is no way currently to avoid this other then not using an email address you care about.]</p>
<p>There are some that will say that this is a feature, i.e. when using email "what good is communicating with someone if there is no chance of a response" -- my answer to this is that an expectation has been set that email addresses can remain private, and if this is to be a feature, then users should be warned before sending an email "Your email address user@domain will be revealed when you send this." More ideally, like other social networking services, the "Reply-to:" should be to a special email address at Orkut that will do the lookup and forward appropriately.</p>
<p>One of the essential problems that Orkut needs to fix very soon is how to report problems like these, and if you are trying to help how to know that these problems exist. I want my criticism to be constructive, but it is very hard when you have no idea what is the best way to offer feedback. I've had many people reply to me in my blog and via email that they feel the same way.</p>
<p>For instance, right now there are 6 Orkut groups about Orkut:</p>
<ul><li><a href="http://www.orkut.com/Community.aspx?cmm=617">What Should Orkut Do?</a></li>
<li><a href="http://www.orkut.com/Community.aspx?cmm=2026">Flaws in Orkut</a></li>
<li><a href="http://www.orkut.com/Community.aspx?cmm=3982">Orkut</a></li>
<li><a href="http://www.orkut.com/Community.aspx?cmm=1289">Orkut Design</a></li>
<li><a href="http://www.orkut.com/Community.aspx?cmm=781">Orkut: Tips, Feedback, ?'s</a></li>
<li><a href="http://www.orkut.com/Community.aspx?cmm=4556">Orkut Members</a></li></ul>
<p>Which groups should I post this problem to? Which will will be read by the Orkut staff?</p>
<p>As I've said in another of my blog postings <a href="/2004/02/followup_on_ork.html">Followup on Orkut</a>: <blockquote>Part of the problem is that even though Orkut is in beta, there is no organized feedback system. For instance they could offer a forum read by the developers, or even better a bug/issues tracking system like TypePad has, or Bugzilla.</p>
<p>In addition, feedback is a two-way street -- they could do a lot by offering a developers daily blog, or some type of regular announcement of what feature they wanted beta testers to test that day, or even acknowledgement "we already know that is an issue". Also, they need to show respect for good feedback publicly, as that will encourage more good feedback.</p>
<p>None of this is happening at this time, which means that people get frustrated, which also makes it easy rumors and conspiracy to spread. I want to be a constructive critic, but Orkut makes it hard for me to be so.</blockquote></p>
<p>For now, I recommend that these type of bug reports go into <a href="http://www.orkut.com/Community.aspx?cmm=6048">Orkut Beta</a></li>. Why not in "Flaws in Orkut" or in one of the other groups? Because I feel that focusing on 'Flaws' is too strongly negative, and none of the others quite fit. I've been a software developer -- everything is a compromise and good design is hard. By staying on the topics of current features, feature requests, bugs, suggestions, and by encouraging constructive critism and a balance of both positive and negative feedback, this group will be the best community for us to help Orkut until they offer us better alternatives.<br />
</p>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">In the above I said "They only way that I know of to avoid this is in your prefences to set that all of your messages should be sent to you via the web, not email."
However, this is incorrect, it will still send your email address in the
"Reply-To:"
At this time there is no way I know of to avoid this flaw if you are concerned about your email address other then changing it to a temporary one.
</p>
<a class="u-author h-card" href="http://www.lifewithalacrity.com/">Christopher Allen</a>
<time class="dt-published" datetime="2004-02-01T21:47:40-07:00">2004-02-01T21:47:40-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">That's a pretty big "bug" (or unpublished feature) indeed (!)
For example, personally I try to keep my work email address off the net as much as possible, and have set pretty strict privacy settings on orkut, assuming they'd keep it private...
Coincidentally (!!??) the amount of spam I'm receiving at my work email address has gone up vastly since joining Orkut... A very odd coincidence...
</p>
<a class="u-author h-card" href="http://www.jacobsen.no/anders/blog/">Anders</a>
<time class="dt-published" datetime="2004-02-03T04:14:32-07:00">2004-02-03T04:14:32-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">I discovered why I got 'jailed' for a third time today. Two of us appear to have been jailed because of a bug when posting to groups. What happens is that if you write a long post, rather then the system tell you something is wrong, your posting form will just be refreshed. This will prompt you to submit a few more times, unsuccessfully. Then you realize it must be because your post is too long, so you'll remove text a few times, and submit. At some point in this process, typically before you successfully trim it down enough to successfully post, you will discover you are in Orkut jail.
Of course, that makes us long-winded bloggers particularly vulnerable ;-)
</p>
<a class="u-author h-card" href="http://www.lifewithalacrity.com/">Christopher Allen</a>
<time class="dt-published" datetime="2004-02-03T07:17:25-07:00">2004-02-03T07:17:25-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
my suggestion for forum:  orkut design, because orkut the man himself is a member of that community.
</p>
<a class="u-author h-card" href="#">reader</a>
<time class="dt-published" datetime="2004-02-04T17:18:21-07:00">2004-02-04T17:18:21-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">beta testing for www.swakto.com social networking is open
</p>
<a class="u-author h-card" href="http://www.swato.com">jemai</a>
<time class="dt-published" datetime="2004-07-14T12:40:16-07:00">2004-07-14T12:40:16-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
ive been banned on orkut. what is the maximum time you are banned or when they reply to you?
</p>
<a class="u-author h-card" href="#">sherrzz</a>
<time class="dt-published" datetime="2004-07-18T19:06:48-07:00">2004-07-18T19:06:48-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
i don't know much more about orkut i just want to know what this side about of side.
</p>
<a class="u-author h-card" href="#">nawin</a>
<time class="dt-published" datetime="2004-10-12T00:51:10-07:00">2004-10-12T00:51:10-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2004/02/confirmed_email.html" rel="syndication">orginal layout</a></p>
