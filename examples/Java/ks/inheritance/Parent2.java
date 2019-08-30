package ks.inheritance;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Parent2 extends KSObject
{
	protected Long number;
	
	// getters
	
	public Long getNumber()
	{
		return this.number;
	}
	
	
	// setters
	
	public void setNumber(Long number)
	{
		this.number = number;
	}
	
	
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
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			number = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Long.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getLong();
			offset += Long.BYTES;
		}
		else
			number = null;
		
		return offset;
	}
}
