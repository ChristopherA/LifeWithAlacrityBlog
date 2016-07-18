---
title: "Getting Ready for the iPhone"
slug: "getting_ready_f"
url: "/2007/06/getting_ready_f.html"
tags:
  - "iPhone"
  - "Social Software"
  - "User Interface"
  - "Web/Tech"
  - "iphone"
  - "wwdc"
  - "web2.0"
  - "ajax"
  - "synchroedit"
  - "safari"
  - "webkit"
  - "subethaedit"
  - "firefox"
  - "readystate"
  - "xmlhttprequest"
  - "iPhoneWebDev"
date: "2007-06-15T20:06:45-07:00"
---
<p><a href="http://www.apple.com/iphone/ads/ad4/"><img border="0" alt="Watereddown" title="Watereddown" src="http://lifewithalacrity.blogs.com/photos/uncategorized/2007/06/15/watereddown.jpg" style="margin: 0px 0px 5px 5px; float: right;" /></a>
I've been excited about the web capabilities of the upcoming <a href="http://www.apple.com/iphone/">iPhone</a> for some time. As a reluctant laptop user (&quot;oh, my aching shoulders&quot;), there is real appeal to me in a better portable web browser. I have tried most of the PDA and cellphone browsers to date, and none offer more then a poor cousin to the web that we experience on the desktop.</p>
<p>Instead, the iPhone offers a desktop-class browser. There is no transcoding, nor any subset of HTML such as <a href="http://en.wikipedia.org/wiki/Wireless_Markup_Language">WML</a>. Full web pages are rendered in the small display, and when you &quot;double-tap&quot; with your finger the section you touch is expanded to a more readable size. The <a href="http://www.apple.com/iphone/ads/ad4/">video</a> available at the Apple website shows this capability in use.</p>
<p>Because of the iPhone's upcoming July 29th release, I decided to participate in this week's <a href="http://developer.apple.com/wwdc/">Apple WWDC</a> conference for Macintosh developers. There a number of announcements about the iPhone were released, and a number of technical sessions on the iPhone and iPhone-related technologies were held. Together the iPhone demonstrations at the public keynote and other demonstrations throughout the WWDC offered some real promise for when the phone is released on June 29th.</p>
<p><a onclick="window.open(this.href, '_blank', 'width=440,height=292,scrollbars=no,resizable=no,toolbar=no,directories=no,location=no,menubar=no,status=no,left=0,top=0'); return false" href="http://lifewithalacrity.blogs.com/.shared/image.html?/photos/uncategorized/2007/06/15/iphonesteve.jpg"><img width="200" height="132" border="0" src="/previous/images/2007/06/15/iphonesteve.jpg" title="Iphonesteve" alt="Iphonesteve" style="margin: 0px 5px 5px 0px; float: left;" /></a>
The biggest announcement at the public <a href="http://events.apple.com.edgesuite.net/d7625zs/event/">keynote</a> was that there will not be an SDK for building native iPhone apps; instead, the only way for third parties to get involved is to create web applications optimized for the iPhone. This came as a big disappointment to the majority of developers participating at WWDC. However, as someone who has been involved lately in creating AJAX/Web 2.0 apps, I was less unhappy.</p>
<p>The other significant announcement at the keynote was that a <a href="http://www.apple.com/safari/download/">Safari 3.0 beta</a> for both Mac and Windows was being released and that a third Safari platform would be released on July 29th—inside the iPhone. This means that web 2.0 applications created to work with Safari on the Mac will likely also work on the iPhone.</p>
<p><a href="http://www.synchroedit.com"><img border="0" alt="SynchroEdit" title="SynchroEdit" src="http://www.synchroedit.com/img/selogo-nobox-green.png" style="margin: 0px 0px 5px 5px; float: right;" /></a>Since <a href="http://www.synchroedit.com">SynchroEdit</a>, an open-source simultaneous web editor (in the style of <a href="http://www.codingmonkeys.de/subethaedit/">SubEthaEdit</a>) for Firefox that I produced last year, is one of the most sophisticated AJAX/Web 2.0 applications, I dug deeper at various WWDC sessions to see if it might be possible to make SynchroEdit work on the iPhone.</p>
<p>One of the biggest things that SynchroEdit needs in order to function is <a href="http://www.w3.org/TR/DOM-Level-2-Events/events.html#Events-eventgroupings-mutationevents">DOM Mutation Events</a>. At a party for <a href="http://www.webkit.org">WebKit</a> (the open source code underpinnings of Safari's web renderer) and in questions after a session at WWDC it was confirmed that these are available to Safari 3.0 and presumably the iPhone.</p>
<p>The other key ability that SynchroEdit requires is WYSIWYG editing. This was terribly broken in Safari 2.0, but I saw many demonstrations of it working in Safari 3.0, so I don't anticipate any problems with this.</p>
<p>SynchroEdit also requires AJAX and in particular the <a href="http://www.w3.org/TR/XMLHttpRequest/">XMLHttpRequest</a> function, and the keynote clearly said that this was available.</p>
<p>The final thing that SynchroEdit needs is the ability to keep the browser at <em>readystate==3</em>, i.e. not &quot;finish&quot; sending the page, so that we can continue to interactively pass updates to users as they arrive, without creating a new connection for every message. It is not clear if this will be supported on the iPhone, but there are ways to work around it.</p>
<p>So, in principle, it appears that we should be able to make SynchoEdit work on the iPhone. I am not sure that many iPhone users need SynchroEdit, but as an example of a very sophisticated web technology that should work on that platform, it shows the potential for what might be possible.</p>
<p>Because of this technological capability I've decided to begin investigating what type of social software apps could be highly useful on the iPhone and that aren't being served by the existing web 2.0 community. I am also going to continue investigating the technical issues of developing web apps for the iPhone</p>
<p>If you are interested as well, I invite you to participate in the new <a href="http://www.iPhoneWebDev.com/">iPhoneWebDev</a> community. It should be a great resource for everyone interested in getting in on the ground floor with this new web technology. I have also begun tagging relevant web pages in <a href="http://del.icio.us/ChristopherA">del.icio.us</a> with the tag <a href="http://del.icio.us/tag/iphonewebdev">iphonewebdev</a>—I hope that others will begin to use this tag as well.</p>
<p>I have quite a bit more I'd like to write about specific iPhone technology, but unfortunately I have to wait until the <a href="http://developer.apple.com/wwdc/attendee/">WWDC confidentiality</a> expires on June 29th with the release of the iPhone, so keep an eye out here for more details.</p>
<p class="previous"><a href="/previous/2007/06/getting_ready_f.html" rel="syndication">orginal layout</a></p>
