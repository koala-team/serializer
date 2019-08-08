# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Parent(object):

	@staticmethod
	def name():
		return 'Parent'


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


class Child(Parent):

	@staticmethod
	def name():
		return 'Child'


	def __init__(self, count=None):
		self.initialize(count)
	

	def initialize(self, count=None):
		Parent.initialize(self, count)
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Parent.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Parent.deserialize(self, s, offset)
		
		return offset
