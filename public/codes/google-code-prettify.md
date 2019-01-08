---
layout: default
title: google-code-prettify
permalink: /google-code-prettify/
---
<style>
body{
	font-family: -apple-system,"Helvetica Neue",Helvetica,Arial,"PingFang SC","Hiragino Sans GB","WenQuanYi Micro Hei","Microsoft Yahei",sans-serif;
	font-size: 17px;
	-webkit-font-smoothing: antialiased !important;
}
code{
	color: #505050;
	background-color: #e1e1e1;
}
@media (min-width:38em) {
	.sidebar-toggle{
	font-size:20px;
	} 
}
</style>



<h2 style="margin-bottom: 30px;">使用 google-code-prettify 实现代码高亮 </h2>

<b>安装方法：</b>

1.首先到 Github 下载最新的 [google-code-prettify][1]. 从压缩包中提取 pretty.css 和 pretty.js 两个文件, 放置到/public/js/文件夹中 (你也可以放在你喜欢放的地方)；

2.在 <head> 标签中引入 pretty.css 文件：
<pre class="prettyprint linenums">
&lt;link href="&lt;?php bloginfo('template_directory'); ?>/prettify.css" type="text/css" rel="stylesheet" />
</pre>

3.在 </body> 标签前引入以下两段代码：
<pre class="prettyprint linenums">
&lt;script type="text/javascript" src="&lt;?php echo home_url(''); ?>/public/js/jquery.js">&lt;/script>
</pre>

如果之前已经引入过 jquery.js, 则可以不再重复引入。但请务必确保 jquery.js 位于 prettify.js 之前。

<pre class="prettyprint linenums">
&lt;script type="text/javascript" src="&lt;?php bloginfo('template_directory'); ?>/public/js/prettify.js">&lt;/script>
&lt;script type="text/javascript">
  window.prettyPrint && window.prettyPrint()
&lt;/script>
</pre>


<b>使用方法：</b>

1.写文章时用 `<pre class="prettyprint linenums">` `</pre>` 包围代码块, 就可以看到上色的效果了。见上图。

2.代码中如果出现 `<` `>`符号，请将其替换成 `&lt;` 和 `&gt;`; 否则浏览器无法显示。 

3.code-prettify 自带5种[主题][2]。其中, prettify.css 显示的是默认主题 Default, 呈白色背景。如果您需要改变样式, 只需把上面第2步中 prettify.css 替换成相应主题的 `.css` 文件即可。 更多主题下载: [color-themes][3].

4.本文所用的主题经过了修改, 下载[请戳][4]。Enjoy!


<hr style="margin-bottom: 3em; border-top: 1px solid #fafafa; border-bottom: 1px solid #fafafa;" />


{% include comments.html %}
{% include footer.html %}

[1]:https://github.com/google/code-prettify

[2]:https://rawgit.com/google/code-prettify/master/styles/index.html

[3]:https://jmblog.github.io/color-themes-for-google-code-prettify/

[4]: https://paypal.b0.upaiyun.com/public/js/prettify/prettify.css