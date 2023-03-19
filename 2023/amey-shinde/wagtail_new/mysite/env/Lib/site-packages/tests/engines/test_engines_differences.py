# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.engines.html5lib import DOM_HTML5LIB
from draftjs_exporter.engines.lxml import DOM_LXML
from draftjs_exporter.engines.string import DOMString


class TestDOMEnginesDifferences(unittest.TestCase):
    def test_html5lib_self_closing_tags(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.create_tag('hr')), '<hr/>')

    def test_lxml_self_closing_tags(self):
        self.assertEqual(DOM_LXML.render_debug(DOM_LXML.create_tag('hr')), '<hr>')

    def test_string_self_closing_tags(self):
        self.assertEqual(DOMString.render_debug(DOMString.create_tag('hr')), '<hr/>')

    def test_html5lib_invalid_attributes(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.create_tag('div', {'*ngFor': 'test'})), '<div *ngFor="test"></div>')

    def test_lxml_invalid_attributes(self):
        with self.assertRaises(ValueError):
            DOM_LXML.render_debug(DOM_LXML.create_tag('div', {'*ngFor': 'test'}))

    def test_string_invalid_attributes(self):
        self.assertEqual(DOMString.render_debug(DOMString.create_tag('div', {'*ngFor': 'test'})), '<div *ngFor="test"></div>')

    def test_html5lib_namespaced_attributes(self):
        bs_elt = DOM_HTML5LIB.create_tag('svg')
        DOM_HTML5LIB.append_child(bs_elt, DOM_HTML5LIB.create_tag('use', {'xlink:href': 'test'}))
        self.assertEqual(DOM_HTML5LIB.render_debug(bs_elt), '<svg><use xlink:href="test"></use></svg>')

    def test_lxml_namespaced_attributes(self):
        lxml_elt = DOM_LXML.create_tag('svg')
        DOM_LXML.append_child(lxml_elt, DOM_LXML.create_tag('use', {'xlink:href': 'test'}))
        self.assertEqual(DOM_LXML.render_debug(lxml_elt), '<svg><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="test"></use></svg>')

    def test_string_namespaced_attributes(self):
        bs_elt = DOMString.create_tag('svg')
        DOMString.append_child(bs_elt, DOMString.create_tag('use', {'xlink:href': 'test'}))
        self.assertEqual(DOMString.render_debug(bs_elt), '<svg><use xlink:href="test"></use></svg>')

    def test_html5lib_html_escaping(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.create_tag('img', {
            'alt': '< " \' < > &',
        })), '<img alt="&lt; &quot; \' &lt; &gt; &amp;"/>')

    def test_lxml_html_escaping(self):
        self.assertEqual(DOM_LXML.render_debug(DOM_LXML.create_tag('img', {
            'alt': '< " \' < > &',
        })), '<img alt="&lt; &quot; \' &lt; &gt; &amp;">')

    def test_string_html_escaping(self):
        self.assertEqual(DOMString.render_debug(DOMString.create_tag('img', {
            'alt': '< " \' < > &',
        })), '<img alt="&lt; &quot; &#x27; &lt; &gt; &amp;"/>')

    def test_html5lib_html_parsing(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.parse_html('<p>Invalid > " &</p>')), '<p>Invalid &gt; " &amp;</p>')

    def test_lxml_html_parsing(self):
        self.assertEqual(DOM_LXML.render_debug(DOM_LXML.parse_html('<p>Invalid > " &</p>')), '<p>Invalid &gt; " &amp;</p>')

    def test_string_html_parsing(self):
        self.assertEqual(DOMString.render_debug(DOMString.parse_html('<p>Invalid > " &</p>')), '<p>Invalid > " &</p>')
