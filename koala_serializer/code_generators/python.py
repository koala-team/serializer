# -*- coding: utf-8 -*-

# project imports
from .python_core import HeaderGenerator, TypeGenerator
from .code_editor import CodeEditor


class PythonCodeGenerator:

    def __init__(self):
        self._code_editor = PythonCodeEditor()
        self._header_generator = HeaderGenerator(self._code_editor)
        self._type_generator = TypeGenerator(self._code_editor)


    def generate(self, parse_tree, module_name):
        self._generate(parse_tree)
        filename = '%s.py' % module_name
        return [(self._code_editor.get_code(), filename)]


    def _generate(self, parse_tree):
        self._header_generator.gen_header()
        for user_defined_type, properties in parse_tree:
            self._type_generator.gen_type(user_defined_type, properties)
            self._code_editor.add_line('\n')



class PythonCodeEditor(CodeEditor):

    pass
