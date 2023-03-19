from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.command import Command
from draftjs_exporter.dom import DOM
from draftjs_exporter.engines.string import DOMString
from draftjs_exporter.html import HTML

config = {
    'entity_decorators': {},
    'block_map': {
        'header-one': {'element': 'h1'},
        'unordered-list-item': {
            'element': 'li',
            'wrapper': ['ul', {'class': 'public-DraftStyleDefault-ul'}]
        },
        'unstyled': {'element': 'p'}
    },
    'style_map': {
        'ITALIC': {'element': 'em'},
        'BOLD': {'element': 'strong'}
    }
}


class TestHTML(unittest.TestCase):
    def setUp(self):
        self.exporter = HTML(config)

    def test_init(self):
        self.assertIsInstance(self.exporter, HTML)

    def test_init_dom_engine_default(self):
        HTML()
        self.assertEqual(DOM.dom, DOMString)

    def test_render_block_exists(self):
        self.assertTrue('render_block' in dir(self.exporter))

    def test_build_style_commands_empty(self):
        self.assertEqual(str(self.exporter.build_style_commands({
            'key': '5s7g9',
            'text': 'Header',
            'type': 'header-one',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        })), str([]))

    def test_build_style_commands_single(self):
        self.assertEqual(str(self.exporter.build_style_commands({
            'key': '5s7g9',
            'text': 'Header',
            'type': 'header-one',
            'depth': 0,
            'inlineStyleRanges': [
                {
                    'offset': 0,
                    'length': 4,
                    'style': 'ITALIC'
                }
            ],
            'entityRanges': []
        })), str([
            Command('start_inline_style', 0, 'ITALIC'),
            Command('stop_inline_style', 4, 'ITALIC'),
        ]))

    def test_build_style_commands_multiple(self):
        self.assertEqual(str(self.exporter.build_style_commands({
            'key': '5s7g9',
            'text': 'Header',
            'type': 'header-one',
            'depth': 0,
            'inlineStyleRanges': [
                {
                    'offset': 0,
                    'length': 4,
                    'style': 'ITALIC'
                },
                {
                    'offset': 9,
                    'length': 3,
                    'style': 'BOLD'
                }
            ],
            'entityRanges': []
        })), str([
            Command('start_inline_style', 0, 'ITALIC'),
            Command('stop_inline_style', 4, 'ITALIC'),
            Command('start_inline_style', 9, 'BOLD'),
            Command('stop_inline_style', 12, 'BOLD'),
        ]))

    def test_build_entity_commands_empty(self):
        self.assertEqual(str(self.exporter.build_entity_commands({
            'key': 'dem5p',
            'text': 'some paragraph text',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        })), str([]))

    def test_build_entity_commands_single(self):
        self.assertEqual(str(self.exporter.build_entity_commands({
            'key': 'dem5p',
            'text': 'some paragraph text',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': [
                {
                    'offset': 5,
                    'length': 9,
                    'key': 0
                }
            ]
        })), str([
            Command('start_entity', 5, 0),
            Command('stop_entity', 14, 0),
        ]))

    def test_build_entity_commands_multiple(self):
        self.assertEqual(str(self.exporter.build_entity_commands({
            'key': 'dem5p',
            'text': 'some paragraph text',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': [
                {
                    'offset': 5,
                    'length': 9,
                    'key': 0
                },
                {
                    'offset': 0,
                    'length': 4,
                    'key': 1
                }
            ]
        })), str([
            Command('start_entity', 5, 0),
            Command('stop_entity', 14, 0),
            Command('start_entity', 0, 1),
            Command('stop_entity', 4, 1),
        ]))

    def test_build_commands_empty(self):
        self.assertEqual(str(self.exporter.build_commands({
            'key': 'dem5p',
            'text': 'some paragraph text',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        })), str([
            Command('start_text', 0),
            Command('stop_text', 19),
        ]))

    def test_build_commands_multiple(self):
        self.assertEqual(str(self.exporter.build_commands({
            'key': 'dem5p',
            'text': 'some paragraph text',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [
                {
                    'offset': 0,
                    'length': 4,
                    'style': 'ITALIC'
                },
                {
                    'offset': 9,
                    'length': 3,
                    'style': 'BOLD'
                }
            ],
            'entityRanges': [
                {
                    'offset': 5,
                    'length': 9,
                    'key': 0
                },
                {
                    'offset': 0,
                    'length': 4,
                    'key': 1
                }
            ]
        })), str([
            Command('start_text', 0),
            Command('start_inline_style', 0, 'ITALIC'),
            Command('start_entity', 0, 1),
            Command('stop_inline_style', 4, 'ITALIC'),
            Command('stop_entity', 4, 1),
            Command('start_entity', 5, 0),
            Command('start_inline_style', 9, 'BOLD'),
            Command('stop_inline_style', 12, 'BOLD'),
            Command('stop_entity', 14, 0),
            Command('stop_text', 19),
        ]))

    def test_build_command_groups_empty(self):
        self.assertEqual(str(self.exporter.build_command_groups({
            'key': 'dem5p',
            'text': 'some paragraph text',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        })), str([
            ('some paragraph text', [
                Command('start_text', 0),
            ]),
            ('', [
                Command('stop_text', 19),
            ])
        ]))

    def test_build_command_groups_multiple(self):
        self.assertEqual(str(self.exporter.build_command_groups({
            'key': 'dem5p',
            'text': 'some paragraph text',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [
                {
                    'offset': 0,
                    'length': 4,
                    'style': 'ITALIC'
                },
                {
                    'offset': 9,
                    'length': 3,
                    'style': 'BOLD'
                }
            ],
            'entityRanges': [
                {
                    'offset': 5,
                    'length': 9,
                    'key': 0
                },
                {
                    'offset': 0,
                    'length': 4,
                    'key': 1
                }
            ]
        })), str([
            ('some', [
                Command('start_text', 0),
                Command('start_inline_style', 0, 'ITALIC'),
                Command('start_entity', 0, 1),
            ]),
            (' ', [
                Command('stop_inline_style', 4, 'ITALIC'),
                Command('stop_entity', 4, 1),
            ]),
            ('para', [
                Command('start_entity', 5, 0),
            ]),
            ('gra', [
                Command('start_inline_style', 9, 'BOLD'),
            ]),
            ('ph', [
                Command('stop_inline_style', 12, 'BOLD'),
            ]),
            (' text', [
                Command('stop_entity', 14, 0),
            ]),
            ('', [
                Command('stop_text', 19),
            ])
        ]))

    def test_render(self):
        self.assertEqual(self.exporter.render({
            'entityMap': {},
            'blocks': [
                {
                    'key': '5s7g9',
                    'text': 'Header',
                    'type': 'header-one',
                    'depth': 0,
                    'inlineStyleRanges': [],
                    'entityRanges': []
                },
            ]
        }), '<h1>Header</h1>')

    def test_render_block_defaults(self):
        self.assertEqual(self.exporter.render({
            'entityMap': {},
            'blocks': [
                {
                    'text': 'Paragraph',
                },
            ]
        }), '<p>Paragraph</p>')

    def test_render_empty(self):
        self.assertEqual(self.exporter.render({
            'entityMap': {},
            'blocks': [
            ]
        }), '')

    def test_render_none(self):
        self.assertEqual(self.exporter.render(None), '')

    def test_render_twice(self):
        """Asserts no state is kept during renders."""
        self.assertEqual(self.exporter.render({
            'entityMap': {},
            'blocks': [
                {
                    'key': '5s7g9',
                    'text': 'Header',
                    'type': 'header-one',
                    'depth': 0,
                    'inlineStyleRanges': [],
                    'entityRanges': []
                },
            ]
        }), '<h1>Header</h1>')
        self.assertEqual(self.exporter.render({
            'entityMap': {},
            'blocks': [
                {
                    'key': '5s7g9',
                    'text': 'Header',
                    'type': 'header-one',
                    'depth': 0,
                    'inlineStyleRanges': [],
                    'entityRanges': []
                },
            ]
        }), '<h1>Header</h1>')
