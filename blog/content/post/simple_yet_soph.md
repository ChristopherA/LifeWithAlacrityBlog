---
title: "Simple Yet Sophisticated Group Page Editing"
slug: "simple_yet_soph"
url: "/2004/05/simple_yet_soph.html"
image: "http://editthispagephp.sourceforge.net/home/index-images/tn_editpage.png"
tags:
  - "Social Software"
  - "User Interface"
  - "Web/Tech"
  - "edit this page"
  - "php"
  - "collaboration"
  - "group"
  - "social software"
  - "editing"
  - "html"
  - "page"
date: "2004-05-13T14:58:39-07:00"
---
<p>I have been leading the design of a new Open Source collaboration tool called <a href="http://editthispagephp.sourceforge.net/home/index.php">EditThisPagePHP<a>, which started <a href="/2003/12/editthispagephp.html">six months ago</a> and now is in beta.</p>
<p>My goal with EditThisPagePHP attempt to come close to <a href="http://www.scripting.com/">Dave Winer's</a> <a href="http://davenet.scripting.com/discuss/msgReader$641?mode=topic">visionary statement</a> back in May of 1999:</p>
<blockquote><i>When I'm writing for the web, and I'm browsing my own site, every bit of text that I create has a button that says Edit This Page when I view it. When I click the button, a new page opens with the text in an HTML textarea. I edit. Click on Submit. The original page displays with the change. Three easy steps. The essential element is that *every* bit of text has this button. There can be no exceptions.</i></blockquote>
<p>At the fundamental level, EditThisPagePHP basically just let you remotely edit a single page. There are many situations where existing Wiki or Blog software is too complicated, or imposes too much structure. EditThisPagePHP lets you have total control over the HTML -- you can use sophisticated CSS layouts, or very simple HTML -- the software does not get in the way.</p>
<p>Yet in spite of this simplicity, EditThisPagePHP also uses ideas drawn from various Wiki, Blog, and CMS (content management system) technologies. Like Wikis, it supports an edit-this-page button, page history, page diffs, and can email users when pages change. Like Blogs, it supports optional user comments, trackbacks (both send and receive), and delivers two RSS feeds -- one for the current version of the page, and one with diffs. Like a CMS, it supports multiple roles, by default a reader, an editor, and a super-editor -- each with different privileges.</p>
<p>I personally plan to use it for standards documents, lists, game rules, and home pages for various groups I collaborate with. I expect that others will use it anytime a group of people want to maintain a publicly accessible page together.</p>
<p>Some screenshots:</p>
<p><a href="http://editthispagephp.sourceforge.net/home/index-images/editpage.png" title="Edit Page"><img src="http://editthispagephp.sourceforge.net/home/index-images/tn_editpage.png" border="0" width="150" height="128" alt="Edit Page" /></a><a href="http://editthispagephp.sourceforge.net/home/index-images/history.png" title="View History"><img src="http://editthispagephp.sourceforge.net/home/index-images/tn_history.png" border="0" width="150" height="128" alt="View History" /></a><a href="http://editthispagephp.sourceforge.net/home/index-images/diffs.png" title="Page Diffs"><img src="http://editthispagephp.sourceforge.net/home/index-images/tn_diffs.png" border="0" width="150" height="128" alt="Page Diffs" /></a><a href="http://editthispagephp.sourceforge.net/home/index-images/trackbacks_comments.png" title="Trackbacks and Comments"><img src="http://editthispagephp.sourceforge.net/home/index-images/tn_trackbacks_comments.png" border="0" width="150" height="128" alt="Trackbacks and Comments" /></a><a href="http://editthispagephp.sourceforge.net/home/index-images/auth_msg.png" title="Edit Authorization Message"><img src="http://editthispagephp.sourceforge.net/home/index-images/tn_auth_msg.png" border="0" width="150" height="128" alt="Edit Authorization Message" /></a></p>
<p><b>Technical Details:</b> EditThisPagePHP is written solely in PHP, and it currently works with PHP 4 and 5, and does not require SQL. Every revision makes a backup of itself, so no data can be lost. PHP is not allowed in the HTML text itself, to minimize security risks. Only two files are required: the core PHP script (editthispage.php) and a data file for your page. The core file can support as many pages as desired. The current version is <a href="http://prdownloads.sourceforge.net/editthispagephp/editthispage-0.5b2.zip?download">0.5b2</a>, is licensed under a BSD-style license, and there is a <a href="http://editthispagephp.sourceforge.net/demo_05b2/index.php">working sandbox demo</a> available to play with.</p>
<p>Future goals are to support more technical features, without losing the elegance and simplicity of the implementation. This may include limited Wiki TextFormatting or a simple WYSIWYG editor, HTML-tidy, some user-interface enhancements, etc. A complete list is available on our <a href="http://editthispagephp.sourceforge.net/home/wishlist.php">wishlist</a> page.</p>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">I'm amused at the talk of prior art and 1999 visions, the very first web client (1990) had EditThisPage built in - the browser was the editor. The same approach is still taken by browsers like Amaya.
http://www.w3.org/People/Berners-Lee/WorldWideWeb.html
</p>
<a class="u-author h-card" href="http://dannyayers.com">Danny</a>
<time class="dt-published" datetime="2004-06-02T05:23:56-07:00">2004-06-02T05:23:56-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
I'm amused at the talk of prior art and 1999 visions, the very first web client (1990) had EditThisPage built in - the browser was the editor. The same approach is still taken by browsers like Amaya.
</p>
<a class="u-author h-card" href="#">alex</a>
<time class="dt-published" datetime="2005-12-06T10:59:45-07:00">2005-12-06T10:59:45-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2004/05/simple_yet_soph.html" rel="syndication nofollow" class="u-syndication" >original layout</a></p>
