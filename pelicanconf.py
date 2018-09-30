#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter'
SITENAME = 'Rather Read Blog'
SITEURL = 'http://petermortimer.de'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = "aboutwilson"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# adding favicon based on https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
STATIC_PATHS = ['extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Blogroll
LINKS = (('Greg Reda', 'http://www.gregreda.com/'),
         ('mkaz.blog', 'https://mkaz.blog/'),
         ('inFERENCe', 'https://www.inference.vc/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/tonyromarock'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
