package ks.inheritance;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.*;

public class Inheritance
{
	public static class Parent1 extends KSObject
	{
		public Integer count;
		

		public Parent1()
		{
		}
		
		public static final String NameStatic = "Parent1";
		
		@Override
		public String Name() { return "Parent1"; }
		
		@Override
		public byte[] serialize()
		{
			List<Byte> s = new ArrayList<>();
			
			// serialize count
			s.add((byte) ((count == null) ? 0 : 1));
			if (count != null)
			{
				s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(count).array()));
			}
			
			return B2b(s);
		}
		
		@Override
		protected int deserialize(byte[] s, int offset)
		{
			// deserialize count
			byte tmp0;
			tmp0 = s[offset];
			offset += Byte.BYTES;
			if (tmp0 == 1)
			{
				count = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				offset += Integer.BYTES;
			}
			else
				count = null;
			
			return offset;
		}
	}
	
	public static class Parent2 extends KSObject
	{
		public Long number;
		

		public Parent2()
		{
		}
		
		public static final String NameStatic = "Parent2";
		
		@Override
		public String Name() { return "Parent2"; }
		
		@Override
		public byte[] serialize()
		{
			List<Byte> s = new ArrayList<>();
			
			// serialize number
			s.add((byte) ((number == null) ? 0 : 1));
			if (number != null)
			{
				s.addAll(b2B(ByteBuffer.allocate(Long.BYTES).order(ByteOrder.LITTLE_ENDIAN).putLong(number).array()));
			}
			
			return B2b(s);
		}
		
		@Override
		protected int deserialize(byte[] s, int offset)
		{
			// deserialize number
			byte tmp1;
			tmp1 = s[offset];
			offset += Byte.BYTES;
			if (tmp1 == 1)
			{
				number = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Long.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getLong();
				offset += Long.BYTES;
			}
			else
				number = null;
			
			return offset;
		}
	}
	
	public static class Parent3 extends KSObject
	{
		

		public Parent3()
		{
		}
		
		public static final String NameStatic = "Parent3";
		
		@Override
		public String Name() { return "Parent3"; }
		
		@Override
		public byte[] serialize()
		{
			List<Byte> s = new ArrayList<>();
			
			return B2b(s);
		}
		
		@Override
		protected int deserialize(byte[] s, int offset)
		{
			return offset;
		}
	}
	
	public static class Child extends Parent1
	{
		public String firstname;
		

		public Child()
		{
		}
		
		public static final String NameStatic = "Child";
		
		@Override
		public String Name() { return "Child"; }
		
		@Override
		public byte[] serialize()
		{
			List<Byte> s = new ArrayList<>();
			
			// serialize parents
			s.addAll(b2B(super.serialize()));
			
			// serialize firstname
			s.add((byte) ((firstname == null) ? 0 : 1));
			if (firstname != null)
			{
				List<Byte> tmp2 = new ArrayList<>();
				tmp2.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(firstname.length()).array()));
				while (tmp2.size() > 0 && tmp2.get(tmp2.size() - 1) == 0)
					tmp2.remove(tmp2.size() - 1);
				s.add((byte) tmp2.size());
				s.addAll(tmp2);
				
				s.addAll(b2B(firstname.getBytes(Charset.forName("ISO-8859-1"))));
			}
			
			return B2b(s);
		}
		
		@Override
		protected int deserialize(byte[] s, int offset)
		{
			// deserialize parents
			offset = super.deserialize(s, offset);
			
			// deserialize firstname
			byte tmp3;
			tmp3 = s[offset];
			offset += Byte.BYTES;
			if (tmp3 == 1)
			{
				byte tmp4;
				tmp4 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp5 = Arrays.copyOfRange(s, offset, offset + tmp4);
				offset += tmp4;
				int tmp6;
				tmp6 = ByteBuffer.wrap(Arrays.copyOfRange(tmp5, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				firstname = new String(s, offset, tmp6, Charset.forName("ISO-8859-1"));
				offset += tmp6;
			}
			else
				firstname = null;
			
			return offset;
		}
	}
	
	public static class GrandChild extends Child
	{
		public Float height;
		

		public GrandChild()
		{
		}
		
		public static final String NameStatic = "GrandChild";
		
		@Override
		public String Name() { return "GrandChild"; }
		
		@Override
		public byte[] serialize()
		{
			List<Byte> s = new ArrayList<>();
			
			// serialize parents
			s.addAll(b2B(super.serialize()));
			
			// serialize height
			s.add((byte) ((height == null) ? 0 : 1));
			if (height != null)
			{
				s.addAll(b2B(ByteBuffer.allocate(Float.BYTES).order(ByteOrder.LITTLE_ENDIAN).putFloat(height).array()));
			}
			
			return B2b(s);
		}
		
		@Override
		protected int deserialize(byte[] s, int offset)
		{
			// deserialize parents
			offset = super.deserialize(s, offset);
			
			// deserialize height
			byte tmp7;
			tmp7 = s[offset];
			offset += Byte.BYTES;
			if (tmp7 == 1)
			{
				height = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
				offset += Float.BYTES;
			}
			else
				height = null;
			
			return offset;
		}
	}
} // Inheritance
