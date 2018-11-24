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
		public uint? p1 { get; set; }
		

		public Parent()
		{
		}
		
		public new static string NameStatic => "Parent";
		
		public override string Name => "Parent";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize p1
			s.Add((byte)((p1 == null) ? 0 : 1));
			if (p1 != null)
			{
				s.AddRange(BitConverter.GetBytes((uint)p1));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize p1
			byte tmp0;
			tmp0 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp0 == 1)
			{
				p1 = BitConverter.ToUInt32(s, (int)offset);
				offset += sizeof(uint);
			}
			else
				p1 = null;
			
			return offset;
		}
	}
	
	public class Child : Parent
	{
		public string c { get; set; }
		

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
			
			// serialize c
			s.Add((byte)((c == null) ? 0 : 1));
			if (c != null)
			{
				List<byte> tmp1 = new List<byte>();
				tmp1.AddRange(BitConverter.GetBytes((uint)c.Count()));
				while (tmp1.Count > 0 && tmp1.Last() == 0)
					tmp1.RemoveAt(tmp1.Count - 1);
				s.Add((byte)tmp1.Count);
				s.AddRange(tmp1);
				
				s.AddRange(System.Text.Encoding.ASCII.GetBytes(c));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize parents
			offset = base.Deserialize(s, offset);
			
			// deserialize c
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
				
				c = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp5).ToArray());
				offset += tmp5;
			}
			else
				c = null;
			
			return offset;
		}
	}
	
	public class Test : KSObject
	{
		public bool? v0 { get; set; }
		public char? v1 { get; set; }
		public sbyte? v2 { get; set; }
		public byte? v3 { get; set; }
		public short? v4 { get; set; }
		public ushort? v5 { get; set; }
		public int? v6 { get; set; }
		public uint? v7 { get; set; }
		public long? v8 { get; set; }
		public ulong? v9 { get; set; }
		public float? v10 { get; set; }
		public double? v11 { get; set; }
		public string v12 { get; set; }
		public EColor? v13 { get; set; }
		public Child v14 { get; set; }
		public List<int?> v15 { get; set; }
		public List<List<char?>> v16 { get; set; }
		public Dictionary<string, int?> v17 { get; set; }
		public Dictionary<char?, List<Dictionary<double?, EColor?>>> v18 { get; set; }
		public sbyte?[] v19 { get; set; }
		public List<string>[,] v20 { get; set; }
		public List<Child[]> v21 { get; set; }
		public Dictionary<string, Child> v22 { get; set; }
		public Child[,] v23 { get; set; }
		

		public Test()
		{
		}
		
		public new static string NameStatic => "Test";
		
		public override string Name => "Test";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize v0
			s.Add((byte)((v0 == null) ? 0 : 1));
			if (v0 != null)
			{
				s.AddRange(BitConverter.GetBytes((bool)v0));
			}
			
			// serialize v1
			s.Add((byte)((v1 == null) ? 0 : 1));
			if (v1 != null)
			{
				s.AddRange(BitConverter.GetBytes((char)v1));
			}
			
			// serialize v2
			s.Add((byte)((v2 == null) ? 0 : 1));
			if (v2 != null)
			{
				s.Add((byte)v2);
			}
			
			// serialize v3
			s.Add((byte)((v3 == null) ? 0 : 1));
			if (v3 != null)
			{
				s.Add((byte)v3);
			}
			
			// serialize v4
			s.Add((byte)((v4 == null) ? 0 : 1));
			if (v4 != null)
			{
				s.AddRange(BitConverter.GetBytes((short)v4));
			}
			
			// serialize v5
			s.Add((byte)((v5 == null) ? 0 : 1));
			if (v5 != null)
			{
				s.AddRange(BitConverter.GetBytes((ushort)v5));
			}
			
			// serialize v6
			s.Add((byte)((v6 == null) ? 0 : 1));
			if (v6 != null)
			{
				s.AddRange(BitConverter.GetBytes((int)v6));
			}
			
			// serialize v7
			s.Add((byte)((v7 == null) ? 0 : 1));
			if (v7 != null)
			{
				s.AddRange(BitConverter.GetBytes((uint)v7));
			}
			
			// serialize v8
			s.Add((byte)((v8 == null) ? 0 : 1));
			if (v8 != null)
			{
				s.AddRange(BitConverter.GetBytes((long)v8));
			}
			
			// serialize v9
			s.Add((byte)((v9 == null) ? 0 : 1));
			if (v9 != null)
			{
				s.AddRange(BitConverter.GetBytes((ulong)v9));
			}
			
			// serialize v10
			s.Add((byte)((v10 == null) ? 0 : 1));
			if (v10 != null)
			{
				s.AddRange(BitConverter.GetBytes((float)v10));
			}
			
			// serialize v11
			s.Add((byte)((v11 == null) ? 0 : 1));
			if (v11 != null)
			{
				s.AddRange(BitConverter.GetBytes((double)v11));
			}
			
			// serialize v12
			s.Add((byte)((v12 == null) ? 0 : 1));
			if (v12 != null)
			{
				List<byte> tmp6 = new List<byte>();
				tmp6.AddRange(BitConverter.GetBytes((uint)v12.Count()));
				while (tmp6.Count > 0 && tmp6.Last() == 0)
					tmp6.RemoveAt(tmp6.Count - 1);
				s.Add((byte)tmp6.Count);
				s.AddRange(tmp6);
				
				s.AddRange(System.Text.Encoding.ASCII.GetBytes(v12));
			}
			
			// serialize v13
			s.Add((byte)((v13 == null) ? 0 : 1));
			if (v13 != null)
			{
				s.Add((byte)((sbyte)v13));
			}
			
			// serialize v14
			s.Add((byte)((v14 == null) ? 0 : 1));
			if (v14 != null)
			{
				s.AddRange(v14.Serialize());
			}
			
			// serialize v15
			s.Add((byte)((v15 == null) ? 0 : 1));
			if (v15 != null)
			{
				List<byte> tmp7 = new List<byte>();
				tmp7.AddRange(BitConverter.GetBytes((uint)v15.Count()));
				while (tmp7.Count > 0 && tmp7.Last() == 0)
					tmp7.RemoveAt(tmp7.Count - 1);
				s.Add((byte)tmp7.Count);
				s.AddRange(tmp7);
				
				foreach (var tmp8 in v15)
				{
					s.Add((byte)((tmp8 == null) ? 0 : 1));
					if (tmp8 != null)
					{
						s.AddRange(BitConverter.GetBytes((int)tmp8));
					}
				}
			}
			
			// serialize v16
			s.Add((byte)((v16 == null) ? 0 : 1));
			if (v16 != null)
			{
				List<byte> tmp9 = new List<byte>();
				tmp9.AddRange(BitConverter.GetBytes((uint)v16.Count()));
				while (tmp9.Count > 0 && tmp9.Last() == 0)
					tmp9.RemoveAt(tmp9.Count - 1);
				s.Add((byte)tmp9.Count);
				s.AddRange(tmp9);
				
				foreach (var tmp10 in v16)
				{
					s.Add((byte)((tmp10 == null) ? 0 : 1));
					if (tmp10 != null)
					{
						List<byte> tmp11 = new List<byte>();
						tmp11.AddRange(BitConverter.GetBytes((uint)tmp10.Count()));
						while (tmp11.Count > 0 && tmp11.Last() == 0)
							tmp11.RemoveAt(tmp11.Count - 1);
						s.Add((byte)tmp11.Count);
						s.AddRange(tmp11);
						
						foreach (var tmp12 in tmp10)
						{
							s.Add((byte)((tmp12 == null) ? 0 : 1));
							if (tmp12 != null)
							{
								s.AddRange(BitConverter.GetBytes((char)tmp12));
							}
						}
					}
				}
			}
			
			// serialize v17
			s.Add((byte)((v17 == null) ? 0 : 1));
			if (v17 != null)
			{
				List<byte> tmp13 = new List<byte>();
				tmp13.AddRange(BitConverter.GetBytes((uint)v17.Count()));
				while (tmp13.Count > 0 && tmp13.Last() == 0)
					tmp13.RemoveAt(tmp13.Count - 1);
				s.Add((byte)tmp13.Count);
				s.AddRange(tmp13);
				
				foreach (var tmp14 in v17)
				{
					s.Add((byte)((tmp14.Key == null) ? 0 : 1));
					if (tmp14.Key != null)
					{
						List<byte> tmp15 = new List<byte>();
						tmp15.AddRange(BitConverter.GetBytes((uint)tmp14.Key.Count()));
						while (tmp15.Count > 0 && tmp15.Last() == 0)
							tmp15.RemoveAt(tmp15.Count - 1);
						s.Add((byte)tmp15.Count);
						s.AddRange(tmp15);
						
						s.AddRange(System.Text.Encoding.ASCII.GetBytes(tmp14.Key));
					}
					
					s.Add((byte)((tmp14.Value == null) ? 0 : 1));
					if (tmp14.Value != null)
					{
						s.AddRange(BitConverter.GetBytes((int)tmp14.Value));
					}
				}
			}
			
			// serialize v18
			s.Add((byte)((v18 == null) ? 0 : 1));
			if (v18 != null)
			{
				List<byte> tmp16 = new List<byte>();
				tmp16.AddRange(BitConverter.GetBytes((uint)v18.Count()));
				while (tmp16.Count > 0 && tmp16.Last() == 0)
					tmp16.RemoveAt(tmp16.Count - 1);
				s.Add((byte)tmp16.Count);
				s.AddRange(tmp16);
				
				foreach (var tmp17 in v18)
				{
					s.Add((byte)((tmp17.Key == null) ? 0 : 1));
					if (tmp17.Key != null)
					{
						s.AddRange(BitConverter.GetBytes((char)tmp17.Key));
					}
					
					s.Add((byte)((tmp17.Value == null) ? 0 : 1));
					if (tmp17.Value != null)
					{
						List<byte> tmp18 = new List<byte>();
						tmp18.AddRange(BitConverter.GetBytes((uint)tmp17.Value.Count()));
						while (tmp18.Count > 0 && tmp18.Last() == 0)
							tmp18.RemoveAt(tmp18.Count - 1);
						s.Add((byte)tmp18.Count);
						s.AddRange(tmp18);
						
						foreach (var tmp19 in tmp17.Value)
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
									s.Add((byte)((tmp21.Key == null) ? 0 : 1));
									if (tmp21.Key != null)
									{
										s.AddRange(BitConverter.GetBytes((double)tmp21.Key));
									}
									
									s.Add((byte)((tmp21.Value == null) ? 0 : 1));
									if (tmp21.Value != null)
									{
										s.Add((byte)((sbyte)tmp21.Value));
									}
								}
							}
						}
					}
				}
			}
			
			// serialize v19
			s.Add((byte)((v19 == null) ? 0 : 1));
			if (v19 != null)
			{
				for (uint tmp22 = 0; tmp22 < 10; tmp22++)
				{
					s.Add((byte)((v19[tmp22] == null) ? 0 : 1));
					if (v19[tmp22] != null)
					{
						s.Add((byte)v19[tmp22]);
					}
				}
			}
			
			// serialize v20
			s.Add((byte)((v20 == null) ? 0 : 1));
			if (v20 != null)
			{
				for (uint tmp23 = 0; tmp23 < 10; tmp23++)
				{
					for (uint tmp24 = 0; tmp24 < 20; tmp24++)
					{
						s.Add((byte)((v20[tmp23, tmp24] == null) ? 0 : 1));
						if (v20[tmp23, tmp24] != null)
						{
							List<byte> tmp25 = new List<byte>();
							tmp25.AddRange(BitConverter.GetBytes((uint)v20[tmp23, tmp24].Count()));
							while (tmp25.Count > 0 && tmp25.Last() == 0)
								tmp25.RemoveAt(tmp25.Count - 1);
							s.Add((byte)tmp25.Count);
							s.AddRange(tmp25);
							
							foreach (var tmp26 in v20[tmp23, tmp24])
							{
								s.Add((byte)((tmp26 == null) ? 0 : 1));
								if (tmp26 != null)
								{
									List<byte> tmp27 = new List<byte>();
									tmp27.AddRange(BitConverter.GetBytes((uint)tmp26.Count()));
									while (tmp27.Count > 0 && tmp27.Last() == 0)
										tmp27.RemoveAt(tmp27.Count - 1);
									s.Add((byte)tmp27.Count);
									s.AddRange(tmp27);
									
									s.AddRange(System.Text.Encoding.ASCII.GetBytes(tmp26));
								}
							}
						}
					}
				}
			}
			
			// serialize v21
			s.Add((byte)((v21 == null) ? 0 : 1));
			if (v21 != null)
			{
				List<byte> tmp28 = new List<byte>();
				tmp28.AddRange(BitConverter.GetBytes((uint)v21.Count()));
				while (tmp28.Count > 0 && tmp28.Last() == 0)
					tmp28.RemoveAt(tmp28.Count - 1);
				s.Add((byte)tmp28.Count);
				s.AddRange(tmp28);
				
				foreach (var tmp29 in v21)
				{
					s.Add((byte)((tmp29 == null) ? 0 : 1));
					if (tmp29 != null)
					{
						for (uint tmp30 = 0; tmp30 < 4; tmp30++)
						{
							s.Add((byte)((tmp29[tmp30] == null) ? 0 : 1));
							if (tmp29[tmp30] != null)
							{
								s.AddRange(tmp29[tmp30].Serialize());
							}
						}
					}
				}
			}
			
			// serialize v22
			s.Add((byte)((v22 == null) ? 0 : 1));
			if (v22 != null)
			{
				List<byte> tmp31 = new List<byte>();
				tmp31.AddRange(BitConverter.GetBytes((uint)v22.Count()));
				while (tmp31.Count > 0 && tmp31.Last() == 0)
					tmp31.RemoveAt(tmp31.Count - 1);
				s.Add((byte)tmp31.Count);
				s.AddRange(tmp31);
				
				foreach (var tmp32 in v22)
				{
					s.Add((byte)((tmp32.Key == null) ? 0 : 1));
					if (tmp32.Key != null)
					{
						List<byte> tmp33 = new List<byte>();
						tmp33.AddRange(BitConverter.GetBytes((uint)tmp32.Key.Count()));
						while (tmp33.Count > 0 && tmp33.Last() == 0)
							tmp33.RemoveAt(tmp33.Count - 1);
						s.Add((byte)tmp33.Count);
						s.AddRange(tmp33);
						
						s.AddRange(System.Text.Encoding.ASCII.GetBytes(tmp32.Key));
					}
					
					s.Add((byte)((tmp32.Value == null) ? 0 : 1));
					if (tmp32.Value != null)
					{
						s.AddRange(tmp32.Value.Serialize());
					}
				}
			}
			
			// serialize v23
			s.Add((byte)((v23 == null) ? 0 : 1));
			if (v23 != null)
			{
				for (uint tmp34 = 0; tmp34 < 5; tmp34++)
				{
					for (uint tmp35 = 0; tmp35 < 10; tmp35++)
					{
						s.Add((byte)((v23[tmp34, tmp35] == null) ? 0 : 1));
						if (v23[tmp34, tmp35] != null)
						{
							s.AddRange(v23[tmp34, tmp35].Serialize());
						}
					}
				}
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize v0
			byte tmp36;
			tmp36 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp36 == 1)
			{
				v0 = BitConverter.ToBoolean(s, (int)offset);
				offset += sizeof(bool);
			}
			else
				v0 = null;
			
			// deserialize v1
			byte tmp37;
			tmp37 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp37 == 1)
			{
				v1 = BitConverter.ToChar(s, (int)offset);
				offset += sizeof(char);
			}
			else
				v1 = null;
			
			// deserialize v2
			byte tmp38;
			tmp38 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp38 == 1)
			{
				v2 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
			}
			else
				v2 = null;
			
			// deserialize v3
			byte tmp39;
			tmp39 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp39 == 1)
			{
				v3 = (byte)s[(int)offset];
				offset += sizeof(byte);
			}
			else
				v3 = null;
			
			// deserialize v4
			byte tmp40;
			tmp40 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp40 == 1)
			{
				v4 = BitConverter.ToInt16(s, (int)offset);
				offset += sizeof(short);
			}
			else
				v4 = null;
			
			// deserialize v5
			byte tmp41;
			tmp41 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp41 == 1)
			{
				v5 = BitConverter.ToUInt16(s, (int)offset);
				offset += sizeof(ushort);
			}
			else
				v5 = null;
			
			// deserialize v6
			byte tmp42;
			tmp42 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp42 == 1)
			{
				v6 = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				v6 = null;
			
			// deserialize v7
			byte tmp43;
			tmp43 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp43 == 1)
			{
				v7 = BitConverter.ToUInt32(s, (int)offset);
				offset += sizeof(uint);
			}
			else
				v7 = null;
			
			// deserialize v8
			byte tmp44;
			tmp44 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp44 == 1)
			{
				v8 = BitConverter.ToInt64(s, (int)offset);
				offset += sizeof(long);
			}
			else
				v8 = null;
			
			// deserialize v9
			byte tmp45;
			tmp45 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp45 == 1)
			{
				v9 = BitConverter.ToUInt64(s, (int)offset);
				offset += sizeof(ulong);
			}
			else
				v9 = null;
			
			// deserialize v10
			byte tmp46;
			tmp46 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp46 == 1)
			{
				v10 = BitConverter.ToSingle(s, (int)offset);
				offset += sizeof(float);
			}
			else
				v10 = null;
			
			// deserialize v11
			byte tmp47;
			tmp47 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp47 == 1)
			{
				v11 = BitConverter.ToDouble(s, (int)offset);
				offset += sizeof(double);
			}
			else
				v11 = null;
			
			// deserialize v12
			byte tmp48;
			tmp48 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp48 == 1)
			{
				byte tmp49;
				tmp49 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp50 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp50, 0, tmp49);
				offset += tmp49;
				uint tmp51;
				tmp51 = BitConverter.ToUInt32(tmp50, (int)0);
				
				v12 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp51).ToArray());
				offset += tmp51;
			}
			else
				v12 = null;
			
			// deserialize v13
			byte tmp52;
			tmp52 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp52 == 1)
			{
				sbyte tmp53;
				tmp53 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				v13 = (EColor)tmp53;
			}
			else
				v13 = null;
			
			// deserialize v14
			byte tmp54;
			tmp54 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp54 == 1)
			{
				v14 = new Child();
				offset = v14.Deserialize(s, offset);
			}
			else
				v14 = null;
			
			// deserialize v15
			byte tmp55;
			tmp55 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp55 == 1)
			{
				byte tmp56;
				tmp56 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp57 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp57, 0, tmp56);
				offset += tmp56;
				uint tmp58;
				tmp58 = BitConverter.ToUInt32(tmp57, (int)0);
				
				v15 = new List<int?>();
				for (uint tmp59 = 0; tmp59 < tmp58; tmp59++)
				{
					int? tmp60;
					byte tmp61;
					tmp61 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp61 == 1)
					{
						tmp60 = BitConverter.ToInt32(s, (int)offset);
						offset += sizeof(int);
					}
					else
						tmp60 = null;
					v15.Add(tmp60);
				}
			}
			else
				v15 = null;
			
			// deserialize v16
			byte tmp62;
			tmp62 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp62 == 1)
			{
				byte tmp63;
				tmp63 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp64 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp64, 0, tmp63);
				offset += tmp63;
				uint tmp65;
				tmp65 = BitConverter.ToUInt32(tmp64, (int)0);
				
				v16 = new List<List<char?>>();
				for (uint tmp66 = 0; tmp66 < tmp65; tmp66++)
				{
					List<char?> tmp67;
					byte tmp68;
					tmp68 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp68 == 1)
					{
						byte tmp69;
						tmp69 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp70 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp70, 0, tmp69);
						offset += tmp69;
						uint tmp71;
						tmp71 = BitConverter.ToUInt32(tmp70, (int)0);
						
						tmp67 = new List<char?>();
						for (uint tmp72 = 0; tmp72 < tmp71; tmp72++)
						{
							char? tmp73;
							byte tmp74;
							tmp74 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp74 == 1)
							{
								tmp73 = BitConverter.ToChar(s, (int)offset);
								offset += sizeof(char);
							}
							else
								tmp73 = null;
							tmp67.Add(tmp73);
						}
					}
					else
						tmp67 = null;
					v16.Add(tmp67);
				}
			}
			else
				v16 = null;
			
			// deserialize v17
			byte tmp75;
			tmp75 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp75 == 1)
			{
				byte tmp76;
				tmp76 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp77 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp77, 0, tmp76);
				offset += tmp76;
				uint tmp78;
				tmp78 = BitConverter.ToUInt32(tmp77, (int)0);
				
				v17 = new Dictionary<string, int?>();
				for (uint tmp79 = 0; tmp79 < tmp78; tmp79++)
				{
					string tmp80;
					byte tmp82;
					tmp82 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp82 == 1)
					{
						byte tmp83;
						tmp83 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp84 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp84, 0, tmp83);
						offset += tmp83;
						uint tmp85;
						tmp85 = BitConverter.ToUInt32(tmp84, (int)0);
						
						tmp80 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp85).ToArray());
						offset += tmp85;
					}
					else
						tmp80 = null;
					
					int? tmp81;
					byte tmp86;
					tmp86 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp86 == 1)
					{
						tmp81 = BitConverter.ToInt32(s, (int)offset);
						offset += sizeof(int);
					}
					else
						tmp81 = null;
					
					v17[tmp80] = tmp81;
				}
			}
			else
				v17 = null;
			
			// deserialize v18
			byte tmp87;
			tmp87 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp87 == 1)
			{
				byte tmp88;
				tmp88 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp89 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp89, 0, tmp88);
				offset += tmp88;
				uint tmp90;
				tmp90 = BitConverter.ToUInt32(tmp89, (int)0);
				
				v18 = new Dictionary<char?, List<Dictionary<double?, EColor?>>>();
				for (uint tmp91 = 0; tmp91 < tmp90; tmp91++)
				{
					char? tmp92;
					byte tmp94;
					tmp94 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp94 == 1)
					{
						tmp92 = BitConverter.ToChar(s, (int)offset);
						offset += sizeof(char);
					}
					else
						tmp92 = null;
					
					List<Dictionary<double?, EColor?>> tmp93;
					byte tmp95;
					tmp95 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp95 == 1)
					{
						byte tmp96;
						tmp96 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp97 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp97, 0, tmp96);
						offset += tmp96;
						uint tmp98;
						tmp98 = BitConverter.ToUInt32(tmp97, (int)0);
						
						tmp93 = new List<Dictionary<double?, EColor?>>();
						for (uint tmp99 = 0; tmp99 < tmp98; tmp99++)
						{
							Dictionary<double?, EColor?> tmp100;
							byte tmp101;
							tmp101 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp101 == 1)
							{
								byte tmp102;
								tmp102 = (byte)s[(int)offset];
								offset += sizeof(byte);
								byte[] tmp103 = new byte[sizeof(uint)];
								Array.Copy(s, offset, tmp103, 0, tmp102);
								offset += tmp102;
								uint tmp104;
								tmp104 = BitConverter.ToUInt32(tmp103, (int)0);
								
								tmp100 = new Dictionary<double?, EColor?>();
								for (uint tmp105 = 0; tmp105 < tmp104; tmp105++)
								{
									double? tmp106;
									byte tmp108;
									tmp108 = (byte)s[(int)offset];
									offset += sizeof(byte);
									if (tmp108 == 1)
									{
										tmp106 = BitConverter.ToDouble(s, (int)offset);
										offset += sizeof(double);
									}
									else
										tmp106 = null;
									
									EColor? tmp107;
									byte tmp109;
									tmp109 = (byte)s[(int)offset];
									offset += sizeof(byte);
									if (tmp109 == 1)
									{
										sbyte tmp110;
										tmp110 = (sbyte)s[(int)offset];
										offset += sizeof(sbyte);
										tmp107 = (EColor)tmp110;
									}
									else
										tmp107 = null;
									
									tmp100[tmp106] = tmp107;
								}
							}
							else
								tmp100 = null;
							tmp93.Add(tmp100);
						}
					}
					else
						tmp93 = null;
					
					v18[tmp92] = tmp93;
				}
			}
			else
				v18 = null;
			
			// deserialize v19
			byte tmp111;
			tmp111 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp111 == 1)
			{
				v19 = new sbyte?[10];
				for (uint tmp112 = 0; tmp112 < 10; tmp112++)
				{
					byte tmp113;
					tmp113 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp113 == 1)
					{
						v19[tmp112] = (sbyte)s[(int)offset];
						offset += sizeof(sbyte);
					}
					else
						v19[tmp112] = null;
				}
			}
			else
				v19 = null;
			
			// deserialize v20
			byte tmp114;
			tmp114 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp114 == 1)
			{
				v20 = new List<string>[10, 20];
				for (uint tmp115 = 0; tmp115 < 10; tmp115++)
				{
					for (uint tmp116 = 0; tmp116 < 20; tmp116++)
					{
						byte tmp117;
						tmp117 = (byte)s[(int)offset];
						offset += sizeof(byte);
						if (tmp117 == 1)
						{
							byte tmp118;
							tmp118 = (byte)s[(int)offset];
							offset += sizeof(byte);
							byte[] tmp119 = new byte[sizeof(uint)];
							Array.Copy(s, offset, tmp119, 0, tmp118);
							offset += tmp118;
							uint tmp120;
							tmp120 = BitConverter.ToUInt32(tmp119, (int)0);
							
							v20[tmp115, tmp116] = new List<string>();
							for (uint tmp121 = 0; tmp121 < tmp120; tmp121++)
							{
								string tmp122;
								byte tmp123;
								tmp123 = (byte)s[(int)offset];
								offset += sizeof(byte);
								if (tmp123 == 1)
								{
									byte tmp124;
									tmp124 = (byte)s[(int)offset];
									offset += sizeof(byte);
									byte[] tmp125 = new byte[sizeof(uint)];
									Array.Copy(s, offset, tmp125, 0, tmp124);
									offset += tmp124;
									uint tmp126;
									tmp126 = BitConverter.ToUInt32(tmp125, (int)0);
									
									tmp122 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp126).ToArray());
									offset += tmp126;
								}
								else
									tmp122 = null;
								v20[tmp115, tmp116].Add(tmp122);
							}
						}
						else
							v20[tmp115, tmp116] = null;
					}
				}
			}
			else
				v20 = null;
			
			// deserialize v21
			byte tmp127;
			tmp127 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp127 == 1)
			{
				byte tmp128;
				tmp128 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp129 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp129, 0, tmp128);
				offset += tmp128;
				uint tmp130;
				tmp130 = BitConverter.ToUInt32(tmp129, (int)0);
				
				v21 = new List<Child[]>();
				for (uint tmp131 = 0; tmp131 < tmp130; tmp131++)
				{
					Child[] tmp132;
					byte tmp133;
					tmp133 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp133 == 1)
					{
						tmp132 = new Child[4];
						for (uint tmp134 = 0; tmp134 < 4; tmp134++)
						{
							byte tmp135;
							tmp135 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp135 == 1)
							{
								tmp132[tmp134] = new Child();
								offset = tmp132[tmp134].Deserialize(s, offset);
							}
							else
								tmp132[tmp134] = null;
						}
					}
					else
						tmp132 = null;
					v21.Add(tmp132);
				}
			}
			else
				v21 = null;
			
			// deserialize v22
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
				
				v22 = new Dictionary<string, Child>();
				for (uint tmp140 = 0; tmp140 < tmp139; tmp140++)
				{
					string tmp141;
					byte tmp143;
					tmp143 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp143 == 1)
					{
						byte tmp144;
						tmp144 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp145 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp145, 0, tmp144);
						offset += tmp144;
						uint tmp146;
						tmp146 = BitConverter.ToUInt32(tmp145, (int)0);
						
						tmp141 = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp146).ToArray());
						offset += tmp146;
					}
					else
						tmp141 = null;
					
					Child tmp142;
					byte tmp147;
					tmp147 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp147 == 1)
					{
						tmp142 = new Child();
						offset = tmp142.Deserialize(s, offset);
					}
					else
						tmp142 = null;
					
					v22[tmp141] = tmp142;
				}
			}
			else
				v22 = null;
			
			// deserialize v23
			byte tmp148;
			tmp148 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp148 == 1)
			{
				v23 = new Child[5, 10];
				for (uint tmp149 = 0; tmp149 < 5; tmp149++)
				{
					for (uint tmp150 = 0; tmp150 < 10; tmp150++)
					{
						byte tmp151;
						tmp151 = (byte)s[(int)offset];
						offset += sizeof(byte);
						if (tmp151 == 1)
						{
							v23[tmp149, tmp150] = new Child();
							offset = v23[tmp149, tmp150].Deserialize(s, offset);
						}
						else
							v23[tmp149, tmp150] = null;
					}
				}
			}
			else
				v23 = null;
			
			return offset;
		}
	}
} // namespace ks.full
