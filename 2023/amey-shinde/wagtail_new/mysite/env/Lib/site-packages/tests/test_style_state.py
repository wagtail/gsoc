# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.command import Command
from draftjs_exporter.dom import DOM
from draftjs_exporter.style_state import StyleState

Important = lambda props: DOM.create_element('strong', {'style': {'color': 'red'}}, props['children'])


def Shout(props):
    return DOM.create_element('span', {'style': {'textTransform': 'uppercase'}}, props['children'])


style_map = {
    'ITALIC': 'em',
    'BOLD': 'strong',
    'HIGHLIGHT': {
        'element': 'strong',
        'props': {'style': {'textDecoration': 'underline'}},
    },
    'KBD': {
        'element': 'kbd',
        'props': {'class': 'o-keyboard-shortcut'}
    },
    'IMPORTANT': Important,
    'SHOUT': Shout,
}


class TestStyleState(unittest.TestCase):
    def setUp(self):
        DOM.use(DOM.STRING)
        self.style_state = StyleState(style_map)

    def test_init(self):
        self.assertIsInstance(self.style_state, StyleState)

    def test_apply_start_inline_style(self):
        self.style_state.apply(Command('start_inline_style', 0, 'ITALIC'))
        self.assertEqual(self.style_state.styles, ['ITALIC'])

    def test_apply_stop_inline_style(self):
        self.style_state.apply(Command('start_inline_style', 0, 'ITALIC'))
        self.style_state.apply(Command('stop_inline_style', 0, 'ITALIC'))
        self.assertEqual(self.style_state.styles, [])

    def test_is_empty_default(self):
        self.assertEqual(self.style_state.is_empty(), True)

    def test_is_empty_styled(self):
        self.style_state.apply(Command('start_inline_style', 0, 'ITALIC'))
        self.assertEqual(self.style_state.is_empty(), False)

    def test_render_styles_unstyled(self):
        self.assertEqual(self.style_state.render_styles('Test text', {}, []), 'Test text')

    def test_render_styles_unicode(self):
        self.assertEqual(self.style_state.render_styles('🍺', {}, []), '🍺')

    def test_render_styles_styled(self):
        self.style_state.apply(Command('start_inline_style', 0, 'ITALIC'))
        self.assertEqual(DOM.render_debug(self.style_state.render_styles('Test text', {}, [])), '<em>Test text</em>')
        self.style_state.apply(Command('stop_inline_style', 9, 'ITALIC'))

    def test_render_styles_styled_multiple(self):
        self.style_state.apply(Command('start_inline_style', 0, 'BOLD'))
        self.style_state.apply(Command('start_inline_style', 0, 'ITALIC'))
        self.assertEqual(DOM.render_debug(self.style_state.render_styles('Test text', {}, [])), '<strong><em>Test text</em></strong>')

    def test_render_styles_attributes(self):
        self.style_state.apply(Command('start_inline_style', 0, 'KBD'))
        self.assertEqual(DOM.render_debug(self.style_state.render_styles('Test text', {}, [])), '<kbd class="o-keyboard-shortcut">Test text</kbd>')
        self.style_state.apply(Command('stop_inline_style', 9, 'KBD'))

    def test_render_styles_component(self):
        self.style_state.apply(Command('start_inline_style', 0, 'IMPORTANT'))
        self.assertEqual(DOM.render_debug(self.style_state.render_styles('Test text', {}, [])), '<strong style="color: red;">Test text</strong>')
        self.style_state.apply(Command('stop_inline_style', 9, 'IMPORTANT'))

    def test_render_styles_component_multiple(self):
        self.style_state.apply(Command('start_inline_style', 0, 'IMPORTANT'))
        self.style_state.apply(Command('start_inline_style', 0, 'SHOUT'))
        self.assertEqual(DOM.render_debug(self.style_state.render_styles('Test text', {}, [])), '<strong style="color: red;"><span style="text-transform: uppercase;">Test text</span></strong>')
        self.style_state.apply(Command('stop_inline_style', 9, 'IMPORTANT'))
        self.style_state.apply(Command('stop_inline_style', 9, 'SHOUT'))

    def test_render_styles_component_multiple_invert(self):
        self.style_state.apply(Command('start_inline_style', 0, 'SHOUT'))
        self.style_state.apply(Command('start_inline_style', 0, 'IMPORTANT'))
        self.assertEqual(DOM.render_debug(self.style_state.render_styles('Test text', {}, [])), '<strong style="color: red;"><span style="text-transform: uppercase;">Test text</span></strong>')
        self.style_state.apply(Command('stop_inline_style', 9, 'SHOUT'))
        self.style_state.apply(Command('stop_inline_style', 9, 'IMPORTANT'))

    def test_render_styles_data(self):
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
            self.assertEqual(props['inline_style_range']['style'], 'ITALIC')
            return None

        style_state = StyleState({
            'ITALIC': component,
        })

        style_state.apply(Command('start_inline_style', 0, 'ITALIC'))
        style_state.render_styles('Test text', blocks[0], blocks)
        style_state.apply(Command('stop_inline_style', 9, 'ITALIC'))
