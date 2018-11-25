using System;
using System.Linq;
using System.Collections.Generic;

namespace ks.inheritance
{
	public class Parent1 : KSObject
	{
		public uint? Count { get; set; }
		

		public Parent1()
		{
		}
		
		public new static string NameStatic => "Parent1";
		
		public override string Name => "Parent1";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Count
			s.Add((byte)((Count == null) ? 0 : 1));
			if (Count != null)
			{
				s.AddRange(BitConverter.GetBytes((uint)Count));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Count
			byte tmp0;
			tmp0 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp0 == 1)
			{
				Count = BitConverter.ToUInt32(s, (int)offset);
				offset += sizeof(uint);
			}
			else
				Count = null;
			
			return offset;
		}
	}
	
	public class Parent2 : KSObject
	{
		public long? Number { get; set; }
		

		public Parent2()
		{
		}
		
		public new static string NameStatic => "Parent2";
		
		public override string Name => "Parent2";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Number
			s.Add((byte)((Number == null) ? 0 : 1));
			if (Number != null)
			{
				s.AddRange(BitConverter.GetBytes((long)Number));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Number
			byte tmp1;
			tmp1 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp1 == 1)
			{
				Number = BitConverter.ToInt64(s, (int)offset);
				offset += sizeof(long);
			}
			else
				Number = null;
			
			return offset;
		}
	}
	
	public class Child : Parent1
	{
		public string Name { get; set; }
		

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
			
			// serialize Name
			s.Add((byte)((Name == null) ? 0 : 1));
			if (Name != null)
			{
				List<byte> tmp2 = new List<byte>();
				tmp2.AddRange(BitConverter.GetBytes((uint)Name.Count()));
				while (tmp2.Count > 0 && tmp2.Last() == 0)
					tmp2.RemoveAt(tmp2.Count - 1);
				s.Add((byte)tmp2.Count);
				s.AddRange(tmp2);
				
				s.AddRange(System.Text.Encoding.ASCII.GetBytes(Name));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize parents
			offset = base.Deserialize(s, offset);
			
			// deserialize Name
			byte tmp3;
			tmp3 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp3 == 1)
			{
				byte tmp4;
				tmp4 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp5 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp5, 0, tmp4);
				offset += tmp4;
				uint tmp6;
				tmp6 = BitConverter.ToUInt32(tmp5, (int)0);
				
				Name = System.Text.Encoding.ASCII.GetString(s.Skip((int)offset).Take((int)tmp6).ToArray());
				offset += tmp6;
			}
			else
				Name = null;
			
			return offset;
		}
	}
} // namespace ks.inheritance
