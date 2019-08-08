package ks.full;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public enum EColor
{
	White((byte) 0),
	Red((byte) 3),
	Green((byte) 4),
	Blue((byte) -2),
	Black((byte) -1),
	;

	private final byte value;
	EColor(byte value) { this.value = value; }
	public byte getValue() { return value; }
	
	private static Map<Byte, EColor> reverseLookup;
	
	public static EColor of(byte value)
	{
		if (reverseLookup == null)
		{
			reverseLookup = new HashMap<>();
			for (EColor c : EColor.values())
				reverseLookup.put(c.getValue(), c);
		}
		return reverseLookup.get(value);
	}
}
