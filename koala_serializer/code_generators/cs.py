# -*- coding: utf-8 -*-

# project imports
from ..parser_core import capitalization_rules
from .cs_core import RootGenerator, HeaderGenerator, FooterGenerator, TypeGenerator
from .cpp import CppCodeEditor


class CsCodeGenerator:

    def __init__(self):
        self._root_code_editor = CsCodeEditor()
        self._root_generator = RootGenerator(self._root_code_editor)

        self._code_editor = CsCodeEditor()
        self._header_generator = HeaderGenerator(self._code_editor)
        self._type_generator = TypeGenerator(self._code_editor)
        self._footer_generator = FooterGenerator(self._code_editor)


    def generate(self, parse_tree, module_name):
        module_name = capitalization_rules['PascalCase'](module_name)
        self._generate_root()
        self._generate(parse_tree, module_name)
        root_filename = 'KSObject.cs'
        filename = '%s.cs' % module_name
        return [
            (self._root_code_editor.get_code(), root_filename),
            (self._code_editor.get_code(), filename)
        ]


    def _generate(self, parse_tree, module_name):
        self._header_generator.gen_header(module_name)
        for user_defined_type, properties in parse_tree:
            self._type_generator.gen_type(user_defined_type, properties)
            if parse_tree.index((user_defined_type, properties)) < len(parse_tree) - 1:
                self._code_editor.add_line()
        self._footer_generator.gen_footer(module_name)


    def _generate_root(self):
        self._root_generator.gen_root()


class CsCodeEditor(CppCodeEditor):

    pass
