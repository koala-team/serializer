# -*- coding: utf-8 -*-

# python imports
import re
import inspect

# project imports
from .parser_core import Patterns, Rules


class RuleParser:

    def __init__(self):
        self._regex_factory = RegexFactory()
        self._current_type = None
        self._user_defined_types = None
        self._rules = Rules(self._regex_factory, self._get_type_tree)
        self._rule_funcs = self._find_rule_funcs()


    def get_type_tree(self, text, current_type, user_defined_types):

        def remove_white_spaces(text):
            return re.sub(
                "(\s*)?([\{\}\[\]\,\<\>\(\)\-])(\s*)?",
                lambda matchobj: matchobj.group(2),
                text
            )

        self._current_type = current_type
        self._user_defined_types = user_defined_types
        clear_text = remove_white_spaces(text)
        tree = self._get_type_tree(clear_text)
        return tree


    def _get_type_tree(self, text):
        for func in self._rule_funcs:
            tree = func(text)
            if tree is not None:
                return tree

        if text in self._user_defined_types and text != self._current_type:
            return (text, )

        raise Exception("error near '%s'" % text)


    def _find_rule_funcs(self):
        funcs = []
        for name, func in inspect.getmembers(self._rules, predicate=inspect.ismethod):
            if name.startswith('_rule_'):
                funcs.append(func)
        return funcs



class RegexFactory:

    def __init__(self):
        self._regex_table = {}
        self._load_patterns()


    def _load_patterns(self):
        for name, pattern in inspect.getmembers(Patterns):
            if not name.startswith('_'):
                self.add(name, pattern)


    def add(self, name, pattern):
        self._regex_table[name] = re.compile(pattern)


    def remove(self, name):
        del self._regex_table[name]


    def get(self, name):
        return self._regex_table[name]


    def match(self, name, text):
        regex = self.get(name)
        return regex.match(text)
