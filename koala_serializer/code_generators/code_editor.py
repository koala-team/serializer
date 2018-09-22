# -*- coding: utf-8 -*-


class CodeEditor(object):

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


    def add_new_line(self, count=1):
        self._code += '\n' * count


    def increase_indentation(self, count=1):
        self._global_indent += count


    def decrease_indentation(self, count=1):
        self._global_indent -= count


    def new_tempvar(self):
        var = 'tmp%s' % self._temp_variable_number
        self._temp_variable_number += 1
        return var
