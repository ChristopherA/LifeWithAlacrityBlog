---
title: "Collective Choice: Rating Systems"
slug: "collective_choi"
url: "/2005/12/collective_choi.html"
tags:
  - "Social Software"
  - "User Interface"
  - "Web/Tech"
  - "collective choice"
  - "comparison systems"
  - "rating systems"
  - "bayesian"
  - "ebay"
  - "user-contributed content"
  - "feedback"
  - "granular ratings"
  - "rating scale"
  - "specific ratings"
  - "statistical ratings"
  - "rating weight"
  - "rpgnet"
  - "board game geek"
  - "wow web designs"
  - "altruistic punishment"
  - "editorial fiat"
  - "bilateralism"
  - "retaliation"
  - "usefulness"
  - "meta-ratings"
date: "2005-12-12T17:58:34-07:00"
---
<p><span style="font-size: 0.7em;">by Christopher Allen &amp; Shannon Appelcline</span></p>
<p><em>[This is the second of a series of articles on <a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html">collective choice</a>, co-written by my collegue <a href="http://www.skotos.net/about/staff/shannon_appelcline">Shannon Appelcline</a>. It will be <a href="http://www.skotos.net/articles/TTnT_179.phtml">jointly posted</a> in Shannon's <a href="http://www.skotos.net/articles/TTnT.shtml">Trials, Triumphs &amp; Trivialities</a> online games column at <a href="http://www.skotos.net/">Skotos</a>.]</em></p>
<p>In our previous article we talked about the many systems available for <a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html">collective choice</a>. There are <a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html#selection_systems">selection systems</a>, which are primarily centered on voting and deliberation, <a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html#opinion_systems">opinion systems</a>, which represent how voting could occur, and finally <a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html#comparison_systems">comparison systems</a>, which rank or rate different people or things in a simple, comparative manner.</p>
<p><a href="http://lifewithalacrity.blogs.com/.shared/image.html?/photos/uncategorized/stars_1.gif" onclick="window.open(this.href, '_blank', 'width=373,height=239,scrollbars=no,resizable=no,toolbar=no,directories=no,location=no,menubar=no,status=no,left=0,top=0'); return false"><img width="200" height="128" border="0" alt="Stars_1" title="Stars_1" src="http://www.lifewithalacrity.com/images/stars_1.gif" style="margin: 0px 0px 5px 5px; float: right;" /></a>One purpose of our previous article was to create a dictionary of terms for talking about these related, but clearly different, systems. Another was to start offering analyses of these systems, many of which had not been well studied before their introduction onto the Internet. </p>
<p>However at best our previous article provided an overview of what should be further investigated in each system. This article provides more in-depth coverage of one of the systems we previously outlined: <a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html#rating_systems">rating systems</a>.</p>
<p>As we wrote in our previous article, in comparison rating systems <em>&quot;the value of individual items (most frequently goods) rise or fall based upon the largely subjective judgment of individual users.&quot;</em> Ratings systems should be clearly differentiated from the closely related <a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html#ranking_systems">ranking systems</a>. Ratings systems have a more subjective component, while ranking systems are largely objective. Amazon, Netflix, BoardGameGeek, and even the Stock Market were offered up as examples of ratings systems. Another example of a comparison rating system, and one of the earliest that appeared on the modern Internet, is eBay. The techniques they use are now beginning to show their age.</p>
<p>&nbsp;</p>
<h3>eBay: A Failed Rating Experiment</h3>
<p><img border="0" alt="Ebaysales" title="Ebaysales" src="http://lifewithalacrity.blogs.com/photos/uncategorized/ebaysales.jpg" style="margin: 0px 5px 5px 0px; float: left;" />Most rating systems center around rating content, often user-contributed content, and they frequently help apply community values and acclaim to that content. However, the idea of ratings can go far beyond that narrow niche (though that will doubtless be its greatest use as the Internet continues to expand). Early Internet site, <a href="http://www.ebay.com">eBay</a>, was one of the first to widely use user-submitted ratings, and it used them for a different manner: to determine the good traders on their auction site.</p>
<p>Unfortunately, as one of the first in this field, eBay made many mistakes which now leave their ratings system only slightly helpful. However, its failures can also provide us with insights in creating new rating systems on the Internet.</p>
<p>eBay allows you to leave positive, negative, or (more recently) neutral feedback for each transaction you conduct in their society. These are aggregated into two numbers. &quot;Feedback Score&quot; is calculated as unique positive feedback received minus unique negative feedback received, and results in a whole number like &quot;32&quot; or &quot;10,302&quot;. &quot;Positive Feedback&quot; is calculated as positive feedback received divided by all feedback received, and results in a percentage like &quot;100%&quot; or &quot;99.8%&quot;.</p>
<p>Unfortunately, for reasons discussed below, almost all feedback is positive, and thus the Feedback Score acts almost entirely as a track record of how many trades someone has made. The Feedback Score could be largely replaced by that single number. You can look at a score of &quot;27&quot;, and say, &quot;That's an amateur trader, or someone just getting started&quot;, at a score of &quot;3&quot;, and say, &quot;That person may or may not know what they're doing&quot;, at a score of &quot;10,302&quot;, and say, &quot;That person has done a lot of trades.&quot; But you still don't know how good the trader is.</p>
<p><a href="http://lifewithalacrity.blogs.com/photos/uncategorized/ebayprofile.jpg"><img border="0" src="http://lifewithalacrity.blogs.com/photos/uncategorized/ebayprofile.jpg" title="Ebayprofile" alt="Ebayprofile" class="image-full" style="margin: 0px 0px 5px 5px; float: right;" /></a>Theoretically, the Positive Feedback percentage should give a more meaningful number, but people so infrequently give bad ratings that, even when they do appear, they look like noise. Does a percentage of &quot;99.8%&quot; on a user with a score of &quot;1,762&quot; mean that the seller has a genuine problem or not? Do those 3 unhappy customers really represent another 30 who were unwilling to actually click the negative feedback? And, did those people have slightly bad experience or really bad experiences? It's pretty hard to say.</p>
<p>Overall, eBay has a few major problems with their rating system:</p>
<ul>
<li><p>It's <strong>non-granular</strong>, with only two options (positive/negative), or more recently three (positive/negative/neutral).</p></li>
<li><p>It's <strong>non-distinct</strong>, with no useful guidelines on what behaviors should result in each rating.</p></li>
<li><p>It's <strong>non-statistical</strong>, and thus ends up showing only a gross number of sales, not a real subjective measure.</p></li>
<li><p>It's <strong>bilateral</strong>, with buyers and sellers rating each other simultaneously, and thus people are afraid to give bad ratings lest they get them in return.</p></li>
<li><p>It's <strong>meaningless</strong>, because there are no good tools to control who bids on an auction based on Feedback numbers. (Technically it may be legitimate to ban low feedback bidders from an auction, then cancel their bids if they enter the auction, but this is neither obvious, automatic, nor simple.)
</p></li></ul>
<p>We're going to address each of these issues in turn, to offer insight into creating new comparison rating systems. The first three topics--granularity, distinction, and a statistical basis--are the most important elements of a good comparison rating system. Bilateral &amp; meaningfulness issues will only be relevant on certain sites.</p>
<p>(As a final caveat: in some ways eBay falls closer in ultimate result to a <em>reputation system</em>, a topic which we'll be covering more in a few articles down the road, but its lessons learned are still entirely accurate for rating systems of all sorts.)</p>
<p>&nbsp;</p>
<h3>Granular Ratings</h3>
<p><img border="0" alt="Smiley" title="Smiley" src="http://lifewithalacrity.blogs.com/photos/uncategorized/smiley.png" style="margin: 0px 5px 5px 0px; float: left;" />
In general, <em>people want to be nice</em>. There are exceptions to that rule, perhaps even great numbers of them, but the average, well-adjusted person would prefer to make other people happy, not sad.</p>
<p>This has a notable effect on any comparison rating system, because it means that people are less likely to use the bottom half of any rating scale. If you did a statistical run on eBay, you'd certainly find that more than 99 out of every 100 ratings are positive. This is largely influenced by concerns of bilateral revenge, as discussed below, and the fact that eBay suggests other means of dispute resolution when you try and leave negative feedback. However, <a href="http://www.rpg.net">RPGnet</a>, a roleplaying site which reviews games, comics, books, movies, and more shows a similar trend despite the lack of bilaterality.</p>
<p>RPGnet uses two 5-points scales for reviews, resulting in a total rating of 2-10. Of all the ratings at RPGnet, 6,983 reviews have a total that's above average, a total rating of 6 or more, and 795 have a total that's below average, a total rating of 5 or less. Perhaps there are more people who sit down to write a review because they really like a game than those who do so because they really hated it, but the result of ~90% of reviews being above average is still stunning.</p>
<p>The following table shows all the ratings for each of the two categories that RPGnet uses, &quot;Style&quot; and &quot;Substance&quot;:</p>
<p><a href="http://www.rpg.net/reviews/archive/9/9971.phtml"><img border="0" alt="Rpgnetsettlersreview" title="Rpgnetsettlersreview" src="http://lifewithalacrity.blogs.com/photos/uncategorized/rpgnetsettlersreview.png" style="margin: 0px 0px 15px 5px; float: right;" /></a>
</p>
<table cellpadding="5">
<thead>
<tr align="right">
<td><strong>Rating</strong></td>
<td><strong>Style</strong></td>
<td><strong>Substance</strong></td>
<td><strong>%</strong></td>
</tr>
</thead>
<tbody>
<tr align="right">
<td>1</td>
<td>73</td>
<td>210</td>
<td>1.8%</td>
</tr>
<tr align="right">
<td>2</td>
<td>687</td>
<td>590</td>
<td>8.2%</td>
</tr>
<tr align="right">
<td>3</td>
<td>2127</td>
<td>1583</td>
<td>23.8%</td>
</tr>
<tr align="right">
<td>4</td>
<td>3337</td>
<td>3242</td>
<td>42.2%</td>
</tr>
<tr align="right">
<td>5</td>
<td>1554</td>
<td>2153</td>
<td>23.8%</td>
</tr>
</tbody></table>
<p>This evidence confirms what we'd already suspected. Only 10% of raters use the bottom two ratings in a 5-point scale, and only 2% use the bottom rating. The median of the 5-point scale is actually the fourth point, with a neat bell curve arranged around it.</p>
<p>Because users are innately unwilling to give bad ratings, as evidenced here, useful comparison ratings truly come about only through fractional differences between good ratings. In this case, the difference between &quot;3&quot;, &quot;4&quot;, and &quot;5&quot; is meaningful, and becomes more meaningful as more ratings are entered. Eventually you can look at a ranked list of ratings and see that &quot;4.2&quot; is a good rating while &quot;3.5&quot; is not.</p>
<p>In order to do this, however, you need enough levels of good ratings to be able to distinguish between them. eBay, only offering one positive rating, does not provide enough differentiation. RPGnet, with its three positive ratings, might. However, sites that offer a 10-point scale are the ones that really seem to be able to produce meaningful statistics. On those sites we can expect that 90% of users will choose between six different numbers, from &quot;5&quot; to &quot;10&quot;, and as the number of ratings builds up, this will produce enough differentiation to be meaningful. If you have already adopted a 5-point scale, consider allowing users to select the half-points, giving users a greater ability to differentiate their ratings.<br /> </p>
<p>&nbsp;</p>
<h3>Distinct Ratings</h3>
<p>No two users are ever going to rate the same; different rating numbers will mean different things to each person. This can introduce minor discrepencies into ratings, if a single individual rates particularly low or high. However, because most ratings are eventually used for comparisons, if that low- or high-rater rates many different things, the ratings equalize. &quot;Item A&quot; is rated low by this person, but so is &quot;Item B&quot;, and so they end up in the correct positions <em>in relation to each other</em>.</p>
<p>A bigger problem occurs when an individual is inconsistent in his ratings over time. If an individual rates everything low for a while, then rates everything high, then he has a greater chance of biasing the overall rating pool. Worse, his individual ratings aren't meaningful, because you can't look at two items, see that one is a &quot;6&quot; and another is an &quot;8&quot;, and truly believe that he likes the &quot;8&quot; a fair amount more than the &quot;6&quot;. This reduces the usability of an individual recommendation system or a friends system where one user might look at what other users thought about products, because their unaggregated numbers are not accurate.</p>
<p>You thus want to help individuals to stay consistent, and the best way to do that is to make the criteria for your ratings distinct. <a href="http://www.boardgamegeek.com">BoardGameGeek</a>, a board game web site that supports a 10-point rating system for games, does a good job of offering distinction in its ratings. </p>
<blockquote><p><a href="http://www.boardgamegeek.com/game/13"><img border="0" alt="Settlers_rating_1" title="Settlers_rating_1" src="http://lifewithalacrity.blogs.com/photos/uncategorized/settlers_rating_1.png" style="margin: 0px 0px 5px 5px; float: right;" /></a>
</p>
<ul>
<li><strong>10</strong> - Outstanding. Always want to play and expect this will never change.</li>
<li><strong>9 </strong>- Excellent game. Always want to play it.</li>
<li><strong>8 </strong>- Very good game. I like to play. Probably I'll suggest it and will never turn down a game.</li>
<li><strong>7 </strong>- Good game, usually willing to play.</li>
<li><strong>6 </strong>- Ok game, some fun or challenge at least, will play sporadically if in the right mood.</li>
<li><strong>5 </strong>- Average game, slightly boring, take it or leave it.</li>
<li><strong>4 </strong>- Not so good, it doesn't get me but could be talked into it on occasion.</li>
<li><strong>3 </strong>- Likely won't play this again although could be convinced. Bad.</li>
<li><strong>2 </strong>- Extremely annoying game, won't play this ever again.</li>
<li><strong>1 -</strong> Defies description of a game. You won't catch me dead playing this. Clearly broken.</li></ul></blockquote>
<p>If you offer a distinct rating listing like this, some users will still come up with their own rating ideas, but if they do, they're more likely to remember what each number means to them. For everyone else, a very clear, s rating system is the most likely to produce meaningful and consistent results. As long as users aren't puzzled by the distinction, they'll be consistent in picking the same numbers for the same rating every time.</p>
<p>&nbsp;</p>
<h3>Statistical Ratings</h3>
<p>The last big topic that you have to think about in creating most comparison rating systems is whether they're statistically sound. </p>
<p>The best way to make your ratings statistically sound is with volume. If you can manage thousands or tens of thousands of ratings for each item, any anomolies are going to become noise. However, the fewer ratings you have, the more likely it is that your ratings are inaccurate in relationship to your database of ratings as a whole. (And thus one of the failures for eBay is that it tries to claim meaningfulness for users with very few ratings, where there's clearly no statistical basis.)</p>
<p><a href="http://en.wikipedia.org/wiki/Thomas_Bayes"><img border="0" alt="Bayes" title="Bayes" src="http://lifewithalacrity.blogs.com/photos/uncategorized/bayes.jpeg" style="margin: 0px 0px 5px 5px; float: right;" /></a>
Ideally what you want to do is give items with fewer ratings among your collection less weight, and those with more ratings higher weight. One simple way to do this is to apply a <em>bayesian average</em>. Variants of this are used by the aforementioned BoardGameGeek and by <a href="http://www.imdb.com">IMDB</a>. RPGnet is using it for some unreleased software as well.</p>
<p>The idea behind a bayesian average is that you normalize ratings by pushing them toward the average rating for your site, and you do that more for items with fewer ratings than those with more ratings. The basic formula looks like this:</p>
<blockquote><p><code> b(r) = [ W(a) * a + W(r) * r ] / (W(a) + W(r)]</code>
</p>
<p><code>r</code> = average rating for an item<br /><code>W(r)</code> = weight of that rating, which is the number of ratings<br /><code> a</code> = average rating for your collection<br /> <code>W(a)</code> = weight of that average, which is an arbitrary number, but should be higher if you generally expect to have more ratings for your items; 100 is used here, for a database which expects many ratings per item<br /><code>b(r)</code> = new bayesian rating </p></blockquote>
<p>Say three &quot;shill&quot; users had come onto your site and rated a brand new indie film a &quot;10&quot; because the producer asked them to. However, you use a bayesian average with a weight of 100, and thus 3 ratings won't move the movie very far from the average site rating of 6.50:</p>
<blockquote><p><code>b(r) = [100 * 6.50 + 3 * 10] / (100 + 3)<br /> b(r) = 680 / 103<br /> b(r) = 6.60</code></p></blockquote>
<p>WowWebDesigns uses a similar model and even offers a <a href="http://www.wowwebdesigns.com/formula.php">good explanation of their methods</a> on their web site.<a href="http://www.wowwebdesigns.com/designs/id_242/ratings/"><img border="0" src="http://lifewithalacrity.blogs.com/photos/uncategorized/wowwebdesignsrating.png" title="Wowwebdesignsrating" alt="Wowwebdesignsrating" class="image-full" halign="middle" style="margin: 5px;" /></a>
</p>
<p>With everything that's been described thus far, including granularity and distinction, a bayesian average (or some other similiar method) will probably be enough to give your ratings a good, sound statistical basis. However, sites with low volume of ratings may still be concerned with &quot;shills&quot; or &quot;crappers&quot; who come in to your site just to put &quot;10&quot;s on their favorite items on &quot;1&quot;s on their least favorite. RPGnet's reviews are an example of a site that could experience this issue, because only a few people are going to ever write reviews for an individual item, and this small number of reviews could compromise the nature of any comparisons generated by the ratings sytems.</p>
<p>In short summary the following additional methods may help with this issue:</p>
<ul>
<li><p><strong>Rate the Raters:</strong> Reviews are low volume, but presumably readers of those reviews are high volume, and you can take advantage of that to then have your readers rate the reviews. <a href="http://www.amazon.com">Amazon</a> and <a href="http://www.netflix.com">Netflix</a> are two examples of sites which use this method by asking &quot;how many readers found this helpful&quot;.</p></li>
<li><p><strong>Altruistic Punishment:</strong> An alternative method for rating raters is to use <a href="http://www.lifewithalacrity.com/2005/03/dunbar_altruist.html#altruistic_punishment">altruistic punishment</a>. Herein users can punish someone who does contribute to the community, but at a cost to themselves. So, a reader could flag a poor rating or a poor review at some minor cost to their own rating. Though this method may seems somewhat paradoxical, <a href="http://en.wikipedia.org/wiki/Game_theory">game theory</a>&nbsp; suggests that it is a generally effective technique for improving the commons.</p>
</li>
<li><p><strong>Adjust Ratings Based on Ratings:</strong> Ratings can be self-adjusted based upon the rater's own behavior. The simplest method here is to map a rater's average rating to the average rating for a site. For example, if the average rating of a site is 6.50 and a shill's average rating is 10.0, then those 10s should be treated as 6.50s. This has the possibility for some intensive calculations, however, and may lead to additional bias in your rating pool if shills figure out the methods you use to adjust ratings.
</p></li>
<li><p><strong>Allow Editorial Fiat:</strong> Another method is to allow editorial fiat, where editors are expected to come in and remove bad ratings (or proactively not release them). This clearly results in time issues, but they may not be major since only sites with small numbers of ratings/item will have to do this type of adjusting. Further, automated systems could flag &quot;suspicious&quot; rating patterns which are outside the norms for average, speed of rating, etc. (RPGnet supports editorial fiat by requiring editorial release of all reviews.)</p></li></ul>
<p>The idea of adjusting ratings based on ratings bears a bit of additional discussion because it's somewhat similar to another well-knowing rating system: slashdot. Herein you have both ratings and meta-ratings. People can rate threads and articles, then other people can agree or disagree with those ratings, which in turn makes it more or less likely that the original rater will be allowed to rate in the future (depending on if people agree or disagree with his ratings). Under a more general classification, this is probably a <em>meta-rating system based on a reputation system</em>, so it's something we'll look at further a couple of articles down the road.</p>
<p>&nbsp;</p>
<h3>Other Issues: Bilateralism &amp; Usefulness</h3>
<p>90% of the rating issues that sites will face are covered by the above. However eBay in particular raised two other issues -- bilateralism and usefulness -- that aren't as generally relevant but do deserve some consideration.</p>
<p><strong><a href="http://lifewithalacrity.blogs.com/photos/uncategorized/ebayfeedback.jpg"><img border="0" src="http://lifewithalacrity.blogs.com/photos/uncategorized/ebayfeedback.jpg" title="Ebayfeedback" alt="Ebayfeedback" class="image-full" style="margin: 0px 0px 5px 5px; float: right;" /></a>
Bilateralism:</strong> One of the reasons that eBay's ratings fall apart is that they're bilateral. Buyers and sellers rate each other simultaneously and thus there's the fear of revenge if you rate someone badly. It's a sufficient issue that eBay has a <a href="http://pages.ebay.com/help/feedback/questions/retaliatory-feedback.html">FAQ on the topic</a>, though they don't offer any good answers. </p>
<p>The following solution would address some issues of bilateral revenge:</p>
<ul>
<li><p>Put a time limit on bilateral ratings</p></li>
<li><p>Release bilateral ratings simultaneously at the end of the time limit</p></li>
<li><p>Don't allow additional ratings after the time period</p></li>
</ul>
<p>This would work well on an eBay, where you're unlikely to conclude an additional deal with someone you rated badly, and thus there's no possibility ever for rating revenge. On a game site, however, where people are arbitrarily put into games with each other, and thus you could end up in a game with someone you rated poorly, there might be room for later revenge, down the road. This would have to be addressed to truly feel comfortable with bilateral ratings. </p>
<p>Additional investigation might reveal more variations of this method, or offer good answers for alternatives, like <em>anonymous ratings</em>.</p>
<p>In addition, good privacy restrictions are really needed to make bilateral ratings work, as well as Terms of Service that protect users from lawsuits for ratings. There have already been cases of physical threats based upon eBay ratings. eBay has also produced cases where people threatened slander or libel lawsuits for bad ratings, and this even further chills the possibility of true ratings appearing on the eBay server.</p>
<p><strong>Usefulness:</strong> Finally, you want to make sure your ratings are useful at your sites. Rankings are a good way to achieve this. You can see the &quot;best games ever&quot; ranked, or you can see the most interesting user content rise to the top of a long listing, and the least interesting sink to the bottom.</p>
<p>eBay offers a counter example of frustration with the usefulness of ratings. As already mentioned, you can theoretically ban &quot;bad&quot; users from bidding on your items, and then cancel bids from these users if they appear. However, there are multiple issues with this approach. First, how do you define &quot;bad&quot; users on eBay? Insufficient feedback? Too much negative feedback? Too high a percentage of negative feedback? Second, there is no automated method for doing this, so you must remain ever vigilant on your auctions to make sure that &quot;bad&quot; users aren't involved. Third, there's no way to keep a bad bidder from returning after you've cancelled his bid. Fourth, these bad bids and cancellations have the possibility of corrupting your auction, as you could lose other bidders who came in, saw the higher bid when the bad bidder was involved, then left before the bid was reduced by his removal. Finally, greed is a powerful motivator on eBay, which might lead to the retention of bad users.</p>
<p>You also need to be careful with your user interface for ratings. Here is an example of a poor UI:</p>
<p><img border="0" src="http://lifewithalacrity.blogs.com/photos/uncategorized/uselessratingui.jpg" title="Uselessratingui" alt="Uselessratingui" />
</p>
<p>&nbsp;</p>
<h3>Conclusion</h3>
<p>Comparison ratings are going to be an increasingly important force as the Internet continues to mature. To produce meaningful comparison ratings for your site, you need to concentrate on four important factors: granularity, specifity, sound statistics, and usefulness. And, if you offer bilateral ratings, make sure you understand the subtleties of that as well.</p>
<hr />
<p><em>Related articles from this blog:</em></p>
<blockquote>
<li><em><a href="http://www.lifewithalacrity.com/2005/12/systems_for_col.html">2005-12: Systems for Collective Choice</a></em></li>
<li><em><a href="http://www.lifewithalacrity.com/2006/01/ranking_systems.html">2006-01: Collective Choice: Competitive Ranking Systems</a></em></li>
<li><em><a href="http://www.lifewithalacrity.com/2006/08/using_5star_rat.html">2006-08: Using 5-Star Rating Systems</a></em></li>
<li><em><a href="http://www.lifewithalacrity.com/2007/01/collective_choi.html">2007-01: Experimenting with Ratings</a></em></li>
</blockquote>
<p>Related articles from Shannon Appelcline's <a href="http://www.skotos.net/articles/show-column.phtml?colname=TTnT_">Trials, Triumphs &amp; Trivialities:</a></p>
<blockquote>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_192.phtml">#192: Managing User Creativity, Part One</a></em></li>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_193.phtml">#193: Managing User Creativity, Part Two</a></em></li>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_196.phtml">#196: Collective Choice: Ratings, Who Do You Trust?</a></em></li>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_198.phtml">#198: Collective Choice: More Thoughts About Ratings</a></em></li>
</blockquote>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">I've ran into my fair share of voting systems, but by far the worst I've ever seen is the one used at www.animenfo.com, a database of anime products with user ratings. When giving a product a rating, a user is required to also write a constructive review on the product. However, the reviews are moderated and, often, removed from the database as "unconstructive" by the limited number of moderators. The problem with this approach is that the moderators are inevitably biased. A submitted, bad rating on a product, if reviewed by a moderator who personally likes the show being rated, is often removed from the database with the claim that the review was not constructive. Perhaps not entirely related, but an example of ratings-gone-awry, all the same.
-Kalle.
</p>
<a class="u-author h-card" href="http://www.livejournal.com/userinfo.bml?user=kallewooof">Kalle</a>
<time class="dt-published" datetime="2005-12-13T10:42:58-07:00">2005-12-13T10:42:58-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">It's rarely used, but asking people to rank from -5 to +5 can be better than ranking from 0 to 10.   You make it very clear that "0" means average/neutral.   You won't entirely eliminate the positive bias in ratings but you can reduce it.  And you bring everybody closer to the same mean.
I've concluded over time that in fact the response to a negative feedback on eBay should be disabled, as it contains no information.   Who, after all, is going to give a positive feedback to somebody after they have slapped a negative on you?  The likely choices there are no-feedback or neutral from a charitable person and of course a revenge negative.
So they could make it simpler.  If the first person gives a negative, the transaction is considered sour.  In your stats it would list the number of first-negatives you left for others.  (The number of negs you leave for others is already visible but harder to find.)  Ideally split buyer/seller.
</p>
<a class="u-author h-card" href="http://ideas.4brad.com">Brad Templeton</a>
<time class="dt-published" datetime="2005-12-13T13:11:31-07:00">2005-12-13T13:11:31-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">An interesting point missing from this good summary:
Many huge ratings sites see a clear bimodal distribution of scores when rating products(movies, cds, books, etc.)  with a simple scoring scheme, such as a single 5-star scale: The nodes are at 1 and 5 stars, with the love-or-hate scores making up more than 80% of all scores.
Clearly, some of that is a function of the intrinsic cost vs. incentive structures of completing ratings and reviews. When there is a clear direct benifit to the user (such as Netflix, Slashdot, or Yahoo! Music's Launchcast) ratings tend to distribute a bit more evenly (but just a bit.)
My point is that the actual end-user application of the rating has a large effect on the nature of the scores that will be created.
</p>
<a class="u-author h-card" href="http://www.fudco.com/habitat">F. Randall Farmer</a>
<time class="dt-published" datetime="2005-12-14T16:13:25-07:00">2005-12-14T16:13:25-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">I find when people give a bad rating on anything from eBay to those hotel and restaurant review sites its usually as a result of an extremely negative personal experience therefore the rating tends to be exagerated and totally not objective.
A blind system like the porposed solution to eBay bilateralism issue is probably best.
I've been a mystery shopper for a handful of restaurants and the system works quite well. In this system the purpose is to behave exactly like a regular consumer. You sit down, ask about the specials, take mental note of everything from the bathroom sink to the temperature of the food (and a hundred other details), but you don't behave in any way that would alter the staff you are a mystery shopper (for example writing things down is strickly prohibited).
Upon returning home you complete a lengthy questionnare about all the details you were supposed to notice. In this system the rewards is for a thorough assesment, regardless of its positive or negative slant. The more detail you provide the better assignments you get next time around. Even if you totally slam a place, but you provide substantial detail, you will be "promoted" to a "bar visit" or something much more rewarding than the typical lunch visit. So, I also agree with this articles suggestion to rate the raters, akin to what Amazon does but without the bias towards volume.
I would also addd that there is no middle ground on such ratings. Whether the choices range from Strongly Agree to Strongly Dissagree, or from "shortest wait" to "longest wait" there is no 'neutral' choice, nothing is "just right" as in the story about the three bears and the porridge. Even with numerical choices they are always even, not odd, so there is not chance of ranking in the middle. I like that. I think it pushes you to be more realistic. Having a middle ground leaves the undecided the opportunity to not make a decision. A "middle" rating is of no use to anyone.
</p>
<a class="u-author h-card" href="http://www.jobmachine.net/shally/">Shally</a>
<time class="dt-published" datetime="2005-12-21T16:23:26-07:00">2005-12-21T16:23:26-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">Researcher Paul Resnick has been looking at eBay, too. His blog is at http://www.livejournal.com/users/presnick/ and has posts like eBay Live Trip Report:
http://www.livejournal.com/users/presnick/8121.html
There are a few relevant articles as well, at http://www.si.umich.edu/~presnick/#publications
</p>
<a class="u-author h-card" href="http://seb.notlong.com">Seb</a>
<time class="dt-published" datetime="2005-12-29T05:53:29-07:00">2005-12-29T05:53:29-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">Good work there, and very thorough. Can we distinguish the social/transactional from the object/informational aspects of a rating situation? I'm just wondering aloud. On the one hand is the fact that publishing one's rating of a transaction will reflect on the transaction partner, on oneself, and so is social. On the other hand is the fact one can indeed rate an experience with some objectivity, assuming that the soft stuff has been bracketed out. I dont see how we can bracket out the social though, at least in a way that users will be able to participate in.
There's a thing about sincerity as a type of interaction: it's an attribute of expression that cannot be stated explicitly (say that you're being sincere and you throw your sincerity into quesion immediately). Ratings may fall into that kind of category of linguistic and metalinguistic acts..
</p>
<a class="u-author h-card" href="http://www.gravity7.com/blog/media/">adrian Chan</a>
<time class="dt-published" datetime="2006-01-04T09:47:53-07:00">2006-01-04T09:47:53-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
Wow, thorough and cogent.
Of all of the points, one missed opportunity occured to me while reading, and that is on the EBay statistical validity criticism. The phrase 'thus one of the failures for eBay is that it tries to claim meaningfulness for users with very few ratings, where there's clearly no statistical basis' struck me as off.
Human transactions are not mechanical actions - they involve situations that often matter. Hence a particular negative may really be cause for serious concern, even if there are not yet many ratings. Also, beginners are not inherantly less important than experienced traders. So though difficult, credit, or blame, is rightly awarded even on the basis of just a few transactions. Exactly how is a subject of further refinement.
I have read some of the EBay dissection papers a while back. This post is far more comprehensive, that is wide ranging, and yet not missing clarity, accuracy or nuance. Master work.
</p>
<a class="u-author h-card" href="#">Brian Hamlin</a>
<time class="dt-published" datetime="2006-05-30T00:43:49-07:00">2006-05-30T00:43:49-07:00</time>
</div>
<div class="u-comment h-cite">
<p class="p-content p-name">I have an interesting brainstorm for you about the netflix challenge:
http://www.thinksketchdesign.com/2008/05/03/design/coding/does-the-netflix-challenge-have-it-backwards
cheers -
thinksketch
</p>
<a class="u-author h-card" href="http://thinksketchdesign.com">thinksketch</a>
<time class="dt-published" datetime="2009-03-03T18:56:13-07:00">2009-03-03T18:56:13-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2005/12/collective_choi.html" rel="syndication">orginal layout</a></p>
