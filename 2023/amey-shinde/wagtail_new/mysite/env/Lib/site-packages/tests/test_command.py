from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.command import Command


class TestCommand(unittest.TestCase):
    def setUp(self):
        self.command = Command('abracadabra', 5, 'shazam')

    def test_init(self):
        self.assertIsInstance(self.command, Command)

    def test_str(self):
        self.assertEqual(str(self.command), '<Command abracadabra 5 shazam>')

    def test_lt_true(self):
        self.assertTrue(self.command.__lt__(Command('a', 10, 's')))

    def test_lt_false(self):
        self.assertFalse(self.command.__lt__(Command('a', 0, 's')))

    def test_key(self):
        self.assertEqual(Command.key(self.command), 5)

    def test_start_stop(self):
        self.assertEqual(str(Command.start_stop('abracadabra', 0, 5, 'shazam')), str([
            Command('start_abracadabra', 0, 'shazam'),
            Command('stop_abracadabra', 5, 'shazam'),
        ]))

    def test_from_ranges_empty(self):
        self.assertEqual(str(Command.from_ranges([], 'abracadabra', 'style')), str([]))

    def test_from_ranges_single(self):
        self.assertEqual(str(Command.from_ranges([
            {
                'offset': 0,
                'length': 4,
                'style': 'shazam'
            }
        ], 'abracadabra', 'style')), str([
            Command('start_abracadabra', 0, 'shazam'),
            Command('stop_abracadabra', 4, 'shazam'),
        ]))

    def test_from_ranges_multiple(self):
        self.assertEqual(str(Command.from_ranges([
            {
                'offset': 0,
                'length': 4,
                'style': 'shazam'
            },
            {
                'offset': 9,
                'length': 3,
                'style': 'wazzum'
            }
        ], 'abracadabra', 'style')), str([
            Command('start_abracadabra', 0, 'shazam'),
            Command('stop_abracadabra', 4, 'shazam'),
            Command('start_abracadabra', 9, 'wazzum'),
            Command('stop_abracadabra', 12, 'wazzum'),
        ]))
