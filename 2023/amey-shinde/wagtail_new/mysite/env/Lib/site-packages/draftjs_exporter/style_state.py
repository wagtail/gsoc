from __future__ import absolute_import, unicode_literals

from draftjs_exporter.constants import INLINE_STYLES
from draftjs_exporter.dom import DOM
from draftjs_exporter.options import Options


class StyleState(object):
    """
    Handles the creation of inline styles on elements.
    Receives inline_style commands, and generates the element's `style`
    attribute from those.
    """
    __slots__ = ('styles', 'style_options')

    def __init__(self, style_options):
        self.styles = []
        self.style_options = style_options

    def apply(self, command):
        if command.name == 'start_inline_style':
            self.styles.append(command.data)
        elif command.name == 'stop_inline_style':
            self.styles.remove(command.data)

    def is_empty(self):
        return not self.styles

    def render_styles(self, decorated_node, block, blocks):
        node = decorated_node
        if not self.is_empty():
            # Nest the tags.
            for style in sorted(self.styles, reverse=True):
                options = Options.get(self.style_options, style, INLINE_STYLES.FALLBACK)
                props = dict(options.props)
                props['block'] = block
                props['blocks'] = blocks
                props['inline_style_range'] = {
                    'style': style,
                }
                node = DOM.create_element(options.element, props, node)

        return node
