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


	def __init__(self, v0=None, v1=None, v2=None, v3=None, v4=None, v5=None, v6=None, v7=None, v8=None, v9=None, v10=None, v11=None, v12=None, v13=None, v14=None, v15=None, v16=None, v17=None, v18=None, v19=None, v20=None):
		self.initialize(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20)
	

	def initialize(self, v0=None, v1=None, v2=None, v3=None, v4=None, v5=None, v6=None, v7=None, v8=None, v9=None, v10=None, v11=None, v12=None, v13=None, v14=None, v15=None, v16=None, v17=None, v18=None, v19=None, v20=None):
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
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.v0
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.v0 = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v0 = None
		
		# deserialize self.v1
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.v1 = struct.unpack('c', s[offset:offset + 1])[0]
			offset += 1
			self.v1 = self.v1.decode('ISO-8859-1') if PY3 else self.v1
		else:
			self.v1 = None
		
		# deserialize self.v2
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			self.v2 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v2 = None
		
		# deserialize self.v3
		tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp32:
			self.v3 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.v3 = None
		
		# deserialize self.v4
		tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp33:
			self.v4 = struct.unpack('h', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.v4 = None
		
		# deserialize self.v5
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			self.v5 = struct.unpack('H', s[offset:offset + 2])[0]
			offset += 2
		else:
			self.v5 = None
		
		# deserialize self.v6
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			self.v6 = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v6 = None
		
		# deserialize self.v7
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			self.v7 = struct.unpack('I', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v7 = None
		
		# deserialize self.v8
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			self.v8 = struct.unpack('q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v8 = None
		
		# deserialize self.v9
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			self.v9 = struct.unpack('Q', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v9 = None
		
		# deserialize self.v10
		tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp39:
			self.v10 = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.v10 = None
		
		# deserialize self.v11
		tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp40:
			self.v11 = struct.unpack('d', s[offset:offset + 8])[0]
			offset += 8
		else:
			self.v11 = None
		
		# deserialize self.v12
		tmp41 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp41:
			tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp43 = s[offset:offset + tmp42]
			offset += tmp42
			tmp43 += b'\x00' * (4 - tmp42)
			tmp44 = struct.unpack('I', tmp43)[0]
			
			self.v12 = s[offset:offset + tmp44].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp44]
			offset += tmp44
		else:
			self.v12 = None
		
		# deserialize self.v13
		tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp45:
			tmp46 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.v13 = EColor(tmp46)
		else:
			self.v13 = None
		
		# deserialize self.v14
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			if self.v14 is None:
				self.v14 = Child()
			offset = self.v14.deserialize(s, offset)
		else:
			self.v14 = None
		
		# deserialize self.v15
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp50 = s[offset:offset + tmp49]
			offset += tmp49
			tmp50 += b'\x00' * (4 - tmp49)
			tmp51 = struct.unpack('I', tmp50)[0]
			
			self.v15 = []
			for tmp52 in range(tmp51):
				tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp54:
					tmp53 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp53 = None
				self.v15.append(tmp53)
		else:
			self.v15 = None
		
		# deserialize self.v16
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp57 = s[offset:offset + tmp56]
			offset += tmp56
			tmp57 += b'\x00' * (4 - tmp56)
			tmp58 = struct.unpack('I', tmp57)[0]
			
			self.v16 = []
			for tmp59 in range(tmp58):
				tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp61:
					tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp63 = s[offset:offset + tmp62]
					offset += tmp62
					tmp63 += b'\x00' * (4 - tmp62)
					tmp64 = struct.unpack('I', tmp63)[0]
					
					tmp60 = []
					for tmp65 in range(tmp64):
						tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp67:
							tmp66 = struct.unpack('c', s[offset:offset + 1])[0]
							offset += 1
							tmp66 = tmp66.decode('ISO-8859-1') if PY3 else tmp66
						else:
							tmp66 = None
						tmp60.append(tmp66)
				else:
					tmp60 = None
				self.v16.append(tmp60)
		else:
			self.v16 = None
		
		# deserialize self.v17
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
			tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp70 = s[offset:offset + tmp69]
			offset += tmp69
			tmp70 += b'\x00' * (4 - tmp69)
			tmp71 = struct.unpack('I', tmp70)[0]
			
			self.v17 = {}
			for tmp72 in range(tmp71):
				tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp75:
					tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp77 = s[offset:offset + tmp76]
					offset += tmp76
					tmp77 += b'\x00' * (4 - tmp76)
					tmp78 = struct.unpack('I', tmp77)[0]
					
					tmp73 = s[offset:offset + tmp78].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp78]
					offset += tmp78
				else:
					tmp73 = None
				tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp79:
					tmp74 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp74 = None
				self.v17[tmp73] = tmp74
		else:
			self.v17 = None
		
		# deserialize self.v18
		tmp80 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp80:
			tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp82 = s[offset:offset + tmp81]
			offset += tmp81
			tmp82 += b'\x00' * (4 - tmp81)
			tmp83 = struct.unpack('I', tmp82)[0]
			
			self.v18 = {}
			for tmp84 in range(tmp83):
				tmp87 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp87:
					tmp85 = struct.unpack('c', s[offset:offset + 1])[0]
					offset += 1
					tmp85 = tmp85.decode('ISO-8859-1') if PY3 else tmp85
				else:
					tmp85 = None
				tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp88:
					tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp90 = s[offset:offset + tmp89]
					offset += tmp89
					tmp90 += b'\x00' * (4 - tmp89)
					tmp91 = struct.unpack('I', tmp90)[0]
					
					tmp86 = []
					for tmp92 in range(tmp91):
						tmp94 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp94:
							tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							tmp96 = s[offset:offset + tmp95]
							offset += tmp95
							tmp96 += b'\x00' * (4 - tmp95)
							tmp97 = struct.unpack('I', tmp96)[0]
							
							tmp93 = {}
							for tmp98 in range(tmp97):
								tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								if tmp101:
									tmp99 = struct.unpack('d', s[offset:offset + 8])[0]
									offset += 8
								else:
									tmp99 = None
								tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								if tmp102:
									tmp103 = struct.unpack('b', s[offset:offset + 1])[0]
									offset += 1
									tmp100 = EColor(tmp103)
								else:
									tmp100 = None
								tmp93[tmp99] = tmp100
						else:
							tmp93 = None
						tmp86.append(tmp93)
				else:
					tmp86 = None
				self.v18[tmp85] = tmp86
		else:
			self.v18 = None
		
		# deserialize self.v19
		tmp104 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp104:
			self.v19 = [None for _ in range(10)]
			for tmp105 in range(10):
				tmp106 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp106:
					self.v19[tmp105] = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
				else:
					self.v19[tmp105] = None
		else:
			self.v19 = None
		
		# deserialize self.v20
		tmp107 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp107:
			self.v20 = [[None for _ in range(10)] for _ in range(20)]
			for tmp108 in range(10):
				for tmp109 in range(20):
					tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					if tmp110:
						tmp111 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						tmp112 = s[offset:offset + tmp111]
						offset += tmp111
						tmp112 += b'\x00' * (4 - tmp111)
						tmp113 = struct.unpack('I', tmp112)[0]
						
						self.v20[tmp108][tmp109] = []
						for tmp114 in range(tmp113):
							tmp116 = struct.unpack('B', s[offset:offset + 1])[0]
							offset += 1
							if tmp116:
								tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
								offset += 1
								tmp118 = s[offset:offset + tmp117]
								offset += tmp117
								tmp118 += b'\x00' * (4 - tmp117)
								tmp119 = struct.unpack('I', tmp118)[0]
								
								tmp115 = s[offset:offset + tmp119].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp119]
								offset += tmp119
							else:
								tmp115 = None
							self.v20[tmp108][tmp109].append(tmp115)
					else:
						self.v20[tmp108][tmp109] = None
		else:
			self.v20 = None
		
		return offset
