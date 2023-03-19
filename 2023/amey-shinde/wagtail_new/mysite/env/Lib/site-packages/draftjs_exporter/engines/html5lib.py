from __future__ import absolute_import, unicode_literals

import re

from draftjs_exporter.engines.base import DOMEngine

try:
    from bs4 import BeautifulSoup

    # Cache empty soup so we can create tags in isolation without the performance overhead.
    soup = BeautifulSoup('', 'html5lib')
except ImportError:
    pass

# Python 2/3 unicode compatibility hack.
# See http://stackoverflow.com/questions/6812031/how-to-make-unicode-string-with-python3
try:
    UNICODE_EXISTS = bool(type(unicode))
except NameError:
    def unicode(s):
        return str(s)

RENDER_RE = re.compile(r'</?(fragment|body|html|head)>')
RENDER_DEBUG_RE = re.compile(r'</?(body|html|head)>')


class DOM_HTML5LIB(DOMEngine):
    """
    html5lib implementation of the DOM API.
    """

    @staticmethod
    def create_tag(type_, attr=None):
        if not attr:
            attr = {}

        return soup.new_tag(type_, **attr)

    @staticmethod
    def parse_html(markup):
        return BeautifulSoup(markup, 'html5lib')

    @staticmethod
    def append_child(elt, child):
        elt.append(child)

    @staticmethod
    def render(elt):
        return RENDER_RE.sub('', unicode(elt))

    @staticmethod
    def render_debug(elt):
        return RENDER_DEBUG_RE.sub('', unicode(elt))
