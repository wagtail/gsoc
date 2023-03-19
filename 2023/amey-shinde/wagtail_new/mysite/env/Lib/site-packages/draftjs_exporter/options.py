from __future__ import absolute_import, unicode_literals

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
from draftjs_exporter.error import ConfigException


class Options(object):
    """
    Facilitates querying configuration from a config map.
    """
    __slots__ = ('type', 'element', 'props', 'wrapper', 'wrapper_props')


    def __init__(self, type_, element, props=None, wrapper=None, wrapper_props=None):
        self.type = type_
        self.element = element
        self.props = props if props else {}
        self.wrapper = wrapper
        self.wrapper_props = wrapper_props

    def __str__(self):
        return '<Options {0} {1} {2} {3} {4}>'.format(self.type, self.element, self.props, self.wrapper, self.wrapper_props)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Equality used in test code only, not to be relied on for the exporter.
    """
        return str(self) == str(other)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(str(self))

    @staticmethod
    def create(kind_map, type_, fallback_key):
        """
        Create an Options object from any mapping.
        """
        if type_ not in kind_map:
            if fallback_key not in kind_map:
                raise ConfigException('"%s" is not in the config and has no fallback' % type_)

            config = kind_map[fallback_key]
        else:
            config = kind_map[type_]

        if isinstance(config, dict):
            if 'element' not in config:
                raise ConfigException('"%s" does not define an element' % type_)

            opts = Options(type_, **config)
        else:
            opts = Options(type_, config)

        return opts

    @staticmethod
    def map(kind_map, fallback_key):
        options = {}
        for type_ in kind_map:
            options[type_] = Options.create(kind_map, type_, fallback_key)

        return options

    @staticmethod
    def map_blocks(block_map):
        return Options.map(block_map, BLOCK_TYPES.FALLBACK)

    @staticmethod
    def map_styles(style_map):
        return Options.map(style_map, INLINE_STYLES.FALLBACK)

    @staticmethod
    def map_entities(entity_map):
        return Options.map(entity_map, ENTITY_TYPES.FALLBACK)

    @staticmethod
    def get(options, type_, fallback_key):
        try:
            return options[type_]
        except KeyError:
            try:
                return options[fallback_key]
            except KeyError:
                raise ConfigException('"%s" is not in the config and has no fallback' % type_)
