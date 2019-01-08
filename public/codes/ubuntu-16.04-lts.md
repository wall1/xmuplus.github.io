---
layout: default
title: Ubuntu 16.04 LTS 初始配置 
permalink: /ubuntu-16.04-lts/
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



<h2 style="margin-bottom: 30px;">Ubuntu 16.04 LTS 初始配置</h2>

<div class="homepic">
<img src="{{ site.baseurl }}/public/img/codes/unbuntu_fullscreen.png" />
</div>

<br/>
<b>一、优化系统：</b>

先删除一些几乎不会用的软件包，像 LibreOffice 这样冗余的大头是必须要先删的，免得后面 `upgrade` 更新全部软件时占用资源下载它的更新。

1.删除 LibreOffice
<pre class="prettyprint linenums">
sudo apt-get remove libreoffice-common  
</pre>

2.删除 Amazon 的链接
<pre class="prettyprint linenums">
sudo apt-get remove unity-webapps-common  
</pre>

3.删掉基本不用的自带软件（用的时候再装也来得及)
<pre class="prettyprint linenums">
sudo apt-get remove thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines cheese transmission-common gnome-orca webbrowser-app gnome-sudoku  landscape-client-ui-install onboard deja-dup 
</pre>
这样系统就基本上干净了。

<br/>
<b>二、更改下载源：</b>

1.依次打开 `System Settings` -> `Software & Updates` -> `Download from:`
点开列表选择国内的下载源
<div class="homepic">
<img src="/public/img/codes/ubuntu_repo.png" />
</div>

2.接着点 `Close`，弹出对话框再点下 `Close` 关闭对话框
<div class="homepic">
<img src="/public/img/codes/ubuntu_close.png" />
</div>

3.打开终端运行 `update` 以同步 `/etc/apt/sources.list` 和 `/etc/apt/sources.list.d` 中列出的源的索引，获取到最新的软件包信息
<pre class="prettyprint linenums">
sudo apt-get update
</pre>

运行后的结果如下图示：
<div class="homepic">
<img src="/public/img/codes/ubuntu_update01.png" />
</div>
<div class="homepic">
<img src="/public/img/codes/ubuntu_update02.png" />
</div>
这样今后软件下载速度会快很多，我选的的是阿里云的源。

4.接着运行 `upgrade` 升级已安装的所有软件包，升级之后的版本就是本地索引里的。因此，在执行 `upgrade` 之前一定要执行 `update`, 这样下载的软件包才是最新版的
<pre class="prettyprint linenums">
sudo apt-get upgrade
</pre>

<br/>

<span style="color: red; font-weight: bold">说明：</span> 如果 `update` 执行后出现以下 `无法连接主机` 的错误提示
<div class="homepic">
<img src="/public/img/codes/ubuntu_resolve.png" />
</div>

在终端打开 `resolv.conf` 文件
<pre class="prettyprint linenums">
sudo nano /etc/resolv.conf
</pre>

在 `nameserver 127.0.1.1` 这一行下面添加两行
<pre class="prettyprint linenums">
nameserver 8.8.8.8
nameserver 8.8.4.4
</pre>

完了之后按 `Ctrl+O` -> `回车键` -> `Ctrl+X` 保存退出。重新执行
<pre class="prettyprint linenums">
sudo apt-get update
</pre>
这样就可以成功连接到你选择的下载源的主机了。

<br/>

><span style="color: red; font-weight: bold">注：</span>你选择完国内下载源后也可以不点上面说的 `Close`，而是点 <i class="fa fa-repeat" style="color:#0095DD;"></i> `Reload` 来 `Updating cache`，获取最新的软件包信息。
<div class="homepic">
<img src="/public/img/codes/ubuntu_cache.png" />
</div>

下载完成之后就可以运行 `sudo apt-get install <package name>` 安装软件了。
这时在终端输入 `update` 会显示：
<pre class="prettyprint linenums">
afanofte@ubuntu:~$ sudo apt-get update
Hit:1 http://mirrors.aliyun.com/ubuntu xenial InRelease
Hit:2 http://mirrors.aliyun.com/ubuntu xenial-updates InRelease
Hit:3 http://mirrors.aliyun.com/ubuntu xenial-backports InRelease
Hit:4 http://mirrors.aliyun.com/ubuntu xenial-security InRelease
Reading package lists... Done                     
afanofte@ubuntu:~$ 
</pre>

<br/>
<b>三、安装谷歌浏览器：</b>

1.安装谷歌公钥
<pre class="prettyprint linenums">
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
</pre>

2.添加下载源
<pre class="prettyprint linenums">
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
</pre>

3.安装
<pre class="prettyprint linenums">
sudo apt-get update 
sudo apt-get install &lt;package name>
</pre>
这里的 `<package name>` 你可以选择你需要的 Chrome [版本][1]，稳定版就填 `google-chrome-stable`

<br/>
<b>四、安装 Sublime Text 3：</b>
<pre class="prettyprint linenums">
sudo add-apt-repository ppa:webupd8team/sublime-text-3 
sudo apt-get update
sudo apt-get install sublime-text-installer
</pre>

<br/>
<b>五、安装 Chromium：</b>
<pre class="prettyprint linenums">
sudo add-apt-repository ppa:chromium-daily/stable 
sudo apt-get update
sudo apt-get install chromium-browser
</pre>

<br/>
<b>六、安装 Wine：</b>

装了 Wine 后就可以在 Ubuntu 中安装和使用以 `.exe` 结尾的 Windows 软件了
<pre class="prettyprint linenums">
sudo add-apt-repository ppa:ubuntu-wine/ppa 
sudo apt-get update
sudo apt-get install wine1.8
</pre>


<hr style="margin-bottom: 3em; border-top: 1px solid #fafafa; border-bottom: 1px solid #fafafa;" />

{% include comments.html %}
{% include footer.html %}

<style>
.homepic{
    position: relative; max-width: 600px; 
    margin: 0 auto; 
    background-color: #eee;
}
</style>

[1]:https://www.ubuntuupdates.org/ppa/google_chrome