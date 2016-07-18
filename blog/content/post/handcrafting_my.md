---
title: "Hand-Crafting My FOAF"
slug: "handcrafting_my"
url: "/2004/02/handcrafting_my.html"
tags:
  - "Social Software"
  - "Web/Tech"
  - "Weblogs"
  - "FOAF"
  - "friend of a friend"
  - "social networking"
  - "RDF"
  - "social software"
  - "friend"
  - "RDF validation"
  - "validator"
date: "2004-02-19T16:25:05-07:00"
---
<p>While at <a href="http://etech.weblogsinc.com/">eTech</a>, I attended a number of "social software" sessions. One thing I heard was a persistent call from folk like <a href="http://blogs.it/0100198/">Marc Canter</a> for all the vendors to support something called <a href="http://xmlns.com/foaf/0.1/">FOAF</a>. FOAF is a standard for "Friend of a Friend" files, and is an attempt to make <em>machine readable</em> information about people, groups, companies, and other online resources. In particular, it is focused on representing the information that you might typically put on your personal home page in a form such that meta-data tools can interpret it.</p>
<p>If you are using the blog service <a href="http://www.typepad.com">TypePad</a> or the social networking service <a href="http://www.ecademy.com">Ecademy</a> you may already have a FOAF file without knowing it, and <a href="http://www.tribe.net">Tribe.Net</a> announced at eTech that they were promising to support it as well for their social networking service.</p>
<p>FOAF as a standard is still in a fairly primitive state -- to me it feels like HTML did during the days of the early Mosaic browser, when every good web page had to be hand-crafted in a text editor and uploaded to a server. However, like HTML, it may have great promise.</p>
<p>The first thing that FOAF may offer us is a way to exchange information between various social networking services. For instance, I just exported all my <a href="http://www.orkut.com">Orkut</a> friends into my own FOAF file by hand, but there are those who are working on tools to do this automatically, and once Tribe offers FOAF, services like Orkut may be forced to do the same.</p>
<p>Probably more important in the long run is that FOAF may decentralize the data that you make public about yourself -- to put the data under your own control. Owned by you rather then owned by the services you use. For instance, many people have <a href="http://www.theregister.co.uk/content/6/35375.html">complained about Orkut's ownership of information</a>.</p>
<p>The biggest problem with FOAF right now is that it doesn't support very much "progressive disclosure" or privacy. Progressive disclosure is how people typically handle private information -- they disclose information about themselves a bit at a time, and as trust builds, offer more. The only small measure of privacy that FOAF has is that it has a way to obscure email addresses so that they can't easily be harvested by spammers. But all your other information is totally public. Theoretically you can <a href="http://usefulinc.com/foaf/encryptingFoafFiles">encrypt your FOAF</a> file, but this method requires external PGP-based encrypted files. There is also the possibility of <a href="http://www.w3.org/Signature/">XML-DSIG</a>, however, I find this standard to also be extremely cumbersome right now. <a href="http://www.plaxo.com">Plaxo</a> is a major social networking service that has some excellent <a href="http://blog.plaxo.com/archives/000007.html">comments on FOAF privacy</a> and other issues.</p>
<p>What I want is something that allows people to make 'local' assertions about themselves and their friends, and be able to have those friends be able to 'discover' more information by using those assertions. Ron Rivest came out with an interesting method for this in an old project called <a href="http://theory.lcs.mit.edu/~rivest/sdsi10.html">SDSI - A Simple Distributed Security Infrastructure</a> that I hope will inspire a few FOAF architects someday. To adopt his method for FOAF requires everyone to have a FOAF service script somewhere and not just a data file. But we've seen broad adoption of personal RSS and Trackback services, so I don't think this is a huge obstacle to overcome.</p>
<p>In the meantime, if you want to play around with FOAF take over control of your own public data, I've included detailed information on how to get started in hand-crafting your own FOAF file.</p>
<h4>Hand-Crafting your own FOAF</h4>
<p>First, start with <a href="http://www.ldodds.com/foaf/foaf-a-matic.html">FOAF-a-Matic</a>. This is a web form page that will create a very simple starting FOAF file for you. Don't put any information in it that you don't want to be public, and skip the section on "people you know". When it asks for your email address, make sure to enter it in all lower-case. When completed, it will look something like this:</p>
<blockquote><pre>&lt;rdf:RDF
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
xmlns:foaf="http://xmlns.com/foaf/0.1/">
&lt;foaf:Person>
&lt;foaf:name>Christopher Allen&lt;/foaf:name>
&lt;foaf:title>Mr&lt;/foaf:title>
&lt;foaf:firstName>Christopher&lt;/foaf:firstName>
&lt;foaf:surname>Allen&lt;/foaf:surname>
&lt;foaf:nick>Chris&lt;/foaf:nick>
&lt;foaf:mbox_sha1sum>9ee1c03552f22e89592ce583be0ab8db0c4f2c59&lt;/foaf:mbox_sha1sum>
&lt;foaf:homepage rdf:resource="http://www.alacrityventures.com/allen.html"/>
&lt;foaf:depiction
rdf:resource="http://web.lifewithalacrity.com/christophera/images/ChristopherAllen(100x100).gif"/>
&lt;foaf:workplaceHomepage rdf:resource="http://www.alacrityventures.com"/>
&lt;foaf:workInfoHomepage rdf:resource="http://www.alacrityventures.com/allen.html"/>
&lt;/foaf:Person>
&lt;/rdf:RDF></pre></blockquote>
<p>The next thing is to add pointers to any other FOAF files that you might have on other services, for instance, I have a profile on Marc Canter's <a href="http://peopleaggregator.com/">People Aggregator</a> service. You should also list the place where you plan on making your FOAF file available -- you might think that this is a circular reference, but it is OK. My convention is to put the most "authoritative" FOAF file last, so that if there is a conflict the last one might override earlier ones. However, in practice I've not found that any FOAF tool I've used supports this convention. Put these right above the closing <code>&lt;/foaf:Person><code> tag.</p>
<blockquote><pre>  &lt;rdfs:seeAlso rdf:resource="http://peopleaggregator.com/profile?id=102" />
&lt;rdfs:seeAlso rdf:resource="http://www.ecademy.com/module.php?mod=network&amp;amp;op=foafrdf&amp;amp;uid=42230" />
&lt;rdfs:seeAlso rdf:resource="http://web.lifewithalacrity.com/christophera/foaf.rdf" />
</pre></blockquote>
<p>Now upload your file to your own web site, and then run your FOAF file through two different validators, the first being the <a href="http://www.w3.org/RDF/Validator/">W3C RDF Validation Service</a>. It will tell you if you've made any mistakes with the RDF aspect of the file. Then use <a href="http://sw1.ilrt.org/discovery/2003/08/validation/">Rosco</a> which will also look at your schema and make recommendations as to missing items. Unfortunately, neither validator is very good at telling you what the problem is if it finds one -- again, it is like the old hand-coding HTML days when you are debugging your web pages.</p>
<p>Once you've got your basic FOAF file working, now to enter your friends. First, add to your <code>foaf:Person</code> the following:</p>
<blockquote><pre>&lt;foaf:knows rdf:nodeID="MarcCanter"/>
</pre></blockquote>
<p>This is a pointer that says "look in this document for a person with the <code>rdf:nodeID</code> of MarcCanter". You can invent any value you want for this ID, mcanter, mark, canter, etc., however, it must be a unique ID on this page.</p>
<p>Then fill out the following template for each person, putting below your own <code>foaf:Person</code> but above the closing <code>rdf:RDF</code> tag:</p>
<blockquote><pre>&lt;foaf:Person rdf:nodeID="">
&lt;foaf:name>&lt;/foaf:name>
&lt;foaf:firstname>&lt;/foaf:name>
&lt;foaf:surname>&lt;/foaf:name>
&lt;foaf:nick>&lt;/foaf:nick>
&lt;foaf:mbox_sha1sum>&lt;/foaf:mbox_sha1sum>
&lt;rdfs:seeAlso rdf:resource="" />
&lt;/foaf:Person>
</pre></blockquote>
<p>So for instance with Marc Canter:</p>
<blockquote><pre>&lt;foaf:Person rdf:nodeID="MarcCanter">
&lt;foaf:name>Marc Canter&lt;/foaf:name>
&lt;foaf:mbox_sha1sum>41e872618d70ba18a7af715083f522afe7fc3238&lt;/foaf:mbox_sha1sum>
&lt;rdfs:seeAlso rdf:resource="http://peopleaggregator.com/profile?id=4" />
&lt;/foaf:Person>
</pre></blockquote>
<p>Now <code>foaf:firstname</code>, <code>foaf:surname</code>, and <code>foaf:nick</code> are not absolutely essential -- you can remove them if they are not needed. I tend to only use them when there might be some confusion, for instance, for "Arthur De Boies" has "De Boise" is a surname, and "Lori Ann Miller" has "Lori Ann" as a firstname. <code>foaf:nick</code> is useful in situatations where there is a dimunitive involved, for instance "Christopher Allen" has "Chris" as a nick, and <code>foaf:nick</code> is also used by some programs online personas or for IRC chat, such as "ChristopherA".</p>
<p>Now where did the <code>foaf:mbox_sha1sum</code> come from? The purpose of this number is to obscure the email address so that it can't be harvested by spammers, yet is unique enough that it can FOAF-based applications can find people. To convert an email address to a <code>foaf:mbox_sha1sum</code> you can use <a href="http://xml.mfd-consult.dk/foaf/">sha1ify</a>. Just enter the email address that you want converted in all lower case, and copy the string it generates to the <code>foaf:mbox_sha1sum</code>.</p>
<p>Finally, you can search and see if any existing FOAF profiles exist for your friend at <a href="http://eikeon.com/foaf/">FOAF: Web View</a>, using their email address. If the friend does have a FOAF file, add it to <code>rdfs:seeAlso</code> tag.</p>
<p>When you are done, test your FOAF file with the two validators, and if it works. One common problem that the validators will fail to give you a good error message about is if any of the URLs you use contain any improper characters like &amp; - in particular, Ecademy's FOAF files use this character. Just substitute &amp;amp; for every occurrence of &amp; and it should work fine. Another problem is if any of your friends have international characters in their names, for instance "Sébastien". To avoid this problem, put the following at the top of your FOAF file above your <code>rdf:RDF</code> tag.</p>
<blockquote><pre>&lt;?xml version="1.0" encoding="iso-8859-1"?>
</pre></blockquote>
<p>Once everything is working you can submit it to services like <a href="http://eikeon.com/foaf/">FOAF: Web View</a>. You can also browse your FOAF file directly by using <a href="http://xml.mfd-consult.dk/foaf/explorer/">FOAF Explorer</a>, or import it into services like <a href="http://peopleaggregator.com">People Aggregator</a>.</p>
<p>Once your FOAF file is working and submitted, you'll want to add an "auto-discovery" meta-tag to your blog or home page. This is placed in the <code>head</code> portion of your HTML code:</p>
<blockquote><pre>&lt;link rel="meta" type="application/rdf+xml"
title="FOAF" href="http://web.lifewithalacrity.com/christophera/foaf.rdf"/>
</pre></blockquote>
<p>If you are using TypePad, it forces you to use their FOAF file for you unless you used an Advanced Template. With an Advanced Template you can remove the following tags and replace it with the above:</p>
<blockquote><pre>&lt;MTUserIfShow field="foaf">
&lt;link rel="meta" type="application/rdf+xml" title="FOAF" href="&lt;$MTUserSiteURL$>foaf.rdf" />
&lt;/MTUserIfShow>
</pre></blockquote>
<p>From this point on it is just a matter of looking at other people's FOAF files and seeing if you want to add any of the other profile properties that they use. I'm trying to keep a well documented foaf at <a href="http://web.lifewithalacrity.com/christophera/foaf.rdf">http://web.lifewithalacrity.com/christophera/foaf.rdf</a>, and I also recommend looking at Morten Frederiksen's FOAF at <a href="http://xml.mfd-consult.dk/foaf/morten.rdf">http://xml.mfd-consult.dk/foaf/morten.rdf</a> which supports far more profile information then my FOAF does.</p>
<p>Also useful is the IRC chat channel at irc.freenode.net #foaf -- I got a lot of useful tips and advice there.</p>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">Please add some notes about how to say that "This foaf file is about this person". See these for detail about PPD, topic, maker, made.
Discussion rdfweb.org/pipermail/rd...-dev/2004-February/thread.html
The post that kicked it off rdfweb.org/pipermail/rd...-dev/2004-February/012546.html
An example www.ecademy.com/module.php
</p>
<a class="u-author h-card" href="http://www.ecademy.com">Julian Bond</a>
<time class="dt-published" datetime="2004-02-22T01:07:49-07:00">2004-02-22T01:07:49-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">On the encryption issue: FOAFbot supports encrypted FOAF files (per the link), and I've just set up a service for hosting these types of files, so you don't have to encrypt them yourself: <a href="http://foaf.dk/hosting/">http://foaf.dk/hosting/</a>
Of course, that means you have to trust me...
On the ordering of seeAlso: RDF/XML doesn't have a sense of order (unless you use rdf:Seq, as in RSS). In short, you're simply making statements of fact (hopefully!), statements that could stand on their own. There's no default or primary.
</p>
<a class="u-author h-card" href="http://purl.org/net/morten/">Morten Frederiksen</a>
<time class="dt-published" datetime="2004-02-25T10:20:15-07:00">2004-02-25T10:20:15-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
And as with the old html days - there will be end user tools created. My take on an foaf-generation tool for non-technical users is at zopto.com
</p>
<a class="u-author h-card" href="#">Ben Nolan</a>
<time class="dt-published" datetime="2004-03-16T04:19:37-07:00">2004-03-16T04:19:37-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">Blogharbor.com also has a FOAF file.  I didn't know it was its own protocol.  My FOAF is through Blogware.
</p>
<a class="u-author h-card" href="http://elamb.blogharbor.com">elamb</a>
<time class="dt-published" datetime="2005-04-24T10:10:12-07:00">2005-04-24T10:10:12-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2004/02/handcrafting_my.html" rel="syndication">orginal layout</a></p>
