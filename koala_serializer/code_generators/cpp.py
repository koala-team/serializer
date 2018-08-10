# -*- coding: utf-8 -*-

# project imports
from .cpp_core import HeaderGenerator, FooterGenerator, TypeGenerator
from .code_editor import CodeEditor


class CppCodeGenerator:

    def __init__(self):
        self._code_editor = CppCodeEditor()
        self._header_generator = HeaderGenerator(self._code_editor)
        self._type_generator = TypeGenerator(self._code_editor)
        self._footer_generator = FooterGenerator(self._code_editor)


    def generate(self, parse_tree, module_name):
        self._generate(parse_tree, module_name)
        filename = '%s.h' % module_name
        return self._code_editor.get_code(), filename


    def _generate(self, parse_tree, module_name):
        self._header_generator.gen_header(module_name)
        for user_defined_type, properties in parse_tree:
            self._type_generator.gen_type(user_defined_type, properties)
            self._code_editor.add_line()
            if parse_tree.index((user_defined_type, properties)) < len(parse_tree) - 1:
                self._code_editor.add_line()
        self._footer_generator.gen_footer(module_name)



class CppCodeEditor(CodeEditor):

    def increase_indentation(self, put_accolade=True):
        if put_accolade:
            self.add_line('{')
        super(CppCodeEditor, self).increase_indentation()


    def decrease_indentation(self, put_accolade=True, add_semi=False):
        super(CppCodeEditor, self).decrease_indentation()
        if put_accolade:
            semi = ';' if add_semi else ''
            self.add_line('}' + semi)
