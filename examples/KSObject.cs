using System;

namespace KS
{
	public abstract partial class KSObject
	{
		public static string NameStatic => "";
		public abstract string Name { get; }
		public abstract byte[] Serialize();
		public abstract uint Deserialize(byte[] s, uint offset = 0);
	}
} // namespace KS
