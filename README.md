# Koala Object Serializer

`Koala Serializer` is a tool designed for creating serializable objects. This is useful when you want to send an object via a socket. For example consider having a server written in **C++** and a client written in **Python**. Suppose you want to send an object from your server to the client. Imagine a game server that wants to send a snapshot of the game world to clients. The snapshot object must be serialized in the server, sent via a socket, and deserialized in the client. `Koala Serializer` enables you to do the first and last steps easily.

## Getting Started

### Install

    $ sudo pip install koala-serializer

### Generate Codes

After installation, define your objects in a **ks** file. Examples can be found [here](https://github.com/koala-team/serializer/tree/master/examples).
To generate source codes run the command below (the *output_dir* is optional):

    $ koalasc <ks_path> <programming_language> <output_dir> <capitalization_rule>

The *programming_language* can be **python**, **cpp** or **cs**.
The *capitalization_rule* can be **snake_case**, **camelCase** or **PascalCase**.

## Usage

### KS Structure

**ks** is a Koala serializer format that enables you to simply define your objects.
Basically the **ks** file has the same structure as the [**ini**](https://en.wikipedia.org/wiki/INI_file) files (so all features of **ini** format like commenting etc. are supported).

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

KS Type  |  Python Type  |  C++ Type  |  C# Type  |  Standard Size
---  |  ---  |  ---  |  ---  | ---
boolean  |  bool  |  bool  |  bool  |  1
char  |  str (of size 1)  |  char  |  char  |  1
byte  |  int  |  signed char  |  sbyte  |  1
ubyte  |  int  |  unsigned char  |  byte  |  1
short  |  int  |  short  |  short  |  2
ushort  |  int  |  unsigned short  |  ushort  |  2
int  |  int  |  int  |  int  |  4
uint  |  int  |  unsigned int  |  uint  |  4
long  |  int  |  long long  |  long  |  8
ulong  |  int  |  unsigned long long  |  ulong  |  8
float  |  float  |  float  |  float  |  4
double  |  float  |  double  |  double  |  8
string  |  str  |  std::string  |  string  |

### Complex Data Types

KS Type  |  Python Type  |  C++ Type  |  C# Type
---  |  ---  |  ---
list <data_type>  |  list  |  std::vector<data_type>  |  List<data_type>
map <data_type1, data_type2>  |  dict  |  std::map<data_type1, data_type2>  |  Dictionary<data_type1, data_type2>
array[dim1_size][dim2_size]...[dimN_size] <data_type>  |  multi-dim list  |  std::array<std::array< ... std::array<data_type, dimN_size> ... , dim2_size>, dim1_size>  |  multi-dim array

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

* Also the enum name values can be optionally specified in parentheses. By default, values start from 0 and increase.

* Enums don't have attributes.

Example:

```ini
[EColor]
_def = enum <byte>
    {
        White,
        Red(3),
        Green,
        Blue(-2),
        Black
    }
```

Python generated code:

```python
class EColor(Enum):
    White = 0
    Red = 3
    Green = 4
    Blue = -2
    Black = -1
```

C++ generated code:

```c++
enum class EColor
{
    White = 0,
    Red = 3,
    Green = 4,
    Blue = -2,
    Black = -1,
};
```

C# generated code:

```c#
public enum EColor
{
    White = 0,
    Red = 3,
    Green = 4,
    Blue = -2,
    Black = -1,
}
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
> **serialize:** Serializes the instance to string or bytearray.
>
> **deserialize:** Deserializes given string or bytearray to instance.

**Python** extras:

* Methods:

> **initialize:** Initializes all attributes of the instance to the given value or *Null*.

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
        static inline const std::string nameStatic() { return ""; }
        virtual inline const std::string name() const = 0;
        virtual std::string serialize() const = 0;
        virtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;
    };
    ```

**C#** extras:

* Methods:

> **NameStatic:** A static method that returns the *class name* of a *class*. Do **not** use this method for *instances*. Use the **Name** method instead.

* **C#** does not support multiple inheritance. So only first parent will be considered and a warning will be shown when generating the class codes.

* Every generated class inherits **KSObject** class. The **KSObject** is an abstract class that is implemented as below:

    ```c#
    using System;

    namespace ks
    {
        public abstract class KSObject
        {
            public static string NameStatic => "";
            public abstract string Name { get; }
            public abstract byte[] Serialize();
            public abstract uint Deserialize(byte[] s, uint offset = 0);
        }
    } // namespace ks
    ```

* This code can be found in a generated file named **KSObject.cs**.

### Coding Style

In order to use **Capitalization Rules** properly, it is supposed to implement **ks** files with these capitalization rules:

> **Enum Names**: PascalCase
>
> **Enum Attributes**: PascalCase
>
> **Class Names**: PascalCase
>
> **Class Attributes**: snake_case
>
> **Module Names**: snake_case

Then your selected capitalization rule will just be applied to **Class Attributes**.
**PascalCase** rule will be used for generating `C#` file names and namespaces.

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

See [inheritance.py](https://github.com/koala-team/serializer/tree/master/examples/inheritance.py)

C++ generated code:

See [inheritance.h](https://github.com/koala-team/serializer/tree/master/examples/inheritance.h)

C# generated code:

See [Inheritance.cs](https://github.com/koala-team/serializer/tree/master/examples/Inheritance.cs)

## Full Example

See [full.ks](https://github.com/koala-team/serializer/tree/master/examples/full.ks) example and run the below commands as noted:

### Python

In bash:

    $ koalasc examples/full.ks python . snake_case

In python shell:

```python
>>> from full import Test, Child
>>> t1 = Test()
>>> t1.v12 = "hello"
>>> t1.v15 = [1, 2, 3]
>>> t1.v17 = {'one': 1, 'two': 2}
>>> t1.v22 = {'one': Child(c='first'), 'two': Child(c='second', first_name='baby', _last_name_='knight')}
>>> s = t1.serialize()

>>> t2 = Test()
>>> t2.deserialize(s)
>>> assert t1.v12 == t2.v12
>>> assert t1.v15 == t2.v15
>>> assert t1.v17 == t2.v17
>>> assert t1.v22['one'].__dict__ == t2.v22['one'].__dict__ and t1.v22['two'].__dict__ == t2.v22['two'].__dict__
```

### C++

In bash:

    $ koalasc examples/full.ks cpp . camelCase

main.cpp:

``` c++
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

    map<string, Child> v22;
    v22["one"] = Child();
    v22["two"] = Child();
    v22["one"].c("first");
    v22["two"].c("second");
    v22["two"].firstName("baby");
    v22["two"]._lastName_("knight");
    t1.v22(v22);

    string s = t1.serialize();

    Test t2;
    t2.deserialize(s);
    assert(t1.v12() == t2.v12());
    assert(t1.v15() == t2.v15());
    assert(t1.v17() == t2.v17());
    assert(t1.v22()["one"].c() == t2.v22()["one"].c() && t1.v22()["two"].c() == t2.v22()["two"].c());
    assert(t1.v22()["two"].firstName() == t2.v22()["two"].firstName());
    assert(t1.v22()["two"]._lastName_() == t2.v22()["two"]._lastName_());
    assert(t1.has_v12() == true);
    assert(t1.has_v11() == false);
}
```

### C#

In bash:

    $ koalasc examples/full.ks cs . PascalCase

Program.cs:

``` c#
using System;
using System.Linq;
using System.Collections.Generic;
using System.Diagnostics;

using KS;
using KS.Full;

namespace CsTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Test t1 = new Test();
            t1.V12 = "hello";

            t1.V15 = new List<int?> {1, 2, 3 };

            t1.V17 = new Dictionary<string, int?>
            {
                ["one"] = 1,
                ["two"] = 2
            };

            t1.V22 = new Dictionary<string, Child>()
            {
                ["one"] = new Child() { C = "first" },
                ["two"] = new Child() { C = "second", FirstName = "baby", _LastName_ = "knight" }
            };

            byte[] s = t1.Serialize();

            Test t2 = new Test();
            t2.Deserialize(s);
            Debug.Assert(t1.V12.Equals(t2.V12));
            Debug.Assert(t1.V15.SequenceEqual(t2.V15));
            Debug.Assert(t1.V17.SequenceEqual(t2.V17));
            Debug.Assert(t1.V22["one"].C.Equals(t2.V22["one"].C) && t1.V22["two"].C.Equals(t2.V22["two"].C));
            Debug.Assert(t1.V22["two"].FirstName.Equals(t2.V22["two"].FirstName));
            Debug.Assert(t1.V22["two"]._LastName_.Equals(t2.V22["two"]._LastName_));
        }
    }
}
```

## TODO

* Advanced optimization and compression.
* Add code generators for other programming languages like **Java**. Currently, **Python**, **C++ 11** and **C#** are the supported languages.
