# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.utils.module_loading import import_string


class TestModuleLoading(unittest.TestCase):
    """
    Taken from Django:
    https://github.com/django/django/blob/f6bd00131e687aedf2719ad31e84b097562ca5f2/tests/utils_tests/test_module_loading.py#L122-L132
    """
    def test_import_string_success(self):
        cls = import_string('draftjs_exporter.utils.module_loading.import_string')
        self.assertEqual(cls, import_string)

    def test_import_string_invalid(self):
        with self.assertRaises(ImportError):
            import_string('no_dots_in_path')

    def test_import_string_unexistent(self):
        with self.assertRaises(ImportError):
            import_string('tests.utils.unexistent')
