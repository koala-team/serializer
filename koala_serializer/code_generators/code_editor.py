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

    def add_new_line(self, count=1):
        """
        this method adds new blank line to code
        :param count: number of blank lines you need default value is 1
        :return:
        """
        self._code += "\n" * count


    def increase_indentation(self, count=1):
        self._global_indent += count


    def decrease_indentation(self, count=1):
        self._global_indent -= count


    def new_tempvar(self):
        """
        :returns a temporary variable name that might be used in your code
        """
        var = "tmp%s" % self._temp_variable_number
        self._temp_variable_number += 1
        return var
