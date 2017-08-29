# K04lA Object Serializer
KoalaSerializer is a tool designed for creating serializable objects. This is useful when you want to send an object via a socket. For example consider having a server written in C++ and a client written in Python. Suppose you want to send an object from your server to the client. Imagine a game server that wants to send a snapshot of the game world to clients. The snapshot object must be serialized in the server, sent via a socket, and deserialized in the client. KoalaSerializer enables you to do the first and last steps easily.


## Getting Started


### Install

	$ sudo pip install koala-serializer

### Generate Codes

After installation, define your objects in a **ks** file. Examples can be found [here](https://github.com/k04la/serializer/tree/master/examples).
To generate source codes run the command below (the *output_dir* is optional):

	$ koalasc <ks_path> <programming_language> <output_dir>

The *programming_language* can be **python** or **cpp**.

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
string  |  str  |  std::string |


### Complex Data Types

KS Type  |  Python Type  |  C++ Type
---  |  ---  |  ---
list <data_type>  |  list  |  std::vector<data_type>
map <data_type1, data_type2>  |  dict  |  std::map<data_type1, data_type2>
array[dim1_size][dim2_size]...[dimN_size] <data_type>  |  multi-dim list  |  std::array<std::array< ... std::array<data_type, dimN_size> ... , dim2_size>, dim1_size>

* The **data_type** can either be *simple data types*, *complex data types*, *enums* or other *classes*.

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
* Also the enum name values can be optionally specified in perantheses. By default, values start from 0 and increase.
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

C++ generated code:

```c++
enum class EColor
{
	white = 0,
	red = 3,
	green = 4,
	blue = -2,
	black = -1,
};
```

Note that the **enum_type** will be used in *serialize* and *deserialize* methods in classes.

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
* In case you want to add new methods to your classes or other similar operations, be noted that it is not possible to add them in the **ks** file. You must create your own class, inherit it from the generated class, and then add your desired methods to this class.
* Each generated class has four methods:

> **name:** Returns the *class name* of an *instance* (or *class* in Python).
> 
> **initialize:** Initializes all attributes of the instance to the given value or *Null*.
> 
> **serialize:** Serializes the instance to string or bytearray.
> 
> **deserialize:** Deserializes given string or bytearray to instance.

* Initial values of the attributes can be passed as arguments to the *constructor* or *initialize* method.

**C++** extras:

* Methods:

> **nameStatic:** A static method that returns the *class name* of a *class*. Do **not** use this method for *instances*. Use the **name** method instead.
> 
> **getters:** Return a copy of attributes. Their names are same as attributes.
> 
> **reference getters:** Return reference of attributes. Their names start with **ref_** and end with an attribute name.
> 
> **setters:** Given a reference value, these methods set the attributes. Their names are same as attributes.
> 
> **has_attribute getters and setters:** They are used to handle *Null* values. Their names start with **has_** and end with an attribute name.

* Inner *Null* values are not supported in **C++**.

* Every generated class inherits **KSObject** class. The **KSObject** is an abstract class that is implemented as below:

	```c++
	class KSObject
	{
	public:
		static std::string nameStatic() { return ""; };
		virtual std::string name() const = 0;
		virtual std::string serialize() const = 0;
		virtual unsigned int deserialize(const std::string &, unsigned int) = 0;
	};
	```

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

C++ generated code:

See [inheritance.h](https://github.com/k04la/serializer/tree/master/examples/inheritance.h)

## Full Example

See [full.ks](https://github.com/k04la/serializer/tree/master/examples/full.ks) example and run the below commands as noted:

### Python:

In bash:

	$ koalasc examples/full.ks python

In python shell:

```python
>>> from full import Test
>>> t1 = Test()
>>> t1.v12 = "hello"
>>> t1.v15 = [1, 2, 3]
>>> t1.v17 = {'one': 1, 'two': 2}
>>> s = t1.serialize()

>>> t2 = Test()
>>> t2.deserialize(s)
>>> assert t1.v12 == t2.v12
>>> assert t1.v15 == t2.v15
>>> assert t1.v17 == t2.v17
```

### C++:

In bash:

	$ koalasc examples/full.ks cpp

main.cpp:
```c++
#include <iostream>
#include <assert.h>

#include "full.h"

using namespace std;
using namespace ks;
using namespace ks::full;

int main()
{
	Test t1;
	t1.v12("hello");

	t1.ref_v15().push_back(1);
	t1.ref_v15().push_back(2);
	t1.ref_v15().push_back(3);
	t1.has_v15(true);

	map<string, int> v17;
	v17["one"] = 1;
	v17["two"] = 2;
	t1.v17(v17);

	string s = t1.serialize();

	Test t2;
	t2.deserialize(s);
	assert(t1.v12() == t2.v12());
	assert(t1.v15() == t2.v15());
	assert(t1.v17() == t2.v17());
	assert(t1.has_v12() == true);
	assert(t1.has_v11() == false);
}
```

## TODO

* Advanced optimization and compression.
* Add code generators for other programming languages like **Java** and **C#**. Currently, **Python** and **C++ 11** are the supported languages.
