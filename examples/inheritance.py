# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Parent1(object):

	@staticmethod
	def get_name():
		return 'Parent1'


	def __init__(self, count=None, init=False):
		super(Parent1, self).__init__()
	
		if init:
			self.initialize(count)
		else:
			self.count = count
	

	def initialize(self, count=None):
		self.count = count or int()
	

	def serialize(self):
		s = b''
		
		# serialize self.count
		s += struct.pack('I', self.count)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.count
		self.count = struct.unpack('I', s[offset:offset + 4])[0]
		offset += 4
		
		return offset


class Parent2(object):

	@staticmethod
	def get_name():
		return 'Parent2'


	def __init__(self, number=None, init=False):
		super(Parent2, self).__init__()
	
		if init:
			self.initialize(number)
		else:
			self.number = number
	

	def initialize(self, number=None):
		self.number = number or int()
	

	def serialize(self):
		s = b''
		
		# serialize self.number
		s += struct.pack('q', self.number)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.number
		self.number = struct.unpack('q', s[offset:offset + 8])[0]
		offset += 8
		
		return offset


class Child(Parent1, Parent2):

	@staticmethod
	def get_name():
		return 'Child'


	def __init__(self, name=None, init=False):
		super(Child, self).__init__()
	
		if init:
			self.initialize(name)
		else:
			self.name = name
	

	def initialize(self, name=None):
		Parent1.initialize(self)
		Parent2.initialize(self)
		
		self.name = name or str()
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Parent1.serialize(self)
		s += Parent2.serialize(self)
		
		# serialize self.name
		tmp0 = b''
		tmp0 += struct.pack('I', len(self.name))
		while len(tmp0) and tmp0[-1] == b'\x00'[0]:
			tmp0 = tmp0[:-1]
		s += struct.pack('B', len(tmp0))
		s += tmp0
		
		s += self.name.encode('ISO-8859-1') if PY3 else self.name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Parent1.deserialize(self, s, offset)
		offset = Parent2.deserialize(self, s, offset)
		
		# deserialize self.name
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		tmp2 = s[offset:offset + tmp1]
		offset += tmp1
		tmp2 += b'\x00' * (4 - tmp1)
		tmp3 = struct.unpack('I', tmp2)[0]
		
		self.name = s[offset:offset + tmp3].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp3]
		offset += tmp3
		
		return offset
