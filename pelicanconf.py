#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jason Beach'
SITENAME = u'IMT Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Custom Solutions', 'https://github.com/IMTorgCustomSoln'),
         ('Visualizations', 'http://github.com/IMTorgVisSoln'),
         ('Integrated Tools', 'http://github.com/IMTorgOpenTools'))

# Social widget
SOCIAL = (('IMT website', 'http://mgmt-tech.org'),
          ('Open Group', 'http://imtorg.github.io'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'Flex'

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
