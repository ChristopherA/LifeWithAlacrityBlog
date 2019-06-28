---
title: "Ratings: Who Do You Trust?"
slug: "ratings_who_do_"
url: "/2006/09/ratings_who_do_.html"
image: "/previous/photos/uncategorized/shannon_appelcline.jpg"
tags:
  - "Games"
  - "Social Software"
  - "User Interface"
  - "Web/Tech"
  - "Weblogs"
  - "rating"
  - "ratings"
  - "collective choice"
  - "reliability"
  - "weight"
  - "weighing"
  - "trust"
  - "volume"
  - "depth"
  - "user content"
  - "rpgnet"
  - "inedex"
  - "creativity"
  - "skotos"
  - "shannon appelcline"
date: "2006-09-14T16:28:58-07:00"
---
<p>My colleague, <a href="http://www.skotos.net/about/staff/shannon_appelcline.php">Shannon Appelcline</a>, has been working on a game rating system for <a href="http://www.rpg.net">RPGnet</a>. This has resulted in real-world application of the principles for designing rating systems which we've previously discussed in our <a href="/2005/12/collective_choi.html">Collective Choice</a> articles. Shannon's newest article, <a href="http://www.skotos.net/articles/TTnT_/TTnT_196.phtml">Ratings,
Who Do You Trust?</a> offers a look at weighting ratings based on reliability.</p>
<p><img border="0" src="/previous/photos/uncategorized/shannon_appelcline.jpg" title="Shannon_appelcline" alt="Shannon_appelcline" style="margin: 0px 0px 5px 5px; float: right;" /></p><blockquote><p><em>On the <a href="http://index.rpg.net/">RPGnet Gaming Index</a> we've put this all together to form a tree of weighted ratings that answer the question, <em>who do you trust</em>?</em></p>
<p><em>Here's how we measured each type of trust, and what we did about it:</em></p>
<ul><li><p><em><strong>Volume of Ratings for an Item.</strong> Introduce a bayesian weight to offset the variability of items with low-volume ratings.</em></p></li>
<li><p><em><strong>Volume of Ratings by a User.</strong> Give each user a weight based on his volume of contribution which is applied to his ratings.</em></p>
</li>
<li><p><em><strong>Depth of Content by a User.</strong> Give each rating a weight based on the depth of thought implicit in the rating which is applied to that rating.</em></p>
</li></ul>
<p><em>These all get put together to create our final ratings for
the Gaming Index, with each user's individual rating for an item
getting multiplied by its user weight and its content weight, and then
all of that averaged with the other user ratings and the bayesian
weight too. The result is in no way intuitive, but users don't really
need to understand the back end of a rating system. Conversely we hope
it's accurate, or at least more accurate than would otherwise be true
given the relatively low volume of ratings we've collected thus far.</em></p>
</blockquote>
<p>Here are some of Shannon's earlier discussions about the design behind the new &quot;user content&quot; based <a href="http://index.rpg.net">RPGnet Gaming Index</a>:</p>
<ul>
<li><a href="http://www.skotos.net/articles/TTnT_/TTnT_191.phtml">Encouraging
User Creativity</a> - A look at the &quot;XP&quot; system which has helped to incentivize the creation of the database at the heart of the ratings.
</li>
<li><a href="http://www.skotos.net/articles/TTnT_/TTnT_193.phtml">Managing User Creativity, Part Two</a> - An examination of the nuts and bolts of RPGnet's Gaming Index database.
</li></ul>
<hr />
<p><em>Related articles from this blog:</em></p>
<blockquote>
<li><em><a href="/2005/12/systems_for_col.html">2005-12: Systems for Collective Choice</a></em></li>
<li><em><a href="/2005/12/collective_choi.html">2005-12: Collective Choice: Rating Systems</a></em></li>
<li><em><a href="/2006/01/ranking_systems.html">2006-01: Collective Choice: Competitive Ranking Systems</a></em></li>
<li><em><a href="/2006/08/using_5star_rat.html">2006-08: Using 5-Star Rating Systems</a></em></li>
<li><em><a href="/2007/01/collective_choi.html">2007-01: Experimenting with Ratings</a></em></li>
</blockquote>
<p>Related articles from Shannon Appelcline's <a href="http://www.skotos.net/articles/show-column.phtml?colname=TTnT_">Trials, Triumphs &amp; Trivialities:</a>
</p><blockquote><li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_196.phtml">#196: Collective Choice: Ratings, Who Do You Trust?</a></em>
</li>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_198.phtml">#198: Collective Choice: More Thoughts About Ratings</a></em></li>
</blockquote>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
Hmm, interesting on the weighting system.
Can you explain with more detail how the rating by depth of content is generated?
I'm looking through the other articles, so hopefully I find the info there.
Frank
</p>
<a class="u-author h-card" href="#">magicback (Frank)</a>
<time class="dt-published" datetime="2006-10-12T01:30:32-07:00">2006-10-12T01:30:32-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
My first pass system just used a different multiplier for weight based on the type of content:
1x for just a raw rating
2x for a rating with a non-blank comment
5x for a review (which goes through a different, approved content system)
My second pass system also included "volume of ratings by user" and thus applied a variable multiplier depending on how many ratings the user has made:
(0-2x) for a raw rating
2x(0-2x) for a rating with comment
5x for a review
The 0-2x is calculated as (# of ratings by user)/50, to 2 max.
I'm pretty sure that the core weighting system by depth is producing better results, though I haven't done any studies of that yet. The additional weighting for volume by users has definitely prevented bias by hit-and-run raters who just stop by to rate one game that they've been asked to.
</p>
<a class="u-author h-card" href="#">Shannon Appelcline</a>
<time class="dt-published" datetime="2006-10-16T15:39:53-07:00">2006-10-16T15:39:53-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2006/09/ratings_who_do_.html" rel="syndication" class="u-syndication" >original layout</a></p>
