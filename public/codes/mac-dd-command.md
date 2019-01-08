---
layout: default
title: manjaro-arm
permalink: /mac-dd-command/
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



<h2 style="margin-bottom: 30px;">用「dd」命令把 ISO 镜像写入 U盘</h2>

<b>写入方法：</b>

1.打开 Mac 终端，输入 `df -h` 查看一下磁盘概况

<pre class="prettyprint linenums">
Macintosh:~ afanofte$ df -h
Filesystem      Size   Used  Avail Capacity  iused   ifree %iused  Mounted on
/dev/disk0s2   233Gi   79Gi  154Gi    34% 20801780 40267660   34%   /
devfs          183Ki  183Ki    0Bi   100%      637        0  100%   /dev
map -hosts       0Bi    0Bi    0Bi   100%        0        0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%        0        0  100%   /home
/dev/disk1s1    29Gi  1.5Mi   29Gi     1%        0        0  100%   /Volumes/你U盘的名称
Macintosh:~ afanofte$
</pre>

这里的 `/dev/disk0s2` 是系统的 SSD 盘，`/dev/disk1s1` 是 32G U盘


2.终端输入 `sudo umount /dev/disk1s1` 卸载掉 U盘所在的 `/dev/disk1s1`。
<pre class="prettyprint linenums">
Macintosh:~ afanofte$ sudo umount /dev/disk1s1
Password:
umount(/Volumes/你U盘的名称): Resource busy -- try 'diskutil unmount'
</pre>

输入密码后显示 `umount` 资源忙，提示用 `diskutil umount`。那么我们就按照提示在终端输入 `sudo diskutil umount /dev/disk1s1`
<pre class="prettyprint linenums">
Macintosh:~ afanofte$ sudo diskutil umount /dev/disk1s1
Volume 你U盘的名称 on disk1s1 unmounted
</pre>

这样 `/dev/disk1s1` 就成功被卸载掉了。


3.接下来就可以用「dd」命令写入镜像了
<pre class="prettyprint linenums">
Macintosh:~ afanofte$ sudo dd if=/Users/afanofte/openSUSE-Leap-42.1-DVD-x86_64.iso of=/dev/disk1
</pre>
这里 `if=` 后面跟的是 Linux 镜像文件的路径，别忘了 `.iso` 也要写。 `of=` 后面就填刚才卸载的磁盘 `/dev/disk1`，这样系统就开始写镜像了，完成前不要关闭终端。

<span style="color: red; font-weight: bold">注意：</span>这里和前面的 `/dev/disk1s1` 不同，没有 `s1`。


4.写入过程中重新打开一个终端窗口，输入 `iostat -w 2` 命令查看磁盘写入状态。 `-w 2` 表示每隔两秒输出一次
<pre class="prettyprint linenums">
Macintosh:~ afanofte$ iostat -w 2
</pre>

<div style="position: relative; max-width: 600px; 
    margin: 0 auto; margin-bottom: 30px">
<img src="/public/img/blog/mac-dd.png" />
</div>


5.写入完成后终端显示：完成 4.15G 镜像数据的写入，共耗时 2204 秒
<pre class="prettyprint linenums">
Macintosh:~ afanofte$ sudo dd if=/Users/afanofte/CentOS-7.0-1406-x86_64-DVD.iso of=/dev/disk1
8101888+0 records in
8101888+0 records out
4148166656 bytes transferred in 2204.642144 secs (1881560 bytes/sec)
Macintosh:~ afanofte$
</pre>

<b>知识相关：</b>

Mac OSX 用 `disk1, disk2, disk3` 来标识物理磁盘 。`disk2s1, disk2s2` 表示 `disk1` 磁盘上的第一个分区和第二个分区。Linux 下是用 `sda, sdb, sdc` 来标识不同的物理磁盘，用 `sda1, sda2, sda3` 来表示同一磁盘不同的分区。

<hr style="margin-bottom: 3em; border-top: 1px solid #fafafa; border-bottom: 1px solid #fafafa;" />


{% include comments.html %}
{% include footer.html %}

[1]:http://manjaro-arm.org/downloads/

[2]:http://wiki.manjaro-arm.org/index.php?title=Main_Page
