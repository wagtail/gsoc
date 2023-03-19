# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.engines.html5lib import DOM_HTML5LIB


class TestDOM_HTML5LIB(unittest.TestCase):
    def test_create_tag(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.create_tag('p', {'class': 'intro'})), '<p class="intro"></p>')

    def test_create_tag_empty(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.create_tag('p')), '<p></p>')

    def test_parse_html(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.parse_html('<p><span>Test text</span></p>')), '<p><span>Test text</span></p>')

    def test_append_child(self):
        parent = DOM_HTML5LIB.create_tag('p')
        DOM_HTML5LIB.append_child(parent, DOM_HTML5LIB.create_tag('span', {}))
        self.assertEqual(DOM_HTML5LIB.render_debug(parent), '<p><span></span></p>')

    def test_render(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.create_tag('p', {'class': 'intro'})), '<p class="intro"></p>')

    def test_render_debug(self):
        self.assertEqual(DOM_HTML5LIB.render_debug(DOM_HTML5LIB.create_tag('p', {'class': 'intro'})), '<p class="intro"></p>')
