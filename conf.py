# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "cattomgithub/Blog@gh-pages"
}

# 站点设置
site_name = "Cat Tom's Blog"
site_logo = "${static_prefix}favicon.ico"
site_build_date = "2020-02-08T00:00+00:00"
author = "Cat Tom"
email = "linweijie2015@gmail.com"
author_homepage = "/"
description = "乌云退散 重见天日"
key_words = ['Cat Tom', 'blog']
language = 'zh-CN'
background_img = "${static_prefix}bg.jpg"
external_links = [
    {
        "name": "Cat Tom's World",
        "url": "https://cattom.space",
        "brief": "我的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "碎碎念",
        "url": "${site_prefix}daily/",
        "target": "_self"
    },
    {
        "name": "随笔",
        "url": "${site_prefix}category/随笔/",
        "target": "_self"
    },
    {
        "name": "游戏",
        "url": "${site_prefix}category/游戏/",
        "target": "_self"
    },
    {
        "name": "技术",
        "url": "${site_prefix}category/技术/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
   
    {
        "name": "GitHub",
        "url": "https://github.com/cattomgithub",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
