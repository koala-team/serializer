# -*- coding: utf-8 -*-

# project imports
from .parser import Parser
from .code_generators import CodeGenerator


def generate(source_path, programming_language, destination_dir, capitalization_rule):
    parser = Parser(source_path)
    code_generator = CodeGenerator(source_path, programming_language, destination_dir, capitalization_rule)
    code_generator.generate(parser.parse_tree())
