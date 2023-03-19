from __future__ import absolute_import, unicode_literals

import re
import unittest

from draftjs_exporter.composite_decorators import render_decorators
from draftjs_exporter.constants import BLOCK_TYPES
from draftjs_exporter.dom import DOM
from example import LINKIFY_RE, br, hashtag, linkify

BR_DECORATOR = {
    'strategy': re.compile(r'\n'),
    'component': br,
}

HASHTAG_DECORATOR = {
    'strategy': re.compile(r'#\w+'),
    'component': hashtag,
}

LINKIFY_DECORATOR = {
    'strategy': LINKIFY_RE,
    'component': linkify,
}


class TestLinkify(unittest.TestCase):
    def test_render(self):
        match = next(LINKIFY_DECORATOR['strategy'].finditer('test https://www.example.com'))

        self.assertEqual(DOM.render(DOM.create_element(LINKIFY_DECORATOR['component'], {
            'block': {'type': BLOCK_TYPES.UNSTYLED},
            'match': match,
        }, match.group(0))), '<a href="https://www.example.com">https://www.example.com</a>')

    def test_render_www(self):
        match = next(LINKIFY_DECORATOR['strategy'].finditer('test www.example.com'))

        self.assertEqual(DOM.render(DOM.create_element(LINKIFY_DECORATOR['component'], {
            'block': {'type': BLOCK_TYPES.UNSTYLED},
            'match': match,
        }, match.group(0))), '<a href="http://www.example.com">www.example.com</a>')

    def test_render_code_block(self):
        match = next(LINKIFY_DECORATOR['strategy'].finditer('test https://www.example.com'))

        self.assertEqual(DOM.create_element(LINKIFY_DECORATOR['component'], {
            'block': {'type': BLOCK_TYPES.CODE},
            'match': match,
        }, match.group(0)), match.group(0))


class TestHashtag(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(HASHTAG_DECORATOR['component'], {'block': {'type': BLOCK_TYPES.UNSTYLED}}, '#hashtagtest')), '<span class="hashtag">#hashtagtest</span>')

    def test_render_code_block(self):
        self.assertEqual(DOM.create_element(HASHTAG_DECORATOR['component'], {'block': {'type': BLOCK_TYPES.CODE}}, '#hashtagtest'), '#hashtagtest')


class TestBR(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(BR_DECORATOR['component'], {'block': {'type': BLOCK_TYPES.UNSTYLED}}, '\n')), '<br/>')

    def test_render_code_block(self):
        self.assertEqual(DOM.create_element(BR_DECORATOR['component'], {'block': {'type': BLOCK_TYPES.CODE}}, '\n'), '\n')


class TestCompositeDecorators(unittest.TestCase):
    def test_render_decorators_empty(self):
        self.assertEqual(render_decorators([], 'test https://www.example.com#hash #hashtagtest', {'type': BLOCK_TYPES.UNSTYLED, 'depth': 0}, []), 'test https://www.example.com#hash #hashtagtest')

    def test_render_decorators_single(self):
        self.assertEqual(DOM.render(render_decorators([LINKIFY_DECORATOR], 'test https://www.example.com#hash #hashtagtest', {'type': BLOCK_TYPES.UNSTYLED, 'depth': 0}, [])), 'test <a href="https://www.example.com#hash">https://www.example.com#hash</a> #hashtagtest')

    def test_render_decorators_conflicting_order_one(self):
        self.assertEqual(DOM.render(render_decorators([LINKIFY_DECORATOR, HASHTAG_DECORATOR], 'test https://www.example.com#hash #hashtagtest', {'type': BLOCK_TYPES.UNSTYLED, 'depth': 0}, [])), 'test <a href="https://www.example.com#hash">https://www.example.com#hash</a> <span class="hashtag">#hashtagtest</span>')

    def test_render_decorators_conflicting_order_two(self):
        self.assertEqual(DOM.render(render_decorators([HASHTAG_DECORATOR, LINKIFY_DECORATOR], 'test https://www.example.com#hash #hashtagtest', {'type': BLOCK_TYPES.UNSTYLED, 'depth': 0}, [])), 'test https://www.example.com<span class="hashtag">#hash</span> <span class="hashtag">#hashtagtest</span>')

    def test_render_decorators_data(self):
        blocks = [
            {
                'key': '5s7g9',
                'text': 'test',
                'type': 'unstyled',
                'depth': 0,
                'inlineStyleRanges': [],
                'entityRanges': [],
            },
        ]

        def component(props):
            self.assertEqual(props['blocks'], blocks)
            self.assertEqual(props['block'], blocks[0])
            return None

        render_decorators([
            {
                'strategy': LINKIFY_RE,
                'component': component,
            },
        ], 'test https://www.example.com#hash #hashtagtest', blocks[0], blocks)
