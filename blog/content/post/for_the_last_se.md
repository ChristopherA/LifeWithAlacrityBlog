---
title: "SynchroEdit: Simultaneous Editing for the Web"
slug: "for_the_last_se"
url: "/2005/10/for_the_last_se.html"
image: "/previous/images/synchroeditmac.png"
tags:
  - "Social Software"
  - "User Interface"
  - "Web/Tech"
  - "Weblogs"
  - "Wiki"
  - "synchroedit"
  - "simultaneous editor"
  - "web editor"
  - "collaboration"
  - "same-time"
  - "open source"
  - "alpha"
  - "demo"
  - "mozilla"
  - "firefox"
  - "subethaedit"
  - "moonedit"
  - "gobby"
  - "web2point1"
  - "for comment"
  - "jotlive"
  - "socialtext"
  - "joichi ito"
  - "kalle alm"
date: "2005-10-08T16:04:17-07:00"
---
<p>For the last several months I've been working on a new open source project that I've been calling <a href="http://www.synchroedit.com">SynchroEdit</a>. SynchroEdit is a browser-based simultaneous multiuser editor, useful for <a href="http://www.it.bton.ac.uk/staff/rng/teaching/notes/CSCWgroupware.html">&quot;same-time&quot; collaboration</a>.</p>
<p><a href="http://lifewithalacrity.blogs.com/.shared/image.html?/photos/uncategorized/synchroeditmac.png" onclick="window.open(this.href, '_blank', 'width=640,height=493,scrollbars=no,resizable=no,toolbar=no,directories=no,location=no,menubar=no,status=no,left=0,top=0'); return false"><img width="262" height="202" border="0" alt="Synchroeditmac" title="Synchroeditmac" src="/previous/images/synchroeditmac.png" style="margin: 0px 0px 5px 5px; float: right;" /></a>The basic concept is that it allows multiple users to WYSIWYG edit a single web-based document, all at exactly the same time. SynchroEdit continuously synchronizes all changes so that users always see the same version. They can also see each others' changes as they type, see where each user is currently editing, and see each others' changes by color.</p>
<p>SynchroEdit is a tool for &quot;same-time&quot; collaboration, either &quot;same-time, different-place&quot;, as in teleconference calls, or &quot;same-time, same-place&quot;, during a meeting or a conference. If you've ever used <a href="http://www.codingmonkeys.de/subethaedit/">SubEthaEdit</a> on Mac OS X, or <a href="http://www.moonedit.com">MoonEdit</a> for Windows or Linux, or the cross-platform <a href="http://gobby.0x539.de/">Gobby</a>, this is a similar experience. The difference is that unlike those tools you are not limited to just plain text -- character styles (bold, italic, etc.) and paragraph styles (rulers, headers, blockquotes, etc) are synchronized as well. And of course, it all works inside your browser.</p>
<p>SynchroEdit is inspired by my frustration with the lack of an easily accessible cross-platform simultaneous editor. Many times when I've been on the phone with a colleague discussing a draft blog entry, or demonstrating some code, or on a teleconference call with others to discuss a proposal or a standard, or at a conference taking notes with others, I've wanted to have this tool. The rare occasions that we all have been on the same platform and have been able to use an existing tool have demonstrated to me the value of having a good simultaneous editor. Having SynchroEdit available will make it easier for people to have these positive collaborative experiences.&nbsp; </p>
<p>I have a long history with &quot;same-time&quot; collaboration tools -- back in 1988 I was briefly executive producer at Broderbund for a same-time groupware product called <a href="http://www.google.com/search?q=cache:1cDDTqwlqGoJ:www.the-scientist.com/yr1988/jul/software_p22_880725.html+%2Bbroderbund+%2B%22for+comment%22+groupware">For Comment</a>. Unfortunately, the success of the Nintendo game console forced Broderbund to drop all of their non-consumer product efforts. In the early 90's I worked on several different &quot;same-time same-place&quot; groupware tools for live meetings. Most recently, my game company <a href="http://www.skotos.net">Skotos Tech</a>, created several browser-based &quot;enhanced chat&quot; clients for playing in MUSH-like storytelling games, which are also &quot;same-time&quot;.</p>
<p>I personally believe that that this capability should be a fundamental feature of the web, sort of the obvious extension of <a href="http://en.wikipedia.org/wiki/Tim_Berners-Lee">Tim Berners-Lee's</a> <a href="http://news.bbc.co.uk/1/hi/technology/4132752.stm">vision</a> of the editable web. Thus my desire to offer this tool as open source, allowing anyone to add this capability to their own software (unlike proprietary editor services such as <a href="http://www.jotlive.com">JotLive</a> or <a href="http://www.writely.com/">Writely</a>).</p>
<p>The challenge with offering SynchroEdit as open source is finding a business model -- unlike an application like <a href="http://www.codingmonkeys.de/subethaedit/">SubEthaEdit</a> or a service like <a href="http://www.jotlive.com">JotLive</a>, it is difficult to get revenues from individual users. Instead, we ask for contributions from companies that might find the tool useful, we offer consulting to customize it for specific purposes, and we give these companies public credit for their contributions to the common good.</p>
<p>The first company to step up to the plate is <a href="http://www.socialtext.com">SocialText</a>, an enterprise wiki company. Clearly, being able to offer this capability to their customers will give them added value, and they already have a history of using open source with their support of <a href="http://www.kwiki.org/">Kwiki</a> and <a href="http://www.wikiwyg.net/">Wikiwyg</a>.</p>
<p>The second supporter is venture capitalist and blogger <a href="http://joi.ito.com/">Joichi Ito</a>. He is is particularly well known for his own experiments with &quot;same-time&quot; collaboration. He runs a continuous #joiito IRC chat room, active 24 hours a day with hundreds of his friends. He also has done many live &quot;same-time&quot; experiments with chat backchannel during his talks at various conferences.</p>
<p>In addition to to financial support of SocialText and Joichi Ito, I have some offers of help from the <a href="http://www.bgiedu.org">Bainbridge Graduate Institute</a>, who plan to use it in its socially responsible and environmentally sustainable MBA program, and we've also taken advantage of some code developed by <a href="http://www.skotos.net/">Skotos</a>.</p>
<p>The development of SynchroEdit is being led by Kalle Alm, a young Swedish coder I met when he was creating an online game at Skotos. Skotos has long had the vision of having games created by its members, and Kalle Alm was the first member to create a game completely from scratch using Skotos' tools.</p>
<p>We are seeking more financial contributions so that we can accelerate development. Currently SynchroEdit only works in Mozilla/Firefox, and I anticipate that making it work with Internet Explorer may be quite difficult, so we'll need more partners to help.</p>
<p><img border="0" src="/previous/photos/uncategorized/christopher_allen_web2point1_brainjam.png" title="Christopher_allen_web2point1_brainjam" alt="Christopher_allen_web2point1_brainjam" style="margin: 0px 5px 5px 0px; float: left;" />I did a demo of last year's open source project, <a href="http://www.EditThisPage.net">EditThisPage</a>, and of the SynchroEdit alpha at <a href="http://www.web2point1.org/">Web 2.1 BrainJam</a> last week; there are two videos available from Enric Teller's vBlog: <a href="http://www.cirne.com/vlog/2005/10/10/web-21-a-brainjam-christopher-allen-presentation/">Presentation</a> and <a href="http://www.cirne.com/vlog/2005/10/10/web-21-a-brainjam-christopher-allen-qa/">Q&amp;A</a>.&nbsp; </p>
<p>If you are interested in learning more, visit the <a href="http://www.synchroedit.com">SynchroEdit website</a>. We have additional information on the program, a <a href="http://wiki.synchroedit.com">developers wiki</a>, as well as a sandbox that you can play in to demonstrate SynchroEdit in use.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
I'm curious about what ways you think this could be useful as a teaching aid? Have you looked into particular implementations or studied existing case studies?
(I have studied this a fair amount and I don't think there are existing case studies, especially in the classroom, which is why I ask.. I'm looking at ways in which chatrooms could be incorporated into classroom environments as a backchannel)
</p>
<a class="u-author h-card" href="#">yardi</a>
<time class="dt-published" datetime="2005-11-16T11:00:54-07:00">2005-11-16T11:00:54-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2005/10/for_the_last_se.html" rel="syndication" class="u-syndication" >original layout</a></p>
