from __future__ import absolute_import, unicode_literals

import re

from draftjs_exporter.engines.base import DOMEngine

try:
    from lxml import etree, html
except ImportError:
    pass

NSMAP = {
    'xlink': 'http://www.w3.org/1999/xlink',
}

RENDER_RE = re.compile(r'</?fragment>')


class DOM_LXML(DOMEngine):
    """
    lxml implementation of the DOM API.
    """
    @staticmethod
    def create_tag(type_, attr=None):
        nsmap = None

        if attr:
            if 'xlink:href' in attr:
                attr['{%s}href' % NSMAP['xlink']] = attr.pop('xlink:href')
                nsmap = NSMAP

        return etree.Element(type_, attrib=attr, nsmap=nsmap)

    @staticmethod
    def parse_html(markup):
        return html.fromstring(markup)

    @staticmethod
    def append_child(elt, child):
        if hasattr(child, 'tag'):
            elt.append(child)
        else:
            c = etree.Element('fragment')
            c.text = child
            elt.append(c)

    @staticmethod
    def render(elt):
        return RENDER_RE.sub('', etree.tostring(elt, method='html', encoding='unicode'))

    @staticmethod
    def render_debug(elt):
        return etree.tostring(elt, method='html', encoding='unicode')
