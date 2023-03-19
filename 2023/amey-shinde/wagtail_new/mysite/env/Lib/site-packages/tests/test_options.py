from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.error import ConfigException
from draftjs_exporter.options import Options


class TestOptions(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Options('unordered-list-item', 'li')), '<Options unordered-list-item li {} None None>')

    def test_eq(self):
        self.assertEqual(Options('unordered-list-item', 'li'), Options('unordered-list-item', 'li'))

    def test_not_eq(self):
        self.assertNotEqual(Options('unordered-list-item', 'li'), Options('unordered-list-item', 'p'))

    def test_for_block_full(self):
        self.assertEqual(Options.for_block({'unordered-list-item': 'li'}, 'unordered-list-item'), Options('unordered-list-item', 'li'))

    def test_for_block_half(self):
        self.assertEqual(Options.for_block({'unordered-list-item': 'li'}, 'unordered-list-item'), Options('unordered-list-item', 'li'))

    def test_for_block_simplest(self):
        self.assertEqual(Options.for_block({'unordered-list-item': 'li'}, 'unordered-list-item'), Options('unordered-list-item', 'li'))

    def test_for_block_uses_fallback(self):
        self.assertEqual(Options.for_block({'header-one': 'h1', 'fallback': 'div'}, 'header-two'), Options('header-two', 'div'))

    def test_for_block_raises_missing_type(self):
        with self.assertRaises(ConfigException):
            Options.for_block({'header-one': 'h1'}, 'header-two')

    def test_for_block_raises_missing_element(self):
        with self.assertRaises(ConfigException):
            Options.for_block({'header-one': {}}, 'header-one')

    def test_for_style_full(self):
        self.assertEqual(Options.for_style({'ITALIC': 'em'}, 'ITALIC'), Options('ITALIC', 'em'))

    def test_for_style_half(self):
        self.assertEqual(Options.for_style({'ITALIC': 'em'}, 'ITALIC'), Options('ITALIC', 'em'))

    def test_for_style_simplest(self):
        self.assertEqual(Options.for_style({'ITALIC': 'em'}, 'ITALIC'), Options('ITALIC', 'em'))

    def test_for_style_uses_fallback(self):
        self.assertEqual(Options.for_style({'BOLD': 'strong', 'FALLBACK': 'span'}, 'CODE'), Options('CODE', 'span'))

    def test_for_style_raises_missing_type(self):
        with self.assertRaises(ConfigException):
            Options.for_style({'BOLD': 'strong'}, 'CODE')

    def test_for_style_raises_missing_element(self):
        with self.assertRaises(ConfigException):
            Options.for_style({'BOLD': {}}, 'BOLD')

    def test_for_entity_full(self):
        self.assertEqual(Options.for_entity({'HORIZONTAL_RULE': 'hr'}, 'HORIZONTAL_RULE'), Options('HORIZONTAL_RULE', 'hr'))

    def test_for_entity_half(self):
        self.assertEqual(Options.for_entity({'HORIZONTAL_RULE': 'hr'}, 'HORIZONTAL_RULE'), Options('HORIZONTAL_RULE', 'hr'))

    def test_for_entity_simplest(self):
        self.assertEqual(Options.for_entity({'HORIZONTAL_RULE': 'hr'}, 'HORIZONTAL_RULE'), Options('HORIZONTAL_RULE', 'hr'))

    def test_for_entity_uses_fallback(self):
        self.assertEqual(Options.for_entity({'HORIZONTAL_RULE': 'hr', 'FALLBACK': 'div'}, 'TEST'), Options('TEST', 'div'))

    def test_for_entity_raises_missing_type(self):
        with self.assertRaises(ConfigException):
            Options.for_entity({'HORIZONTAL_RULE': 'hr'}, 'TEST')

    def test_for_entity_raises_missing_element(self):
        with self.assertRaises(ConfigException):
            Options.for_entity({'HORIZONTAL_RULE': {}}, 'HORIZONTAL_RULE')
