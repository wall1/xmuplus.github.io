---
layout: default
title: Changelog
permalink: /changelog/
---

<h1 style="margin-top: 1.25em;">Changelog</h1>

### 2017

* June 14 - Add [instantclick.js](http://instantclick.io/) to speed up website by preloading links.

* Apr 02 - Replace [duoshuo](http://duoshuo.com/) comment with [typecho](http://typecho.org/).

* Mar 11 - Add [clipboard.js](https://github.com/zenorocha/clipboard.js) - <span class="qtip2">Modern</span> copy to clipboard.

* Mar 04 - Add a color bar at the top of the page.

* Feb 10 - Host <span class="qtip2"><span style="color:#4885ed">G</span><span style="color:#db3236">o</span><span style="color:#f4c20d">o</span><span style="color:#4885ed">g</span><span style="color:#3cba54">l</span><span style="color:#db3236">e</span> Fonts</span> locally.

* Jan 21 - Serve static files such as images, css files, and javascript files in [upyun](https://www.upyun.com/index.html).

* Jan 09 - Fix some bugs.

### 2016

* Dec 12 - Add [nprogress](https://github.com/rstacruz/nprogress) to show the loading state of the pages with a slim progress bar at the top side.

* Nov 28 - Add [code-prettify](https://github.com/google/code-prettify) to make source-code snippets in <span class="qtip2">HTML</span> prettier.

* Nov 25 - Add a back-to-top icon at the bottom right corner.

* Nov 19 - Add [emojify.js](https://github.com/Ranks/emojify.js) to convert <span class="qtip2">Emoji</span> keywords to images.

* Oct 6 - Show detailed type of web browser and operating system using <span class="qtip2">[UAParser.js](https://github.com/faisalman/ua-parser-js)</span>.

* Oct 2 - Add <span class="qtip2">Share Buttons.</span>

* Oct 1 - Add <span class="qtip2">[IcoMoon](https://icomoon.io/)</span> - pixel perfect icon solutions.       

* Sept 13 - Add the <span class="qtip2">Github</span> logo <i class="fa fa-github" aria-hidden="true"></i> to site header, and change color to blue when hovering over it.

* Sept 11 - Build a <a href="/googlemap/">xmu<sup class="googlemap"><span style="color:#4885ed">G</span><span style="color:#db3236">o</span><span style="color:#f4c20d">o</span><span style="color:#4885ed">g</span><span style="color:#3cba54">l</span><span style="color:#db3236">e</span></sup></a> map using [<span class="qtip2"><span style="color:#4885ed">G</span><span style="color:#db3236">o</span><span style="color:#f4c20d">o</span><span style="color:#4885ed">g</span><span style="color:#3cba54">l</span><span style="color:#db3236">e</span> Maps API</span>](https://developers.google.com/maps/).

* Sept 10 - Add <strong title="Pretty powerful tooltips">qTip<sup>2</sup></strong>. The second generation of the advanced [<span class="qtip2">qTip</span>](http://qtip2.com/) plugin for the ever popular <span class="qtip2">jQuery</span> framework.

* Sept 8 - Add [<span class="qtip2">PhotoSwipe</span>](https://github.com/dimsemenov/PhotoSwipe) - a <span class="qtip2">JavaScript</span> image gallery for mobile and desktop.

* Sept 5 - Build the full-text [search](/search) engine using [<span title="A client side full-text search engine">lunr.js</span>](http://jekyll.tips/jekyll-casts/jekyll-search-using-lunr-js/).

* Aug 15 - Add [<span class="qtip2">Fon<span class="tumblr"><i class="fa fa-tumblr-square" aria-hidden="true"></i></span> Awesome</span>](http://fontawesome.io/icons/).

* Aug 13 - Add [<span class="qtip2"><span style="color:#4885ed">G</span><span style="color:#db3236">o</span><span style="color:#f4c20d">o</span><span style="color:#4885ed">g</span><span style="color:#3cba54">l</span><span style="color:#db3236">e</span> Analytics</span>](https://www.google.com/analytics/).

* Aug 9 - <span class="qtip2">My</span> [<span class="qtip2">Jekyll</span>](https://jekyllrb.com/) blog launched, which is hosted on <a href="https://pages.github.com/"><span class="qtip2">Github Pages</span></a>.


<!-- footer -->
<div class="footer">
<a href="/changelog/">博客</a>已萌萌哒运行<br/>
<span id="span_dt_dt"></span><span class="my-face">(●'◡'●)ﾉ♥</span>
</div>
<!-- CSS -->
<script>
  function show_date_time(){
  window.setTimeout("show_date_time()", 1000);
  BirthDay=new Date("8/9/2016 21:30:00");
  today=new Date();
  timeold=(today.getTime()-BirthDay.getTime());
  sectimeold=timeold/1000
  secondsold=Math.floor(sectimeold);
  msPerDay=24*60*60*1000
  e_daysold=timeold/msPerDay
  daysold=Math.floor(e_daysold);
  e_hrsold=(e_daysold-daysold)*24;
  hrsold=Math.floor(e_hrsold);
  e_minsold=(e_hrsold-hrsold)*60;
  minsold=Math.floor((e_hrsold-hrsold)*60);
  seconds=Math.floor((e_minsold-minsold)*60);
  span_dt_dt.innerHTML=""+daysold+"天"+hrsold+"小时"+minsold+"分"+seconds+"秒";
  }
show_date_time();
</script>
<style>
.fa-github:hover{
	color: #268bd2;
}
/**/
.masthead-title {
	color: #505050;
}
/**/
sup.googlemap {
	font-size: 9px;
}
.qtip2{
	font-size: 90%;	
}
strong {
	font-size: 90%;
    font-weight: 700;
    color: #8BCF01;
}
.tumblr{
	font-size: 80%;		
}
.footer{
	text-align:center;
	font-size: 12px;
	margin-bottom: 12px; 
	margin-top: 50px;
  }
@media (min-width:38em) {
	body {
	font-size: 19px;
}
</style>

