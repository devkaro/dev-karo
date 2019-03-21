#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Surbakti'
SITENAME = u'Developer Karo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SUMMARY_MAX_LENGTH = 30
TAG_FEED_RSS = 'feeds/{slug}.tag.xml'
PDF_GENERATOR = True
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

# DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10
STATIC_PATHS = ['gambar']

DISQUS_SITENAME = "devkaro"
