#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'surbakti'
SITENAME = 'Dev Karo - Mekaro'
SITEURL = 'https://dev.karo.or.id/'
SUMMARY_MAX_LENGTH = 30
TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'
TE_FORMATS = {
    'en': '%d %m %Y'
}
# Feed generation is usually not desired when developing
#FEED_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%s.tag.xml'
PDF_GENERATOR = True
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

DISPLAY_PAGES_ON_MENU =True
DEFAULT_PAGINATION = 10
STATIC_PATHS = ['gambar']

THEME = "themes/mekaro/"
DISQUS_SITENAME = "devkaro"