from __future__ import absolute_import, unicode_literals


class Command(object):
    """
    A Command represents an operation that has to be executed
    on a block for it to be converted into an arbitrary number
    of HTML nodes.
    """
    __slots__ = ('name', 'index', 'data')

    def __init__(self, name, index, data=''):
        self.name = name
        self.index = index
        self.data = data

    def __str__(self):
        return '<Command {0} {1} {2}>'.format(self.name, self.index, self.data)

    def __repr__(self):
        return str(self)

    @staticmethod
    def start_stop(name, start, stop, data=''):
        """
        Builds a pair of start/stop commands with the same data.
        """
        return (
            Command('start_%s' % name, start, data),
            Command('stop_%s' % name, stop, data),
        )

    @staticmethod
    def from_ranges(ranges, name, data_key, start_key='offset', length_key='length'):
        """
        Creates a list of commands from a list of ranges. Each range
        is converted to two commands: a start_* and a stop_*.
        """
        commands = []
        for r in ranges:
            data = r[data_key]
            start = r[start_key]
            stop = start + r[length_key]
            commands.extend(Command.start_stop(name, start, stop, data))
        return commands
