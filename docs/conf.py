import os
import sys
import json
import datetime
sys.path.insert(0, os.path.abspath(".."))
from scripts.gallery_directive import GalleryDirective

project = "zc notebook"
author = "子川"
year = str(datetime.date.today().year)
copyright = '2021--' + year + ' ' + author
root_doc = 'index' # Changed in version 4.0: Renamed master_doc to root_doc.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "ablog",
]

bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'

########################################################################################
numfig = True
numfig_format = {
    'figure': 'Fig. %s '
}

templates_path = ["_templates"]
exclude_patterns = [
    "_build", 
    "Thumbs.db", 
    ".DS_Store", 
    '**.ipynb_checkpoints', 
    'scripts', 
    "**/pandoc_ipynb/inputs/*", 
    ".nox/*", "README.md",
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}
nb_execution_mode = "off"
suppress_warnings = ["mystnb.unknown_mime_type", "myst.strikethrough"]
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "substitution",
    "tasklist",
    "strikethrough",
]
myst_heading_anchors = 3

blog_path = "blog"
blog_post_pattern = "posts/*/*"
blog_authors = {
    "zclab": ("子川", "https://github.com"),
}
blog_locations = {
    "beijing": ("北京", "https://zh.wikipedia.org/wiki/%E5%8C%97%E4%BA%AC%E5%B8%82"),
}
blog_languages = {
    'en': ('English', None),
    'cn': ('中文', None)
}
blog_default_language = "cn"
blog_default_location = "beijing"
post_show_prev_next = False

fontawesome_included = True
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ['extra.css',]
html_title = "ZC Notebook"
html_favicon = "_static/favicon.svg"
html_last_updated_fmt = ""
html_sidebars = {
    'index': ['search-field.html', 'components/sidebar-quicklinks.html'],
    "posts/**": ["ablog/postcard.html","ablog/categories.html","ablog/tagcloud.html","ablog/archives.html",],
    "blog": ["ablog/categories.html","ablog/tagcloud.html","ablog/archives.html",],
    "blog/**": ["ablog/postcard.html","ablog/categories.html","ablog/tagcloud.html","ablog/archives.html",],
}

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "zclab",
    "github_repo": "notebook",
    "github_version": "main",
    "doc_path": "docs",
}

html_theme_options = {
    "search_bar_text": "Search this site...",
    "logo": {
        "text": "ZC's Notebook",
        "image_light": "logo.png",
        "image_dark": "logo-dark.png",
    },
    "navbar_align": "content",
    "show_prev_next": True,
    "navigation_with_keys": True,
    "use_edit_page_button": True,
    "header_links_before_dropdown": 4,
    "external_links": [
        {
            "name": "Rust语言圣经", 
            "url": "https://course.rs/about-book.html"
        },
        {
            "name": "Rust入门秘籍", 
            "url": "https://rust-book.junmajinlong.com/"
        },
        {
            "name": "Rust 秘典", 
            "url": "https://nomicon.purewhite.io/intro.html"
        },
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
    ],
    "footer_items": ["footer/copyright", "footer/sphinx-version"],
}

# ---- Other documentation options -------------------------

todo_include_todos = True
todo_link_only = True


def setup(app):
    # Add the gallery directive
    app.add_directive("gallery-grid", GalleryDirective)
