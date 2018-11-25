using System;
using System.Linq;
using System.Collections.Generic;

namespace ks.full
{
	public enum EColor
	{
		white = 0,
		red = 3,
		green = 4,
		blue = -2,
		black = -1,
	}
	
	public class Parent : KSObject
	{
		public string FirstName { get; set; }
		public string _LastName_ { get; set; }
		

		public Parent()
		{
		}
		
		public new static string NameStatic => "Parent";
		
		public override string Name => "Parent";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize FirstName
			s.Add((byte)((FirstName == null) ? 0 : 1));
			if (FirstName != null)
			{
				List<byte> tmp0 = new List<byte>();
				tmp0.AddRange(BitConverter.GetBytes((uint)FirstName.Count()));
				while (tmp0.Count > 0 && tmp0.Last() == 0)
					tmp0.RemoveAt(tmp0.Count - 1);
				s.Add((byte)tmp0.Count);
				s.AddRange(tmp0);
				
				s.AddRange(System.Text.Encoding.ASCII.GetBytes(FirstName));
			}
			
			// serialize _LastName_
			s.Add((byte)((_LastName_ == null) ? 0 : 1));
			if (_LastName_ != null)
			{
				List<byte> tmp1 = new List<byte>();
				tmp1.AddRange(BitConverter.GetBytes((uint)_LastName_.Count()));
				while (tmp1.Count > 0 && tmp1.Last() == 0)
					tmp1.RemoveAt(tmp1.Count - 1);
				s.Add((byte)tmp1.Count);
				s.AddRange(tmp1);
				
				s.AddRange(System.Text.Encoding.ASCII.GetBytes(_LastName_));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize FirstName
			byte tmp2;
			tmp2 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp2 == 1)
			{
				byte tmp3;
				tmp3 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp4 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp4, 0, tmp3);
				offset += tmp3;
				uint tmp5;
				tmp5 = BitConverter.ToUInt32(tmp4, (int)0);
				
				FirstName = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp5).ToArray());
				offset += tmp5;
			}
			else
				FirstName = null;
			
			// deserialize _LastName_
			byte tmp6;
			tmp6 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp6 == 1)
			{
				byte tmp7;
				tmp7 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp8 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp8, 0, tmp7);
				offset += tmp7;
				uint tmp9;
				tmp9 = BitConverter.ToUInt32(tmp8, (int)0);
				
				_LastName_ = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp9).ToArray());
				offset += tmp9;
			}
			else
				_LastName_ = null;
			
			return offset;
		}
	}
	
	public class Child : Parent
	{
		public string C { get; set; }
		

		public Child()
		{
		}
		
		public new static string NameStatic => "Child";
		
		public override string Name => "Child";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize parents
			s.AddRange(base.Serialize());
			
			// serialize C
			s.Add((byte)((C == null) ? 0 : 1));
			if (C != null)
			{
				List<byte> tmp10 = new List<byte>();
				tmp10.AddRange(BitConverter.GetBytes((uint)C.Count()));
				while (tmp10.Count > 0 && tmp10.Last() == 0)
					tmp10.RemoveAt(tmp10.Count - 1);
				s.Add((byte)tmp10.Count);
				s.AddRange(tmp10);
				
				s.AddRange(System.Text.Encoding.ASCII.GetBytes(C));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize parents
			offset = base.Deserialize(s, offset);
			
			// deserialize C
			byte tmp11;
			tmp11 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp11 == 1)
			{
				byte tmp12;
				tmp12 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp13 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp13, 0, tmp12);
				offset += tmp12;
				uint tmp14;
				tmp14 = BitConverter.ToUInt32(tmp13, (int)0);
				
				C = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp14).ToArray());
				offset += tmp14;
			}
			else
				C = null;
			
			return offset;
		}
	}
	
	public class Test : KSObject
	{
		public bool? V0 { get; set; }
		public char? V1 { get; set; }
		public sbyte? V2 { get; set; }
		public byte? V3 { get; set; }
		public short? V4 { get; set; }
		public ushort? V5 { get; set; }
		public int? V6 { get; set; }
		public uint? V7 { get; set; }
		public long? V8 { get; set; }
		public ulong? V9 { get; set; }
		public float? V10 { get; set; }
		public double? V11 { get; set; }
		public string V12 { get; set; }
		public EColor? V13 { get; set; }
		public Child V14 { get; set; }
		public List<int?> V15 { get; set; }
		public List<List<char?>> V16 { get; set; }
		public Dictionary<string, int?> V17 { get; set; }
		public Dictionary<char?, List<Dictionary<double?, EColor?>>> V18 { get; set; }
		public sbyte?[] V19 { get; set; }
		public List<string>[,] V20 { get; set; }
		public List<Child[]> V21 { get; set; }
		public Dictionary<string, Child> V22 { get; set; }
		public Child[,] V23 { get; set; }
		

		public Test()
		{
		}
		
		public new static string NameStatic => "Test";
		
		public override string Name => "Test";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize V0
			s.Add((byte)((V0 == null) ? 0 : 1));
			if (V0 != null)
			{
				s.AddRange(BitConverter.GetBytes((bool)V0));
			}
			
			// serialize V1
			s.Add((byte)((V1 == null) ? 0 : 1));
			if (V1 != null)
			{
				s.AddRange(BitConverter.GetBytes((char)V1));
			}
			
			// serialize V2
			s.Add((byte)((V2 == null) ? 0 : 1));
			if (V2 != null)
			{
				s.Add((byte)V2);
			}
			
			// serialize V3
			s.Add((byte)((V3 == null) ? 0 : 1));
			if (V3 != null)
			{
				s.Add((byte)V3);
			}
			
			// serialize V4
			s.Add((byte)((V4 == null) ? 0 : 1));
			if (V4 != null)
			{
				s.AddRange(BitConverter.GetBytes((short)V4));
			}
			
			// serialize V5
			s.Add((byte)((V5 == null) ? 0 : 1));
			if (V5 != null)
			{
				s.AddRange(BitConverter.GetBytes((ushort)V5));
			}
			
			// serialize V6
			s.Add((byte)((V6 == null) ? 0 : 1));
			if (V6 != null)
			{
				s.AddRange(BitConverter.GetBytes((int)V6));
			}
			
			// serialize V7
			s.Add((byte)((V7 == null) ? 0 : 1));
			if (V7 != null)
			{
				s.AddRange(BitConverter.GetBytes((uint)V7));
			}
			
			// serialize V8
			s.Add((byte)((V8 == null) ? 0 : 1));
			if (V8 != null)
			{
				s.AddRange(BitConverter.GetBytes((long)V8));
			}
			
			// serialize V9
			s.Add((byte)((V9 == null) ? 0 : 1));
			if (V9 != null)
			{
				s.AddRange(BitConverter.GetBytes((ulong)V9));
			}
			
			// serialize V10
			s.Add((byte)((V10 == null) ? 0 : 1));
			if (V10 != null)
			{
				s.AddRange(BitConverter.GetBytes((float)V10));
			}
			
			// serialize V11
			s.Add((byte)((V11 == null) ? 0 : 1));
			if (V11 != null)
			{
				s.AddRange(BitConverter.GetBytes((double)V11));
			}
			
			// serialize V12
			s.Add((byte)((V12 == null) ? 0 : 1));
			if (V12 != null)
			{
				List<byte> tmp15 = new List<byte>();
				tmp15.AddRange(BitConverter.GetBytes((uint)V12.Count()));
				while (tmp15.Count > 0 && tmp15.Last() == 0)
					tmp15.RemoveAt(tmp15.Count - 1);
				s.Add((byte)tmp15.Count);
				s.AddRange(tmp15);
				
				s.AddRange(System.Text.Encoding.ASCII.GetBytes(V12));
			}
			
			// serialize V13
			s.Add((byte)((V13 == null) ? 0 : 1));
			if (V13 != null)
			{
				s.Add((byte)((sbyte)V13));
			}
			
			// serialize V14
			s.Add((byte)((V14 == null) ? 0 : 1));
			if (V14 != null)
			{
				s.AddRange(V14.Serialize());
			}
			
			// serialize V15
			s.Add((byte)((V15 == null) ? 0 : 1));
			if (V15 != null)
			{
				List<byte> tmp16 = new List<byte>();
				tmp16.AddRange(BitConverter.GetBytes((uint)V15.Count()));
				while (tmp16.Count > 0 && tmp16.Last() == 0)
					tmp16.RemoveAt(tmp16.Count - 1);
				s.Add((byte)tmp16.Count);
				s.AddRange(tmp16);
				
				foreach (var tmp17 in V15)
				{
					s.Add((byte)((tmp17 == null) ? 0 : 1));
					if (tmp17 != null)
					{
						s.AddRange(BitConverter.GetBytes((int)tmp17));
					}
				}
			}
			
			// serialize V16
			s.Add((byte)((V16 == null) ? 0 : 1));
			if (V16 != null)
			{
				List<byte> tmp18 = new List<byte>();
				tmp18.AddRange(BitConverter.GetBytes((uint)V16.Count()));
				while (tmp18.Count > 0 && tmp18.Last() == 0)
					tmp18.RemoveAt(tmp18.Count - 1);
				s.Add((byte)tmp18.Count);
				s.AddRange(tmp18);
				
				foreach (var tmp19 in V16)
				{
					s.Add((byte)((tmp19 == null) ? 0 : 1));
					if (tmp19 != null)
					{
						List<byte> tmp20 = new List<byte>();
						tmp20.AddRange(BitConverter.GetBytes((uint)tmp19.Count()));
						while (tmp20.Count > 0 && tmp20.Last() == 0)
							tmp20.RemoveAt(tmp20.Count - 1);
						s.Add((byte)tmp20.Count);
						s.AddRange(tmp20);
						
						foreach (var tmp21 in tmp19)
						{
							s.Add((byte)((tmp21 == null) ? 0 : 1));
							if (tmp21 != null)
							{
								s.AddRange(BitConverter.GetBytes((char)tmp21));
							}
						}
					}
				}
			}
			
			// serialize V17
			s.Add((byte)((V17 == null) ? 0 : 1));
			if (V17 != null)
			{
				List<byte> tmp22 = new List<byte>();
				tmp22.AddRange(BitConverter.GetBytes((uint)V17.Count()));
				while (tmp22.Count > 0 && tmp22.Last() == 0)
					tmp22.RemoveAt(tmp22.Count - 1);
				s.Add((byte)tmp22.Count);
				s.AddRange(tmp22);
				
				foreach (var tmp23 in V17)
				{
					s.Add((byte)((tmp23.Key == null) ? 0 : 1));
					if (tmp23.Key != null)
					{
						List<byte> tmp24 = new List<byte>();
						tmp24.AddRange(BitConverter.GetBytes((uint)tmp23.Key.Count()));
						while (tmp24.Count > 0 && tmp24.Last() == 0)
							tmp24.RemoveAt(tmp24.Count - 1);
						s.Add((byte)tmp24.Count);
						s.AddRange(tmp24);
						
						s.AddRange(System.Text.Encoding.ASCII.GetBytes(tmp23.Key));
					}
					
					s.Add((byte)((tmp23.Value == null) ? 0 : 1));
					if (tmp23.Value != null)
					{
						s.AddRange(BitConverter.GetBytes((int)tmp23.Value));
					}
				}
			}
			
			// serialize V18
			s.Add((byte)((V18 == null) ? 0 : 1));
			if (V18 != null)
			{
				List<byte> tmp25 = new List<byte>();
				tmp25.AddRange(BitConverter.GetBytes((uint)V18.Count()));
				while (tmp25.Count > 0 && tmp25.Last() == 0)
					tmp25.RemoveAt(tmp25.Count - 1);
				s.Add((byte)tmp25.Count);
				s.AddRange(tmp25);
				
				foreach (var tmp26 in V18)
				{
					s.Add((byte)((tmp26.Key == null) ? 0 : 1));
					if (tmp26.Key != null)
					{
						s.AddRange(BitConverter.GetBytes((char)tmp26.Key));
					}
					
					s.Add((byte)((tmp26.Value == null) ? 0 : 1));
					if (tmp26.Value != null)
					{
						List<byte> tmp27 = new List<byte>();
						tmp27.AddRange(BitConverter.GetBytes((uint)tmp26.Value.Count()));
						while (tmp27.Count > 0 && tmp27.Last() == 0)
							tmp27.RemoveAt(tmp27.Count - 1);
						s.Add((byte)tmp27.Count);
						s.AddRange(tmp27);
						
						foreach (var tmp28 in tmp26.Value)
						{
							s.Add((byte)((tmp28 == null) ? 0 : 1));
							if (tmp28 != null)
							{
								List<byte> tmp29 = new List<byte>();
								tmp29.AddRange(BitConverter.GetBytes((uint)tmp28.Count()));
								while (tmp29.Count > 0 && tmp29.Last() == 0)
									tmp29.RemoveAt(tmp29.Count - 1);
								s.Add((byte)tmp29.Count);
								s.AddRange(tmp29);
								
								foreach (var tmp30 in tmp28)
								{
									s.Add((byte)((tmp30.Key == null) ? 0 : 1));
									if (tmp30.Key != null)
									{
										s.AddRange(BitConverter.GetBytes((double)tmp30.Key));
									}
									
									s.Add((byte)((tmp30.Value == null) ? 0 : 1));
									if (tmp30.Value != null)
									{
										s.Add((byte)((sbyte)tmp30.Value));
									}
								}
							}
						}
					}
				}
			}
			
			// serialize V19
			s.Add((byte)((V19 == null) ? 0 : 1));
			if (V19 != null)
			{
				for (uint tmp31 = 0; tmp31 < 10; tmp31++)
				{
					s.Add((byte)((V19[tmp31] == null) ? 0 : 1));
					if (V19[tmp31] != null)
					{
						s.Add((byte)V19[tmp31]);
					}
				}
			}
			
			// serialize V20
			s.Add((byte)((V20 == null) ? 0 : 1));
			if (V20 != null)
			{
				for (uint tmp32 = 0; tmp32 < 10; tmp32++)
				{
					for (uint tmp33 = 0; tmp33 < 20; tmp33++)
					{
						s.Add((byte)((V20[tmp32, tmp33] == null) ? 0 : 1));
						if (V20[tmp32, tmp33] != null)
						{
							List<byte> tmp34 = new List<byte>();
							tmp34.AddRange(BitConverter.GetBytes((uint)V20[tmp32, tmp33].Count()));
							while (tmp34.Count > 0 && tmp34.Last() == 0)
								tmp34.RemoveAt(tmp34.Count - 1);
							s.Add((byte)tmp34.Count);
							s.AddRange(tmp34);
							
							foreach (var tmp35 in V20[tmp32, tmp33])
							{
								s.Add((byte)((tmp35 == null) ? 0 : 1));
								if (tmp35 != null)
								{
									List<byte> tmp36 = new List<byte>();
									tmp36.AddRange(BitConverter.GetBytes((uint)tmp35.Count()));
									while (tmp36.Count > 0 && tmp36.Last() == 0)
										tmp36.RemoveAt(tmp36.Count - 1);
									s.Add((byte)tmp36.Count);
									s.AddRange(tmp36);
									
									s.AddRange(System.Text.Encoding.ASCII.GetBytes(tmp35));
								}
							}
						}
					}
				}
			}
			
			// serialize V21
			s.Add((byte)((V21 == null) ? 0 : 1));
			if (V21 != null)
			{
				List<byte> tmp37 = new List<byte>();
				tmp37.AddRange(BitConverter.GetBytes((uint)V21.Count()));
				while (tmp37.Count > 0 && tmp37.Last() == 0)
					tmp37.RemoveAt(tmp37.Count - 1);
				s.Add((byte)tmp37.Count);
				s.AddRange(tmp37);
				
				foreach (var tmp38 in V21)
				{
					s.Add((byte)((tmp38 == null) ? 0 : 1));
					if (tmp38 != null)
					{
						for (uint tmp39 = 0; tmp39 < 4; tmp39++)
						{
							s.Add((byte)((tmp38[tmp39] == null) ? 0 : 1));
							if (tmp38[tmp39] != null)
							{
								s.AddRange(tmp38[tmp39].Serialize());
							}
						}
					}
				}
			}
			
			// serialize V22
			s.Add((byte)((V22 == null) ? 0 : 1));
			if (V22 != null)
			{
				List<byte> tmp40 = new List<byte>();
				tmp40.AddRange(BitConverter.GetBytes((uint)V22.Count()));
				while (tmp40.Count > 0 && tmp40.Last() == 0)
					tmp40.RemoveAt(tmp40.Count - 1);
				s.Add((byte)tmp40.Count);
				s.AddRange(tmp40);
				
				foreach (var tmp41 in V22)
				{
					s.Add((byte)((tmp41.Key == null) ? 0 : 1));
					if (tmp41.Key != null)
					{
						List<byte> tmp42 = new List<byte>();
						tmp42.AddRange(BitConverter.GetBytes((uint)tmp41.Key.Count()));
						while (tmp42.Count > 0 && tmp42.Last() == 0)
							tmp42.RemoveAt(tmp42.Count - 1);
						s.Add((byte)tmp42.Count);
						s.AddRange(tmp42);
						
						s.AddRange(System.Text.Encoding.ASCII.GetBytes(tmp41.Key));
					}
					
					s.Add((byte)((tmp41.Value == null) ? 0 : 1));
					if (tmp41.Value != null)
					{
						s.AddRange(tmp41.Value.Serialize());
					}
				}
			}
			
			// serialize V23
			s.Add((byte)((V23 == null) ? 0 : 1));
			if (V23 != null)
			{
				for (uint tmp43 = 0; tmp43 < 5; tmp43++)
				{
					for (uint tmp44 = 0; tmp44 < 10; tmp44++)
					{
						s.Add((byte)((V23[tmp43, tmp44] == null) ? 0 : 1));
						if (V23[tmp43, tmp44] != null)
						{
							s.AddRange(V23[tmp43, tmp44].Serialize());
						}
					}
				}
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize V0
			byte tmp45;
			tmp45 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp45 == 1)
			{
				V0 = BitConverter.ToBoolean(s, (int)offset);
				offset += sizeof(bool);
			}
			else
				V0 = null;
			
			// deserialize V1
			byte tmp46;
			tmp46 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp46 == 1)
			{
				V1 = BitConverter.ToChar(s, (int)offset);
				offset += sizeof(char);
			}
			else
				V1 = null;
			
			// deserialize V2
			byte tmp47;
			tmp47 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp47 == 1)
			{
				V2 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
			}
			else
				V2 = null;
			
			// deserialize V3
			byte tmp48;
			tmp48 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp48 == 1)
			{
				V3 = (byte)s[(int)offset];
				offset += sizeof(byte);
			}
			else
				V3 = null;
			
			// deserialize V4
			byte tmp49;
			tmp49 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp49 == 1)
			{
				V4 = BitConverter.ToInt16(s, (int)offset);
				offset += sizeof(short);
			}
			else
				V4 = null;
			
			// deserialize V5
			byte tmp50;
			tmp50 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp50 == 1)
			{
				V5 = BitConverter.ToUInt16(s, (int)offset);
				offset += sizeof(ushort);
			}
			else
				V5 = null;
			
			// deserialize V6
			byte tmp51;
			tmp51 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp51 == 1)
			{
				V6 = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				V6 = null;
			
			// deserialize V7
			byte tmp52;
			tmp52 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp52 == 1)
			{
				V7 = BitConverter.ToUInt32(s, (int)offset);
				offset += sizeof(uint);
			}
			else
				V7 = null;
			
			// deserialize V8
			byte tmp53;
			tmp53 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp53 == 1)
			{
				V8 = BitConverter.ToInt64(s, (int)offset);
				offset += sizeof(long);
			}
			else
				V8 = null;
			
			// deserialize V9
			byte tmp54;
			tmp54 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp54 == 1)
			{
				V9 = BitConverter.ToUInt64(s, (int)offset);
				offset += sizeof(ulong);
			}
			else
				V9 = null;
			
			// deserialize V10
			byte tmp55;
			tmp55 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp55 == 1)
			{
				V10 = BitConverter.ToSingle(s, (int)offset);
				offset += sizeof(float);
			}
			else
				V10 = null;
			
			// deserialize V11
			byte tmp56;
			tmp56 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp56 == 1)
			{
				V11 = BitConverter.ToDouble(s, (int)offset);
				offset += sizeof(double);
			}
			else
				V11 = null;
			
			// deserialize V12
			byte tmp57;
			tmp57 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp57 == 1)
			{
				byte tmp58;
				tmp58 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp59 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp59, 0, tmp58);
				offset += tmp58;
				uint tmp60;
				tmp60 = BitConverter.ToUInt32(tmp59, (int)0);
				
				V12 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp60).ToArray());
				offset += tmp60;
			}
			else
				V12 = null;
			
			// deserialize V13
			byte tmp61;
			tmp61 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp61 == 1)
			{
				sbyte tmp62;
				tmp62 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				V13 = (EColor)tmp62;
			}
			else
				V13 = null;
			
			// deserialize V14
			byte tmp63;
			tmp63 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp63 == 1)
			{
				V14 = new Child();
				offset = V14.Deserialize(s, offset);
			}
			else
				V14 = null;
			
			// deserialize V15
			byte tmp64;
			tmp64 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp64 == 1)
			{
				byte tmp65;
				tmp65 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp66 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp66, 0, tmp65);
				offset += tmp65;
				uint tmp67;
				tmp67 = BitConverter.ToUInt32(tmp66, (int)0);
				
				V15 = new List<int?>();
				for (uint tmp68 = 0; tmp68 < tmp67; tmp68++)
				{
					int? tmp69;
					byte tmp70;
					tmp70 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp70 == 1)
					{
						tmp69 = BitConverter.ToInt32(s, (int)offset);
						offset += sizeof(int);
					}
					else
						tmp69 = null;
					V15.Add(tmp69);
				}
			}
			else
				V15 = null;
			
			// deserialize V16
			byte tmp71;
			tmp71 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp71 == 1)
			{
				byte tmp72;
				tmp72 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp73 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp73, 0, tmp72);
				offset += tmp72;
				uint tmp74;
				tmp74 = BitConverter.ToUInt32(tmp73, (int)0);
				
				V16 = new List<List<char?>>();
				for (uint tmp75 = 0; tmp75 < tmp74; tmp75++)
				{
					List<char?> tmp76;
					byte tmp77;
					tmp77 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp77 == 1)
					{
						byte tmp78;
						tmp78 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp79 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp79, 0, tmp78);
						offset += tmp78;
						uint tmp80;
						tmp80 = BitConverter.ToUInt32(tmp79, (int)0);
						
						tmp76 = new List<char?>();
						for (uint tmp81 = 0; tmp81 < tmp80; tmp81++)
						{
							char? tmp82;
							byte tmp83;
							tmp83 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp83 == 1)
							{
								tmp82 = BitConverter.ToChar(s, (int)offset);
								offset += sizeof(char);
							}
							else
								tmp82 = null;
							tmp76.Add(tmp82);
						}
					}
					else
						tmp76 = null;
					V16.Add(tmp76);
				}
			}
			else
				V16 = null;
			
			// deserialize V17
			byte tmp84;
			tmp84 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp84 == 1)
			{
				byte tmp85;
				tmp85 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp86 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp86, 0, tmp85);
				offset += tmp85;
				uint tmp87;
				tmp87 = BitConverter.ToUInt32(tmp86, (int)0);
				
				V17 = new Dictionary<string, int?>();
				for (uint tmp88 = 0; tmp88 < tmp87; tmp88++)
				{
					string tmp89;
					byte tmp91;
					tmp91 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp91 == 1)
					{
						byte tmp92;
						tmp92 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp93 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp93, 0, tmp92);
						offset += tmp92;
						uint tmp94;
						tmp94 = BitConverter.ToUInt32(tmp93, (int)0);
						
						tmp89 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp94).ToArray());
						offset += tmp94;
					}
					else
						tmp89 = null;
					
					int? tmp90;
					byte tmp95;
					tmp95 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp95 == 1)
					{
						tmp90 = BitConverter.ToInt32(s, (int)offset);
						offset += sizeof(int);
					}
					else
						tmp90 = null;
					
					V17[tmp89] = tmp90;
				}
			}
			else
				V17 = null;
			
			// deserialize V18
			byte tmp96;
			tmp96 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp96 == 1)
			{
				byte tmp97;
				tmp97 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp98 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp98, 0, tmp97);
				offset += tmp97;
				uint tmp99;
				tmp99 = BitConverter.ToUInt32(tmp98, (int)0);
				
				V18 = new Dictionary<char?, List<Dictionary<double?, EColor?>>>();
				for (uint tmp100 = 0; tmp100 < tmp99; tmp100++)
				{
					char? tmp101;
					byte tmp103;
					tmp103 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp103 == 1)
					{
						tmp101 = BitConverter.ToChar(s, (int)offset);
						offset += sizeof(char);
					}
					else
						tmp101 = null;
					
					List<Dictionary<double?, EColor?>> tmp102;
					byte tmp104;
					tmp104 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp104 == 1)
					{
						byte tmp105;
						tmp105 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp106 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp106, 0, tmp105);
						offset += tmp105;
						uint tmp107;
						tmp107 = BitConverter.ToUInt32(tmp106, (int)0);
						
						tmp102 = new List<Dictionary<double?, EColor?>>();
						for (uint tmp108 = 0; tmp108 < tmp107; tmp108++)
						{
							Dictionary<double?, EColor?> tmp109;
							byte tmp110;
							tmp110 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp110 == 1)
							{
								byte tmp111;
								tmp111 = (byte)s[(int)offset];
								offset += sizeof(byte);
								byte[] tmp112 = new byte[sizeof(uint)];
								Array.Copy(s, offset, tmp112, 0, tmp111);
								offset += tmp111;
								uint tmp113;
								tmp113 = BitConverter.ToUInt32(tmp112, (int)0);
								
								tmp109 = new Dictionary<double?, EColor?>();
								for (uint tmp114 = 0; tmp114 < tmp113; tmp114++)
								{
									double? tmp115;
									byte tmp117;
									tmp117 = (byte)s[(int)offset];
									offset += sizeof(byte);
									if (tmp117 == 1)
									{
										tmp115 = BitConverter.ToDouble(s, (int)offset);
										offset += sizeof(double);
									}
									else
										tmp115 = null;
									
									EColor? tmp116;
									byte tmp118;
									tmp118 = (byte)s[(int)offset];
									offset += sizeof(byte);
									if (tmp118 == 1)
									{
										sbyte tmp119;
										tmp119 = (sbyte)s[(int)offset];
										offset += sizeof(sbyte);
										tmp116 = (EColor)tmp119;
									}
									else
										tmp116 = null;
									
									tmp109[tmp115] = tmp116;
								}
							}
							else
								tmp109 = null;
							tmp102.Add(tmp109);
						}
					}
					else
						tmp102 = null;
					
					V18[tmp101] = tmp102;
				}
			}
			else
				V18 = null;
			
			// deserialize V19
			byte tmp120;
			tmp120 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp120 == 1)
			{
				V19 = new sbyte?[10];
				for (uint tmp121 = 0; tmp121 < 10; tmp121++)
				{
					byte tmp122;
					tmp122 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp122 == 1)
					{
						V19[tmp121] = (sbyte)s[(int)offset];
						offset += sizeof(sbyte);
					}
					else
						V19[tmp121] = null;
				}
			}
			else
				V19 = null;
			
			// deserialize V20
			byte tmp123;
			tmp123 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp123 == 1)
			{
				V20 = new List<string>[10, 20];
				for (uint tmp124 = 0; tmp124 < 10; tmp124++)
				{
					for (uint tmp125 = 0; tmp125 < 20; tmp125++)
					{
						byte tmp126;
						tmp126 = (byte)s[(int)offset];
						offset += sizeof(byte);
						if (tmp126 == 1)
						{
							byte tmp127;
							tmp127 = (byte)s[(int)offset];
							offset += sizeof(byte);
							byte[] tmp128 = new byte[sizeof(uint)];
							Array.Copy(s, offset, tmp128, 0, tmp127);
							offset += tmp127;
							uint tmp129;
							tmp129 = BitConverter.ToUInt32(tmp128, (int)0);
							
							V20[tmp124, tmp125] = new List<string>();
							for (uint tmp130 = 0; tmp130 < tmp129; tmp130++)
							{
								string tmp131;
								byte tmp132;
								tmp132 = (byte)s[(int)offset];
								offset += sizeof(byte);
								if (tmp132 == 1)
								{
									byte tmp133;
									tmp133 = (byte)s[(int)offset];
									offset += sizeof(byte);
									byte[] tmp134 = new byte[sizeof(uint)];
									Array.Copy(s, offset, tmp134, 0, tmp133);
									offset += tmp133;
									uint tmp135;
									tmp135 = BitConverter.ToUInt32(tmp134, (int)0);
									
									tmp131 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp135).ToArray());
									offset += tmp135;
								}
								else
									tmp131 = null;
								V20[tmp124, tmp125].Add(tmp131);
							}
						}
						else
							V20[tmp124, tmp125] = null;
					}
				}
			}
			else
				V20 = null;
			
			// deserialize V21
			byte tmp136;
			tmp136 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp136 == 1)
			{
				byte tmp137;
				tmp137 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp138 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp138, 0, tmp137);
				offset += tmp137;
				uint tmp139;
				tmp139 = BitConverter.ToUInt32(tmp138, (int)0);
				
				V21 = new List<Child[]>();
				for (uint tmp140 = 0; tmp140 < tmp139; tmp140++)
				{
					Child[] tmp141;
					byte tmp142;
					tmp142 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp142 == 1)
					{
						tmp141 = new Child[4];
						for (uint tmp143 = 0; tmp143 < 4; tmp143++)
						{
							byte tmp144;
							tmp144 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp144 == 1)
							{
								tmp141[tmp143] = new Child();
								offset = tmp141[tmp143].Deserialize(s, offset);
							}
							else
								tmp141[tmp143] = null;
						}
					}
					else
						tmp141 = null;
					V21.Add(tmp141);
				}
			}
			else
				V21 = null;
			
			// deserialize V22
			byte tmp145;
			tmp145 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp145 == 1)
			{
				byte tmp146;
				tmp146 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp147 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp147, 0, tmp146);
				offset += tmp146;
				uint tmp148;
				tmp148 = BitConverter.ToUInt32(tmp147, (int)0);
				
				V22 = new Dictionary<string, Child>();
				for (uint tmp149 = 0; tmp149 < tmp148; tmp149++)
				{
					string tmp150;
					byte tmp152;
					tmp152 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp152 == 1)
					{
						byte tmp153;
						tmp153 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp154 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp154, 0, tmp153);
						offset += tmp153;
						uint tmp155;
						tmp155 = BitConverter.ToUInt32(tmp154, (int)0);
						
						tmp150 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp155).ToArray());
						offset += tmp155;
					}
					else
						tmp150 = null;
					
					Child tmp151;
					byte tmp156;
					tmp156 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp156 == 1)
					{
						tmp151 = new Child();
						offset = tmp151.Deserialize(s, offset);
					}
					else
						tmp151 = null;
					
					V22[tmp150] = tmp151;
				}
			}
			else
				V22 = null;
			
			// deserialize V23
			byte tmp157;
			tmp157 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp157 == 1)
			{
				V23 = new Child[5, 10];
				for (uint tmp158 = 0; tmp158 < 5; tmp158++)
				{
					for (uint tmp159 = 0; tmp159 < 10; tmp159++)
					{
						byte tmp160;
						tmp160 = (byte)s[(int)offset];
						offset += sizeof(byte);
						if (tmp160 == 1)
						{
							V23[tmp158, tmp159] = new Child();
							offset = V23[tmp158, tmp159].Deserialize(s, offset);
						}
						else
							V23[tmp158, tmp159] = null;
					}
				}
			}
			else
				V23 = null;
			
			return offset;
		}
	}
} // namespace ks.full
