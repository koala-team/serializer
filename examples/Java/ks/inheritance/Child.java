package ks.inheritance;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Child extends Parent1
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
			List<Byte> tmp0 = new ArrayList<>();
			tmp0.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(firstname.length()).array()));
			while (tmp0.size() > 0 && tmp0.get(tmp0.size() - 1) == 0)
				tmp0.remove(tmp0.size() - 1);
			s.add((byte) tmp0.size());
			s.addAll(tmp0);
			
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
		byte tmp1;
		tmp1 = s[offset];
		offset += Byte.BYTES;
		if (tmp1 == 1)
		{
			byte tmp2;
			tmp2 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp3 = Arrays.copyOfRange(s, offset, offset + tmp2);
			offset += tmp2;
			int tmp4;
			tmp4 = ByteBuffer.wrap(Arrays.copyOfRange(tmp3, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			firstname = new String(s, offset, tmp4, Charset.forName("ISO-8859-1"));
			offset += tmp4;
		}
		else
			firstname = null;
		
		return offset;
	}
}
