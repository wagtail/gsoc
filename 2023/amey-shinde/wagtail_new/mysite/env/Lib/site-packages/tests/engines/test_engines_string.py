# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.engines.string import DOMString


class TestDOMString(unittest.TestCase):
    def test_create_tag(self):
        self.assertEqual(DOMString.render_debug(DOMString.create_tag('p', {'class': 'intro'})), '<p class="intro"></p>')

    def test_create_tag_empty(self):
        self.assertEqual(DOMString.render_debug(DOMString.create_tag('p')), '<p></p>')

    def test_parse_html(self):
        self.assertEqual(DOMString.render(DOMString.parse_html('<p><span>Test text</span></p>')), '<p><span>Test text</span></p>')

    def test_append_child(self):
        parent = DOMString.create_tag('p')
        DOMString.append_child(parent, DOMString.create_tag('span', {}))
        self.assertEqual(DOMString.render_debug(parent), '<p><span></span></p>')

    def test_append_child_identical_text(self):
        parent = DOMString.create_tag('p')
        DOMString.append_child(parent, 'test')
        DOMString.append_child(parent, 'test')
        self.assertEqual(DOMString.render_debug(parent), '<p>testtest</p>')

    def test_append_child_identical_elements(self):
        parent = DOMString.create_tag('p')
        DOMString.append_child(parent, DOMString.create_tag('br'))
        DOMString.append_child(parent, DOMString.create_tag('br'))
        self.assertEqual(DOMString.render_debug(parent), '<p><br/><br/></p>')

    def test_render_attrs(self):
        self.assertEqual(DOMString.render_attrs({
            'src': 'src.png',
            'alt': 'img\'s alt',
            'class': 'intro',
        }), ' alt="img&#x27;s alt" class="intro" src="src.png"')


    def test_render_children(self):
        self.assertEqual(DOMString.render_children([
            'render children',
            DOMString.create_tag('p', {'class': 'intro'}),
            'test test',
        ]), 'render children<p class="intro"></p>test test')

    def test_render(self):
        self.assertEqual(DOMString.render_debug(DOMString.create_tag('p', {'class': 'intro'})), '<p class="intro"></p>')

    def test_render_debug(self):
        self.assertEqual(DOMString.render_debug(DOMString.create_tag('p', {'class': 'intro'})), '<p class="intro"></p>')
