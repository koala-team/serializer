# K04lA Object Serializer
KoalaSerializer is a tool designed for creating serializable objects. This is useful when you want to send an object via a socket. For example consider having a server written in C++ and a client written in Python. Suppose you want to send an object from your server to the client. Imagine a game server that wants to send a snapshot of the game world to clients. The snapshot object must be serialized in the server, sent via a socket, and deserialized in the client. KoalaSerializer enables you to do the first and last steps easily.


## Getting Started


### Install

	$ sudo pip install koala-serializer

### Generate Codes

After installation, define your objects in a **ks** file. Examples can be found [here](https://github.com/k04la/serializer/tree/master/examples).
To generate source codes run the command below:

	$ koalasc <ks_path> <programming_language> <output_dir>


## Usage

### KS Structure
**ks** is a Koala serializer format that enables you to define your objects simply.
Basically the **ks** file has the same structure as the [**ini**](https://en.wikipedia.org/wiki/INI_file) files.

```ini
[ObjectName1]
_def = ObjectSpecification
attribute1 = attribute_type
attribute2 = attribute_type

[ObjectName2]
_def = ObjectSpecification
attribute1 = attribute_type
attribute2 = attribute_type

[ObjectName3]
_def = ObjectSpecification
```


### Simple Data Types

KS Type  |  Python Type  |  C++ Type  |  Standard Size
---  |  ---  |  ---  | ---
boolean  |  bool  |  bool  |  1
char  |  str (of size 1)  |  char  |  1
byte  |  int  |  signed char |  1
ubyte  |  int  |  unsigned char |  1
short  |  int  |  short |  2
ushort  |  int  |  unsigned short |  2
int  |  int  |  int |  4
uint  |  int  |  unsigned int |  4
long  |  int  |  long long |  8
ulong  |  int  |  unsigned long long |  8
float  |  float  |  float |  4
double  | float  |  double |  8
string  |  str  |  string |


### Complex Data Types

KS Type  |  Python Type  |  C++ Type
---  |  ---  |  ---
list <data_type\>  |  list  |  vector<data_type\>
map <data_type, data_type\>  |  dict  |  map<data_type, data_type\>
array[dim1_size][dim2_size]...[dimN_size] <data_type\>  |  multi-dim list  |  data_type[dim1_size][dim2_size]...[dimN_size]

* The **data_type** can either be *simple data types*, *complex data types*, *enums* or other *classes*.
* It is not recommended to use *arrays*, unless you are experienced and professional enough.

### Objects
Objects are specified using ``_def`` in **ks** files.

#### Enum

Structure:

```ini
[EnumName]
_def = enum <enum_type>
	{
		name1,
		name2,
		name3(value3),
		name4
	}
```

* The **enum_type** can be one of the following types: *byte*, *ubyte*, *short*, *ushort*, *int*, *uint*, *long* and *ulong*.
For example if you choose *byte*, then your enum values must be between *-128* and *127*.
* Also you can specify the value of enum names optionally in parentheses. By default, values start from 0 and increase.
* Enums don't have attributes.

Example:

```ini
[EColor]
_def = enum <byte>
	{
		white,
		red(3),
		green,
		blue(-2),
		black
	}
```

Python generated code:

```python
class EColor(Enum):
	white = 0
	red = 3
	green = 4
	blue = -2
	black = -1
```

Note that the **enum_type** will be used in *serializer* and *deserializer* functions in classes.

#### Class

Structure:

```ini
[ClassName]
_def = class
attribute1 = attribute_type
attribute2 = attribute_type
```

Inheritance:

```ini
[ChildClassName]
_def = class(ParentClassName1, ParentClassName2, ...)
attribute1 = attribute_type
attribute2 = attribute_type
```

* The **attribute_type** can either be *simple data types*, *complex data types*, *enums* or other *classes*.
* In case you want to add new functions to your classes or other similar operations, be noted that it is not possible to add them in the **ks** file. You must create your own class, inherit it from the generated class, and then add your desired functions to this class.
* Each generated class has three functions:

> **initialize:** Initializes all attributes of the instance to default value.
> 
> **serialize:** Serializes the instance to string or bytearray.
> 
> **deserialize:** Deserializes given string or bytearray to instance.

* The instance can be initialized using **init** argument of the constructor. Recursive initialization is not supported yet.
* Attributes with **Null** or **None** value are not supported in *serialize* function yet. Assigning a value to all the attributes is essential before serialization.
* Arrays must be initialized before serialization or deserialization.

Example:

```ini
[Parent1]
_def = class
count = uint


[Parent2]
_def = class
number = long


[Child]
_def = class(Parent1, Parent2)
name = string
```

Python generated code:

See [inheritance.py](https://github.com/k04la/serializer/tree/master/examples/inheritance.py)

## Full Example

See [full.ks](https://github.com/k04la/serializer/tree/master/examples/full.ks) example and run the below commands as noted:

In bash:

	$ koalasc examples/full.ks python .

In python shell:

```python
>>> from full import Test
>>> t1 = Test(init=True)
>>> t1.v14.initialize()
>>> t1.v12 = "hello"
>>> t1.v15 = [1, 2, 3]
>>> t1.v17 = {'one': 1, 'two': 2}
>>> s = t1.serialize()

>>> t2 = Test(init=True)
>>> t2.deserialize(s)
>>> assert t1.v12 == t2.v12
>>> assert t1.v15 == t2.v15
>>> assert t1.v17 == t2.v17
```

## TODO

* Pass initial value of attributes via constructor.
* Support recursive initialization.
* Advanced optimization and compression.
* Add code generators for other programming languages like **C++**, **Java** and **C#**. Currently, **Python** is the only supported language.
* Support *Null* values.
