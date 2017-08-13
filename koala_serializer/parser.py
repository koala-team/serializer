# -*- coding: utf-8 -*-

# python imports
import configparser
from collections import OrderedDict

# project imports
from .rule_parser import RuleParser


class Parser:

    def __init__(self, source_path):
        self._src = configparser.ConfigParser()
        self._src.optionxform = str
        with open(source_path) as f:
            self._src.readfp(f)

        self._rule_parser = RuleParser()
        self._parse_tree = self._parse()


    def parse_tree(self):
        return self._parse_tree


    def _parse(self):
        src = self._src
        parse_tree = []

        user_defined_types = src.sections()
        for udt in user_defined_types:
            attr_trees = OrderedDict()
            for attr, type in src.items(udt):
                attr_trees[attr] = self._rule_parser.get_type_tree(type, udt, user_defined_types)
            parse_tree.append((udt, attr_trees))

        return parse_tree
