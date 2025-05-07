#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://petermortimer.de"
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = False
LOAD_CONTENT_CACHE = False

# Paths and URLs for articles (blog posts)
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'

# ✅ Add these lines to ensure static pages (e.g. about.md) are built
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Optional: turn on plugins, analytics, etc.
# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
