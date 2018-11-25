# -*- coding: utf-8 -*-

class Tokens:
    # objects

    Class = 'class'
    Enum = 'enum'

    # simple types

    Boolean = 'boolean'
    Char = 'char'
    Byte = 'byte'
    UnsignedByte = 'ubyte'
    Short = 'short'
    UnsignedShort = 'ushort'
    Integer = 'int'
    UnsignedInteger = 'uint'
    Long = 'long'
    UnsignedLong = 'ulong'
    Float = 'float'
    Double = 'double'
    String = 'string'

    # complex types

    List = 'list'
    Map = 'map'
    Array = 'array'



class Patterns:
    # objects

    Class = "%s(\((([a-zA-Z_][a-zA-Z0-9_]*,)*([a-zA-Z_][a-zA-Z0-9_]*))\))?$" % Tokens.Class
    Enum = "%s<(%s)>{(([a-zA-Z_][a-zA-Z0-9_]*(\(-?[0-9]+\))?,)*([a-zA-Z_][a-zA-Z0-9_]*(\(-?[0-9]+\))?))}$" % \
            (Tokens.Enum, '|'.join([
                Tokens.Byte, Tokens.UnsignedByte, Tokens.Short, Tokens.UnsignedShort,
                Tokens.Integer, Tokens.UnsignedInteger, Tokens.Long, Tokens.UnsignedLong
            ]))
    EnumValue = "([a-zA-Z_][a-zA-Z0-9_]*)(\((-?[0-9]+)\))?$"

    # simple types

    Boolean = "%s$" % Tokens.Boolean
    Char = "%s$" % Tokens.Char
    Byte = "%s$" % Tokens.Byte
    UnsignedByte = "%s$" % Tokens.UnsignedByte
    Short = "%s$" % Tokens.Short
    UnsignedShort = "%s$" % Tokens.UnsignedShort
    Integer = "%s$" % Tokens.Integer
    UnsignedInteger = "%s$" % Tokens.UnsignedInteger
    Long = "%s$" % Tokens.Long
    UnsignedLong = "%s$" % Tokens.UnsignedLong
    Float = "%s$" % Tokens.Float
    Double = "%s$" % Tokens.Double
    String = "%s$" % Tokens.String

    # complex types

    List = "%s<(.*)>$" % Tokens.List
    Map = "%s<(.*,.*)>$" % Tokens.Map
    Array = "%s((\[[0-9]+\])+)<(.*)>$" % Tokens.Array



class Rules:

    def __init__(self, regex_factory, get_type_tree):
        self._simples_token_list = [
            Tokens.Boolean,
            Tokens.Char,
            Tokens.Byte,
            Tokens.UnsignedByte,
            Tokens.Short,
            Tokens.UnsignedShort,
            Tokens.Integer,
            Tokens.UnsignedInteger,
            Tokens.Long,
            Tokens.UnsignedLong,
            Tokens.Float,
            Tokens.Double,
            Tokens.String
        ]

        self._simples_pattern_list = [
            'Boolean',
            'Char',
            'Byte',
            'UnsignedByte',
            'Short',
            'UnsignedShort',
            'Integer',
            'UnsignedInteger',
            'Long',
            'UnsignedLong',
            'Float',
            'Double',
            'String'
        ]

        self._regex_factory = regex_factory
        self._get_type_tree = get_type_tree


    # objects

    def _rule_class(self, text):
        result = self._regex_factory.match('Class', text)
        if result is None:
            return None

        parent_classes = result.group(2)
        if parent_classes is None:
            return (Tokens.Class, )

        parent_trees = []
        for parent in parent_classes.split(','):
            parent_trees.append(self._get_type_tree(parent))
        return (Tokens.Class, tuple(parent_trees))


    def _rule_enum(self, text):
        result = self._regex_factory.match('Enum', text)
        if result is None:
            return None

        value_type = self._get_type_tree(result.group(1))
        members = []

        for member_text in result.group(2).split(','):
            r = self._regex_factory.match('EnumValue', member_text)
            name = r.group(1)
            value = r.group(3)
            member = (name, ) if value is None else (name, int(value))
            members.append(member)
        return (Tokens.Enum, (value_type, tuple(members)))


    # simple types

    def _rule_simples(self, text):
        for i in range(len(self._simples_token_list)):
            result = self._regex_factory.match(self._simples_pattern_list[i], text)
            if result is None:
                continue
            return (self._simples_token_list[i], )
        return None


    # complex types

    def _rule_list(self, text):
        result = self._regex_factory.match('List', text)
        if result is None:
            return None

        inner_text = result.group(1)
        return (Tokens.List, self._get_type_tree(inner_text))


    def _rule_map(self, text):
        result = self._regex_factory.match('Map', text)
        if result is None:
            return None

        text = result.group(1)
        result = None

        diff = 0
        for i in range(len(text)):
            if text[i] == '<':
                diff += 1
            elif text[i] == '>':
                diff -= 1
            elif text[i] == ',' and diff == 0:
                result = (text[:i], text[i + 1:])
                break

        if result is None:
            return None

        inner_text_left = result[0]
        inner_text_right = result[1]
        return (Tokens.Map, (self._get_type_tree(inner_text_left), self._get_type_tree(inner_text_right)))


    def _rule_array(self, text):
        result = self._regex_factory.match('Array', text)
        if result is None:
            return None

        array_type = self._get_type_tree(result.group(3))
        dims = [int(r) for r in result.group(1)[1:-1].split('][')]

        if 0 in dims:
            return None
        return (Tokens.Array, (tuple(dims), array_type))



def convert_camel_case(name, is_lower):
    name = list(name)
    first_underscore_index = -1
    while name[first_underscore_index + 1] == '_':
        first_underscore_index += 1

    for i in range(len(name) - 2, first_underscore_index, -1):
        if name[i] == '_' and name[i + 1] not in ['_', '']:
            name[i + 1] = name[i + 1].upper()
            name[i] = ''
    for i in range(len(name)):
        if name[i] not in ['_', '']:
            if is_lower:
                name[i] = name[i].lower()
            else:
                name[i] = name[i].upper()
            break
    return ''.join(name)


capitalization_rules = {
    'snake_case': lambda name: name,
    'camelCase': lambda name: convert_camel_case(name, True),
    'PascalCase': lambda name: convert_camel_case(name, False)
}
