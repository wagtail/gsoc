from __future__ import absolute_import, unicode_literals

from operator import itemgetter
from draftjs_exporter.dom import DOM


def get_decorations(decorators, text):
    occupied = {}
    decorations = []

    for decorator in decorators:
        for match in decorator['strategy'].finditer(text):
            begin, end = match.span()
            if not any(occupied.get(i) for i in range(begin, end)):
                for i in range(begin, end):
                    occupied[i] = 1
                decorations.append((begin, end, match, decorator))

    decorations.sort(key=itemgetter(0))

    return decorations


def apply_decorators(decorators, text, block, blocks):
    decorations = get_decorations(decorators, text)

    pointer = 0
    for begin, end, match, decorator in decorations:
        if pointer < begin:
            yield text[pointer:begin]

        yield DOM.create_element(decorator['component'], {
            'match': match,
            'block': block,
            'blocks': blocks,
        }, match.group(0))
        pointer = end

    if pointer < len(text):
        yield text[pointer:]


def render_decorators(decorators, text, block, blocks):
    decorated_children = list(apply_decorators(decorators, text, block, blocks))

    if len(decorated_children) == 1:
        decorated_node = decorated_children[0]
    else:
        decorated_node = DOM.create_element()
        for decorated_child in decorated_children:
            DOM.append_child(decorated_node, decorated_child)

    return decorated_node
