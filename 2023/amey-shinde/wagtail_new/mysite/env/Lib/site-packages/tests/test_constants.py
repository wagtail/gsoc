from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES, Enum


class EnumConstants(unittest.TestCase):
    def test_enum_returns_the_key_if_valid(self):
        foo_value = 'foo'
        e = Enum(foo_value)

        self.assertEqual(e.foo, foo_value)

    def test_enum_raises_an_error_for_invalid_keys(self):
        e = Enum('foo', 'bar')

        with self.assertRaises(AttributeError):
            e.invalid_key


class TestConstants(unittest.TestCase):
    def test_block_types(self):
        self.assertIsInstance(BLOCK_TYPES, object)
        self.assertEqual(BLOCK_TYPES.UNSTYLED, 'unstyled')

    def test_entity_types(self):
        self.assertIsInstance(ENTITY_TYPES, object)
        self.assertEqual(ENTITY_TYPES.LINK, 'LINK')

    def test_inline_styles(self):
        self.assertIsInstance(INLINE_STYLES, object)
        self.assertEqual(INLINE_STYLES.BOLD, 'BOLD')
