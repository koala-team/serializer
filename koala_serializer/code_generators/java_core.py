# -*- coding: utf-8 -*-

# python imports
import warnings

# project imports
from ..parser_core import Tokens, capitalization_rules


class RootGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_root(self):
        code_editor = self._code_editor

        self._gen_package('ks')
        code_editor.add_line()
        self._gen_imports()
        code_editor.add_line()
        self._gen_ks_object()


    def _gen_imports(self):
        self._code_editor.add_line("import java.lang.*;")
        self._code_editor.add_line("import java.util.*;")


    def _gen_ks_object(self):
        self._code_editor.add_lines([
            "public abstract class KSObject",
            "{",
            "\tpublic static final String nameStatic = \"\";",
            "\tpublic abstract String name();",
            "\tpublic abstract byte[] serialize();",
            "\tpublic int deserialize(byte[] s) { return deserialize(s, 0); }",
            "\tprotected abstract int deserialize(byte[] s, int offset);",
            "",
            "",
			"\tprotected static List<Byte> b2B(byte[] bytes)",
			"\t{",
			"\t\tList<Byte> result = new ArrayList<>();",
			"\t\tfor (byte b : bytes)",
			"\t\t\tresult.add(b);",
			"\t\treturn result;",
			"\t}",
            "",
			"\tprotected static byte[] B2b(List<Byte> bytes)",
			"\t{",
			"\t\tbyte[] result = new byte[bytes.size()];",
			"\t\tfor(int i = 0; i < result.length; i++)",
			"\t\t\tresult[i] = bytes.get(i);",
			"\t\treturn result;",
			"\t}",
            "}",
        ])


    def _gen_package(self, pkg_name):
        self._code_editor.add_line("package %s;" % pkg_name)


###################################################################################
###################################################################################


class HeaderGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_header(self, module_name):
        code_editor = self._code_editor

        self._gen_package("ks." + module_name)
        code_editor.add_line()
        self._gen_imports()
        code_editor.add_line()


    def _gen_imports(self):
        self._code_editor.add_line("import java.lang.*;")
        self._code_editor.add_line("import java.util.*;")
        self._code_editor.add_line("import java.nio.*;")
        self._code_editor.add_line("import java.nio.charset.Charset;")
        self._code_editor.add_line()
        self._code_editor.add_line("import ks.KSObject;")


    def _gen_package(self, pkg_name):
        self._code_editor.add_line("package %s;" % pkg_name)


###################################################################################
###################################################################################


class FooterGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_footer(self, module_name):
        self._code_editor.decrease_indentation(put_accolade=False)


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
            warnings.warn("Java does not support multiple inheritance. Only first parent will be considered.")
            parents = parents[:1]
        self._user_defined_types[Tokens.Class][type_name] = (parents, properties)

        # generate definitions
        code_editor.add_line("public class %s extends %s" % (type_name, ', '.join(parents)))
        code_editor.increase_indentation()
        for attr_name, tree in properties:
            vartype = self._variable_type_generator.gen_vartype(tree)
            if tree[0] in [Tokens.UnsignedByte, Tokens.UnsignedShort, Tokens.UnsignedInteger, Tokens.UnsignedLong]:
                warnings.warn("Java does not support unsigned types. Instead, signed types will be considered.")
            code_editor.add_line("protected %s %s;" % (vartype, attr_name))
        code_editor.add_line()

        # generate getters
        code_editor.add_line("// getters")
        code_editor.add_line()
        for attr_name, tree in properties:
            vartype = self._variable_type_generator.gen_vartype(tree)
            code_editor.add_line("public %s get%s()" % (vartype, capitalization_rules['PascalCase'](attr_name)))
            code_editor.increase_indentation()
            code_editor.add_line("return this.%s;" % attr_name)
            code_editor.decrease_indentation()
            code_editor.add_line()
        code_editor.add_line()

        # generate setters
        code_editor.add_line("// setters")
        code_editor.add_line()
        for attr_name, tree in properties:
            vartype = self._variable_type_generator.gen_vartype(tree)
            code_editor.add_line("public void set%s(%s %s)" % (capitalization_rules['PascalCase'](attr_name), vartype, attr_name))
            code_editor.increase_indentation()
            code_editor.add_line("this.%s = %s;" % (attr_name, attr_name))
            code_editor.decrease_indentation()
            code_editor.add_line()
        code_editor.add_line()

        # generate constructor
        code_editor.add_line("public %s()" % type_name)
        code_editor.increase_indentation()
        code_editor.decrease_indentation()
        code_editor.add_line()

        # generate name
        code_editor.add_line("public static final String nameStatic = \"%s\";" % type_name)
        code_editor.add_line()

        code_editor.add_line("@Override")
        code_editor.add_line("public String name() { return \"%s\"; }" % type_name)
        code_editor.add_line()

        # generate serializer
        result_name = 's'
        code_editor.add_line("@Override")
        code_editor.add_line("public byte[] serialize()")
        code_editor.increase_indentation()
        code_editor.add_line("List<Byte> %s = new ArrayList<>();" % result_name)
        code_editor.add_line()

        if parents[0] != 'KSObject':
            code_editor.add_line("// serialize parents")
            # for parent in parents:
            #     code_editor.add_line("%s.addAll(b2B(%s.serialize()));" % (result_name, parent))
            code_editor.add_line("%s.addAll(b2B(super.serialize()));" % result_name)
            code_editor.add_line()

        for attr_name, tree in properties:
            code_editor.add_line("// serialize %s" % attr_name)
            self._serializer_generator.gen_serializer(attr_name, result_name, tree)
            code_editor.add_line()

        code_editor.add_line("return B2b(%s);" % result_name)
        code_editor.decrease_indentation()
        code_editor.add_line()

        # generate deserializer
        data_name = 's'
        offset_name = 'offset'
        code_editor.add_line("@Override")
        code_editor.add_line("protected int deserialize(byte[] %s, int %s)" %
                             (data_name, offset_name))
        code_editor.increase_indentation()

        if parents[0] != 'KSObject':
            code_editor.add_line("// deserialize parents")
            # for parent in parents:
            #     code_editor.add_line("%s = %s.deserialize(%s, %s);" % 
            #                          (offset_name, parent, data_name, offset_name))
            code_editor.add_line("%s = super.deserialize(%s, %s);" % 
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
        value_type = _def[1][0]
        self._user_defined_types[Tokens.Enum][type_name] = value_type
        code_editor.add_line("public enum %s" % type_name)
        code_editor.increase_indentation()

        value_type_cls = self._variable_type_generator.gen_vartype(value_type)
        value_type = self._variable_type_generator.gen_vartype(value_type, is_primitive=True)

        value = 0
        for attr in _def[1][1]:
            name = attr[0]
            if len(attr) > 1:
                value = attr[1]
            code_editor.add_line("%s((%s) %s)," % (name, value_type, value))
            value += 1
        code_editor.add_line(";\n")

        code_editor.add_lines([
            "private final %s value;" % value_type,
            "%s(%s value) { this.value = value; }" % (type_name, value_type),
            "public %s getValue() { return value; }" % value_type,
            "",
            "private static Map<%s, %s> reverseLookup;" % (value_type_cls, type_name),
            "",
            "public static %s of(%s value)" % (type_name, value_type),
            "{",
			"\tif (reverseLookup == null)",
			"\t{",
			"\t\treverseLookup = new HashMap<>();",
			"\t\tfor (%s c : %s.values())" % (type_name, type_name),
			"\t\t\treverseLookup.put(c.getValue(), c);",
			"\t}",
			"\treturn reverseLookup.get(value);",
            "}",
        ])
        code_editor.decrease_indentation()

###################################################################################
###################################################################################


class SerializerGenerator:

    def __init__(self, user_defined_types, code_editor):
        self._simples_token_table = {
            Tokens.Short: 'Short',
            Tokens.UnsignedShort: 'Short',
            Tokens.Integer: 'Integer',
            Tokens.UnsignedInteger: 'Integer',
            Tokens.Long: 'Long',
            Tokens.UnsignedLong: 'Long',
            Tokens.Float: 'Float',
            Tokens.Double: 'Double' 
        }
        self._simples_conversion_method_table = {
            Tokens.Short: 'Short',
            Tokens.UnsignedShort: 'Short',
            Tokens.Integer: 'Int',
            Tokens.UnsignedInteger: 'Int',
            Tokens.Long: 'Long',
            Tokens.UnsignedLong: 'Long',
            Tokens.Float: 'Float',
            Tokens.Double: 'Double' 
        }

        self._user_defined_types = user_defined_types
        self._code_editor = code_editor
        self._variable_type_generator = VariableTypeGenerator(self._user_defined_types)


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

        self._code_editor.add_line("%s.add((byte) ((%s == null) ? 0 : 1));" % 
                                   (result_name, value_name))
        self._code_editor.add_line("if (%s != null)" % value_name)
        self._code_editor.increase_indentation()
        serializer_func(value_name, result_name, tree)
        self._code_editor.decrease_indentation()



    def _gen_serializer_class(self, value_name, result_name, tree):
        self._code_editor.add_line("%s.addAll(b2B(%s.serialize()));" % (result_name, value_name))


    def _gen_serializer_enum(self, value_name, result_name, tree):
        self._gen_serializer_simples(
            "(%s.getValue())" % value_name,
            result_name,
            self._user_defined_types[Tokens.Enum][tree[0]]
        )


    def _gen_serializer_list(self, value_name, result_name, tree):
        code_editor = self._code_editor

        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen items
        value_type = self._variable_type_generator.gen_vartype(tree[1])
        item = code_editor.new_tempvar()
        code_editor.add_line("for (%s %s : %s)" % (value_type, item, value_name))
        code_editor.increase_indentation()
        self.gen_serializer(item, result_name, tree[1])
        code_editor.decrease_indentation()


    def _gen_serializer_map(self, value_name, result_name, tree):
        code_editor = self._code_editor

        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen items
        value_type = self._variable_type_generator.gen_vartype(tree).replace('Map', 'Map.Entry', 1)
        pair = code_editor.new_tempvar()
        code_editor.add_line("for (%s %s : %s.entrySet())" % (value_type, pair, value_name))
        code_editor.increase_indentation()
        self.gen_serializer("%s.getKey()" % pair, result_name, tree[1][0])
        code_editor.add_line()
        self.gen_serializer("%s.getValue()" % pair, result_name, tree[1][1])
        code_editor.decrease_indentation()


    def _gen_serializer_array(self, value_name, result_name, tree):
        code_editor = self._code_editor

        dims = tree[1][0]
        array_type = tree[1][1]

        indexes = []
        for dim in dims:
            index = code_editor.new_tempvar()
            indexes.append(index)
            code_editor.add_line("for (int %s = 0; %s < %s; %s++)" %
                                 (index, index, dim, index))
            code_editor.increase_indentation()

        value_name += "[%s]" % ']['.join(indexes)
        self.gen_serializer(value_name, result_name, array_type)
        for _ in range(len(dims)):
            code_editor.decrease_indentation()


    def _gen_serializer_string(self, value_name, result_name, tree):
        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen string
        self._code_editor.add_line("%s.addAll(b2B(%s.getBytes(Charset.forName(\"ISO-8859-1\"))));" %
                                    (result_name, value_name))


    def _gen_serializer_simples(self, value_name, result_name, tree):
        if tree[0] == Tokens.UnsignedByte:
            self._code_editor.add_line("%s.add((byte) %s);" % (result_name, value_name))
        elif tree[0] == Tokens.Byte:
            self._code_editor.add_line("%s.add((byte) %s);" % (result_name, value_name))
        elif tree[0] == Tokens.Boolean:
            self._code_editor.add_line("%s.add((byte) ((%s) ? 1 : 0));" % (result_name, value_name))
        elif tree[0] == Tokens.Char:
            self._code_editor.add_line("%s.add((byte) (char) %s);" % (result_name, value_name))
        else:
            value_type = self._simples_token_table[tree[0]]
            conversion_method = self._simples_conversion_method_table[tree[0]]
            self._code_editor.add_line("%s.addAll(b2B(ByteBuffer.allocate(%s.BYTES).order(ByteOrder.LITTLE_ENDIAN).put%s(%s).array()));" % 
                                        (result_name, value_type, conversion_method, value_name))


    def _gen_size(self, value_name, result_name, tree):
        code_editor = self._code_editor

        size_method = 'length' if tree[0] == Tokens.String else 'size'
        size = code_editor.new_tempvar()
        code_editor.add_line("List<Byte> %s = new ArrayList<>();" % size)
        self._gen_serializer_simples("%s.%s()" % (value_name, size_method), size, (Tokens.UnsignedInteger, ))
        code_editor.add_line("while (%s.size() > 0 && %s.get(%s.size() - 1) == 0)" % (size, size, size))
        code_editor.add_line("%s.remove(%s.size() - 1);" % (size, size), 1)

        self._gen_serializer_simples("%s.size()" % size, result_name, (Tokens.UnsignedByte, ))
        code_editor.add_line("%s.addAll(%s);" % (result_name, size))
        code_editor.add_line()


###################################################################################
###################################################################################


class DeserializerGenerator:

    def __init__(self, user_defined_types, code_editor):
        self._simples_token_table = {
            Tokens.Short: 'Short',
            Tokens.UnsignedShort: 'Short',
            Tokens.Integer: 'Integer',
            Tokens.UnsignedInteger: 'Integer',
            Tokens.Long: 'Long',
            Tokens.UnsignedLong: 'Long',
            Tokens.Float: 'Float',
            Tokens.Double: 'Double' 
        }
        self._simples_conversion_method_table = {
            Tokens.Short: 'Short',
            Tokens.UnsignedShort: 'Short',
            Tokens.Integer: 'Int',
            Tokens.UnsignedInteger: 'Int',
            Tokens.Long: 'Long',
            Tokens.UnsignedLong: 'Long',
            Tokens.Float: 'Float',
            Tokens.Double: 'Double' 
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
        code_editor.add_line("%s = %s.deserialize(%s, %s);" % 
                             (offset_name, value_name, data_name, offset_name))


    def _gen_deserializer_enum(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        enum_type = tree[0]
        val = code_editor.new_tempvar()
        val_type = self._user_defined_types[Tokens.Enum][tree[0]][0]
        val_type = self._variable_type_generator.gen_vartype((val_type, ), is_primitive=True)
        code_editor.add_line("%s %s;" % (val_type, val))

        self._gen_deserializer_simples(
            data_name,
            offset_name,
            val,
            self._user_defined_types[Tokens.Enum][tree[0]]
        )
        code_editor.add_line("%s = %s.of(%s);" % (value_name, enum_type, val))


    def _gen_deserializer_list(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen items
        code_editor.add_line("%s = new ArrayList<>();" % value_name)
        i = code_editor.new_tempvar()
        code_editor.add_line("for (int %s = 0; %s < %s; %s++)" % (i, i, size, i))
        code_editor.increase_indentation()
        item = code_editor.new_tempvar()
        item_type = self._variable_type_generator.gen_vartype(tree[1])
        code_editor.add_line("%s %s;" % (item_type, item))
        self.gen_deserializer(data_name, offset_name, item, tree[1])
        code_editor.add_line("%s.add(%s);" % (value_name, item))
        code_editor.decrease_indentation()


    def _gen_deserializer_map(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen items
        code_editor.add_line("%s = new HashMap<>();" % value_name)
        i = code_editor.new_tempvar()
        code_editor.add_line("for (int %s = 0; %s < %s; %s++)" % (i, i, size, i))
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

        code_editor.add_line("%s.put(%s, %s);" % (value_name, key, val))
        code_editor.decrease_indentation()


    def _gen_deserializer_array(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        dims = tree[1][0]
        array_type_tree = tree[1][1]
        array_type = self._variable_type_generator.gen_vartype(array_type_tree)
        if array_type.startswith('List'):
            array_type = 'ArrayList'
        elif array_type.startswith('Map'):
            array_type = 'HashMap'
        code_editor.add_line("%s = new %s[%s];" %
                             (value_name, array_type, ']['.join([str(dim) for dim in dims])))

        indexes = []
        for dim in dims:
            index = code_editor.new_tempvar()
            indexes.append(index)
            code_editor.add_line("for (int %s = 0; %s < %s; %s++)" %
                                 (index, index, dim, index))
            code_editor.increase_indentation()

        value_name += "[%s]" % ']['.join(indexes)
        self.gen_deserializer(data_name, offset_name, value_name, array_type_tree)
        for _ in range(len(dims)):
            code_editor.decrease_indentation()


    def _gen_deserializer_string(self, data_name, offset_name, value_name, tree):
        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen string
        self._code_editor.add_line("%s = new String(%s, %s, %s, Charset.forName(\"ISO-8859-1\"));" %
                                   (value_name, data_name, offset_name, size))
        self._code_editor.add_line("%s += %s;" % (offset_name, size))


    def _gen_deserializer_simples(self, data_name, offset_name, value_name, tree):
        value_type = self._variable_type_generator.gen_vartype(tree)
        if tree[0] in [Tokens.UnsignedByte, Tokens.Byte]:
            self._code_editor.add_line("%s = %s[%s];" %
                                       (value_name, data_name, offset_name or 0))
        elif tree[0] == Tokens.Boolean:
            self._code_editor.add_line("%s = (%s[%s] == 0) ? false : true;" %
                                       (value_name, data_name, offset_name or 0))
        elif tree[0] == Tokens.Char:
            self._code_editor.add_line("%s = (char) %s[%s];" %
                                       (value_name, data_name, offset_name or 0))
        else:
            method = self._simples_conversion_method_table[tree[0]]
            self._code_editor.add_line("%s = ByteBuffer.wrap(Arrays.copyOfRange(%s, %s, %s + %s.BYTES)).order(ByteOrder.LITTLE_ENDIAN).get%s();" %
                                        (value_name, data_name, offset_name or 0, offset_name or 0, value_type, method))
        if offset_name is not None:
            if tree[0] == Tokens.Boolean:
                value_type = 'Byte'
            self._code_editor.add_line("%s += %s.BYTES;" % (offset_name, value_type))


    def _gen_size(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        size_len = code_editor.new_tempvar()
        code_editor.add_line("byte %s;" % size_len)
        self._gen_deserializer_simples(data_name, offset_name, size_len, (Tokens.UnsignedByte, ))
        size_bytes = code_editor.new_tempvar()
        code_editor.add_line("byte[] %s = Arrays.copyOfRange(%s, %s, %s + %s);" %
                             (size_bytes, data_name, offset_name, offset_name, size_len))
        code_editor.add_line("%s += %s;" % (offset_name, size_len))

        size = code_editor.new_tempvar()
        code_editor.add_line("int %s;" % size)
        self._gen_deserializer_simples(size_bytes, None, size, (Tokens.UnsignedInteger, ))
        code_editor.add_line()

        return size


###################################################################################
###################################################################################


class VariableTypeGenerator:

    def __init__(self, user_defined_types):
        self._user_defined_types = user_defined_types

        self._simples_token_table = {
            Tokens.Boolean: ('Boolean', 'bool'),
            Tokens.Char: ('Character', 'char'),
            Tokens.Byte: ('Byte', 'byte'),
            Tokens.UnsignedByte: ('Byte', 'byte'),
            Tokens.Short: ('Short', 'short'),
            Tokens.UnsignedShort: ('Short', 'short'),
            Tokens.Integer: ('Integer', 'int'),
            Tokens.UnsignedInteger: ('Integer', 'int'),
            Tokens.Long: ('Long', 'long'),
            Tokens.UnsignedLong: ('Long', 'long'),
            Tokens.Float: ('Float', 'float'),
            Tokens.Double: ('Double', 'double'),
            Tokens.String: ('String', 'String')
        }


    def gen_vartype(self, tree, is_primitive=False):
        vartype = tree[0]

        for type_token in self._user_defined_types:
            if vartype in self._user_defined_types[type_token]:
                return vartype

        gen_vartype_func = getattr(
            self,
            '_gen_vartype_%s' % vartype,
            self._gen_vartype_simples
        )

        return gen_vartype_func(tree, is_primitive)


    def _gen_vartype_list(self, tree, is_primitive):
        return "List<%s>" % self.gen_vartype(tree[1])


    def _gen_vartype_map(self, tree, is_primitive):
        first_type = self.gen_vartype(tree[1][0])
        second_type = self.gen_vartype(tree[1][1])
        return "Map<%s, %s>" % (first_type, second_type)


    def _gen_vartype_array(self, tree, is_primitive):
        dims = list(reversed(tree[1][0]))
        initial_type = self.gen_vartype(tree[1][1])

        array_type = initial_type
        dim = '][' * (len(dims) - 1)
        array_type = "%s[%s]" % (array_type, dim)
        return array_type


    def _gen_vartype_simples(self, tree, is_primitive):
        primitive_index = 1 if is_primitive else 0
        return self._simples_token_table[tree[0]][primitive_index]
