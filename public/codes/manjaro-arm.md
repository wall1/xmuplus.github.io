---
layout: default
title: manjaro-arm
permalink: /manjaro-arm/
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



<h2 style="margin-bottom: 30px;">树莓派3上跑 Manjaro Linux </h2>

<div class="homepic">
<img src="/public/img/codes/raspberry-pi.jpg" />
</div>

<style>
.homepic{
    position: relative; max-width: 600px; 
    margin: 0 auto; 
    background-color: #eee;
}
</style>

<b>安装方法：</b>

1.先从 [Manjaro-arm][1] 官网下载 Base Edition 16.08 镜像。这个基本版是 Xfce 桌面环境，你也可以在这里下载到 KDE 桌面版以及其他社区版本。

2.解压得到以 `.img` 结尾的镜像(3.6G)。在 Windows 上用 Win32DiskImager，将 Manjaro-arm 镜像写入 SD 卡中(我用的是16G)。

3.接下来就可以将 SD 卡放入树莓派；用 HDMI 线将树莓派和显示器连接，调整显示器(Dell U2414H) 输入模式为 HDMI；把鼠标键盘连到树莓派的 USB 接口上。最后连上电源，Manjaro 系统自动运行。默认账号和密码都是 `manjaro`。SSH 默认启用。

4.打开 Terminal(终端) 输入 `df -h`，得到
<pre class="prettyprint linenums">
[manjaro@manjaro-arm ~]$ df -h          
Filesystem      Size  Used Avail Use% Mounted on 
/dev/root       3.2G  3.0G  131M  96% / 
devtmpfs        457M     0  457M   0% /dev 
tmpfs           462M   80K  462M   1% /dev/shm 
tmpfs           462M  664K  461M   1% /run 
tmpfs           462M     0  462M   0% /sys/fs/cgroup 
tmpfs           462M  4.0K  462M   1% /tmp 
/dev/mmcblk0p1  100M   19M   82M  19% /boot 
tmpfs            93M  8.0K   93M   1% /run/user/1000
</pre>

很容易发现这里的 `/dev/root` Filesystem 只有 3.2个G，并且已经使用了3个G。而之前已经提到我的 SD 卡是16G的，所以接下来要进行扩容。在终端运行
<pre class="prettyprint linenums">
sudo resize-sd
</pre>
接着按提示操作，其实就是按两次回车键 orz~。系统会自动重启，这样 SD 卡剩余的空间就被填充了。在终端再次输入 `df -h` 会发现 `／dev/root` 已经扩展到了15个G
<pre class="prettyprint linenums">
[manjaro@manjaro-arm ~]$ df -h          
Filesystem      Size  Used Avail Use% Mounted on 
/dev/root        15G  3.1G   11G  23% / 
devtmpfs        457M     0  457M   0% /dev 
tmpfs           462M   80K  462M   1% /dev/shm 
tmpfs           462M  664K  461M   1% /run 
tmpfs           462M     0  462M   0% /sys/fs/cgroup 
tmpfs           462M  4.0K  462M   1% /tmp 
/dev/mmcblk0p1  100M   19M   82M  19% /boot 
tmpfs            93M  8.0K   93M   1% /run/user/1000
</pre>

5.接下来就可以愉快地更新系统了
<pre class="prettyprint linenums">
排列源(在终端输入）：
sudo pacman-mirrors -g
然后同步：
sudo pacman-optimize && sync
升级系统：
sudo pacman -Syyu
</pre>


<b>说明：</b>

1.如果第4步不对文件系统进行扩容，那么在第5步更新系统时会提示空间不足，无法更新。

2.你也可以按照官方 [Wiki][2] 介绍的几种方法在树莓派上安装 Manjaro-arm。Enjoy!

<hr style="margin-bottom: 3em; border-top: 1px solid #fafafa; border-bottom: 1px solid #fafafa;" />


{% include comments.html %}
{% include footer.html %}

[1]:http://manjaro-arm.org/downloads/

[2]:http://wiki.manjaro-arm.org/index.php?title=Main_Page
