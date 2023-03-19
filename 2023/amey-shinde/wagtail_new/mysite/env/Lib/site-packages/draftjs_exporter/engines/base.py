from __future__ import absolute_import, unicode_literals


class DOMEngine(object):
    """
    Parent class of all DOM implementations.
    """

    @staticmethod
    def create_tag(type_, attr=None):
        """
        Creates and returns a tree node of the given type and attributes.
        """
        raise NotImplementedError

    @staticmethod
    def parse_html(markup):
        """
        Creates nodes based on the input html.
        Note: this method is used in component implementations only, and
        is not required for the exporter to operate.
        """
        raise NotImplementedError

    @staticmethod
    def append_child(elt, child):
        """
        Appends the given child node in the children of elt.
        """
        raise NotImplementedError

    @staticmethod
    def render(elt):
        """
        Renders a given element to HTML.
        """
        raise NotImplementedError

    @staticmethod
    def render_debug(elt):
        """
        Renders a given element to HTML.
        Note: this method is only used for draftjs_exporter's tests, and
        is not required for the exporter to operate.
        """
        raise NotImplementedError
