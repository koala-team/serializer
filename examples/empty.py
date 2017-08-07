# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Parent(object):

	@staticmethod
	def get_name():
		return 'Parent'


	def __init__(self, init=False):
		super(Parent, self).__init__()
	
		if init:
			self.initialize()
		else:
			self.count = None
	

	def initialize(self):
		self.count = int()
	

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
	def get_name():
		return 'Child'