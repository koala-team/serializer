# -*- coding: utf-8 -*-

# project imports
from ..parser_core import Tokens


class HeaderGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_header(self, module_name):
        code_editor = self._code_editor

        code_editor.add_line("#ifndef _KS_%s_H_" % module_name.upper())
        code_editor.add_line("#define _KS_%s_H_\n" % module_name.upper())
        self._gen_includes()
        code_editor.add_line('\n')
        self._gen_namespace('ks')
        code_editor.add_line()
        self._gen_ks_object()
        code_editor.add_line('\n')
        self._gen_namespace(module_name)
        code_editor.add_line()


    def _gen_includes(self):
        self._code_editor.add_line("#include <string>")
        self._code_editor.add_line("#include <vector>")
        self._code_editor.add_line("#include <map>")
        self._code_editor.add_line("#include <array>")


    def _gen_ks_object(self):
        self._code_editor.add_lines([
            "#ifndef _KS_OBJECT_",
            "#define _KS_OBJECT_",
            "",
            "class KSObject",
            "{",
            "public:",
            "\tstatic inline const std::string nameStatic() { return \"\"; }",
            "\tvirtual inline const std::string name() const = 0;",
            "\tvirtual std::string serialize() const = 0;",
            "\tvirtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;",
            "};",
            "",
            "#endif // _KS_OBJECT_",
        ])


    def _gen_namespace(self, ns_name):
        self._code_editor.add_line("namespace %s" % ns_name)
        self._code_editor.add_line('{')


###################################################################################
###################################################################################


class FooterGenerator:

    def __init__(self, code_editor):
        self._code_editor = code_editor


    def gen_footer(self, module_name):
        self._gen_namespace(module_name)
        self._code_editor.add_line()
        self._gen_namespace('ks')
        self._code_editor.add_line()
        self._code_editor.add_line("#endif // _KS_%s_H_" % module_name.upper())


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
        self._user_defined_types[Tokens.Class][type_name] = (parents, properties)

        # generate definitions
        code_editor.add_line("class %s : public %s" % (type_name, ', '.join(parents)))
        code_editor.add_line("{\n")
        code_editor.add_line("protected:\n")
        for attr_name, tree in properties:
            attr_name = '__' + attr_name
            vartype = self._variable_type_generator.gen_vartype(tree)
            code_editor.add_line("%s %s;" % (vartype, attr_name), 1)

        code_editor.add_line()
        for attr_name, tree in properties:
            attr_name = '__has_' + attr_name
            code_editor.add_line("bool %s;" % attr_name, 1)

        code_editor.add_line('\n')

        # generate getters
        code_editor.add_line("public: // getters\n")
        code_editor.increase_indentation(put_accolade=False)
        for attr_name, tree in properties:
            vartype = self._variable_type_generator.gen_vartype(tree)
            code_editor.add_line("inline %s %s() const" % (vartype, attr_name))
            code_editor.increase_indentation()
            code_editor.add_line("return __%s;" % attr_name)
            code_editor.decrease_indentation()
            code_editor.add_line()
        code_editor.decrease_indentation(put_accolade=False)
        code_editor.add_line()

        # generate reference getters
        code_editor.add_line("public: // reference getters\n")
        code_editor.increase_indentation(put_accolade=False)
        for attr_name, tree in properties:
            vartype = self._variable_type_generator.gen_vartype(tree)
            code_editor.add_line("inline %s &ref_%s() const" % (vartype, attr_name))
            code_editor.increase_indentation()
            code_editor.add_line("return (%s&) __%s;" % (vartype, attr_name))
            code_editor.decrease_indentation()
            code_editor.add_line()
        code_editor.decrease_indentation(put_accolade=False)
        code_editor.add_line()

        # generate setters
        code_editor.add_line("public: // setters\n")
        code_editor.increase_indentation(put_accolade=False)
        for attr_name, tree in properties:
            vartype = self._variable_type_generator.gen_vartype(tree)
            code_editor.add_line("inline void %s(const %s &%s)" % (attr_name, vartype, attr_name))
            code_editor.increase_indentation()
            code_editor.add_line("__%s = %s;" % (attr_name, attr_name))
            code_editor.add_line("has_%s(true);" % attr_name)
            code_editor.decrease_indentation()
            code_editor.add_line()
        code_editor.decrease_indentation(put_accolade=False)
        code_editor.add_line()

        # generate has_attribute getters
        code_editor.add_line("public: // has_attribute getters\n")
        code_editor.increase_indentation(put_accolade=False)
        for attr_name, _ in properties:
            attr_name = 'has_' + attr_name
            code_editor.add_line("inline bool %s() const" % attr_name)
            code_editor.increase_indentation()
            code_editor.add_line("return __%s;" % attr_name)
            code_editor.decrease_indentation()
            code_editor.add_line()
        code_editor.decrease_indentation(put_accolade=False)
        code_editor.add_line()

        # generate has_attribute setters
        code_editor.add_line("public: // has_attribute setters\n")
        code_editor.increase_indentation(put_accolade=False)
        for attr_name, _ in properties:
            attr_name = 'has_' + attr_name
            code_editor.add_line("inline void %s(const bool &%s)" % (attr_name, attr_name))
            code_editor.increase_indentation()
            code_editor.add_line("__%s = %s;" % (attr_name, attr_name))
            code_editor.decrease_indentation()
            code_editor.add_line()
        code_editor.decrease_indentation(put_accolade=False)
        code_editor.add_line()


        code_editor.add_line("public:\n")
        code_editor.increase_indentation(put_accolade=False)

        # generate constructor
        code_editor.add_line("%s()" % type_name)
        code_editor.increase_indentation()
        for attr_name, _ in properties:
            code_editor.add_line("has_%s(false);" % attr_name)
        code_editor.decrease_indentation()
        code_editor.add_line()

        # generate name
        code_editor.add_line("static inline const std::string nameStatic()")
        code_editor.increase_indentation()
        code_editor.add_line("return \"%s\";" % type_name)
        code_editor.decrease_indentation()
        code_editor.add_line()

        code_editor.add_line("virtual inline const std::string name() const")
        code_editor.increase_indentation()
        code_editor.add_line("return \"%s\";" % type_name)
        code_editor.decrease_indentation()
        code_editor.add_line()

        # generate serializer
        result_name = 's'
        code_editor.add_line("std::string serialize() const")
        code_editor.increase_indentation()
        code_editor.add_line("std::string %s = \"\";" % result_name)
        code_editor.add_line()

        if parents[0] != 'KSObject':
            code_editor.add_line("// serialize parents")
            for parent in parents:
                code_editor.add_line("%s += %s::serialize();" % (result_name, parent))
            code_editor.add_line()

        for attr_name, tree in properties:
            code_editor.add_line("// serialize %s" % attr_name)
            attr_name = '__' + attr_name
            self._serializer_generator.gen_serializer(attr_name, result_name, tree, True)
            code_editor.add_line()

        code_editor.add_line("return %s;" % result_name)
        code_editor.decrease_indentation()
        code_editor.add_line()

        # generate deserializer
        data_name = 's'
        offset_name = 'offset'
        code_editor.add_line("unsigned int deserialize(const std::string &%s, unsigned int %s=0)" %
                             (data_name, offset_name))
        code_editor.increase_indentation()

        if parents[0] != 'KSObject':
            code_editor.add_line("// deserialize parents")
            for parent in parents:
                code_editor.add_line("%s = %s::deserialize(%s, %s);" % 
                                     (offset_name, parent, data_name, offset_name))
            code_editor.add_line()

        for attr_name, tree in properties:
            code_editor.add_line("// deserialize %s" % attr_name)
            attr_name = '__' + attr_name
            self._deserializer_generator.gen_deserializer(data_name, offset_name, attr_name, tree, True)
            code_editor.add_line()

        code_editor.add_line("return %s;" % offset_name)
        code_editor.decrease_indentation()

        code_editor.decrease_indentation(add_semi=True)


    def _gen_type_enum(self, type_name, properties):
        code_editor = self._code_editor

        _def = properties.pop('_def')
        self._user_defined_types[Tokens.Enum][type_name] = _def[1][0]
        value_type = _def[1][0][0]
        code_editor.add_line("enum class %s" % type_name)
        code_editor.increase_indentation()

        value = 0
        for attr in _def[1][1]:
            name = attr[0]
            if len(attr) > 1:
                value = attr[1]
            code_editor.add_line("%s = %s," % (name, value))
            value += 1

        code_editor.decrease_indentation(add_semi=True)

###################################################################################
###################################################################################


class SerializerGenerator:

    def __init__(self, user_defined_types, code_editor):
        self._simples_token_table = {
            Tokens.Boolean: 'bool',
            Tokens.Char: 'char',
            Tokens.Byte: 'char',
            Tokens.UnsignedByte: 'unsigned char',
            Tokens.Short: 'short',
            Tokens.UnsignedShort: 'unsigned short',
            Tokens.Integer: 'int',
            Tokens.UnsignedInteger: 'unsigned int',
            Tokens.Long: 'long long',
            Tokens.UnsignedLong: 'unsigned long long',
            Tokens.Float: 'float',
            Tokens.Double: 'double'
        }

        self._user_defined_types = user_defined_types
        self._code_editor = code_editor


    def gen_serializer(self, value_name, result_name, tree, check_null=False):
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

        if check_null:
            self._code_editor.add_line("%s += __has_%s;" % 
                                       (result_name, value_name[2:]))
            self._code_editor.add_line("if (__has_%s)" % value_name[2:])
            self._code_editor.increase_indentation()
        else:
            self._code_editor.add_line("%s += '\\x01';" % result_name)

        serializer_func(value_name, result_name, tree)

        if check_null:
            self._code_editor.decrease_indentation()



    def _gen_serializer_class(self, value_name, result_name, tree):
        self._code_editor.add_line("%s += %s.serialize();" % (result_name, value_name))


    def _gen_serializer_enum(self, value_name, result_name, tree):
        value_type = self._user_defined_types[Tokens.Enum][tree[0]][0]
        value_type = self._simples_token_table[value_type]
        self._gen_serializer_simples(
            "(%s) %s" % (value_type, value_name),
            result_name,
            self._user_defined_types[Tokens.Enum][tree[0]]
        )


    def _gen_serializer_list(self, value_name, result_name, tree):
        code_editor = self._code_editor

        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen items
        item = code_editor.new_tempvar()
        code_editor.add_line("for (auto &%s : %s)" % (item, value_name))
        code_editor.increase_indentation()
        self.gen_serializer(item, result_name, tree[1])
        code_editor.decrease_indentation()


    def _gen_serializer_map(self, value_name, result_name, tree):
        code_editor = self._code_editor

        # gen size
        self._gen_size(value_name, result_name, tree)

        # gen items
        pair = code_editor.new_tempvar()
        code_editor.add_line("for (auto &%s : %s)" % (pair, value_name))
        code_editor.increase_indentation()
        self.gen_serializer("%s.first" % pair, result_name, tree[1][0])
        code_editor.add_line()
        self.gen_serializer("%s.second" % pair, result_name, tree[1][1])
        code_editor.decrease_indentation()


    def _gen_serializer_array(self, value_name, result_name, tree):
        code_editor = self._code_editor

        dims = tree[1][0]
        array_type = tree[1][1]

        indexes = []
        for dim in dims:
            index = code_editor.new_tempvar()
            indexes.append(index)
            code_editor.add_line("for (unsigned int %s = 0; %s < %s; %s++)" %
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
        self._code_editor.add_line("%s += %s;" % (result_name, value_name))


    def _gen_serializer_simples(self, value_name, result_name, tree):
        code_editor = self._code_editor

        i = code_editor.new_tempvar()
        tmp = code_editor.new_tempvar()
        rc = code_editor.new_tempvar()

        value_type = self._simples_token_table[tree[0]]
        size = "sizeof(%s)" % value_type
        code_editor.add_line("%s %s = %s;" % (value_type, tmp, value_name))
        code_editor.add_line("auto %s = reinterpret_cast<char*>(&%s);" % (rc, tmp))
        self._code_editor.add_line("%s += std::string(%s, %s);" % (result_name, rc, size))


    def _gen_size(self, value_name, result_name, tree):
        code_editor = self._code_editor

        size = code_editor.new_tempvar()
        code_editor.add_line("std::string %s = \"\";" % size)
        self._gen_serializer_simples("%s.size()" % value_name, size, (Tokens.UnsignedInteger, ))
        code_editor.add_line("while (%s.size() && %s.back() == 0)" % (size, size))
        code_editor.add_line("%s.pop_back();" % size, 1)

        self._gen_serializer_simples("%s.size()" % size, result_name, (Tokens.UnsignedByte, ))
        code_editor.add_line("%s += %s;" % (result_name, size))
        code_editor.add_line()


###################################################################################
###################################################################################


class DeserializerGenerator:

    def __init__(self, user_defined_types, code_editor):
        self._simples_token_table = {
            Tokens.Boolean: 'bool',
            Tokens.Char: 'char',
            Tokens.Byte: 'char',
            Tokens.UnsignedByte: 'unsigned char',
            Tokens.Short: 'short',
            Tokens.UnsignedShort: 'unsigned short',
            Tokens.Integer: 'int',
            Tokens.UnsignedInteger: 'unsigned int',
            Tokens.Long: 'long long',
            Tokens.UnsignedLong: 'unsigned long long',
            Tokens.Float: 'float',
            Tokens.Double: 'double'
        }

        self._user_defined_types = user_defined_types
        self._code_editor = code_editor
        self._variable_type_generator = VariableTypeGenerator(self._user_defined_types)



    def gen_deserializer(self, data_name, offset_name, value_name, tree, check_null=False):
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

        if check_null:
            self._gen_deserializer_simples(data_name, offset_name, '__has_' + value_name[2:], 
                                           (Tokens.UnsignedByte, ))
            self._code_editor.add_line("if (__has_%s)" % value_name[2:])
            self._code_editor.increase_indentation()
        else:
            self._code_editor.add_line("%s++;" % offset_name)

        deserializer_func(data_name, offset_name, value_name, tree)

        if check_null:
            self._code_editor.decrease_indentation()



    def _gen_deserializer_class(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        code_editor.add_line("%s = %s.deserialize(%s, %s);" % 
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
        code_editor.add_line("%s = (%s) %s;" % (value_name, enum_type, val))


    def _gen_deserializer_list(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen items
        code_editor.add_line("%s.clear();" % value_name)
        i = code_editor.new_tempvar()
        code_editor.add_line("for (unsigned int %s = 0; %s < %s; %s++)" % (i, i, size, i))
        code_editor.increase_indentation()
        item = code_editor.new_tempvar()
        item_type = self._variable_type_generator.gen_vartype(tree[1])
        code_editor.add_line("%s %s;" % (item_type, item))
        self.gen_deserializer(data_name, offset_name, item, tree[1])
        code_editor.add_line("%s.push_back(%s);" % (value_name, item))
        code_editor.decrease_indentation()


    def _gen_deserializer_map(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen items
        code_editor.add_line("%s.clear();" % value_name)
        i = code_editor.new_tempvar()
        code_editor.add_line("for (unsigned int %s = 0; %s < %s; %s++)" % (i, i, size, i))
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
        array_type = tree[1][1]

        indexes = []
        for dim in dims:
            index = code_editor.new_tempvar()
            indexes.append(index)
            code_editor.add_line("for (unsigned int %s = 0; %s < %s; %s++)" %
                                 (index, index, dim, index))
            code_editor.increase_indentation()

        value_name += "[%s]" % ']['.join(indexes)
        self.gen_deserializer(data_name, offset_name, value_name, array_type)
        for _ in range(len(dims)):
            code_editor.decrease_indentation()


    def _gen_deserializer_string(self, data_name, offset_name, value_name, tree):
        # gen size
        size = self._gen_size(data_name, offset_name, value_name, tree)

        # gen string
        self._code_editor.add_line("%s = %s.substr(%s, %s);" %
                                   (value_name, data_name, offset_name, size))
        self._code_editor.add_line("%s += %s;" % (offset_name, size))


    def _gen_deserializer_simples(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor
        value_type = self._simples_token_table[tree[0]]
        code_editor.add_line("%s = *((%s*) (&%s[%s]));" %
                             (value_name, value_type, data_name, offset_name or 0))
        if offset_name is not None:
            code_editor.add_line("%s += sizeof(%s);" % (offset_name, value_type))


    def _gen_size(self, data_name, offset_name, value_name, tree):
        code_editor = self._code_editor

        size_len = code_editor.new_tempvar()
        code_editor.add_line("unsigned char %s;" % size_len)
        self._gen_deserializer_simples(data_name, offset_name, size_len, (Tokens.UnsignedByte, ))
        size_bytes = code_editor.new_tempvar()
        code_editor.add_line("std::string %s = std::string(&%s[%s], %s);" %
                              (size_bytes, data_name, offset_name, size_len))
        code_editor.add_line("%s += %s;" % (offset_name, size_len))

        code_editor.add_line("while (%s.size() < sizeof(unsigned int))" % size_bytes)
        code_editor.add_line("%s += '\\x00';" % size_bytes, 1)

        size = code_editor.new_tempvar()
        code_editor.add_line("unsigned int %s;" % size)
        self._gen_deserializer_simples(size_bytes, None, size, (Tokens.UnsignedInteger, ))
        code_editor.add_line()

        return size


###################################################################################
###################################################################################


class VariableTypeGenerator:

    def __init__(self, user_defined_types):
        self._user_defined_types = user_defined_types

        self._simples_token_table = {
            Tokens.Boolean: 'bool',
            Tokens.Char: 'char',
            Tokens.Byte: 'char',
            Tokens.UnsignedByte: 'unsigned char',
            Tokens.Short: 'short',
            Tokens.UnsignedShort: 'unsigned short',
            Tokens.Integer: 'int',
            Tokens.UnsignedInteger: 'unsigned int',
            Tokens.Long: 'long long',
            Tokens.UnsignedLong: 'unsigned long long',
            Tokens.Float: 'float',
            Tokens.Double: 'double',
            Tokens.String: 'std::string'
        }


    def gen_vartype(self, tree):
        vartype = tree[0]

        for type_token in self._user_defined_types:
            if vartype in self._user_defined_types[type_token]:
                return vartype

        gen_vartype_func = getattr(
            self,
            '_gen_vartype_%s' % vartype,
            self._gen_vartype_simples
        )

        return gen_vartype_func(tree)


    def _gen_vartype_list(self, tree):
        return "std::vector<%s>" % self.gen_vartype(tree[1])


    def _gen_vartype_map(self, tree):
        first_type = self.gen_vartype(tree[1][0])
        second_type = self.gen_vartype(tree[1][1])
        return "std::map<%s, %s>" % (first_type, second_type)


    def _gen_vartype_array(self, tree):
        dims = list(reversed(tree[1][0]))
        initial_type = self.gen_vartype(tree[1][1])

        array_type = initial_type
        for dim in dims:
            array_type = "std::array<%s, %s>" % (array_type, dim)
        return array_type


    def _gen_vartype_simples(self, tree):
        return self._simples_token_table[tree[0]]
