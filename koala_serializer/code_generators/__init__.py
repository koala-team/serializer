# -*- coding: utf-8 -*-

# python imports
import os

# project imports
from .python import PythonCodeGenerator
from .cpp import CppCodeGenerator
from .cs import CsCodeGenerator


class CodeGenerator:

    def __init__(self, source_path, programming_language, destination_dir):
        self._generators = {
            'python': PythonCodeGenerator(),
            'cpp': CppCodeGenerator(),
            'cs': CsCodeGenerator()
        }

        self._module_name = os.path.splitext(os.path.basename(source_path))[0]
        self._programming_language = programming_language
        self._destination_dir = os.path.realpath(destination_dir)


    def generate(self, parse_tree):
        result = self._generators[self._programming_language].generate(parse_tree, self._module_name)
        for code, filename in result:
            with open(os.path.join(self._destination_dir, filename), 'w') as f:
                f.write(code)
