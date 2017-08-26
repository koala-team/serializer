# -*- coding: utf-8 -*-

# project imports
from .cpp_core import HeaderGenerator, FooterGenerator, TypeGenerator


class CppCodeGenerator:

    def __init__(self):
        self._code_editor = CodeEditor()
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



class CodeEditor:

    def __init__(self):
        self._code = ""
        self._global_indent = 0
        self._temp_variable_number = 0


    def get_code(self):
        while self._code[-1] == '\n':
            self._code = self._code[:-1]
        self._code += '\n'
        return self._code


    def add_line(self, text="", local_indent=0):
        local_indent += self._global_indent
        self._code += '\t' * local_indent + text + '\n'


    def add_lines(self, lines, local_indent=0):
        for text in lines:
            self.add_line(text, local_indent)


    def increase_indentation(self, put_accolade=True):
        if put_accolade:
            self.add_line('{')
        self._global_indent += 1


    def decrease_indentation(self, put_accolade=True, add_semi=False):
        self._global_indent -= 1
        if put_accolade:
            semi = ';' if add_semi else ''
            self.add_line('}' + semi)


    def new_tempvar(self):
        var = "tmp%s" % self._temp_variable_number
        self._temp_variable_number += 1
        return var
