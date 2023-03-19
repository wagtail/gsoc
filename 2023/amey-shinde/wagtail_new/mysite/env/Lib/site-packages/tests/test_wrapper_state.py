from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.dom import DOM
from draftjs_exporter.wrapper_state import WrapperState
from example import blockquote, list_item, ordered_list


class TestWrapperState(unittest.TestCase):
    def setUp(self):
        DOM.use(DOM.STRING)

        self.wrapper_state = WrapperState({
            'header-one': 'h1',
            'unstyled': 'div',
            'atomic': lambda props: props['children'],
            'ignore': None,
            'blockquote': blockquote,
            'ordered-list-item': {
                'element': list_item,
                'wrapper': ordered_list
            },
        }, [])

    def test_init(self):
        self.assertIsInstance(self.wrapper_state, WrapperState)

    def test_element_for_data(self):
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

        def unstyled(props):
            self.assertEqual(props['blocks'], blocks)
            self.assertEqual(props['block'], blocks[0])

        WrapperState({'unstyled': unstyled}, blocks).element_for(blocks[0], 'test')

    def test_element_for_simple_content(self):
        self.assertEqual(DOM.render_debug(self.wrapper_state.element_for({
            'key': '5s7g9',
            'text': 'Header',
            'type': 'header-one',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        }, 'Header')), '<h1>Header</h1>')

    def test_element_for_element_content(self):
        self.assertEqual(DOM.render_debug(self.wrapper_state.element_for({
            'key': '5s7g9',
            'text': 'Paragraph',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        }, DOM.create_element('strong', {}, 'Paragraph'))), '<div><strong>Paragraph</strong></div>')

    def test_element_for_dismiss_content(self):
        self.assertEqual(DOM.render_debug(self.wrapper_state.element_for({
            'key': '5s7g9',
            'text': 'Paragraph',
            'type': 'ignore',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        }, DOM.create_element('img', {'src': '/example.png'}))), '<fragment></fragment>')

    def test_element_for_no_block(self):
        self.assertEqual(DOM.render_debug(self.wrapper_state.element_for({
            'key': '5s7g9',
            'text': 'Paragraph',
            'type': 'atomic',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        }, DOM.create_element('img', {'src': '/example.png'}))), '<img src="/example.png"/>')

    def test_element_for_component(self):
        self.assertEqual(DOM.render_debug(self.wrapper_state.element_for({
            'key': '5s7g9',
            'text': 'Paragraph',
            'type': 'blockquote',
            'depth': 0,
            'data': {
                'cite': 'http://example.com/',
            },
            'inlineStyleRanges': [],
            'entityRanges': []
        }, 'Test')), '<blockquote cite="http://example.com/">Test</blockquote>')

    def test_element_for_component_wrapper(self):
        self.assertEqual(DOM.render_debug(self.wrapper_state.element_for({
            'key': '5s7g9',
            'text': 'Test',
            'type': 'ordered-list-item',
            'depth': 0,
            'data': {},
            'inlineStyleRanges': [],
            'entityRanges': []
        }, 'Test')), '<ol class="list--depth-0"><li class="list-item--depth-0">Test</li></ol>')

    def test_str_elts(self):
        self.assertEqual(DOM.render_debug(self.wrapper_state.element_for({
            'key': '5s7g9',
            'text': 'Header',
            'type': 'header-one',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        }, '')), '<h1></h1>')

    def test_str(self):
        self.assertEqual(str(self.wrapper_state), '<WrapperState: []>')


class TestBlockquote(unittest.TestCase):
    def setUp(self):
        DOM.use(DOM.STRING)

    def test_render_debug(self):
        self.assertEqual(DOM.render_debug(DOM.create_element(blockquote, {
            'block': {
                'data': {
                    'cite': 'http://example.com/',
                },
            },
        }, 'Test')), '<blockquote cite="http://example.com/">Test</blockquote>')


class TestListItem(unittest.TestCase):
    def setUp(self):
        DOM.use(DOM.STRING)

    def test_render_debug(self):
        self.assertEqual(DOM.render_debug(DOM.create_element(list_item, {
            'block': {
                'depth': 5,
            },
        }, 'Test')), '<li class="list-item--depth-5">Test</li>')
