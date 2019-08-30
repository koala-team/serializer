package ks.full;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Parent extends KSObject
{
	protected String firstName;
	protected String _lastName_;
	
	// getters
	
	public String getFirstName()
	{
		return this.firstName;
	}
	
	public String get_LastName_()
	{
		return this._lastName_;
	}
	
	
	// setters
	
	public void setFirstName(String firstName)
	{
		this.firstName = firstName;
	}
	
	public void set_LastName_(String _lastName_)
	{
		this._lastName_ = _lastName_;
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
		
		// serialize firstName
		s.add((byte) ((firstName == null) ? 0 : 1));
		if (firstName != null)
		{
			List<Byte> tmp0 = new ArrayList<>();
			tmp0.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(firstName.length()).array()));
			while (tmp0.size() > 0 && tmp0.get(tmp0.size() - 1) == 0)
				tmp0.remove(tmp0.size() - 1);
			s.add((byte) tmp0.size());
			s.addAll(tmp0);
			
			s.addAll(b2B(firstName.getBytes(Charset.forName("ISO-8859-1"))));
		}
		
		// serialize _lastName_
		s.add((byte) ((_lastName_ == null) ? 0 : 1));
		if (_lastName_ != null)
		{
			List<Byte> tmp1 = new ArrayList<>();
			tmp1.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(_lastName_.length()).array()));
			while (tmp1.size() > 0 && tmp1.get(tmp1.size() - 1) == 0)
				tmp1.remove(tmp1.size() - 1);
			s.add((byte) tmp1.size());
			s.addAll(tmp1);
			
			s.addAll(b2B(_lastName_.getBytes(Charset.forName("ISO-8859-1"))));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize firstName
		byte tmp2;
		tmp2 = s[offset];
		offset += Byte.BYTES;
		if (tmp2 == 1)
		{
			byte tmp3;
			tmp3 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp4 = Arrays.copyOfRange(s, offset, offset + tmp3);
			offset += tmp3;
			int tmp5;
			tmp5 = ByteBuffer.wrap(Arrays.copyOfRange(tmp4, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			firstName = new String(s, offset, tmp5, Charset.forName("ISO-8859-1"));
			offset += tmp5;
		}
		else
			firstName = null;
		
		// deserialize _lastName_
		byte tmp6;
		tmp6 = s[offset];
		offset += Byte.BYTES;
		if (tmp6 == 1)
		{
			byte tmp7;
			tmp7 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp8 = Arrays.copyOfRange(s, offset, offset + tmp7);
			offset += tmp7;
			int tmp9;
			tmp9 = ByteBuffer.wrap(Arrays.copyOfRange(tmp8, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			_lastName_ = new String(s, offset, tmp9, Charset.forName("ISO-8859-1"));
			offset += tmp9;
		}
		else
			_lastName_ = null;
		
		return offset;
	}
}
