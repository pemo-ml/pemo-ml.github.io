#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Peter"
SITENAME = "A Place for Asides"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Paris"
DEFAULT_DATE_FORMAT = "%B %d %Y"

DEFAULT_LANG = "en"

THEME = "mywilson"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# additional plugins
PLUGIN_PATHS = ["/home/peter/Documents/pelican-plugins"]
PLUGINS = ["render_math"]

# adding favicon based on https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
STATIC_PATHS = ["extra/favicon.ico", "extra/CNAME", "images"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
}

# Links in header
HEADER_LINKS = (
    ("About", "/pages/about.html"),
    ("Previous Projects", "/pages/previous-projects.html"),
    ("Blog", "/"),
    ("Books I've read", "/pages/books.html"),
)

# Blogroll
LINKS = (
    ("Greg Reda", "http://www.gregreda.com/"),
    ("mkaz.blog", "https://mkaz.blog/"),
    ("inFERENCe", "https://www.inference.vc/"),
    ("Matt Might", "http://matt.might.net/#blog"),
)

# Social widget
SOCIAL = (("GitHub", "https://github.com/tonyromarock"),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
