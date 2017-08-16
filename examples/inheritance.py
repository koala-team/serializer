# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Parent1(object):

	@staticmethod
	def name():
		return 'Parent1'


	def __init__(self, count=None):
		self.initialize(count)
	

	def initialize(self, count=None):
		self.count = count
	

	def serialize(self):
		s = b''
		
		# serialize self.count
		s += b'\x00' if self.count is None else b'\x01'
		if self.count is not None:
			s += struct.pack('I', self.count)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.count
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.count = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.count = None
		
		return offset


class Parent2(object):

	@staticmethod
	def name():
		return 'Parent2'


	def __init__(self, number=None):
		self.initialize(number)
	

	def initialize(self, number=None):
		self.number = number
	

	def serialize(self):
		s = b''
		
		# serialize self.number
		s += b'\x00' if self.number is None else b'\x01'
		if self.number is not None:
			s += struct.pack('q', self.number)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.number
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.number = struct.unpack('q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.number = None
		
		return offset


class Child(Parent1, Parent2):

	@staticmethod
	def name():
		return 'Child'


	def __init__(self, name=None):
		self.initialize(name)
	

	def initialize(self, name=None):
		Parent1.initialize(self)
		Parent2.initialize(self)
		
		self.name = name
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Parent1.serialize(self)
		s += Parent2.serialize(self)
		
		# serialize self.name
		s += b'\x00' if self.name is None else b'\x01'
		if self.name is not None:
			tmp2 = b''
			tmp2 += struct.pack('I', len(self.name))
			while len(tmp2) and tmp2[-1] == b'\x00'[0]:
				tmp2 = tmp2[:-1]
			s += struct.pack('B', len(tmp2))
			s += tmp2
			
			s += self.name.encode('ISO-8859-1') if PY3 else self.name
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Parent1.deserialize(self, s, offset)
		offset = Parent2.deserialize(self, s, offset)
		
		# deserialize self.name
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp5 = s[offset:offset + tmp4]
			offset += tmp4
			tmp5 += b'\x00' * (4 - tmp4)
			tmp6 = struct.unpack('I', tmp5)[0]
			
			self.name = s[offset:offset + tmp6].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp6]
			offset += tmp6
		else:
			self.name = None
		
		return offset
