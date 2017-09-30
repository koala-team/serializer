# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class EColor(Enum):
	white = 0
	red = 3
	green = 4
	blue = -2
	black = -1


class Parent1(object):

	@staticmethod
	def name():
		return 'Parent1'


	def __init__(self, p1=None):
		self.initialize(p1)
	

	def initialize(self, p1=None):
		self.p1 = p1
	

	def serialize(self):
		s = b''
		
		# serialize self.p1
		s += b'\x00' if self.p1 is None else b'\x01'
		if self.p1 is not None:
			s += struct.pack('I', self.p1)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.p1
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.p1 = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.p1 = None
		
		return offset


class Parent2(object):

	@staticmethod
	def name():
		return 'Parent2'


	def __init__(self, p2=None):
		self.initialize(p2)
	

	def initialize(self, p2=None):
		self.p2 = p2
	

	def serialize(self):
		s = b''
		
		# serialize self.p2
		s += b'\x00' if self.p2 is None else b'\x01'
		if self.p2 is not None:
			s += struct.pack('q', self.p2)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.p2
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.p2 = struct.unpack('q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.p2 = None
		
		return offset


class Child(Parent1, Parent2):

	@staticmethod
	def name():
		return 'Child'


	def __init__(self, c=None):
		self.initialize(c)
	

	def initialize(self, c=None):
		Parent1.initialize(self)
		Parent2.initialize(self)
		
		self.c = c
	

	def serialize(self):
		s = b''
		
		# serialize parents
		s += Parent1.serialize(self)
		s += Parent2.serialize(self)
		
		# serialize self.c
		s += b'\x00' if self.c is None else b'\x01'
		if self.c is not None:
			tmp2 = b''
			tmp2 += struct.pack('I', len(self.c))
			while len(tmp2) and tmp2[-1] == b'\x00'[0]:
				tmp2 = tmp2[:-1]
			s += struct.pack('B', len(tmp2))
			s += tmp2
			
			s += self.c.encode('ISO-8859-1') if PY3 else self.c
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize parents
		offset = Parent1.deserialize(self, s, offset)
		offset = Parent2.deserialize(self, s, offset)
		
		# deserialize self.c
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp5 = s[offset:offset + tmp4]
			offset += tmp4
			tmp5 += b'\x00' * (4 - tmp4)
			tmp6 = struct.unpack('I', tmp5)[0]
			
			self.c = s[offset:offset + tmp6].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp6]
			offset += tmp6
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
			tmp7 = b''
			tmp7 += struct.pack('I', len(self.v12))
			while len(tmp7) and tmp7[-1] == b'\x00'[0]:
				tmp7 = tmp7[:-1]
			s += struct.pack('B', len(tmp7))
			s += tmp7
			
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
			tmp8 = b''
			tmp8 += struct.pack('I', len(self.v15))
			while len(tmp8) and tmp8[-1] == b'\x00'[0]:
				tmp8 = tmp8[:-1]
			s += struct.pack('B', len(tmp8))
			s += tmp8
			
			for tmp9 in self.v15:
				s += b'\x00' if tmp9 is None else b'\x01'
				if tmp9 is not None:
					s += struct.pack('i', tmp9)
		
		# serialize self.v16
		s += b'\x00' if self.v16 is None else b'\x01'
		if self.v16 is not None:
			tmp10 = b''
			tmp10 += struct.pack('I', len(self.v16))
			while len(tmp10) and tmp10[-1] == b'\x00'[0]:
				tmp10 = tmp10[:-1]
			s += struct.pack('B', len(tmp10))
			s += tmp10
			
			for tmp11 in self.v16:
				s += b'\x00' if tmp11 is None else b'\x01'
				if tmp11 is not None:
					tmp12 = b''
					tmp12 += struct.pack('I', len(tmp11))
					while len(tmp12) and tmp12[-1] == b'\x00'[0]:
						tmp12 = tmp12[:-1]
					s += struct.pack('B', len(tmp12))
					s += tmp12
					
					for tmp13 in tmp11:
						s += b'\x00' if tmp13 is None else b'\x01'
						if tmp13 is not None:
							s += struct.pack('c', tmp13.encode('ISO-8859-1') if PY3 else tmp13)
		
		# serialize self.v17
		s += b'\x00' if self.v17 is None else b'\x01'
		if self.v17 is not None:
			tmp14 = b''
			tmp14 += struct.pack('I', len(self.v17))
			while len(tmp14) and tmp14[-1] == b'\x00'[0]:
				tmp14 = tmp14[:-1]
			s += struct.pack('B', len(tmp14))
			s += tmp14
			
			for tmp15 in self.v17:
				s += b'\x00' if tmp15 is None else b'\x01'
				if tmp15 is not None:
					tmp16 = b''
					tmp16 += struct.pack('I', len(tmp15))
					while len(tmp16) and tmp16[-1] == b'\x00'[0]:
						tmp16 = tmp16[:-1]
					s += struct.pack('B', len(tmp16))
					s += tmp16
					
					s += tmp15.encode('ISO-8859-1') if PY3 else tmp15
				s += b'\x00' if self.v17[tmp15] is None else b'\x01'
				if self.v17[tmp15] is not None:
					s += struct.pack('i', self.v17[tmp15])
		
		# serialize self.v18
		s += b'\x00' if self.v18 is None else b'\x01'
		if self.v18 is not None:
			tmp17 = b''
			tmp17 += struct.pack('I', len(self.v18))
			while len(tmp17) and tmp17[-1] == b'\x00'[0]:
				tmp17 = tmp17[:-1]
			s += struct.pack('B', len(tmp17))
			s += tmp17
			
			for tmp18 in self.v18:
				s += b'\x00' if tmp18 is None else b'\x01'
				if tmp18 is not None:
					s += struct.pack('c', tmp18.encode('ISO-8859-1') if PY3 else tmp18)
				s += b'\x00' if self.v18[tmp18] is None else b'\x01'
				if self.v18[tmp18] is not None:
					tmp19 = b''
					tmp19 += struct.pack('I', len(self.v18[tmp18]))
					while len(tmp19) and tmp19[-1] == b'\x00'[0]:
						tmp19 = tmp19[:-1]
					s += struct.pack('B', len(tmp19))
					s += tmp19
					
					for tmp20 in self.v18[tmp18]:
						s += b'\x00' if tmp20 is None else b'\x01'
						if tmp20 is not None:
							tmp21 = b''
							tmp21 += struct.pack('I', len(tmp20))
							while len(tmp21) and tmp21[-1] == b'\x00'[0]:
								tmp21 = tmp21[:-1]
							s += struct.pack('B', len(tmp21))
							s += tmp21
							
							for tmp22 in tmp20:
								s += b'\x00' if tmp22 is None else b'\x01'
								if tmp22 is not None:
									s += struct.pack('d', tmp22)
								s += b'\x00' if tmp20[tmp22] is None else b'\x01'
								if tmp20[tmp22] is not None:
									s += struct.pack('b', tmp20[tmp22].value)
		
		# serialize self.v19
		s += b'\x00' if self.v19 is None else b'\x01'
		if self.v19 is not None:
			for tmp23 in range(10):
				s += b'\x00' if self.v19[tmp23] is None else b'\x01'
				if self.v19[tmp23] is not None:
					s += struct.pack('b', self.v19[tmp23])
		
		# serialize self.v20
		s += b'\x00' if self.v20 is None else b'\x01'
		if self.v20 is not None:
			for tmp24 in range(10):
				for tmp25 in range(20):
					s += b'\x00' if self.v20[tmp24][tmp25] is None else b'\x01'
					if self.v20[tmp24][tmp25] is not None:
						tmp26 = b''
						tmp26 += struct.pack('I', len(self.v20[tmp24][tmp25]))
						while len(tmp26) and tmp26[-1] == b'\x00'[0]:
							tmp26 = tmp26[:-1]
						s += struct.pack('B', len(tmp26))
						s += tmp26
						
						for tmp27 in self.v20[tmp24][tmp25]:
							s += b'\x00' if tmp27 is None else b'\x01'
							if tmp27 is not None:
								tmp28 = b''
								tmp28 += struct.pack('I', len(tmp27))
								while len(tmp28) and tmp28[-1] == b'\x00'[0]:
									tmp28 = tmp28[:-1]
								s += struct.pack('B', len(tmp28))
								s += tmp28
								
								s += tmp27.encode('ISO-8859-1') if PY3 else tmp27
		
		# serialize self.v21
		s += b'\x00' if self.v21 is None else b'\x01'
		if self.v21 is not None:
			tmp29 = b''
			tmp29 += struct.pack('I', len(self.v21))
			while len(tmp29) and tmp29[-1] == b'\x00'[0]:
				tmp29 = tmp29[:-1]
			s += struct.pack('B', len(tmp29))
			s += tmp29
			
			for tmp30 in self.v21:
				s += b'\x00' if tmp30 is None else b'\x01'
				if tmp30 is not None:
					s += tmp30.serialize()
		
		# serialize self.v22
		s += b'\x00' if self.v22 is None else b'\x01'
		if self.v22 is not None:
			tmp31 = b''
			tmp31 += struct.pack('I', len(self.v22))
			while len(tmp31) and tmp31[-1] == b'\x00'[0]:
				tmp31 = tmp31[:-1]
			s += struct.pack('B', len(tmp31))
			s += tmp31
			
			for tmp32 in self.v22:
				s += b'\x00' if tmp32 is None else b'\x01'
				if tmp32 is not None:
					tmp33 = b''
					tmp33 += struct.pack('I', len(tmp32))
					while len(tmp33) and tmp33[-1] == b'\x00'[0]:
						tmp33 = tmp33[:-1]
					s += struct.pack('B', len(tmp33))
					s += tmp33
					
					s += tmp32.encode('ISO-8859-1') if PY3 else tmp32
				s += b'\x00' if self.v22[tmp32] is None else b'\x01'
				if self.v22[tmp32] is not None:
					s += self.v22[tmp32].serialize()
		
		# serialize self.v23
		s += b'\x00' if self.v23 is None else b'\x01'
		if self.v23 is not None:
			for tmp34 in range(5):
				for tmp35 in range(10):
					s += b'\x00' if self.v23[tmp34][tmp35] is None else b'\x01'
					if self.v23[tmp34][tmp35] is not None:
						s += self.v23[tmp34][tmp35].serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.v0
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			self.v0 = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v0 = None
		
		# deserialize self.v1
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			self.v1 = struct.unpack('c', s[offset:offset + 1])[0]
			offset += 1
			self.v1 = self.v1.decode('ISO-8859-1') if PY3 else self.v1
		else:
			self.v1 = None
		
		# deserialize self.v2
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			self.v2 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v2 = None
		
		# deserialize self.v3
		tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp39:
			self.v3 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v3 = None
		
		# deserialize self.v4
		tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp40:
			self.v4 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.v4 = None
		
		# deserialize self.v5
		tmp41 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp41:
			self.v5 = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.v5 = None
		
		# deserialize self.v6
		tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp42:
			self.v6 = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v6 = None
		
		# deserialize self.v7
		tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp43:
			self.v7 = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v7 = None
		
		# deserialize self.v8
		tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp44:
			self.v8 = struct.unpack('q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v8 = None
		
		# deserialize self.v9
		tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp45:
			self.v9 = struct.unpack('Q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v9 = None
		
		# deserialize self.v10
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			self.v10 = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v10 = None
		
		# deserialize self.v11
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			self.v11 = struct.unpack('d', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v11 = None
		
		# deserialize self.v12
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp50 = s[offset:offset + tmp49]
			offset += tmp49
			tmp50 += b'\x00' * (4 - tmp49)
			tmp51 = struct.unpack('I', tmp50)[0]
			
			self.v12 = s[offset:offset + tmp51].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp51]
			offset += tmp51
		else:
			self.v12 = None
		
		# deserialize self.v13
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			tmp53 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.v13 = EColor(tmp53)
		else:
			self.v13 = None
		
		# deserialize self.v14
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			self.v14 = Child()
			offset = self.v14.deserialize(s, offset)
		else:
			self.v14 = None
		
		# deserialize self.v15
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp57 = s[offset:offset + tmp56]
			offset += tmp56
			tmp57 += b'\x00' * (4 - tmp56)
			tmp58 = struct.unpack('I', tmp57)[0]
			
			self.v15 = []
			for tmp59 in range(tmp58):
				tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp61:
					tmp60 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp60 = None
				self.v15.append(tmp60)
		else:
			self.v15 = None
		
		# deserialize self.v16
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp64 = s[offset:offset + tmp63]
			offset += tmp63
			tmp64 += b'\x00' * (4 - tmp63)
			tmp65 = struct.unpack('I', tmp64)[0]
			
			self.v16 = []
			for tmp66 in range(tmp65):
				tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp68:
					tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp70 = s[offset:offset + tmp69]
					offset += tmp69
					tmp70 += b'\x00' * (4 - tmp69)
					tmp71 = struct.unpack('I', tmp70)[0]
					
					tmp67 = []
					for tmp72 in range(tmp71):
						tmp74 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp74:
							tmp73 = struct.unpack('c', s[offset:offset + 1])[0]
							offset += 1
							tmp73 = tmp73.decode('ISO-8859-1') if PY3 else tmp73
						else:
							tmp73 = None
						tmp67.append(tmp73)
				else:
					tmp67 = None
				self.v16.append(tmp67)
		else:
			self.v16 = None
		
		# deserialize self.v17
		tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp75:
			tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp77 = s[offset:offset + tmp76]
			offset += tmp76
			tmp77 += b'\x00' * (4 - tmp76)
			tmp78 = struct.unpack('I', tmp77)[0]
			
			self.v17 = {}
			for tmp79 in range(tmp78):
				tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp82:
					tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp84 = s[offset:offset + tmp83]
					offset += tmp83
					tmp84 += b'\x00' * (4 - tmp83)
					tmp85 = struct.unpack('I', tmp84)[0]
					
					tmp80 = s[offset:offset + tmp85].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp85]
					offset += tmp85
				else:
					tmp80 = None
				tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp86:
					tmp81 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp81 = None
				self.v17[tmp80] = tmp81
		else:
			self.v17 = None
		
		# deserialize self.v18
		tmp87 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp87:
			tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp89 = s[offset:offset + tmp88]
			offset += tmp88
			tmp89 += b'\x00' * (4 - tmp88)
			tmp90 = struct.unpack('I', tmp89)[0]
			
			self.v18 = {}
			for tmp91 in range(tmp90):
				tmp94 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp94:
					tmp92 = struct.unpack('c', s[offset:offset + 1])[0]
					offset += 1
					tmp92 = tmp92.decode('ISO-8859-1') if PY3 else tmp92
				else:
					tmp92 = None
				tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp95:
					tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp97 = s[offset:offset + tmp96]
					offset += tmp96
					tmp97 += b'\x00' * (4 - tmp96)
					tmp98 = struct.unpack('I', tmp97)[0]
					
					tmp93 = []
					for tmp99 in range(tmp98):
						tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp101:
							tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp103 = s[offset:offset + tmp102]
							offset += tmp102
							tmp103 += b'\x00' * (4 - tmp102)
							tmp104 = struct.unpack('I', tmp103)[0]
							
							tmp100 = {}
							for tmp105 in range(tmp104):
								tmp108 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								if tmp108:
									tmp106 = struct.unpack('d', s[offset:offset + 8])[0]
									offset += 8
								else:
									tmp106 = None
								tmp109 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								if tmp109:
									tmp110 = struct.unpack('b', s[offset:offset + 1])[0]
									offset += 1
									tmp107 = EColor(tmp110)
								else:
									tmp107 = None
								tmp100[tmp106] = tmp107
						else:
							tmp100 = None
						tmp93.append(tmp100)
				else:
					tmp93 = None
				self.v18[tmp92] = tmp93
		else:
			self.v18 = None
		
		# deserialize self.v19
		tmp111 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp111:
			self.v19 = [None for _ in range(10)]
			for tmp112 in range(10):
				tmp113 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp113:
					self.v19[tmp112] = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
				else:
					self.v19[tmp112] = None
		else:
			self.v19 = None
		
		# deserialize self.v20
		tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp114:
			self.v20 = [[None for _ in range(10)] for _ in range(20)]
			for tmp115 in range(10):
				for tmp116 in range(20):
					tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					if tmp117:
						tmp118 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						tmp119 = s[offset:offset + tmp118]
						offset += tmp118
						tmp119 += b'\x00' * (4 - tmp118)
						tmp120 = struct.unpack('I', tmp119)[0]
						
						self.v20[tmp115][tmp116] = []
						for tmp121 in range(tmp120):
							tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							if tmp123:
								tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								tmp125 = s[offset:offset + tmp124]
								offset += tmp124
								tmp125 += b'\x00' * (4 - tmp124)
								tmp126 = struct.unpack('I', tmp125)[0]
								
								tmp122 = s[offset:offset + tmp126].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp126]
								offset += tmp126
							else:
								tmp122 = None
							self.v20[tmp115][tmp116].append(tmp122)
					else:
						self.v20[tmp115][tmp116] = None
		else:
			self.v20 = None
		
		# deserialize self.v21
		tmp127 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp127:
			tmp128 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp129 = s[offset:offset + tmp128]
			offset += tmp128
			tmp129 += b'\x00' * (4 - tmp128)
			tmp130 = struct.unpack('I', tmp129)[0]
			
			self.v21 = []
			for tmp131 in range(tmp130):
				tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp133:
					tmp132 = Child()
					offset = tmp132.deserialize(s, offset)
				else:
					tmp132 = None
				self.v21.append(tmp132)
		else:
			self.v21 = None
		
		# deserialize self.v22
		tmp134 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp134:
			tmp135 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp136 = s[offset:offset + tmp135]
			offset += tmp135
			tmp136 += b'\x00' * (4 - tmp135)
			tmp137 = struct.unpack('I', tmp136)[0]
			
			self.v22 = {}
			for tmp138 in range(tmp137):
				tmp141 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp141:
					tmp142 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp143 = s[offset:offset + tmp142]
					offset += tmp142
					tmp143 += b'\x00' * (4 - tmp142)
					tmp144 = struct.unpack('I', tmp143)[0]
					
					tmp139 = s[offset:offset + tmp144].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp144]
					offset += tmp144
				else:
					tmp139 = None
				tmp145 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp145:
					tmp140 = Child()
					offset = tmp140.deserialize(s, offset)
				else:
					tmp140 = None
				self.v22[tmp139] = tmp140
		else:
			self.v22 = None
		
		# deserialize self.v23
		tmp146 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp146:
			self.v23 = [[None for _ in range(5)] for _ in range(10)]
			for tmp147 in range(5):
				for tmp148 in range(10):
					tmp149 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					if tmp149:
						self.v23[tmp147][tmp148] = Child()
						offset = self.v23[tmp147][tmp148].deserialize(s, offset)
					else:
						self.v23[tmp147][tmp148] = None
		else:
			self.v23 = None
		
		return offset
