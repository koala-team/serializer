package ks.inheritance;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Parent3 extends KSObject
{
	
	// getters
	
	
	// setters
	
	
	public Parent3()
	{
	}
	
	public static final String nameStatic = "Parent3";
	
	@Override
	public String name() { return "Parent3"; }
	
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
