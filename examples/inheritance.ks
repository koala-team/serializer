[Parent1]
_def = class
count = uint


[Parent2]
_def = class
number = long


[Parent3]
_def = class


[Child]
_def = class(Parent1, Parent2)
firstname = string


[GrandChild]
_def = class(Child, Parent3)
height = float
