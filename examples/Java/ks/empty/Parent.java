package ks.empty;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Parent extends KSObject
{
	protected Integer count;
	
	// getters
	
	public Integer getCount()
	{
		return this.count;
	}
	
	
	// setters
	
	public void setCount(Integer count)
	{
		this.count = count;
	}
	
	
	public Parent()
	{
	}
	
	public static final String nameStatic = "Parent";
	
	@Override
	public String name() { return "Parent"; }
	
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
