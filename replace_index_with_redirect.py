#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import os.path as osp

publications_text = """
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=/publications.html">
    <title>Redirecting...</title>
</head>
<body>
    <p>If you are not redirected, <a href="/publications.html">click here</a>.</p>
</body>
</html>
"""

# Ensure output/ exists, then write the redirect index.html
os.makedirs("output", exist_ok=True)
with open("output/index.html", "w") as file_handle:
    file_handle.write(publications_text)
