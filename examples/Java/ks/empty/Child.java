package ks.empty;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Child extends Parent
{
	
	// getters
	
	
	// setters
	
	
	public Child()
	{
	}
	
	public static final String nameStatic = "Child";
	
	@Override
	public String name() { return "Child"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize parents
		s.addAll(b2B(super.serialize()));
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize parents
		offset = super.deserialize(s, offset);
		
		return offset;
	}
}
