# -*- coding: utf-8 -*-

import sys
import os
import shlex

sys.path.insert(0, 'src')

try:
    from ocupado import __version__
except ImportError:
    __version__ = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'ocupado'
copyright = u'2015, Steve Milner'
author = u'Steve Milner'

version = __version__
release = version

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'nature'
# html_theme_options = {}
# html_theme_path = []
# html_title = None
# html_short_title = None
# html_logo = None
# html_favicon = None
html_static_path = ['_static']
# html_extra_path = []
# html_last_updated_fmt = '%b %d, %Y'
# html_use_smartypants = True
# html_sidebars = {}
# html_additional_pages = {}
# html_domain_indices = True
# html_use_index = True
# html_split_index = False
# html_show_sourcelink = True
# html_show_sphinx = True
# html_show_copyright = True
# html_use_opensearch = ''
# html_file_suffix = None
# html_search_language = 'en'
# html_search_options = {'type': 'default'}
# html_search_scorer = 'scorer.js'

htmlhelp_basename = 'ocupadodoc'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

latex_documents = [
  (master_doc, 'ocupado.tex', u'ocupado Documentation',
   u'Steve Milner', 'manual'),
]

# latex_logo = None
# latex_use_parts = False
# latex_show_pagerefs = False
# latex_show_urls = False
# latex_appendices = []
# latex_domain_indices = True

man_pages = [
    (master_doc, 'ocupado', u'ocupado Documentation',
     [author], 1)
]

# man_show_urls = False

texinfo_documents = [
  (master_doc, 'ocupado', u'ocupado Documentation',
   author, 'ocupado', 'One line description of project.',
   'Miscellaneous'),
]

# texinfo_appendices = []
# texinfo_domain_indices = True
# texinfo_show_urls = 'footnote'
# texinfo_no_detailmenu = False
