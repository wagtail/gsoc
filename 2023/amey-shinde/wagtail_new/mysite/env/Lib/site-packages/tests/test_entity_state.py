from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.command import Command
from draftjs_exporter.entity_state import EntityException, EntityState
from tests.test_entities import link

entity_decorators = {
    'LINK': link
}

entity_map = {
    '0': {
        'type': 'LINK',
        'mutability': 'MUTABLE',
        'data': {
            'url': 'http://example.com'
        }
    }
}


class TestEntityState(unittest.TestCase):
    def setUp(self):
        self.entity_state = EntityState(entity_decorators, entity_map)

    def test_init(self):
        self.assertIsInstance(self.entity_state, EntityState)

    def test_apply_start_entity(self):
        self.assertEqual(len(self.entity_state.entity_stack), 0)
        self.entity_state.apply(Command('start_entity', 0, 0))
        self.assertEqual(self.entity_state.entity_stack[-1], 0)

    def test_apply_stop_entity(self):
        self.assertEqual(len(self.entity_state.entity_stack), 0)
        self.entity_state.apply(Command('start_entity', 0, 0))
        self.entity_state.apply(Command('stop_entity', 5, 0))
        self.assertEqual(len(self.entity_state.entity_stack), 0)

    def test_apply_raises(self):
        with self.assertRaises(EntityException):
            self.entity_state.apply(Command('start_entity', 0, 0))
            self.entity_state.apply(Command('stop_entity', 0, 1))

    def test_has_no_entity_default(self):
        self.assertEqual(self.entity_state.has_no_entity(), True)

    def test_has_no_entity_styled(self):
        self.entity_state.apply(Command('start_entity', 0, 0))
        self.assertEqual(self.entity_state.has_no_entity(), False)

    def test_get_entity_details(self):
        self.assertEqual(self.entity_state.get_entity_details(0), {
            'data': {
                'url': 'http://example.com'
            },
            'type': 'LINK',
            'mutability': 'MUTABLE',
        })

    def test_get_entity_details_raises(self):
        with self.assertRaises(EntityException):
            self.entity_state.get_entity_details(1)
