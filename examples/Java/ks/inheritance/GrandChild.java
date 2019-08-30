package ks.inheritance;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class GrandChild extends Child
{
	protected Float height;
	
	// getters
	
	public Float getHeight()
	{
		return this.height;
	}
	
	
	// setters
	
	public void setHeight(Float height)
	{
		this.height = height;
	}
	
	
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
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			height = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
			offset += Float.BYTES;
		}
		else
			height = null;
		
		return offset;
	}
}
