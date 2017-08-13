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


	def __init__(self, count=None, init=False):
		super(Parent, self).__init__()
	
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


class Child(Parent):

	@staticmethod
	def name():
		return 'Child'


	def __init__(self, init=False):
		super(Child, self).__init__()
	
		if init:
			self.initialize()
	

	def initialize(self):
		Parent.initialize(self)
		
		return
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Parent.serialize(self)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Parent.deserialize(self, s, offset)
		
		return offset
