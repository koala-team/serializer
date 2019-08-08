# -*- coding: utf-8 -*-

# python imports
import os

# project imports
from ..parser_core import capitalization_rules
from .java_core import RootGenerator, HeaderGenerator, FooterGenerator, TypeGenerator
from .cpp import CppCodeEditor


class JavaCodeGenerator:

    def __init__(self):
        self._root_code_editor = JavaCodeEditor()
        self._root_generator = RootGenerator(self._root_code_editor)

        self._code_editor = JavaCodeEditor()
        self._header_generator = HeaderGenerator(self._code_editor)
        self._type_generator = TypeGenerator(self._code_editor)
        self._footer_generator = FooterGenerator(self._code_editor)

        self._generated_result = []


    def generate(self, parse_tree, module_name):
        result = []
        result += self._generate_root()
        result += self._generate(parse_tree, module_name)
        return result


    def _generate(self, parse_tree, module_name):
        result = []

        for user_defined_type, properties in parse_tree:
            self._header_generator.gen_header(module_name)
            self._type_generator.gen_type(user_defined_type, properties)
            self._footer_generator.gen_footer(module_name)

            code = self._code_editor.get_code()
            dirname = os.path.join('ks', module_name)
            filename = '%s.java' % capitalization_rules['PascalCase'](user_defined_type)
            result.append((code, os.path.join(dirname, filename)))
            self._code_editor.clear()

        return result


    def _generate_root(self):
        self._root_generator.gen_root()
        return [(self._root_code_editor.get_code(), 'ks/KSObject.java')]



class JavaCodeEditor(CppCodeEditor):

    pass
