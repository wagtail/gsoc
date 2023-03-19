from __future__ import absolute_import, unicode_literals

import cProfile
import json
import os
import unittest
from pstats import Stats

import six

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES
from draftjs_exporter.defaults import BLOCK_MAP, STYLE_MAP
from draftjs_exporter.dom import DOM
from draftjs_exporter.html import HTML
from tests.test_composite_decorators import BR_DECORATOR, HASHTAG_DECORATOR, LINKIFY_DECORATOR
from tests.test_entities import hr, image, link

fixtures_path = os.path.join(os.path.dirname(__file__), 'test_exports.json')
fixtures = json.loads(open(fixtures_path, 'r').read())

exporter = HTML({
    'entity_decorators': {
        ENTITY_TYPES.LINK: link,
        ENTITY_TYPES.HORIZONTAL_RULE: hr,
        ENTITY_TYPES.IMAGE: image,
        ENTITY_TYPES.EMBED: None,
    },
    'composite_decorators': [
        BR_DECORATOR,
        LINKIFY_DECORATOR,
        HASHTAG_DECORATOR,
    ],
    'block_map': dict(BLOCK_MAP, **{
        BLOCK_TYPES.UNORDERED_LIST_ITEM: {
            'element': 'li',
            'wrapper': 'ul',
            'wrapper_props': {'class': 'bullet-list'},
        },
    }),
    'style_map': dict(STYLE_MAP, **{
        'KBD': 'kbd',
        'HIGHLIGHT': {'element': 'strong', 'props': {'style': {'textDecoration': 'underline'}}},
    }),
})


class TestExportsMeta(type):
    """
    Generates test cases dynamically.
    See http://stackoverflow.com/a/20870875/1798491
    """
    def __new__(mcs, name, bases, tests):
        def gen_test(content, html):
            def test(self):
                self.assertEqual(exporter.render(content), html)

            return test

        engine = name.replace('TestExports', '').lower()

        for export in fixtures:
            test_label = export['label'].lower().replace(' ', '_')
            test_name = 'test_export_{0}_{1}'.format(engine, test_label)
            content = export['content_state']
            html = export['output'][engine]
            tests[test_name] = gen_test(content, html)

        return type.__new__(mcs, name, bases, tests)


class TestExportsHTML5LIB(six.with_metaclass(TestExportsMeta, unittest.TestCase)):
    @classmethod
    def setUpClass(cls):
        DOM.use(DOM.HTML5LIB)
        cls.pr = cProfile.Profile()
        cls.pr.enable()
        print('\nhtml5lib')

    @classmethod
    def tearDownClass(cls):
        cls.pr.disable()
        Stats(cls.pr).strip_dirs().sort_stats('cumulative').print_stats(0)


class TestExportsLXML(six.with_metaclass(TestExportsMeta, unittest.TestCase)):
    @classmethod
    def setUpClass(cls):
        DOM.use(DOM.LXML)
        cls.pr = cProfile.Profile()
        cls.pr.enable()
        print('\nlxml')

    @classmethod
    def tearDownClass(cls):
        cls.pr.disable()
        Stats(cls.pr).strip_dirs().sort_stats('cumulative').print_stats(0)


class TestExportsSTRING(six.with_metaclass(TestExportsMeta, unittest.TestCase)):
    @classmethod
    def setUpClass(cls):
        DOM.use(DOM.STRING)
        cls.pr = cProfile.Profile()
        cls.pr.enable()
        print('\nstring')

    @classmethod
    def tearDownClass(cls):
        cls.pr.disable()
        Stats(cls.pr).strip_dirs().sort_stats('cumulative').print_stats(0)


if __name__ == "__main__":
    unittest.main()
