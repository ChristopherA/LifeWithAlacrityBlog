---
title: "Map Mashup"
slug: "map_mashup"
url: "/2004/10/map_mashup.html"
image: "http://lifewithalacrity.github.io/previous/images/mapmashup_1.gif"
tags:
  - "User Interface"
  - "Web/Tech"
  - "user interface"
  - "web"
  - "map"
  - "graphic"
  - "overlay"
  - "transparency"
  - "cursor"
date: "2004-10-06T00:12:46-07:00"
---
<p><a href="/previous/photos/uncategorized/mapmashup_1.gif" onclick="window.open(this.href, '_blank', 'width=495,height=298,scrollbars=no,resizable=no,toolbar=no,directories=no,location=no,menubar=no,status=no,left=0,top=0'); return false"><img alt="Mapmashup_1" title="Mapmashup_1" src="/previous/images/mapmashup_1.gif" width="247" height="149" border="0" style="float: right; margin: 0px 0px 5px 5px;" /></a>I'm a sucker for great user-interface design ideas, especially if they succeed with what typically has poor UI design -- web pages.</p>
<p>MultiMap is a company that sells maps and aerial photos, primarily for Great Britain. They offer an online map tool that is very similar to that used by MapQuest or Yahoo Maps.</p>
<p>However, for certain regions, they have this fabulous capability to show you the aerial photo of the place, then display hovering around the cursor a slightly transparent map. For instance, take a look at this map of <a href="http://www.multimap.com/map/photo.cgi?client=public&X=533258&Y=180057&width=500&height=310&gride=529090&gridn=179645&srec=0&coordsys=gb&db=pc&pc=&zm=0&scale=10000&up.x=186&up.y=3">the Tower of London and the Tower Bridge</a>.</p>
<p>This trick is done completely in Javascript, located in <a href="http://www.multimap.com/static/global.js">global.js</a>, and uses the overlay.style.* properties that I've really only seen used in Javascript-based menus before. I'm a bit confused on how this works in IE, as it does not support alpha tranparency as this posting <a href="http://persistent.info/archives/2004/04/27/overlays">semi-transparent image overlays</a> discusses, but I suspect they accomplished it through careful use of transparency in the .gif overlay image. I'll have to investigate more.</p>
<p>There are probably many more other innovative uses of this type of transparency overlay tracking to the cursor that can be helpful in other web tools.</p>
<p>[original link via <a href="http://www.futurismic.com/2004/10/magical-maps.html">Futurismic</a>]</p>
<p>[<a href="http://www.thingsthemselves.com/">Jeffery To</a> adds some more detail about this Javascript technique in this post's <a href="/2004/10/map_mashup.html#comments">comments</a>.]</p>
<footer><h3>Comments</h3>
<div class="u-comment h-cite">
<p class="p-content p-name">The Javascript in http://www.multimap.com/static/global.js only sets the clipping for the overlay layer, since it changes everytime the user moves the mouse. The layer transparency (for overDiv) is set in http://www.multimap.com/static/ps_new.css . No need for transparent GIFs.
IE does support alpha transparency for layers, using their filter:alpha(opacity=x) declaration. As the posting on semi-transparent image overlays points out, IE doesn't support alpha transparency for PNG images.
</p>
<a class="u-author h-card" href="http://www.thingsthemselves.com/">Jeffery To</a>
<time class="dt-published" datetime="2004-10-10T11:31:41-07:00">2004-10-10T11:31:41-07:00</time>
</div>
</footer>
<p class="previous"><a href="/previous/2004/10/map_mashup.html" rel="syndication" class="u-syndication" >orginal layout</a></p>
