using System;
using System.Linq;
using System.Collections.Generic;

namespace ks.empty
{
	public class Parent : KSObject
	{
		public uint? Count { get; set; }
		

		public Parent()
		{
		}
		
		public new static string NameStatic => "Parent";
		
		public override string Name => "Parent";
		
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
	
	public class Child : Parent
	{
		

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
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize parents
			offset = base.Deserialize(s, offset);
			
			return offset;
		}
	}
} // namespace ks.empty
