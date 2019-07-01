---
title: "Collective Choice: Experimenting with Ratings"
slug: "collective_choi"
url: "/2007/01/collective_choi.html"
image: "/previous/photos/uncategorized/rpgnetlogo_1.gif"
tags:
  - "Social Software"
  - "User Interface"
  - "Web/Tech"
  - "rating"
  - "review"
  - "ratings"
  - "collective choice"
  - "selection system"
  - "statistics"
  - "bayesian"
  - "rpg"
  - "gaming index"
  - "user content"
date: "2007-01-01T22:38:15-07:00"
---
<p><span style="font-size: 0.7em;">by Christopher Allen &amp; Shannon Appelcline</span></p>
<p><em>[This is the fourth in a series of articles on <a href="/2005/12/systems_for_col.html">collective choice</a>, co-written by my collegue <a href="http://www.skotos.net/about/staff/shannon_appelcline">Shannon Appelcline</a>. It will be <a href="http://www.skotos.net/articles/TTnT_179.phtml">jointly posted</a> in Shannon's <a href="http://www.skotos.net/articles/TTnT.shtml">Trials, Triumphs &amp; Trivialities</a> online games column at <a href="http://www.skotos.net/">Skotos</a>.]</em></p>
<p>Last year in <a href="/2005/12/collective_choi.html">Collective Choice: Rating Systems</a> we took a careful look at eBay and other websites that collect ratings, and used those systems as examples to highlight a number of theories about how to make rating systems more useful.</p>
<p>We suggested three main methods for improving rating systems:</p>
<p><strong>Granular Ratings:</strong> Based on the clumping of ratings to high values, we believed that ratings could be made more useful by increasing the size of a rating scale. Most rating scales are 5-point ranges, so we suggested a 10-point range instead.</p>
<p><strong>Distinct Ratings:</strong> Raters can be somewhat arbitrary in how they rate items, varying both from each other and even from themselves (usually over multiple sessions). Thus we believed that providing explicit statements of what each number meant could improve ratings.</p>
<p><strong>Statistical Ratings:</strong> Finally we stated that in low volumes ratings could be biased by various quirks of data entry, either malevolent or not, and that ratings could be improved with strong statistical methods being used to polish up data and automatically keep &quot;bad&quot; data in line with &quot;good&quot;.</p>
<p>In the year since we wrote that article we've decided to practice what we preach and have rolled out an entirely new rating system called <a href="http://index.rpg.net">The RPGnet Gaming Index</a>. We've applied all of the above theories and thus far it looks like they're not only working, but that they're actually providing better rating systems than previous ones we've used at the RPGnet site.</p>
<p>In this article we're going to step through the data we've collected from this experience and see how it applies to our theory: first by looking at our previous RPGnet rating system, then by looking at the new system, and finally by by examining the data from these two systems and comparing their results. We've also run into some unexpected troubles along the way, and we'll talk about that too.</p>
<h3>The RPGnet Reviews System</h3>
<p><a href="http://www.rpg.net"><img border="0" src="/previous/photos/uncategorized/rpgnetlogo_1.gif" title="Rpgnetlogo_1" alt="Rpgnetlogo_1" style="margin: 0px 5px 5px 0px; float: left;" /></a>
RPGnet is our gaming site for tabletop roleplaying—games like <em>Dungeons &amp; Dragons</em> and <em>Vampire: The Masquerade</em>. We purchased it in 2001 from the original owners. One of the benefits of RPGnet was that it had a very large community. As of today it sports one of the top-100 forums on the Internet, with over 1000 simultaneous users regularly logging in. However, because of its maturity, we also inherited many existing systems.</p>
<p><a href="http://www.rpg.net/reviews/archive/9/9971.phtml"><img border="0" alt="Rpgnet_review_summary_1" title="Rpgnet_review_summary_1" src="/previous/photos/uncategorized/rpgnet_review_summary_1.jpg" style="margin: 0px 0px 5px 5px; float: right;" /></a>
One of these was the <a href="http://www.rpg.net/reviews/">RPGnet Reviews System</a> which gave individual users the ability to review gaming products—mostly role-playing games, but also board games, books, DVDs, and a smattering of related products.</p>
<p>Most of these reviews are submitted by average readers who just want to talk about a product that they like (or don't), though a fair percentage are instead submitted by staff reviewers. (Overall at least 26% of our reviews are based on publisher &quot;comp&quot; copies, and thus may be considered largely professional, while the other 74% may or may not be.) The large community size of RPGnet applies to the Reviews System as well: currently it features 8,505 published reviews.</p>
<p>Looking at the RPGnet Reviews through our three filters we find the following:</p>
<p><strong>Granularity.</strong> The ratings from our existing reviews aren't as granular as we'd like. We have a theoretical scale of 2-10, but that's based upon a Style rating of 1-5 and a Substance rating of 1-5.</p>
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
<td>81</td>
<td>225</td>
<td>1.8%</td>
</tr>
<tr align="right">
<td>2</td>
<td>732</td>
<td>651</td>
<td>8.1%</td>
</tr>
<tr align="right">
<td>3</td>
<td>2364</td>
<td>1777</td>
<td>24.3%</td>
</tr>
<tr align="right">
<td>4</td>
<td>3618</td>
<td>3525</td>
<td>42.0%</td>
</tr>
<tr align="right">
<td>5</td>
<td>1709</td>
<td>2326</td>
<td>23.7%</td>
</tr>
</tbody></table>
<p> Approximately 90% of raters rate only with values of 3-5, and thus our scale is more limited than the 2-10 range would indicate. 42.9% of reviews further rate Style and Substance exactly the same, suggesting that not everyone sees a difference between these two elements. On the whole this scale isn't as a bad as a singular 5-point scale, but it also isn't a real 10-point scale, and the two orthogonal types of comparison don't necessarily provide a coherent description of a product.</p>
<p><strong>Distinctiveness.</strong> Conversely, the review ratings are fairly distinct because the Review System provides an explanation of what each rating number means. For example the five Substance ratings are: I Wasted My Money (1); Sparse (2); Average (3); Meaty (4); Excellent(5). The descriptions could be better, but hopefully they connect to some users in meaningful ways, and help them to rate consistently.</p>
<p><strong>Statistics.</strong> Our review ratings have no statistical basis. These values are used entirely unfiltered.</p>
<p>On the whole, the existing RPGnet Reviews embodied slightly less than half of what we wanted to see in a rating systems: some improvement over a simple 5-point scale; some effort put into making individual ratings distinct; and nothing statistical.</p>
<p>There is room for improvement, however, as we'll see when we analyze this system more fully.</p>
<h3>The RPGnet Gaming Index</h3>
<p>Our newer system is the <a href="http://index.rpg.net/">RPGnet Gaming Index</a>. It doesn't supersede our Reviews, but instead offers a complementary look at the roleplaying field. The Index is essentially an RPG industry database. It contains individual entries for many different gamebooks—currently 5248—and allows registered users to rate each of them. Those ratings are then turned into averages by various mathematical formulas on a nightly basis and the roleplaying games in our index are then ranked.</p>
<p>The large size of RPGnet has allowed us to very quickly turn our ideas of a Gaming Index into reality. Just six months after release we have:</p>
<ul><li>5248 well-written Index entries </li>
<li> 5908 different editions</li>
<li> 4240 authors</li>
<li> 4478 covers</li>
<li> 360 different game systems</li>
<li> 345 series</li>
<li> 10142 individual ratings</li></ul>
<p>Most of the ratings are clumped around the best and worst games, with many less popular games unrated as of yet. Four different items have at least 80 ratings each (<em>Call of Cthulhu</em>, <em>Exalted</em>, <em>Nobilis</em>, and <em>Unknown Armies</em>). Our average rating is 6.79. Ratings above 7.82 are in the 99th
percentile, ratings above 7.21 are in the 90th percentile, and ratings
below 6.53 are beneath the 10th percentile.</p>
<p>(For more info on the creation of the RPG Index, and how to encourage user generated content, see Shannon's articles, &quot;Managing User Creativity&quot;, <a href="http://www.skotos.net/articles/TTnT_/TTnT_192.phtml">Part One</a> and <a href="http://www.skotos.net/articles/TTnT_/TTnT_193.phtml">Part Two</a>.) </p>
<p>The RPGnet Index also handles some unusual situations, such as when a game book contains other game books as part of an anthology or compilation. For instance, the 8-book compilation <a href="http://index.rpg.net/display-entry.phtml?mainid=64">In Search of Adventure</a> has a composite rating of <a href="http://index.rpg.net/display-entry-ratings.phtml?mainid=64">6.57</a> which is partially based upon the individual adventures that make it up.</p>
<p><strong>Granularity:</strong> The first thing we did was provide a 10-point scale for this new system.</p>
<p><strong>Distinctiveness:</strong> We also made sure each point of the scale was clearly defined. Currently the points of our scale are: Worthless (1), Poor (2), Some Flaws (3), Almost Average (4), Average (5), Above Average (6), Good (7), Very Good (8), Outstanding (9), and One of the Best Ever (10).</p>
<p>We made some mistakes in our original release of our &quot;distinctive&quot; titles, and we discovered this had real effects on the user input, telling us that these title labels <em>are</em> meaningful to users.</p>
<p>First, we initially labeled 6 as &quot;average&quot;, to mirror the rating system for our existing Reviews, rather than setting 5 to be average. But as we noted in our first article, people like to be nice, and thus they tend to rate on the good side of a scale. Changing the label for our definition of average from 6 to 5 has slowly started dropping the average of all ratings down as a result (providing more breadth, a topic we'll talk about more shortly).</p>
<p>Second, two of our original distinctive titles were at odds with the others. Our original &quot;2&quot; value said that the game had &quot;a few useful elements&quot; and our original &quot;9&quot; value said that it was the &quot;best of the year&quot;. The 2 was much more specific than any of our other terms and the 9 created a comparative query that was very different from anything else. Overall our ratings conformed to a bell curve centered between 6 and 7, but we saw very clear dropouts in our curve at 2 and 9, telling us that we'd made mistakes in those terms, and that people were less willing to use them as a result. Since we've made the change to our current set of titles those two discontinuities have disappeared.</p>
<p><strong>Statistics.</strong> Finally, we fully integrated statistics into our new Index by using two main methods: bayesian weights and trust.</p>
<p>We explained bayesian weights pretty fully in our previous article. Here's what we said then:</p>
<blockquote>
<table width="90%" border="1" cellpading="3"><tbody><tr><p>
The idea behind a bayesian average is that you normalize ratings by pushing them toward the average rating for your site, and you do that more for items with fewer ratings than those with more ratings. The basic formula looks like this:</p>
<p><code>
b(r) = [ W(a) * a + W(r) * r ] / (W(a) + W(r)]</code></p>
<p>r = average rating for an item</p>
<p>W(r) = weight of that rating, which is the number of ratings</p>
<p>a = average rating for your collection</p>
<p>W(a) = weight of that average, which is an arbitrary number, but should be higher if you generally expect to have more ratings for your items; 100 is used here, for a database which expects many ratings per item</p>
<p>b(r) = new bayesian rating </p>
<p>Say three &quot;shill&quot; users had come onto your site and rated a brand new indie film a &quot;10&quot; because the producer asked them to. However, you use a bayesian average with a weight of 100, and thus 3 ratings won't move the movie very far from the average site rating of 6.50:</p>
<p><code>
b(r) = [100 * 6.50 + 3 * 10] / (100 + 3)</code><code><br />b(r) = 680 / 103</code><code><br />b(r) = 6.60
</code>
</p></tr></tbody></table>
</blockquote>
<p>We implemented bayesian weights exactly as we'd detailed, but with a lower weight of 25. Since then we've accrued over 10,000 ratings in the database, and we can probably start thinking about cranking that weight up, another topic we'll return to.</p>
<p>Our trust-based algorithms suggest that some ratings are better than others, and should thus be more trusted (and thus more weighted when we calculate the average rating of an item). Though bayesian weights have been used before, we're not aware of other systems that weight ratings based on trust. </p>
<p>The calculation of trust is very simple:</p>
<p><code>
Weight = 0 if #ratings(user) &lt;= 2</code><code><br />Otherwise Weight = #ratings(user) / 50 to a maximum of 2</code><code><br />Weight *= 2, to a maximum of 4, if the user included a comment
</code>
</p>
<p>This was based on the idea that the average good rater would rate 25 different items and the average great rater would rate at least 50. Additionally, we believed that ratings with comments were more likely to be thoughtful than those without.</p>
<p>That, overall, is a quick picture of what we've done with the RPGnet Gaming Index. Some of these ideas were laid out from the start, and others have been tuned as we progressed. </p>
<p>So how did we do, particularly in comparison to our existing RPGnet Reviews System?</p>
<h3>The Comparison</h3>
<p>One of our goals in improving rating systems has been to widen the range of possible input. As we noted earlier we discovered that 90% of our RPGnet Reviews Ratings were in the 3-5 range, and only 10% in the 1-2 range.</p>
<p>Generally, we can measure the success of widening a range by seeing whether the average rating of a database moves toward the <em>true</em> average. For the purposes of a 10-point scale from 1-10, that's a desired value of 5.5. That generally means we're looking for our average rating to <em>decrease</em> because people tend to rate high.</p>
<p>The following table compares the average results of Reviews ratings and Index ratings.</p>
<center><table cellpadding="3" border="1"><tbody><tr><td><strong>Database</strong></td>
<td><strong>Average</strong></td></tr>
<tr><td><strong>Converted Reviews</strong></td>
<td>7.25</td></tr>
<tr><td><strong>Massaged Reviews</strong></td>
<td>7.29</td></tr>
<tr><td><strong>Unweighted Index</strong></td>
<td>7.10</td></tr>
<tr><td><strong>Weighted Index</strong></td>
<td>6.78</td></tr>
</tbody></table></center>
<p>Here's what the categories in the above chart represent:</p>
<p><strong>Converted Reviews:</strong> The Style + Substance of the Reviews, converted from its 2-10 scale to a 1-10 scale: </p>
<p><code>
$rating = avg($style) + avg($substance);</code><br /><code>$rating = ($rating * 1.125) - 1.25;
</code>
</p>
<p><strong>Massaged Reviews:</strong> The Style + Substance of the Reviews, with Substance given double weight over Style because we think that more closely reflects the intentions of the reviewer, converted from its 2-10 scale to a 1-10 scale:</p>
<p><code>
$rating = (average($style) + 2*average($substance))/1.5;</code><br /><code>$rating = ($rating * 1.125) - 1.25;
</code>
</p>
<p><strong>Unweighted Index:</strong> Index ratings exactly as users have entered into our Gaming Index:</p>
<p><code>
$rating = average($index-rating);
</code>
</p>
<p><strong>Weighted Index:</strong> Index ratings adjusted by the weight of each individual rating, which is based on user trust and inclusion of comments:</p>
<p><code>
$rating = average($index-rating*$index-weight)/average($index-weight);
</code>
</p>
<p>Our average rating—which is our criteria for success—decreased somewhat from the Reviews System to the Gaming Index and it decreased much more dramatically when we introduced our trust systems.</p>
<p>The following chart shows the a typical example of how review and index ratings differ, using the venerable <em>Dungeons &amp; Dragons Player's Handbook</em> as an example:</p>
<center><a href="http://index.rpg.net/display-entry-ratings.phtml?mainid=72"><img border="0" src="/previous/photos/uncategorized/dd_players_handbook_rpgnet_reviews_only.jpg" title="Dd_players_handbook_rpgnet_reviews_only" alt="Dd_players_handbook_rpgnet_reviews_only" /><img border="0" src="/previous/photos/uncategorized/dd_players_handbook_index_ratings_only.jpg" title="Dd_players_handbook_index_ratings_only" alt="Dd_players_handbook_index_ratings_only" /></a></center><p>For this book the median ratings from reviews-only is 8, and the median from index-only is 7. A one-to-two point drop in median rating from reviews to index was consistent in all of our most-rated games other than those which were a rated a &quot;10&quot; in both places.</p>
<p>We believe that this initial success of our unweighted Gaming Index can be attributed to the slightly better <em>granularity</em>—a 10-point scale versus two 5-point scales—and our improved <em>distinctiviness</em>—based on better naming of the rating levels. The veracity of this will ultimately be played out as the Index grows.</p>
<p>However we have no doubt that our <em>statistical</em> approach to the index data, when we moved from our unweighted Index to our weighted Index, is providing even better results. We had theorized that users who input more and who include comments would provide &quot;better&quot; data, and by our criteria of the average of the ratings moving toward 5.5 that seems to be borne out. The following table looks at the information a bit more precisely, by comparing average ratings as total number of ratings increases over several ranges:</p>
<center><table cellpadding="3" border="1"><tbody><tr><td><strong># of Ratings</strong></td>
<td><strong>Average w/Comment</strong></td>
<td><strong>Average w/o Comment</strong></td></tr>
<tr><td><strong>1-2</strong></td>
<td>8.55</td>
<td>8.88</td></tr>
<tr><td><strong>3-24</strong></td>
<td>8.08</td>
<td>8.16</td></tr>
<tr><td><strong>25-49</strong></td>
<td>7.32</td>
<td>7.11</td></tr>
<tr><td><strong>50-99</strong></td>
<td>7.14</td>
<td>7.03</td></tr>
<tr><td><strong>100+</strong></td>
<td>6.17</td>
<td>6.99</td></tr></tbody></table></center>
<p>This table fairly definitively shows that base maxim: that the breadth of the ratings, and thus their quality, increases the more ratings a user makes. The improved quality of ratings with comments is less definitive. Among the vast mass of users the two values are pretty close, and sometimes the reverse of what we expect, but for the best and the worst users, ratings with comments seem to be better than those without. This latter point is another one that we'll have to continue to monitor as the Index grows beyond its current total of 10,000 ratings.</p>
<p>The other major element of our <em>statistical</em> approach to the Index is our bayesian weight. The following chart shows a top-ten chart for roleplaying games calculated via four different methodologies: our Reviews; our Index with no weighting; our Index with a 25 bayesian weighting (as it currently stands); and our Index with a 50 bayesian weighting:</p>
<center><table cellpadding="3" border="1"><tbody><tr><td><strong>#</strong></td>
<td><strong>Reviews-Only</strong></td>
<td><strong>0-weight Index</strong></td>
<td><strong>25-weight Index</strong></td>
<td><strong>50-weight Index</strong></td></tr>
<tr><td><strong>1</strong></td>
<td>Delta Green: Countdown</td>
<td>The Chronicles of Talislanta</td>
<td>Delta Green: Countdown</td>
<td>Delta Green</td></tr>
<tr><td><strong>2</strong></td>
<td>Nobilis</td>
<td>Wildside</td>
<td>Spirit of the Century</td>
<td>Delta Green: Countdown</td></tr>
<tr><td><strong>3</strong></td>
<td>Castle Falkenstein</td>
<td>Devil's Due</td>
<td>Delta Green</td>
<td>Unknown Armies</td></tr>
<tr><td><strong>4</strong></td>
<td>Vimary Sourcebook</td>
<td>Lodges: The Faithful</td>
<td>Unknown Armies</td>
<td>Call of Cthulhu</td></tr>
<tr><td><strong>5</strong></td>
<td>Liber Servitorum</td>
<td>Apocalypse</td>
<td>Call of Cthulhu</td>
<td>Nobilis</td></tr>
<tr><td><strong>6</strong></td>
<td>Ork!</td>
<td>Earthdawn Gamemaster's Compendium</td>
<td>Nobilis</td>
<td>Spirit of the Century</td></tr>
<tr><td><strong>7</strong></td>
<td>GURPS Russia</td>
<td>Into the Badlands</td>
<td>Pendragon</td>
<td>Over the Edge</td></tr>
<tr><td><strong>8</strong></td>
<td>GURPS Reign of Steel</td>
<td>Earthdawn Player's Compendium</td>
<td>Over the Edge</td>
<td>Pendragon</td></tr>
<tr><td><strong>9</strong></td>
<td>Cudgel's Compendium</td>
<td>Chronicle of the Black Labyrinth</td>
<td>Mutants &amp; Masterminds</td>
<td>Mutants &amp; Masterminds</td></tr>
<tr><td><strong>10</strong></td>
<td>Corum</td>
<td>The Spell Book</td>
<td>Pulp Hero</td>
<td>Vimary Sourcebook</td></tr></tbody></table></center>
<p>We actually <em>did</em> do a little bit of statistical analysis on the Reviews because on our first try to produce this chart we got a random clump of reviews that were 5/5 from a much larger pool, so we further ordered them by descending total count of reviews, and as a result you're seeing a better selection of ranked reviews than a truly unstatistical sampling would allow. We did the same for the unweighted Index (which clumped a number of results at &quot;10&quot;), except we further ordered items at the same weight by decreasing number of views (another statistical decision).</p>
<p>Clearly, deciding which of these lists is &quot;right&quot; is a much more subjective measure than the mathematical analysis we were able to apply to earlier problems. However, most roleplayers would tell you that the unweighted Reviews and Index lists are terrible. The top 5 items in the Reviews list actually aren't bad for a starting list of good games—but only because we did the aforementioned statistical ordering. Before that we just had a random listing of gaming items. Even with our attempts at quickie statistical analysis the unweighted Index is still quite bad, with only <em>Talislanta</em> regularly showing up on other &quot;best&quot; lists.</p>
<p>The problem is the ability of one person to come in and rate an item a &quot;10&quot; (or a &quot;5&quot;/&quot;5&quot;), thereby making that item more highly rated than <em>any</em> item which has an actual consensus of ratings. Of our unweighted top Reviews only the top three had more than 2 reviews and the rest had 2. Not surprisingly those top three were the best fits to a typical top-ten list. Of the unweighted Index only the top three had more than 1 rating, and the rest had 1. Our single good pick was in those top three.</p>
<p>Our 25-weight Index, which is what we currently use, has been generally accepted by the RPGnet community as a good marker of what's good and what's not. However there have been two items on it which some percentage of people disagree with: <em>Spirit of the Century</em> and <em>Pulp Hero</em>. It's instructive to see that when we increase to a 50-weight Index <em>Spirit of the Century</em> drops (even more notably than depicted here, because its actual rating changes from .01 from first place to .16 from first place) and <em>Pulp Hero</em> disappears entirely.</p>
<p>The questions of <em>what</em> to set your bayesian weight to, when to increase it, and what maximum value to set it to are all relatively unstudied and thus we don't have good answers to them. As we pass 10,000 ratings we're considering upping the bayesian value to 50. We expect that 100 will be our ultimate value when the Index is fully mature, however if we increase the weight too far an older, less rated game will never be able to get enough weight to get out of the doldrums.</p>
<h3>Conclusion</h3>
<p>We're by no means done with this ratings experiment. Though we've pleased and impressed with the growth of the RPGnet Index thus far, by next year we hope that the Index will include the vast majority of all games in print (as opposed to somewhat less than half now) and that our 10,000 ratings will grow to 50,000 or more. This will allow us to offer even more definitive answers to our questions.</p>
<p>In the meantime we're still mucking with our statistics and facing new problems.&nbsp; Some of the newest:</p>
<ul><li><strong>What to do about drive-by ratings:</strong> Our trust algorithm does a good job of making drive-by ratings, where a publisher points his audience to an item in our site, mostly irrelevant, but there's some concern that they could have more effect in the long run.</li>
<li><strong>How to incorporate our review ratings in our index ratings:</strong> It seems a shame to waste the thousands of reviews that have been written—and indeed currently they're calculated into a composite rating we use in the Index—but we're realizing that people have very different purposes for writing reviews and inputing ratings, which may result in some of the upward skew we see on the review side of things. Ultimately we need to decide whether they're just too different or whether our statistical massaging is enough to incorporate those reviews into a composite Index rating.</li>
<li><strong>How to pick some of our numbers:</strong> As we already noted we don't have good formulas for when to choose which bayesian weights. Likewise we've been guessing at which values to use for the trust-based weighting of our raters. Originally we set our desired rating count to 100 for good rater and 200 for great raters, but we've since dropped those to 50 for good and 100 for great based upon the real numbers of ratings that users were making. Again, we'd prefer to derive an actual formula for this type of calculation</li></ul>
<p>Shannon has discussed some of these issues more in his recent article <a href="http://www.skotos.net/articles/TTnT_/TTnT_198.phtml">More Thoughts Abour Ratings</a>.</p>
<p>Despite unanswered questions, we still feel good about the basic ideas we laid out in our article last year. We have no doubt that giving our ratings a <em>statistical</em> basis has dramatically improved them and evidence thus far suggests that both <em>granularity</em> and <em>distinctiveness</em> have been helpful as well.<br />
</p>
<hr />
<p><em>Related articles from this blog:</em></p>
<blockquote>
<li><em><a href="/2005/12/systems_for_col.html">2005-12: Systems for Collective Choice</a></em></li>
<li><em><a href="/2005/12/collective_choi.html">2005-12: Collective Choice: Rating Systems</a></em></li>
<li><em><a href="/2006/01/ranking_systems.html">2006-01: Collective Choice: Competitive Ranking Systems</a></em></li>
<li><em><a href="/2006/08/using_5star_rat.html">2006-08: Using 5-Star Rating Systems</a></em></li>
</blockquote>
<p>Related articles from Shannon Appelcline's <a href="http://www.skotos.net/articles/show-column.phtml?colname=TTnT_">Trials, Triumphs &amp; Trivialities:</a>
</p><blockquote>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_192.phtml">#192: Managing User Creativity, Part One</a></em></li>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_193.phtml">#193: Managing User Creativity, Part Two</a></em></li>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_196.phtml">#196: Collective Choice: Ratings, Who Do You Trust?</a></em></li>
<li><em><a href="http://www.skotos.net/articles/TTnT_/TTnT_198.phtml">#198: Collective Choice: More Thoughts About Ratings</a></em></li>
</blockquote>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">URL:
0-10 scale is too large for most relevant human ratings systems. maybe i should pull the psych papers, but people tend to do a 1-5 or 0-5 scale better. it's a sign of immaturity to only use the endpoints.
</p>
<a class="u-author h-card" href="#">Grumpy</a>
<time class="dt-published" datetime="2007-12-18T10:24:24-07:00">2007-12-18T10:24:24-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2007/01/collective_choi.html" rel="syndication nofollow" class="u-syndication" >original layout</a></p>
