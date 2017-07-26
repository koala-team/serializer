# -*- coding: utf-8 -*-

# project imports
from .python_core import HeaderGenerator, TypeGenerator


class PythonCodeGenerator:

    def __init__(self):
        self._code_editor = CodeEditor()
        self._header_generator = HeaderGenerator(self._code_editor)
        self._type_generator = TypeGenerator(self._code_editor)


    def generate(self, parse_tree, module_name):
        self._generate(parse_tree)
        filename = '%s.py' % module_name
        return self._code_editor.get_code(), filename


    def _generate(self, parse_tree):
        self._header_generator.gen_header()
        for user_defined_type, properties in parse_tree:
            self._type_generator.gen_type(user_defined_type, properties)
            self._code_editor.add_line('\n')



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


    def increase_indentation(self, count=1):
        self._global_indent += count


    def decrease_indentation(self, count=1):
        self._global_indent -= count


    def new_tempvar(self):
        var = "tmp%s" % self._temp_variable_number
        self._temp_variable_number += 1
        return var
