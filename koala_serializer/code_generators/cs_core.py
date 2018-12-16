# -*- coding: utf-8 -*-

# python imports
import warnings

# project imports
from ..parser_core import Tokens



class RootGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_root(self):
        code_editor = self._code_editor

        self._gen_imports()
        code_editor.add_line()
        self._gen_namespace('KS')
        self._gen_ks_object()
        self._code_editor.add_line("} // namespace KS")


    def _gen_imports(self):
        self._code_editor.add_line("using System;")


    def _gen_ks_object(self):
        self._code_editor.add_lines([
            "public abstract partial class KSObject",
            "{",
            "\tpublic const string NameStatic = \"\";",
            "\tpublic abstract string Name();",
            "\tpublic abstract byte[] Serialize();",
            "\tpublic abstract uint Deserialize(byte[] s, uint offset = 0);",
            "}",
        ], local_indent=1)


    def _gen_namespace(self, ns_name):
        self._code_editor.add_line("namespace %s" % ns_name)
        self._code_editor.add_line('{')


###################################################################################
###################################################################################


class HeaderGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_header(self, module_name):
        code_editor = self._code_editor

        self._gen_imports()
        code_editor.add_line()
        self._gen_namespace("KS." + module_name)
        code_editor.increase_indentation(put_accolade=False)


    def _gen_imports(self):
        self._code_editor.add_line("using System;")
        self._code_editor.add_line("using System.Linq;")
        self._code_editor.add_line("using System.Collections.Generic;")


    def _gen_namespace(self, ns_name):
        self._code_editor.add_line("namespace %s" % ns_name)
        self._code_editor.add_line('{')


###################################################################################
###################################################################################


class FooterGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_footer(self, module_name):
        self._code_editor.decrease_indentation(put_accolade=False)
        self._gen_namespace("KS." + module_name)


    def _gen_namespace(self, ns_name):
        self._code_editor.add_line("} // namespace %s" % ns_name)


###################################################################################
###################################################################################


class TypeGenerator:

    def __init__(self, code_editor):
        self._user_defined_types = {
            Tokens.Class: {},
            Tokens.Enum: {}
        }

        self._code_editor = code_editor
        self._serializer_generator = SerializerGenerator(self._user_defined_types, code_editor)
        self._deserializer_generator = DeserializerGenerator(self._user_defined_types, code_editor)
        self._variable_type_generator = VariableTypeGenerator(self._user_defined_types)


    def gen_type(self, type_name, properties):
        gen_func = getattr(self, '_gen_type_%s' % properties['_def'][0])
        gen_func(type_name, properties)



    def _gen_type_class(self, type_name, properties):
        code_editor = self._code_editor

        _def = properties.pop('_def')
        properties = properties.items()

        parents = ['KSObject'] if len(_def) == 1 else [p[0] for p in _def[1]]
        if len(parents) > 1:
            warnings.warn("C# does not support multiple inheritance. Only first parent will be considered.")
            parents = parents[:1]
        self._user_defined_types[Tokens.Class][type_name] = (parents, properties)

        # generate definitions
        code_editor.add_line("public partial class %s : %s" % (type_name, ', '.join(parents)))
        code_editor.increase_indentation()
        for attr_name, tree in properties:
            vartype = self._variable_type_generator.gen_vartype(tree)
            code_editor.add_line("public %s %s { get; set; }" % (vartype, attr_name))

        code_editor.add_line('\n')

        # generate constructor
        code_editor.add_line("public %s()" % type_name)
        code_editor.increase_indentation()
        code_editor.decrease_indentation()
        code_editor.add_line()

        # generate name
        code_editor.add_line("public new const string NameStatic = \"%s\";" % type_name)
        code_editor.add_line()

        code_editor.add_line("public override string Name() => \"%s\";" % type_name)
        code_editor.add_line()

        # generate serializer
        result_name = 's'
        code_editor.add_line("public override byte[] Serialize()")
        code_editor.increase_indentation()
        code_editor.add_line("List<byte> %s = new List<byte>();" % result_name)
        code_editor.add_line()

        if parents[0] != 'KSObject':
            code_editor.add_line("// serialize parents")
            # for parent in parents:
            #     code_editor.add_line("%s.AddRange(%s.Serialize());" % (result_name, parent))
            code_editor.add_line("%s.AddRange(base.Serialize());" % result_name)
            code_editor.add_line()

        for attr_name, tree in properties:
            code_editor.add_line("// serialize %s" % attr_name)
            self._serializer_generator.gen_serializer(attr_name, result_name, tree)
            code_editor.add_line()

        code_editor.add_line("return %s.ToArray();" % result_name)
        code_editor.decrease_indentation()
        code_editor.add_line()

        # generate deserializer
        data_name = 's'
        offset_name = 'offset'
        code_editor.add_line("public override uint Deserialize(byte[] %s, uint %s = 0)" %
                             (data_name, offset_name))
        code_editor.increase_indentation()

        if parents[0] != 'KSObject':
            code_editor.add_line("// deserialize parents")
            # for parent in parents:
            #     code_editor.add_line("%s = %s.Deserialize(%s, %s);" % 
            #                          (offset_name, parent, data_name, offset_name))
            code_editor.add_line("%s = base.Deserialize(%s, %s);" % 
                                 (offset_name, data_name, offset_name))
            code_editor.add_line()

        for attr_name, tree in properties:
            code_editor.add_line("// deserialize %s" % attr_name)
            self._deserializer_generator.gen_deserializer(data_name, offset_name, attr_name, tree)
            code_editor.add_line()

        code_editor.add_line("return %s;" % offset_name)
        code_editor.decrease_indentation()

        code_editor.decrease_indentation()


    def _gen_type_enum(self, type_name, properties):
        code_editor = self._code_editor

        _def = properties.pop('_def')
        self._user_defined_types[Tokens.Enum][type_name] = _def[1][0]
        value_type = _def[1][0][0]
        code_editor.add_line("public enum %s" % type_name)
        code_editor.increase_indentation()

        value = 0
        for attr in _def[1][1]:
            name = attr[0]
            if len(attr) > 1:
                value = attr[1]
            code_editor.add_line("%s = %s," % (name, value))
            value += 1

        code_editor.decrease_indentation()

###################################################################################
###################################################################################


class SerializerGenerator:

    def __init__(self, user_defined_types, code_editor):
        self._simples_token_table = {
            Tokens.Boolean: 'bool',
            Tokens.Char: 'char',
            Tokens.Byte: 'sbyte',
            Tokens.UnsignedByte: 'byte',
            Tokens.Short: 'short',
            Tokens.UnsignedShort: 'ushort',
            Tokens.Integer: 'int',
            Tokens.UnsignedInteger: 'uint',
            Tokens.Long: 'long',
            Tokens.UnsignedLong: 'ulong',
            Tokens.Float: 'float',
            Tokens.Double: 'double'
        }

        self._user_defined_types = user_defined_types
        self._code_editor = code_editor


    def gen_serializer(self, value_name, result_name, tree):
        value_type = tree[0]
        serializer_func = None

        for type_token in self._user_defined_types:
            if value_type in self._user_defined_types[type_token]:
                serializer_func = getattr(self, '_gen_serializer_%s' % type_token)
                break

        if serializer_func is None:
            serializer_func = getattr(
                self,
                '_gen_serializer_%s' % value_type,
                self._gen_serializer_simples
            )

        self._code_editor.add_line("%s.Add((byte)((%s == null) ? 0 : 1));" % 
                                   (result_name, value_name))
        self._code_editor.add_line("if (%s != null)" % value_name)
        self._code_editor.increase_indentation()
        serializer_func(value_name, result_name, tree)
        self._code_editor.decrease_indentation()



    def _gen_serializer_class(self, value_name, result_name, tree):
        self._code_editor.add_line("%s.AddRange(%s.Serialize());" % (result_name, value_name))


    def _gen_serializer_enum(self, value_name, result_name, tree):
        value_type = self._user_defined_types[Tokens.Enum][tree[0]][0]
        value_type = self._simples_token_table[value_type]
        self._gen_serializer_simples(
            "((%s)%s)" % (value_type, value_name),
            result_name,
            self._user_defined_types[Tokens.Enum][tree[0]]
        )


    def _gen_serializer_list(self, value_name, result_name, tree):
        code_editor = self._code_editor

        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen items
        item = code_editor.new_tempvar()
        code_editor.add_line("foreach (var %s in %s)" % (item, value_name))
        code_editor.increase_indentation()
        self.gen_serializer(item, result_name, tree[1])
        code_editor.decrease_indentation()


    def _gen_serializer_map(self, value_name, result_name, tree):
        code_editor = self._code_editor

        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen items
        pair = code_editor.new_tempvar()
        code_editor.add_line("foreach (var %s in %s)" % (pair, value_name))
        code_editor.increase_indentation()
        self.gen_serializer("%s.Key" % pair, result_name, tree[1][0])
        code_editor.add_line()
        self.gen_serializer("%s.Value" % pair, result_name, tree[1][1])
        code_editor.decrease_indentation()


    def _gen_serializer_array(self, value_name, result_name, tree):
        code_editor = self._code_editor

        dims = tree[1][0]
        array_type = tree[1][1]

        indexes = []
        for dim in dims:
            index = code_editor.new_tempvar()
            indexes.append(index)
            code_editor.add_line("for (uint %s = 0; %s < %s; %s++)" %
                                 (index, index, dim, index))
            code_editor.increase_indentation()

        value_name += "[%s]" % ', '.join(indexes)
        self.gen_serializer(value_name, result_name, array_type)
        for _ in range(len(dims)):
            code_editor.decrease_indentation()


    def _gen_serializer_string(self, value_name, result_name, tree):
        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen string
        self._code_editor.add_line("%s.AddRange(System.Text.Encoding.ASCII.GetBytes(%s));" %
                                    (result_name, value_name))


    def _gen_serializer_simples(self, value_name, result_name, tree):
        if tree[0] == Tokens.UnsignedByte:
            self._code_editor.add_line("%s.Add((byte)%s);" % (result_name, value_name))
        elif tree[0] == Tokens.Byte:
            self._code_editor.add_line("%s.Add((byte)%s);" % (result_name, value_name))
        else:
            value_type = self._simples_token_table[tree[0]]
            self._code_editor.add_line("%s.AddRange(BitConverter.GetBytes((%s)%s));" % 
                                        (result_name, value_type, value_name))


    def _gen_size(self, value_name, result_name, tree):
        code_editor = self._code_editor

        size = code_editor.new_tempvar()
        code_editor.add_line("List<byte> %s = new List<byte>();" % size)
        self._gen_serializer_simples("%s.Count()" % value_name, size, (Tokens.UnsignedInteger, ))
        code_editor.add_line("while (%s.Count > 0 && %s.Last() == 0)" % (size, size))
        code_editor.add_line("%s.RemoveAt(%s.Count - 1);" % (size, size), 1)

        self._gen_serializer_simples("%s.Count" % size, result_name, (Tokens.UnsignedByte, ))
        code_editor.add_line("%s.AddRange(%s);" % (result_name, size))
        code_editor.add_line()


###################################################################################
###################################################################################


class DeserializerGenerator:

    def __init__(self, user_defined_types, code_editor):
        self._simples_method_table = {
            Tokens.Boolean: 'ToBoolean',
            Tokens.Char: 'ToChar',
            Tokens.Byte: None,
            Tokens.UnsignedByte: None,
            Tokens.Short: 'ToInt16',
            Tokens.UnsignedShort: 'ToUInt16',
            Tokens.Integer: 'ToInt32',
            Tokens.UnsignedInteger: 'ToUInt32',
            Tokens.Long: 'ToInt64',
            Tokens.UnsignedLong: 'ToUInt64',
            Tokens.Float: 'ToSingle',
            Tokens.Double: 'ToDouble'
        }
        self._simples_token_table = {
            Tokens.Boolean: 'bool',
            Tokens.Char: 'char',
            Tokens.Byte: 'sbyte',
            Tokens.UnsignedByte: 'byte',
            Tokens.Short: 'short',
            Tokens.UnsignedShort: 'ushort',
            Tokens.Integer: 'int',
            Tokens.UnsignedInteger: 'uint',
            Tokens.Long: 'long',
            Tokens.UnsignedLong: 'ulong',
            Tokens.Float: 'float',
            Tokens.Double: 'double'
        }

        self._user_defined_types = user_defined_types
        self._code_editor = code_editor
        self._variable_type_generator = VariableTypeGenerator(self._user_defined_types)


    def gen_deserializer(self, data_name, offset_name, value_name, tree):
        value_type = tree[0]
        deserializer_func = None

        for type_token in self._user_defined_types:
            if value_type in self._user_defined_types[type_token]:
                deserializer_func = getattr(self, '_gen_deserializer_%s' % type_token)
                break

        if deserializer_func is None:
            deserializer_func = getattr(
                self,
                '_gen_deserializer_%s' % value_type,
                self._gen_deserializer_simples
            )

        
        is_null = self._code_editor.new_tempvar()
        self._code_editor.add_line("byte %s;" % is_null)
        self._gen_deserializer_simples(data_name, offset_name, is_null, (Tokens.UnsignedByte, ))
        self._code_editor.add_line("if (%s == 1)" % is_null)
        self._code_editor.increase_indentation()
        deserializer_func(data_name, offset_name, value_name, tree)
        self._code_editor.decrease_indentation()
        self._code_editor.add_line("else")
        self._code_editor.add_line("%s = null;" % value_name, 1)



    def _gen_deserializer_class(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        code_editor.add_line("%s = new %s();" % (value_name, tree[0]))
        code_editor.add_line("%s = %s.Deserialize(%s, %s);" % 
                             (offset_name, value_name, data_name, offset_name))


    def _gen_deserializer_enum(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        enum_type = tree[0]
        val = code_editor.new_tempvar()
        val_type = self._user_defined_types[Tokens.Enum][tree[0]][0]
        val_type = self._simples_token_table[val_type]
        code_editor.add_line("%s %s;" % (val_type, val))

        self._gen_deserializer_simples(
            data_name,
            offset_name,
            val,
            self._user_defined_types[Tokens.Enum][tree[0]]
        )
        code_editor.add_line("%s = (%s)%s;" % (value_name, enum_type, val))


    def _gen_deserializer_list(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen items
        value_type = self._variable_type_generator.gen_vartype(tree)
        code_editor.add_line("%s = new %s();" % (value_name, value_type))
        i = code_editor.new_tempvar()
        code_editor.add_line("for (uint %s = 0; %s < %s; %s++)" % (i, i, size, i))
        code_editor.increase_indentation()
        item = code_editor.new_tempvar()
        item_type = self._variable_type_generator.gen_vartype(tree[1])
        code_editor.add_line("%s %s;" % (item_type, item))
        self.gen_deserializer(data_name, offset_name, item, tree[1])
        code_editor.add_line("%s.Add(%s);" % (value_name, item))
        code_editor.decrease_indentation()


    def _gen_deserializer_map(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen items
        value_type = self._variable_type_generator.gen_vartype(tree)
        code_editor.add_line("%s = new %s();" % (value_name, value_type))
        i = code_editor.new_tempvar()
        code_editor.add_line("for (uint %s = 0; %s < %s; %s++)" % (i, i, size, i))
        code_editor.increase_indentation()

        key = code_editor.new_tempvar()
        val = code_editor.new_tempvar()
        key_type = self._variable_type_generator.gen_vartype(tree[1][0])
        val_type = self._variable_type_generator.gen_vartype(tree[1][1])

        code_editor.add_line("%s %s;" % (key_type, key))
        self.gen_deserializer(data_name, offset_name, key, tree[1][0])
        code_editor.add_line()

        code_editor.add_line("%s %s;" % (val_type, val))
        self.gen_deserializer(data_name, offset_name, val, tree[1][1])
        code_editor.add_line()

        code_editor.add_line("%s[%s] = %s;" % (value_name, key, val))
        code_editor.decrease_indentation()


    def _gen_deserializer_array(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        dims = tree[1][0]
        array_type_tree = tree[1][1]
        array_type = self._variable_type_generator.gen_vartype(array_type_tree)
        code_editor.add_line("%s = new %s[%s];" %
                             (value_name, array_type, ', '.join([str(dim) for dim in dims])))

        indexes = []
        for dim in dims:
            index = code_editor.new_tempvar()
            indexes.append(index)
            code_editor.add_line("for (uint %s = 0; %s < %s; %s++)" %
                                 (index, index, dim, index))
            code_editor.increase_indentation()

        value_name += "[%s]" % ', '.join(indexes)
        self.gen_deserializer(data_name, offset_name, value_name, array_type_tree)
        for _ in range(len(dims)):
            code_editor.decrease_indentation()


    def _gen_deserializer_string(self, data_name, offset_name, value_name, tree):
        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen string
        self._code_editor.add_line("%s = System.Text.Encoding.ASCII.GetString(%s.Skip((int)%s).Take((int)%s).ToArray());" %
                                   (value_name, data_name, offset_name, size))
        self._code_editor.add_line("%s += %s;" % (offset_name, size))


    def _gen_deserializer_simples(self, data_name, offset_name, value_name, tree):
        method = self._simples_method_table[tree[0]]
        value_type = self._simples_token_table[tree[0]]
        if tree[0] in [Tokens.UnsignedByte, Tokens.Byte]:
            self._code_editor.add_line("%s = (%s)%s[(int)%s];" %
                                       (value_name, value_type, data_name, offset_name or 0))
        else:
            self._code_editor.add_line("%s = BitConverter.%s(%s, (int)%s);" %
                                        (value_name, method, data_name, offset_name or 0))
        if offset_name is not None:
            self._code_editor.add_line("%s += sizeof(%s);" % (offset_name, value_type))


    def _gen_size(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        size_len = code_editor.new_tempvar()
        code_editor.add_line("byte %s;" % size_len)
        self._gen_deserializer_simples(data_name, offset_name, size_len, (Tokens.UnsignedByte, ))
        size_bytes = code_editor.new_tempvar()
        code_editor.add_line("byte[] %s = new byte[sizeof(%s)];" %
                             (size_bytes, Tokens.UnsignedInteger))
        code_editor.add_line("Array.Copy(%s, %s, %s, 0, %s);" %
                             (data_name, offset_name, size_bytes, size_len))
        code_editor.add_line("%s += %s;" % (offset_name, size_len))

        size = code_editor.new_tempvar()
        code_editor.add_line("uint %s;" % size)
        self._gen_deserializer_simples(size_bytes, None, size, (Tokens.UnsignedInteger, ))
        code_editor.add_line()

        return size


###################################################################################
###################################################################################


class VariableTypeGenerator:

    def __init__(self, user_defined_types):
        self._user_defined_types = user_defined_types

        self._simples_token_table = {
            Tokens.Boolean: 'bool?',
            Tokens.Char: 'char?',
            Tokens.Byte: 'sbyte?',
            Tokens.UnsignedByte: 'byte?',
            Tokens.Short: 'short?',
            Tokens.UnsignedShort: 'ushort?',
            Tokens.Integer: 'int?',
            Tokens.UnsignedInteger: 'uint?',
            Tokens.Long: 'long?',
            Tokens.UnsignedLong: 'ulong?',
            Tokens.Float: 'float?',
            Tokens.Double: 'double?',
            Tokens.String: 'string'
        }


    def gen_vartype(self, tree):
        vartype = tree[0]

        for type_token in self._user_defined_types:
            if vartype in self._user_defined_types[type_token]:
                nullable = '?' if type_token == Tokens.Enum else ''
                return vartype + nullable

        gen_vartype_func = getattr(
            self,
            '_gen_vartype_%s' % vartype,
            self._gen_vartype_simples
        )

        return gen_vartype_func(tree)


    def _gen_vartype_list(self, tree):
        return "List<%s>" % self.gen_vartype(tree[1])


    def _gen_vartype_map(self, tree):
        first_type = self.gen_vartype(tree[1][0])
        second_type = self.gen_vartype(tree[1][1])
        return "Dictionary<%s, %s>" % (first_type, second_type)


    def _gen_vartype_array(self, tree):
        dims = list(reversed(tree[1][0]))
        initial_type = self.gen_vartype(tree[1][1])

        array_type = initial_type
        dim = ',' * (len(dims) - 1)
        array_type = "%s[%s]" % (array_type, dim)
        return array_type


    def _gen_vartype_simples(self, tree):
        return self._simples_token_table[tree[0]]
