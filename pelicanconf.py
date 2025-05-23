#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import six

AUTHOR = "Peter"
SITENAME = "A Place for Asides"
SITEURL = ""
RELATIVE_URLS = True

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
PLUGINS = ["metadataparsing", "render_math"]

# adding favicon based on https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
STATIC_PATHS = ["extra/favicon.ico", "extra/CNAME", "images", "pages/bibtex", "extra/vis/paragraph-reading"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
}

# Links in header
HEADER_LINKS = (
    ("About", "/about.html"),
    ("Publications", "/publications.html"),
    ("Previous Projects", "/previous-projects.html"),
    ("Blog", "/index.html"),
    ("Book List", "/books.html"),
)

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (("GitHub", "https://github.com/tonyromarock"),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
OUTPUT_SOURCES = True

# custom metadata parsers from pelican-metadataparsing
def parseTocify(string):
    return string == 'True'

METADATA_PARSERS = {
    "Tocify": parseTocify
}