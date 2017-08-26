# -*- coding: utf-8 -*-

# python imports
import os

# project imports
from .python import PythonCodeGenerator
from .cpp import CppCodeGenerator


class CodeGenerator:

    def __init__(self, source_path, programming_language, destination_dir):
        self._generators = {
            'python': PythonCodeGenerator(),
            'cpp': CppCodeGenerator()
        }

        self._module_name = os.path.splitext(os.path.basename(source_path))[0]
        self._programming_language = programming_language
        self._destination_dir = os.path.realpath(destination_dir)


    def generate(self, parse_tree):
        code, filename = self._generators[self._programming_language].generate(parse_tree, self._module_name)
        with open(os.path.join(self._destination_dir, filename), 'w') as f:
            f.write(code)
