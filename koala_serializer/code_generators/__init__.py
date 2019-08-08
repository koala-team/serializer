# -*- coding: utf-8 -*-

# python imports
import os
import errno
from copy import deepcopy

# project imports
from ..parser_core import Tokens, capitalization_rules
from .python import PythonCodeGenerator
from .cpp import CppCodeGenerator
from .cs import CsCodeGenerator
from .java import JavaCodeGenerator


class CodeGenerator:

    def __init__(self, source_path, programming_language, destination_dir, capitalization_rule):
        self._generators = {
            'python': PythonCodeGenerator(),
            'cpp': CppCodeGenerator(),
            'cs': CsCodeGenerator(),
            'java': JavaCodeGenerator()
        }

        self._module_name = os.path.splitext(os.path.basename(source_path))[0]
        self._programming_language = programming_language
        self._destination_dir = os.path.realpath(destination_dir)
        self._capitalization_rule = capitalization_rule


    def generate(self, parse_tree):
        parse_tree = self._apply_capitalization_rule(parse_tree)
        result = self._generators[self._programming_language].generate(parse_tree, self._module_name)
        for code, filename in result:
            path = os.path.join(self._destination_dir, filename)
            # os.makedirs(os.path.dirname(path), exist_ok=True)
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            with open(path, 'w') as f:
                f.write(code)


    def _apply_capitalization_rule(self, parse_tree):
        parse_tree = deepcopy(parse_tree)
        for user_defined_type, attribute_trees in parse_tree:
            if attribute_trees['_def'][0] == Tokens.Class:
                new_attr_names = []
                for attr_name in attribute_trees:
                    if attr_name != '_def':
                        new_attr_name = capitalization_rules[self._capitalization_rule](attr_name)
                        new_attr_names.append((attr_name, new_attr_name))
                for attr_name, new_attr_name in new_attr_names:
                    attribute_trees[new_attr_name] = attribute_trees.pop(attr_name)
        return parse_tree
