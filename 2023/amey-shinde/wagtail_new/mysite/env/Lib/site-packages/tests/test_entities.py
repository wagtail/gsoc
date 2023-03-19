from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.dom import DOM


def hr(props):
    return DOM.create_element('hr')


def link(props):
    attributes = {}
    for key in props:
        attr = key if key != 'url' else 'href'
        attributes[attr] = props[key]

    return DOM.create_element('a', attributes, props['children'])


def image(props):
    return DOM.create_element('img', {
        'src': props.get('src'),
        'width': props.get('width'),
        'height': props.get('height'),
        'alt': props.get('alt'),
    })


def icon(props):
    href = '#icon-%s' % props.get('name', '')
    return DOM.create_element('svg', {'class': 'icon'}, DOM.create_element('use', {'xlink:href': href}))


def button(props):
    href = props.get('href', '#')
    icon_name = props.get('icon', None)
    text = props.get('text', '')

    return DOM.create_element(
        'a',
        {'class': 'icon-text' if icon_name else None, 'href': href},
        DOM.create_element(icon, {'name': icon_name}) if icon_name else None,
        DOM.create_element('span', {'class': 'icon-text__text'}, text) if icon_name else text
    )


class TestIcon(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(icon, {'name': 'rocket'})), '<svg class="icon"><use xlink:href="#icon-rocket"></use></svg>')


class TestImage(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(image, {
            'src': 'http://example.com/example.png',
            'width': 320,
            'height': 580,
        })), '<img height="580" src="http://example.com/example.png" width="320"/>')


class TestLink(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(link, {
            'url': 'http://example.com',
        }, 'wow')), '<a href="http://example.com">wow</a>')


class TestButton(unittest.TestCase):
    def test_render_with_icon(self):
        self.assertEqual(DOM.render(DOM.create_element(button, {
            'href': 'http://example.com',
            'icon': 'rocket',
            'text': 'Launch',
        })), '<a class="icon-text" href="http://example.com"><svg class="icon"><use xlink:href="#icon-rocket"></use></svg><span class="icon-text__text">Launch</span></a>')

    def test_render_without_icon(self):
        self.assertEqual(DOM.render(DOM.create_element(button, {
            'href': 'http://example.com',
            'text': 'Launch',
        })), '<a href="http://example.com">Launch</a>')
