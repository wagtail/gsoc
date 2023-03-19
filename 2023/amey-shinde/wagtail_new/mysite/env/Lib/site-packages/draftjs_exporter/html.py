from __future__ import absolute_import, unicode_literals

from itertools import groupby
from operator import attrgetter

from draftjs_exporter.command import Command
from draftjs_exporter.composite_decorators import render_decorators
from draftjs_exporter.defaults import BLOCK_MAP, STYLE_MAP
from draftjs_exporter.dom import DOM
from draftjs_exporter.entity_state import EntityState
from draftjs_exporter.options import Options
from draftjs_exporter.style_state import StyleState
from draftjs_exporter.wrapper_state import WrapperState


class HTML(object):
    """
    Entry point of the exporter. Combines entity, wrapper and style state
    to generate the right HTML nodes.
    """
    __slots__ = ('composite_decorators', 'has_decorators', 'entity_options', 'block_options', 'style_options')

    def __init__(self, config=None):
        if config is None:
            config = {}

        self.composite_decorators = config.get('composite_decorators', [])
        self.has_decorators = len(self.composite_decorators) > 0

        self.entity_options = Options.map_entities(config.get('entity_decorators', {}))
        self.block_options = Options.map_blocks(config.get('block_map', BLOCK_MAP))
        self.style_options = Options.map_styles(config.get('style_map', STYLE_MAP))

        DOM.use(config.get('engine', DOM.STRING))

    def render(self, content_state=None):
        """
        Starts the export process on a given piece of content state.
        """
        if content_state is None:
            content_state = {}

        blocks = content_state.get('blocks', [])
        wrapper_state = WrapperState(self.block_options, blocks)
        document = DOM.create_element()
        entity_map = content_state.get('entityMap', {})
        min_depth = 0

        for block in blocks:
            # Assume a depth of 0 if it's not specified, like Draft.js would.
            depth = block['depth'] if 'depth' in block else 0
            elt = self.render_block(block, entity_map, wrapper_state)

            if depth > min_depth:
                min_depth = depth

            # At level 0, append the element to the document.
            if depth == 0:
                DOM.append_child(document, elt)

        # If there is no block at depth 0, we need to add the wrapper that contains the whole tree to the document.
        if min_depth > 0 and wrapper_state.stack.length() != 0:
            DOM.append_child(document, wrapper_state.stack.tail().elt)

        return DOM.render(document)

    def render_block(self, block, entity_map, wrapper_state):
        if 'inlineStyleRanges' in block and block['inlineStyleRanges'] or 'entityRanges' in block and block['entityRanges']:
            content = DOM.create_element()
            entity_state = EntityState(self.entity_options, entity_map)
            style_state = StyleState(self.style_options)

            for (text, commands) in self.build_command_groups(block):
                for command in commands:
                    entity_state.apply(command)
                    style_state.apply(command)

                # Decorators are not rendered inside entities.
                if entity_state.has_no_entity() and self.has_decorators:
                    decorated_node = render_decorators(self.composite_decorators, text, block, wrapper_state.blocks)
                else:
                    decorated_node = text

                styled_node = style_state.render_styles(decorated_node, block, wrapper_state.blocks)
                entity_node = entity_state.render_entities(styled_node)

                if entity_node is not None:
                    DOM.append_child(content, entity_node)

                    # Check whether there actually are two different nodes, confirming we are not inserting an upcoming entity.
                    if styled_node != entity_node and entity_state.has_no_entity():
                        DOM.append_child(content, styled_node)
        # Fast track for blocks which do not contain styles nor entities, which is very common.
        elif self.has_decorators:
            content = render_decorators(self.composite_decorators, block['text'], block, wrapper_state.blocks)
        else:
            content = block['text']

        return wrapper_state.element_for(block, content)

    def build_command_groups(self, block):
        """
        Creates block modification commands, grouped by start index,
        with the text to apply them on.
        """
        text = block['text']

        commands = self.build_commands(block)
        grouped = groupby(commands, attrgetter('index'))
        listed = list(groupby(commands, attrgetter('index')))
        sliced = []

        i = 0
        for start_index, commands in grouped:
            if i < len(listed) - 1:
                stop_index = listed[i + 1][0]
                sliced.append((text[start_index:stop_index], list(commands)))
            else:
                sliced.append(('', list(commands)))
            i += 1

        return sliced

    def build_commands(self, block):
        """
        Build all of the manipulation commands for a given block.
        - One pair to set the text.
        - Multiple pairs for styles.
        - Multiple pairs for entities.
        """
        style_commands = self.build_style_commands(block)
        entity_commands = self.build_entity_commands(block)

        return [Command('start_text', 0)] + sorted(style_commands + entity_commands, key=attrgetter('index')) + [Command('stop_text', len(block['text']))]

    def build_style_commands(self, block):
        ranges = block['inlineStyleRanges']
        return Command.from_ranges(ranges, 'inline_style', 'style')

    def build_entity_commands(self, block):
        ranges = block['entityRanges']
        return Command.from_ranges(ranges, 'entity', 'key')
