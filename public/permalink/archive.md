---
layout: page
title: Archive 
permalink: /archive/
---
<style>
.page{
  margin-top: 3em;  /*About title*/
}
.page-title{
  margin-bottom: .5em;  /*About title*/    
}
body {
    font-family: -apple-system,"Helvetica Neue",Helvetica,Arial,"PingFang SC","Hiragino Sans GB","WenQuanYi Micro Hei","Microsoft Yahei",sans-serif;
}
</style>

<section>
  <h3>Codes <i class="fa fa-slideshare" style="color:#3cba54;"></i></h3>
      <ul class="post-list">
      <li><a href="/ubuntu-16.04-lts/">Ubuntu 16.04 LTS 初始配置 
      <span class="entry-date">Jan 16, 2017</span></a></li>
      <li><a href="/mac-dd-command/">用「dd」命令把 iso 镜像写入 u盘
      <span class="entry-date">Dec 23, 2016</span></a></li>    
      <li><a href="/manjaro-arm/">树莓派3上跑 Manjaro Linux
      <span class="entry-date">Dec 8, 2016</span></a></li> 
      <li><a href="/google-code-prettify/">使用 google-code-prettify 实现代码高亮
      <span class="entry-date">Nov 27, 2016</span></a></li> 
  </ul>
</section>

<section id="archive">
  <h3>2017</h3>
  {%for post in site.posts %}
    {% unless post.next %}
      <ul class="post-list">
    {% else %}
      {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
      {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
      {% if year != nyear %}
        </ul>
        <h3>{{ post.date | date: '%Y' }}</h3>
        <ul class="post-list">
      {% endif %}
    {% endunless %}
      <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}<span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" }}</time></span></a></li>
  {% endfor %}
  </ul>
</section>

{% include footer.html %}
