from parsimonious.grammar import Grammar

from .html_path_reader import read_html_path, grammar_text as html_path_grammar, read_html_path_node
from .document_matcher_reader import read_document_matcher, grammar_text as document_matcher_grammar, read_document_matcher_node
from ..styles import Style


__all__ = ["read_style", "read_html_path", "read_document_matcher"]


def read_style(string):
    style_node = _grammar.parse(string)
    return _read_style_node(style_node)


def _read_style_node(style_node):
    document_matcher_node = style_node.children[0]
    html_path_node = style_node.children[4]
    
    document_matcher = read_document_matcher_node(document_matcher_node)
    html_path = read_html_path_node(html_path_node)
    
    return Style(document_matcher, html_path)
    


_grammar = Grammar("""
style = document_matcher whitespace "=>" whitespace html_path
""" + html_path_grammar + document_matcher_grammar
)
