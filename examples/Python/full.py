# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class EColor(Enum):
	White = 0
	Red = 3
	Green = 4
	Blue = -2
	Black = -1


class Parent(object):

	@staticmethod
	def name():
		return 'Parent'


	def __init__(self, first_name=None, _last_name_=None):
		self.initialize(first_name, _last_name_)
	

	def initialize(self, first_name=None, _last_name_=None):
		self.first_name = first_name
		self._last_name_ = _last_name_
	

	def serialize(self):
		s = b''
		
		# serialize self.first_name
		s += b'\x00' if self.first_name is None else b'\x01'
		if self.first_name is not None:
			tmp0 = b''
			tmp0 += struct.pack('I', len(self.first_name))
			while len(tmp0) and tmp0[-1] == b'\x00'[0]:
				tmp0 = tmp0[:-1]
			s += struct.pack('B', len(tmp0))
			s += tmp0
			
			s += self.first_name.encode('ISO-8859-1') if PY3 else self.first_name
		
		# serialize self._last_name_
		s += b'\x00' if self._last_name_ is None else b'\x01'
		if self._last_name_ is not None:
			tmp1 = b''
			tmp1 += struct.pack('I', len(self._last_name_))
			while len(tmp1) and tmp1[-1] == b'\x00'[0]:
				tmp1 = tmp1[:-1]
			s += struct.pack('B', len(tmp1))
			s += tmp1
			
			s += self._last_name_.encode('ISO-8859-1') if PY3 else self._last_name_
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.first_name
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp4 = s[offset:offset + tmp3]
			offset += tmp3
			tmp4 += b'\x00' * (4 - tmp3)
			tmp5 = struct.unpack('I', tmp4)[0]
			
			self.first_name = s[offset:offset + tmp5].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp5]
			offset += tmp5
		else:
			self.first_name = None
		
		# deserialize self._last_name_
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp8 = s[offset:offset + tmp7]
			offset += tmp7
			tmp8 += b'\x00' * (4 - tmp7)
			tmp9 = struct.unpack('I', tmp8)[0]
			
			self._last_name_ = s[offset:offset + tmp9].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp9]
			offset += tmp9
		else:
			self._last_name_ = None
		
		return offset


class Child(Parent):

	@staticmethod
	def name():
		return 'Child'


	def __init__(self, first_name=None, _last_name_=None, c=None):
		self.initialize(first_name, _last_name_, c)
	

	def initialize(self, first_name=None, _last_name_=None, c=None):
		Parent.initialize(self, first_name, _last_name_)
		
		self.c = c
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Parent.serialize(self)
		
		# serialize self.c
		s += b'\x00' if self.c is None else b'\x01'
		if self.c is not None:
			tmp10 = b''
			tmp10 += struct.pack('I', len(self.c))
			while len(tmp10) and tmp10[-1] == b'\x00'[0]:
				tmp10 = tmp10[:-1]
			s += struct.pack('B', len(tmp10))
			s += tmp10
			
			s += self.c.encode('ISO-8859-1') if PY3 else self.c
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Parent.deserialize(self, s, offset)
		
		# deserialize self.c
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp13 = s[offset:offset + tmp12]
			offset += tmp12
			tmp13 += b'\x00' * (4 - tmp12)
			tmp14 = struct.unpack('I', tmp13)[0]
			
			self.c = s[offset:offset + tmp14].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp14]
			offset += tmp14
		else:
			self.c = None
		
		return offset


class Test(object):

	@staticmethod
	def name():
		return 'Test'


	def __init__(self, v0=None, v1=None, v2=None, v3=None, v4=None, v5=None, v6=None, v7=None, v8=None, v9=None, v10=None, v11=None, v12=None, v13=None, v14=None, v15=None, v16=None, v17=None, v18=None, v19=None, v20=None, v21=None, v22=None, v23=None):
		self.initialize(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23)
	

	def initialize(self, v0=None, v1=None, v2=None, v3=None, v4=None, v5=None, v6=None, v7=None, v8=None, v9=None, v10=None, v11=None, v12=None, v13=None, v14=None, v15=None, v16=None, v17=None, v18=None, v19=None, v20=None, v21=None, v22=None, v23=None):
		self.v0 = v0
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3
		self.v4 = v4
		self.v5 = v5
		self.v6 = v6
		self.v7 = v7
		self.v8 = v8
		self.v9 = v9
		self.v10 = v10
		self.v11 = v11
		self.v12 = v12
		self.v13 = v13
		self.v14 = v14
		self.v15 = v15
		self.v16 = v16
		self.v17 = v17
		self.v18 = v18
		self.v19 = v19
		self.v20 = v20
		self.v21 = v21
		self.v22 = v22
		self.v23 = v23
	

	def serialize(self):
		s = b''
		
		# serialize self.v0
		s += b'\x00' if self.v0 is None else b'\x01'
		if self.v0 is not None:
			s += struct.pack('?', self.v0)
		
		# serialize self.v1
		s += b'\x00' if self.v1 is None else b'\x01'
		if self.v1 is not None:
			s += struct.pack('c', self.v1.encode('ISO-8859-1') if PY3 else self.v1)
		
		# serialize self.v2
		s += b'\x00' if self.v2 is None else b'\x01'
		if self.v2 is not None:
			s += struct.pack('b', self.v2)
		
		# serialize self.v3
		s += b'\x00' if self.v3 is None else b'\x01'
		if self.v3 is not None:
			s += struct.pack('B', self.v3)
		
		# serialize self.v4
		s += b'\x00' if self.v4 is None else b'\x01'
		if self.v4 is not None:
			s += struct.pack('h', self.v4)
		
		# serialize self.v5
		s += b'\x00' if self.v5 is None else b'\x01'
		if self.v5 is not None:
			s += struct.pack('H', self.v5)
		
		# serialize self.v6
		s += b'\x00' if self.v6 is None else b'\x01'
		if self.v6 is not None:
			s += struct.pack('i', self.v6)
		
		# serialize self.v7
		s += b'\x00' if self.v7 is None else b'\x01'
		if self.v7 is not None:
			s += struct.pack('I', self.v7)
		
		# serialize self.v8
		s += b'\x00' if self.v8 is None else b'\x01'
		if self.v8 is not None:
			s += struct.pack('q', self.v8)
		
		# serialize self.v9
		s += b'\x00' if self.v9 is None else b'\x01'
		if self.v9 is not None:
			s += struct.pack('Q', self.v9)
		
		# serialize self.v10
		s += b'\x00' if self.v10 is None else b'\x01'
		if self.v10 is not None:
			s += struct.pack('f', self.v10)
		
		# serialize self.v11
		s += b'\x00' if self.v11 is None else b'\x01'
		if self.v11 is not None:
			s += struct.pack('d', self.v11)
		
		# serialize self.v12
		s += b'\x00' if self.v12 is None else b'\x01'
		if self.v12 is not None:
			tmp15 = b''
			tmp15 += struct.pack('I', len(self.v12))
			while len(tmp15) and tmp15[-1] == b'\x00'[0]:
				tmp15 = tmp15[:-1]
			s += struct.pack('B', len(tmp15))
			s += tmp15
			
			s += self.v12.encode('ISO-8859-1') if PY3 else self.v12
		
		# serialize self.v13
		s += b'\x00' if self.v13 is None else b'\x01'
		if self.v13 is not None:
			s += struct.pack('b', self.v13.value)
		
		# serialize self.v14
		s += b'\x00' if self.v14 is None else b'\x01'
		if self.v14 is not None:
			s += self.v14.serialize()
		
		# serialize self.v15
		s += b'\x00' if self.v15 is None else b'\x01'
		if self.v15 is not None:
			tmp16 = b''
			tmp16 += struct.pack('I', len(self.v15))
			while len(tmp16) and tmp16[-1] == b'\x00'[0]:
				tmp16 = tmp16[:-1]
			s += struct.pack('B', len(tmp16))
			s += tmp16
			
			for tmp17 in self.v15:
				s += b'\x00' if tmp17 is None else b'\x01'
				if tmp17 is not None:
					s += struct.pack('i', tmp17)
		
		# serialize self.v16
		s += b'\x00' if self.v16 is None else b'\x01'
		if self.v16 is not None:
			tmp18 = b''
			tmp18 += struct.pack('I', len(self.v16))
			while len(tmp18) and tmp18[-1] == b'\x00'[0]:
				tmp18 = tmp18[:-1]
			s += struct.pack('B', len(tmp18))
			s += tmp18
			
			for tmp19 in self.v16:
				s += b'\x00' if tmp19 is None else b'\x01'
				if tmp19 is not None:
					tmp20 = b''
					tmp20 += struct.pack('I', len(tmp19))
					while len(tmp20) and tmp20[-1] == b'\x00'[0]:
						tmp20 = tmp20[:-1]
					s += struct.pack('B', len(tmp20))
					s += tmp20
					
					for tmp21 in tmp19:
						s += b'\x00' if tmp21 is None else b'\x01'
						if tmp21 is not None:
							s += struct.pack('c', tmp21.encode('ISO-8859-1') if PY3 else tmp21)
		
		# serialize self.v17
		s += b'\x00' if self.v17 is None else b'\x01'
		if self.v17 is not None:
			tmp22 = b''
			tmp22 += struct.pack('I', len(self.v17))
			while len(tmp22) and tmp22[-1] == b'\x00'[0]:
				tmp22 = tmp22[:-1]
			s += struct.pack('B', len(tmp22))
			s += tmp22
			
			for tmp23 in self.v17:
				s += b'\x00' if tmp23 is None else b'\x01'
				if tmp23 is not None:
					tmp24 = b''
					tmp24 += struct.pack('I', len(tmp23))
					while len(tmp24) and tmp24[-1] == b'\x00'[0]:
						tmp24 = tmp24[:-1]
					s += struct.pack('B', len(tmp24))
					s += tmp24
					
					s += tmp23.encode('ISO-8859-1') if PY3 else tmp23
				s += b'\x00' if self.v17[tmp23] is None else b'\x01'
				if self.v17[tmp23] is not None:
					s += struct.pack('i', self.v17[tmp23])
		
		# serialize self.v18
		s += b'\x00' if self.v18 is None else b'\x01'
		if self.v18 is not None:
			tmp25 = b''
			tmp25 += struct.pack('I', len(self.v18))
			while len(tmp25) and tmp25[-1] == b'\x00'[0]:
				tmp25 = tmp25[:-1]
			s += struct.pack('B', len(tmp25))
			s += tmp25
			
			for tmp26 in self.v18:
				s += b'\x00' if tmp26 is None else b'\x01'
				if tmp26 is not None:
					s += struct.pack('c', tmp26.encode('ISO-8859-1') if PY3 else tmp26)
				s += b'\x00' if self.v18[tmp26] is None else b'\x01'
				if self.v18[tmp26] is not None:
					tmp27 = b''
					tmp27 += struct.pack('I', len(self.v18[tmp26]))
					while len(tmp27) and tmp27[-1] == b'\x00'[0]:
						tmp27 = tmp27[:-1]
					s += struct.pack('B', len(tmp27))
					s += tmp27
					
					for tmp28 in self.v18[tmp26]:
						s += b'\x00' if tmp28 is None else b'\x01'
						if tmp28 is not None:
							tmp29 = b''
							tmp29 += struct.pack('I', len(tmp28))
							while len(tmp29) and tmp29[-1] == b'\x00'[0]:
								tmp29 = tmp29[:-1]
							s += struct.pack('B', len(tmp29))
							s += tmp29
							
							for tmp30 in tmp28:
								s += b'\x00' if tmp30 is None else b'\x01'
								if tmp30 is not None:
									s += struct.pack('d', tmp30)
								s += b'\x00' if tmp28[tmp30] is None else b'\x01'
								if tmp28[tmp30] is not None:
									s += struct.pack('b', tmp28[tmp30].value)
		
		# serialize self.v19
		s += b'\x00' if self.v19 is None else b'\x01'
		if self.v19 is not None:
			for tmp31 in range(10):
				s += b'\x00' if self.v19[tmp31] is None else b'\x01'
				if self.v19[tmp31] is not None:
					s += struct.pack('b', self.v19[tmp31])
		
		# serialize self.v20
		s += b'\x00' if self.v20 is None else b'\x01'
		if self.v20 is not None:
			for tmp32 in range(10):
				for tmp33 in range(20):
					s += b'\x00' if self.v20[tmp32][tmp33] is None else b'\x01'
					if self.v20[tmp32][tmp33] is not None:
						tmp34 = b''
						tmp34 += struct.pack('I', len(self.v20[tmp32][tmp33]))
						while len(tmp34) and tmp34[-1] == b'\x00'[0]:
							tmp34 = tmp34[:-1]
						s += struct.pack('B', len(tmp34))
						s += tmp34
						
						for tmp35 in self.v20[tmp32][tmp33]:
							s += b'\x00' if tmp35 is None else b'\x01'
							if tmp35 is not None:
								tmp36 = b''
								tmp36 += struct.pack('I', len(tmp35))
								while len(tmp36) and tmp36[-1] == b'\x00'[0]:
									tmp36 = tmp36[:-1]
								s += struct.pack('B', len(tmp36))
								s += tmp36
								
								s += tmp35.encode('ISO-8859-1') if PY3 else tmp35
		
		# serialize self.v21
		s += b'\x00' if self.v21 is None else b'\x01'
		if self.v21 is not None:
			tmp37 = b''
			tmp37 += struct.pack('I', len(self.v21))
			while len(tmp37) and tmp37[-1] == b'\x00'[0]:
				tmp37 = tmp37[:-1]
			s += struct.pack('B', len(tmp37))
			s += tmp37
			
			for tmp38 in self.v21:
				s += b'\x00' if tmp38 is None else b'\x01'
				if tmp38 is not None:
					for tmp39 in range(4):
						s += b'\x00' if tmp38[tmp39] is None else b'\x01'
						if tmp38[tmp39] is not None:
							s += tmp38[tmp39].serialize()
		
		# serialize self.v22
		s += b'\x00' if self.v22 is None else b'\x01'
		if self.v22 is not None:
			tmp40 = b''
			tmp40 += struct.pack('I', len(self.v22))
			while len(tmp40) and tmp40[-1] == b'\x00'[0]:
				tmp40 = tmp40[:-1]
			s += struct.pack('B', len(tmp40))
			s += tmp40
			
			for tmp41 in self.v22:
				s += b'\x00' if tmp41 is None else b'\x01'
				if tmp41 is not None:
					tmp42 = b''
					tmp42 += struct.pack('I', len(tmp41))
					while len(tmp42) and tmp42[-1] == b'\x00'[0]:
						tmp42 = tmp42[:-1]
					s += struct.pack('B', len(tmp42))
					s += tmp42
					
					s += tmp41.encode('ISO-8859-1') if PY3 else tmp41
				s += b'\x00' if self.v22[tmp41] is None else b'\x01'
				if self.v22[tmp41] is not None:
					s += self.v22[tmp41].serialize()
		
		# serialize self.v23
		s += b'\x00' if self.v23 is None else b'\x01'
		if self.v23 is not None:
			for tmp43 in range(5):
				for tmp44 in range(10):
					s += b'\x00' if self.v23[tmp43][tmp44] is None else b'\x01'
					if self.v23[tmp43][tmp44] is not None:
						s += self.v23[tmp43][tmp44].serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.v0
		tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp45:
			self.v0 = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v0 = None
		
		# deserialize self.v1
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			self.v1 = struct.unpack('c', s[offset:offset + 1])[0]
			offset += 1
			self.v1 = self.v1.decode('ISO-8859-1') if PY3 else self.v1
		else:
			self.v1 = None
		
		# deserialize self.v2
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			self.v2 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v2 = None
		
		# deserialize self.v3
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			self.v3 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v3 = None
		
		# deserialize self.v4
		tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp49:
			self.v4 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.v4 = None
		
		# deserialize self.v5
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			self.v5 = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.v5 = None
		
		# deserialize self.v6
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			self.v6 = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v6 = None
		
		# deserialize self.v7
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			self.v7 = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v7 = None
		
		# deserialize self.v8
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			self.v8 = struct.unpack('q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v8 = None
		
		# deserialize self.v9
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			self.v9 = struct.unpack('Q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v9 = None
		
		# deserialize self.v10
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			self.v10 = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v10 = None
		
		# deserialize self.v11
		tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp56:
			self.v11 = struct.unpack('d', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v11 = None
		
		# deserialize self.v12
		tmp57 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp57:
			tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp59 = s[offset:offset + tmp58]
			offset += tmp58
			tmp59 += b'\x00' * (4 - tmp58)
			tmp60 = struct.unpack('I', tmp59)[0]
			
			self.v12 = s[offset:offset + tmp60].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp60]
			offset += tmp60
		else:
			self.v12 = None
		
		# deserialize self.v13
		tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp61:
			tmp62 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.v13 = EColor(tmp62)
		else:
			self.v13 = None
		
		# deserialize self.v14
		tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp63:
			self.v14 = Child()
			offset = self.v14.deserialize(s, offset)
		else:
			self.v14 = None
		
		# deserialize self.v15
		tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp64:
			tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp66 = s[offset:offset + tmp65]
			offset += tmp65
			tmp66 += b'\x00' * (4 - tmp65)
			tmp67 = struct.unpack('I', tmp66)[0]
			
			self.v15 = []
			for tmp68 in range(tmp67):
				tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp70:
					tmp69 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp69 = None
				self.v15.append(tmp69)
		else:
			self.v15 = None
		
		# deserialize self.v16
		tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp71:
			tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp73 = s[offset:offset + tmp72]
			offset += tmp72
			tmp73 += b'\x00' * (4 - tmp72)
			tmp74 = struct.unpack('I', tmp73)[0]
			
			self.v16 = []
			for tmp75 in range(tmp74):
				tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp77:
					tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp79 = s[offset:offset + tmp78]
					offset += tmp78
					tmp79 += b'\x00' * (4 - tmp78)
					tmp80 = struct.unpack('I', tmp79)[0]
					
					tmp76 = []
					for tmp81 in range(tmp80):
						tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp83:
							tmp82 = struct.unpack('c', s[offset:offset + 1])[0]
							offset += 1
							tmp82 = tmp82.decode('ISO-8859-1') if PY3 else tmp82
						else:
							tmp82 = None
						tmp76.append(tmp82)
				else:
					tmp76 = None
				self.v16.append(tmp76)
		else:
			self.v16 = None
		
		# deserialize self.v17
		tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp84:
			tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp86 = s[offset:offset + tmp85]
			offset += tmp85
			tmp86 += b'\x00' * (4 - tmp85)
			tmp87 = struct.unpack('I', tmp86)[0]
			
			self.v17 = {}
			for tmp88 in range(tmp87):
				tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp91:
					tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp93 = s[offset:offset + tmp92]
					offset += tmp92
					tmp93 += b'\x00' * (4 - tmp92)
					tmp94 = struct.unpack('I', tmp93)[0]
					
					tmp89 = s[offset:offset + tmp94].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp94]
					offset += tmp94
				else:
					tmp89 = None
				tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp95:
					tmp90 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp90 = None
				self.v17[tmp89] = tmp90
		else:
			self.v17 = None
		
		# deserialize self.v18
		tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp96:
			tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp98 = s[offset:offset + tmp97]
			offset += tmp97
			tmp98 += b'\x00' * (4 - tmp97)
			tmp99 = struct.unpack('I', tmp98)[0]
			
			self.v18 = {}
			for tmp100 in range(tmp99):
				tmp103 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp103:
					tmp101 = struct.unpack('c', s[offset:offset + 1])[0]
					offset += 1
					tmp101 = tmp101.decode('ISO-8859-1') if PY3 else tmp101
				else:
					tmp101 = None
				tmp104 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp104:
					tmp105 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp106 = s[offset:offset + tmp105]
					offset += tmp105
					tmp106 += b'\x00' * (4 - tmp105)
					tmp107 = struct.unpack('I', tmp106)[0]
					
					tmp102 = []
					for tmp108 in range(tmp107):
						tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp110:
							tmp111 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp112 = s[offset:offset + tmp111]
							offset += tmp111
							tmp112 += b'\x00' * (4 - tmp111)
							tmp113 = struct.unpack('I', tmp112)[0]
							
							tmp109 = {}
							for tmp114 in range(tmp113):
								tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								if tmp117:
									tmp115 = struct.unpack('d', s[offset:offset + 8])[0]
									offset += 8
								else:
									tmp115 = None
								tmp118 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								if tmp118:
									tmp119 = struct.unpack('b', s[offset:offset + 1])[0]
									offset += 1
									tmp116 = EColor(tmp119)
								else:
									tmp116 = None
								tmp109[tmp115] = tmp116
						else:
							tmp109 = None
						tmp102.append(tmp109)
				else:
					tmp102 = None
				self.v18[tmp101] = tmp102
		else:
			self.v18 = None
		
		# deserialize self.v19
		tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp120:
			self.v19 = [None for _ in range(10)]
			for tmp121 in range(10):
				tmp122 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp122:
					self.v19[tmp121] = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
				else:
					self.v19[tmp121] = None
		else:
			self.v19 = None
		
		# deserialize self.v20
		tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp123:
			self.v20 = [[None for _ in range(10)] for _ in range(20)]
			for tmp124 in range(10):
				for tmp125 in range(20):
					tmp126 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					if tmp126:
						tmp127 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						tmp128 = s[offset:offset + tmp127]
						offset += tmp127
						tmp128 += b'\x00' * (4 - tmp127)
						tmp129 = struct.unpack('I', tmp128)[0]
						
						self.v20[tmp124][tmp125] = []
						for tmp130 in range(tmp129):
							tmp132 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							if tmp132:
								tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								tmp134 = s[offset:offset + tmp133]
								offset += tmp133
								tmp134 += b'\x00' * (4 - tmp133)
								tmp135 = struct.unpack('I', tmp134)[0]
								
								tmp131 = s[offset:offset + tmp135].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp135]
								offset += tmp135
							else:
								tmp131 = None
							self.v20[tmp124][tmp125].append(tmp131)
					else:
						self.v20[tmp124][tmp125] = None
		else:
			self.v20 = None
		
		# deserialize self.v21
		tmp136 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp136:
			tmp137 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp138 = s[offset:offset + tmp137]
			offset += tmp137
			tmp138 += b'\x00' * (4 - tmp137)
			tmp139 = struct.unpack('I', tmp138)[0]
			
			self.v21 = []
			for tmp140 in range(tmp139):
				tmp142 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp142:
					tmp141 = [None for _ in range(4)]
					for tmp143 in range(4):
						tmp144 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp144:
							tmp141[tmp143] = Child()
							offset = tmp141[tmp143].deserialize(s, offset)
						else:
							tmp141[tmp143] = None
				else:
					tmp141 = None
				self.v21.append(tmp141)
		else:
			self.v21 = None
		
		# deserialize self.v22
		tmp145 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp145:
			tmp146 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp147 = s[offset:offset + tmp146]
			offset += tmp146
			tmp147 += b'\x00' * (4 - tmp146)
			tmp148 = struct.unpack('I', tmp147)[0]
			
			self.v22 = {}
			for tmp149 in range(tmp148):
				tmp152 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp152:
					tmp153 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp154 = s[offset:offset + tmp153]
					offset += tmp153
					tmp154 += b'\x00' * (4 - tmp153)
					tmp155 = struct.unpack('I', tmp154)[0]
					
					tmp150 = s[offset:offset + tmp155].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp155]
					offset += tmp155
				else:
					tmp150 = None
				tmp156 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp156:
					tmp151 = Child()
					offset = tmp151.deserialize(s, offset)
				else:
					tmp151 = None
				self.v22[tmp150] = tmp151
		else:
			self.v22 = None
		
		# deserialize self.v23
		tmp157 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp157:
			self.v23 = [[None for _ in range(5)] for _ in range(10)]
			for tmp158 in range(5):
				for tmp159 in range(10):
					tmp160 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					if tmp160:
						self.v23[tmp158][tmp159] = Child()
						offset = self.v23[tmp158][tmp159].deserialize(s, offset)
					else:
						self.v23[tmp158][tmp159] = None
		else:
			self.v23 = None
		
		return offset
