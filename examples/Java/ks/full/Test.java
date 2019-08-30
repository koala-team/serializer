package ks.full;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Test extends KSObject
{
	protected Boolean v0;
	protected Character v1;
	protected Byte v2;
	protected Byte v3;
	protected Short v4;
	protected Short v5;
	protected Integer v6;
	protected Integer v7;
	protected Long v8;
	protected Long v9;
	protected Float v10;
	protected Double v11;
	protected String v12;
	protected EColor v13;
	protected Child v14;
	protected List<Integer> v15;
	protected List<List<Character>> v16;
	protected Map<String, Integer> v17;
	protected Map<Character, List<Map<Double, EColor>>> v18;
	protected Byte[] v19;
	protected List<String>[][] v20;
	protected List<Child[]> v21;
	protected Map<String, Child> v22;
	protected Child[][] v23;
	
	// getters
	
	public Boolean getV0()
	{
		return this.v0;
	}
	
	public Character getV1()
	{
		return this.v1;
	}
	
	public Byte getV2()
	{
		return this.v2;
	}
	
	public Byte getV3()
	{
		return this.v3;
	}
	
	public Short getV4()
	{
		return this.v4;
	}
	
	public Short getV5()
	{
		return this.v5;
	}
	
	public Integer getV6()
	{
		return this.v6;
	}
	
	public Integer getV7()
	{
		return this.v7;
	}
	
	public Long getV8()
	{
		return this.v8;
	}
	
	public Long getV9()
	{
		return this.v9;
	}
	
	public Float getV10()
	{
		return this.v10;
	}
	
	public Double getV11()
	{
		return this.v11;
	}
	
	public String getV12()
	{
		return this.v12;
	}
	
	public EColor getV13()
	{
		return this.v13;
	}
	
	public Child getV14()
	{
		return this.v14;
	}
	
	public List<Integer> getV15()
	{
		return this.v15;
	}
	
	public List<List<Character>> getV16()
	{
		return this.v16;
	}
	
	public Map<String, Integer> getV17()
	{
		return this.v17;
	}
	
	public Map<Character, List<Map<Double, EColor>>> getV18()
	{
		return this.v18;
	}
	
	public Byte[] getV19()
	{
		return this.v19;
	}
	
	public List<String>[][] getV20()
	{
		return this.v20;
	}
	
	public List<Child[]> getV21()
	{
		return this.v21;
	}
	
	public Map<String, Child> getV22()
	{
		return this.v22;
	}
	
	public Child[][] getV23()
	{
		return this.v23;
	}
	
	
	// setters
	
	public void setV0(Boolean v0)
	{
		this.v0 = v0;
	}
	
	public void setV1(Character v1)
	{
		this.v1 = v1;
	}
	
	public void setV2(Byte v2)
	{
		this.v2 = v2;
	}
	
	public void setV3(Byte v3)
	{
		this.v3 = v3;
	}
	
	public void setV4(Short v4)
	{
		this.v4 = v4;
	}
	
	public void setV5(Short v5)
	{
		this.v5 = v5;
	}
	
	public void setV6(Integer v6)
	{
		this.v6 = v6;
	}
	
	public void setV7(Integer v7)
	{
		this.v7 = v7;
	}
	
	public void setV8(Long v8)
	{
		this.v8 = v8;
	}
	
	public void setV9(Long v9)
	{
		this.v9 = v9;
	}
	
	public void setV10(Float v10)
	{
		this.v10 = v10;
	}
	
	public void setV11(Double v11)
	{
		this.v11 = v11;
	}
	
	public void setV12(String v12)
	{
		this.v12 = v12;
	}
	
	public void setV13(EColor v13)
	{
		this.v13 = v13;
	}
	
	public void setV14(Child v14)
	{
		this.v14 = v14;
	}
	
	public void setV15(List<Integer> v15)
	{
		this.v15 = v15;
	}
	
	public void setV16(List<List<Character>> v16)
	{
		this.v16 = v16;
	}
	
	public void setV17(Map<String, Integer> v17)
	{
		this.v17 = v17;
	}
	
	public void setV18(Map<Character, List<Map<Double, EColor>>> v18)
	{
		this.v18 = v18;
	}
	
	public void setV19(Byte[] v19)
	{
		this.v19 = v19;
	}
	
	public void setV20(List<String>[][] v20)
	{
		this.v20 = v20;
	}
	
	public void setV21(List<Child[]> v21)
	{
		this.v21 = v21;
	}
	
	public void setV22(Map<String, Child> v22)
	{
		this.v22 = v22;
	}
	
	public void setV23(Child[][] v23)
	{
		this.v23 = v23;
	}
	
	
	public Test()
	{
	}
	
	public static final String NameStatic = "Test";
	
	@Override
	public String Name() { return "Test"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize v0
		s.add((byte) ((v0 == null) ? 0 : 1));
		if (v0 != null)
		{
			s.add((byte) ((v0) ? 1 : 0));
		}
		
		// serialize v1
		s.add((byte) ((v1 == null) ? 0 : 1));
		if (v1 != null)
		{
			s.add((byte) (char) v1);
		}
		
		// serialize v2
		s.add((byte) ((v2 == null) ? 0 : 1));
		if (v2 != null)
		{
			s.add((byte) v2);
		}
		
		// serialize v3
		s.add((byte) ((v3 == null) ? 0 : 1));
		if (v3 != null)
		{
			s.add((byte) v3);
		}
		
		// serialize v4
		s.add((byte) ((v4 == null) ? 0 : 1));
		if (v4 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Short.BYTES).order(ByteOrder.LITTLE_ENDIAN).putShort(v4).array()));
		}
		
		// serialize v5
		s.add((byte) ((v5 == null) ? 0 : 1));
		if (v5 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Short.BYTES).order(ByteOrder.LITTLE_ENDIAN).putShort(v5).array()));
		}
		
		// serialize v6
		s.add((byte) ((v6 == null) ? 0 : 1));
		if (v6 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v6).array()));
		}
		
		// serialize v7
		s.add((byte) ((v7 == null) ? 0 : 1));
		if (v7 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v7).array()));
		}
		
		// serialize v8
		s.add((byte) ((v8 == null) ? 0 : 1));
		if (v8 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Long.BYTES).order(ByteOrder.LITTLE_ENDIAN).putLong(v8).array()));
		}
		
		// serialize v9
		s.add((byte) ((v9 == null) ? 0 : 1));
		if (v9 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Long.BYTES).order(ByteOrder.LITTLE_ENDIAN).putLong(v9).array()));
		}
		
		// serialize v10
		s.add((byte) ((v10 == null) ? 0 : 1));
		if (v10 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Float.BYTES).order(ByteOrder.LITTLE_ENDIAN).putFloat(v10).array()));
		}
		
		// serialize v11
		s.add((byte) ((v11 == null) ? 0 : 1));
		if (v11 != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Double.BYTES).order(ByteOrder.LITTLE_ENDIAN).putDouble(v11).array()));
		}
		
		// serialize v12
		s.add((byte) ((v12 == null) ? 0 : 1));
		if (v12 != null)
		{
			List<Byte> tmp0 = new ArrayList<>();
			tmp0.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v12.length()).array()));
			while (tmp0.size() > 0 && tmp0.get(tmp0.size() - 1) == 0)
				tmp0.remove(tmp0.size() - 1);
			s.add((byte) tmp0.size());
			s.addAll(tmp0);
			
			s.addAll(b2B(v12.getBytes(Charset.forName("ISO-8859-1"))));
		}
		
		// serialize v13
		s.add((byte) ((v13 == null) ? 0 : 1));
		if (v13 != null)
		{
			s.add((byte) (v13.getValue()));
		}
		
		// serialize v14
		s.add((byte) ((v14 == null) ? 0 : 1));
		if (v14 != null)
		{
			s.addAll(b2B(v14.serialize()));
		}
		
		// serialize v15
		s.add((byte) ((v15 == null) ? 0 : 1));
		if (v15 != null)
		{
			List<Byte> tmp1 = new ArrayList<>();
			tmp1.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v15.size()).array()));
			while (tmp1.size() > 0 && tmp1.get(tmp1.size() - 1) == 0)
				tmp1.remove(tmp1.size() - 1);
			s.add((byte) tmp1.size());
			s.addAll(tmp1);
			
			for (Integer tmp2 : v15)
			{
				s.add((byte) ((tmp2 == null) ? 0 : 1));
				if (tmp2 != null)
				{
					s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp2).array()));
				}
			}
		}
		
		// serialize v16
		s.add((byte) ((v16 == null) ? 0 : 1));
		if (v16 != null)
		{
			List<Byte> tmp3 = new ArrayList<>();
			tmp3.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v16.size()).array()));
			while (tmp3.size() > 0 && tmp3.get(tmp3.size() - 1) == 0)
				tmp3.remove(tmp3.size() - 1);
			s.add((byte) tmp3.size());
			s.addAll(tmp3);
			
			for (List<Character> tmp4 : v16)
			{
				s.add((byte) ((tmp4 == null) ? 0 : 1));
				if (tmp4 != null)
				{
					List<Byte> tmp5 = new ArrayList<>();
					tmp5.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp4.size()).array()));
					while (tmp5.size() > 0 && tmp5.get(tmp5.size() - 1) == 0)
						tmp5.remove(tmp5.size() - 1);
					s.add((byte) tmp5.size());
					s.addAll(tmp5);
					
					for (Character tmp6 : tmp4)
					{
						s.add((byte) ((tmp6 == null) ? 0 : 1));
						if (tmp6 != null)
						{
							s.add((byte) (char) tmp6);
						}
					}
				}
			}
		}
		
		// serialize v17
		s.add((byte) ((v17 == null) ? 0 : 1));
		if (v17 != null)
		{
			List<Byte> tmp7 = new ArrayList<>();
			tmp7.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v17.size()).array()));
			while (tmp7.size() > 0 && tmp7.get(tmp7.size() - 1) == 0)
				tmp7.remove(tmp7.size() - 1);
			s.add((byte) tmp7.size());
			s.addAll(tmp7);
			
			for (Map.Entry<String, Integer> tmp8 : v17.entrySet())
			{
				s.add((byte) ((tmp8.getKey() == null) ? 0 : 1));
				if (tmp8.getKey() != null)
				{
					List<Byte> tmp9 = new ArrayList<>();
					tmp9.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp8.getKey().length()).array()));
					while (tmp9.size() > 0 && tmp9.get(tmp9.size() - 1) == 0)
						tmp9.remove(tmp9.size() - 1);
					s.add((byte) tmp9.size());
					s.addAll(tmp9);
					
					s.addAll(b2B(tmp8.getKey().getBytes(Charset.forName("ISO-8859-1"))));
				}
				
				s.add((byte) ((tmp8.getValue() == null) ? 0 : 1));
				if (tmp8.getValue() != null)
				{
					s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp8.getValue()).array()));
				}
			}
		}
		
		// serialize v18
		s.add((byte) ((v18 == null) ? 0 : 1));
		if (v18 != null)
		{
			List<Byte> tmp10 = new ArrayList<>();
			tmp10.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v18.size()).array()));
			while (tmp10.size() > 0 && tmp10.get(tmp10.size() - 1) == 0)
				tmp10.remove(tmp10.size() - 1);
			s.add((byte) tmp10.size());
			s.addAll(tmp10);
			
			for (Map.Entry<Character, List<Map<Double, EColor>>> tmp11 : v18.entrySet())
			{
				s.add((byte) ((tmp11.getKey() == null) ? 0 : 1));
				if (tmp11.getKey() != null)
				{
					s.add((byte) (char) tmp11.getKey());
				}
				
				s.add((byte) ((tmp11.getValue() == null) ? 0 : 1));
				if (tmp11.getValue() != null)
				{
					List<Byte> tmp12 = new ArrayList<>();
					tmp12.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp11.getValue().size()).array()));
					while (tmp12.size() > 0 && tmp12.get(tmp12.size() - 1) == 0)
						tmp12.remove(tmp12.size() - 1);
					s.add((byte) tmp12.size());
					s.addAll(tmp12);
					
					for (Map<Double, EColor> tmp13 : tmp11.getValue())
					{
						s.add((byte) ((tmp13 == null) ? 0 : 1));
						if (tmp13 != null)
						{
							List<Byte> tmp14 = new ArrayList<>();
							tmp14.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp13.size()).array()));
							while (tmp14.size() > 0 && tmp14.get(tmp14.size() - 1) == 0)
								tmp14.remove(tmp14.size() - 1);
							s.add((byte) tmp14.size());
							s.addAll(tmp14);
							
							for (Map.Entry<Double, EColor> tmp15 : tmp13.entrySet())
							{
								s.add((byte) ((tmp15.getKey() == null) ? 0 : 1));
								if (tmp15.getKey() != null)
								{
									s.addAll(b2B(ByteBuffer.allocate(Double.BYTES).order(ByteOrder.LITTLE_ENDIAN).putDouble(tmp15.getKey()).array()));
								}
								
								s.add((byte) ((tmp15.getValue() == null) ? 0 : 1));
								if (tmp15.getValue() != null)
								{
									s.add((byte) (tmp15.getValue().getValue()));
								}
							}
						}
					}
				}
			}
		}
		
		// serialize v19
		s.add((byte) ((v19 == null) ? 0 : 1));
		if (v19 != null)
		{
			for (int tmp16 = 0; tmp16 < 10; tmp16++)
			{
				s.add((byte) ((v19[tmp16] == null) ? 0 : 1));
				if (v19[tmp16] != null)
				{
					s.add((byte) v19[tmp16]);
				}
			}
		}
		
		// serialize v20
		s.add((byte) ((v20 == null) ? 0 : 1));
		if (v20 != null)
		{
			for (int tmp17 = 0; tmp17 < 10; tmp17++)
			{
				for (int tmp18 = 0; tmp18 < 20; tmp18++)
				{
					s.add((byte) ((v20[tmp17][tmp18] == null) ? 0 : 1));
					if (v20[tmp17][tmp18] != null)
					{
						List<Byte> tmp19 = new ArrayList<>();
						tmp19.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v20[tmp17][tmp18].size()).array()));
						while (tmp19.size() > 0 && tmp19.get(tmp19.size() - 1) == 0)
							tmp19.remove(tmp19.size() - 1);
						s.add((byte) tmp19.size());
						s.addAll(tmp19);
						
						for (String tmp20 : v20[tmp17][tmp18])
						{
							s.add((byte) ((tmp20 == null) ? 0 : 1));
							if (tmp20 != null)
							{
								List<Byte> tmp21 = new ArrayList<>();
								tmp21.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp20.length()).array()));
								while (tmp21.size() > 0 && tmp21.get(tmp21.size() - 1) == 0)
									tmp21.remove(tmp21.size() - 1);
								s.add((byte) tmp21.size());
								s.addAll(tmp21);
								
								s.addAll(b2B(tmp20.getBytes(Charset.forName("ISO-8859-1"))));
							}
						}
					}
				}
			}
		}
		
		// serialize v21
		s.add((byte) ((v21 == null) ? 0 : 1));
		if (v21 != null)
		{
			List<Byte> tmp22 = new ArrayList<>();
			tmp22.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v21.size()).array()));
			while (tmp22.size() > 0 && tmp22.get(tmp22.size() - 1) == 0)
				tmp22.remove(tmp22.size() - 1);
			s.add((byte) tmp22.size());
			s.addAll(tmp22);
			
			for (Child[] tmp23 : v21)
			{
				s.add((byte) ((tmp23 == null) ? 0 : 1));
				if (tmp23 != null)
				{
					for (int tmp24 = 0; tmp24 < 4; tmp24++)
					{
						s.add((byte) ((tmp23[tmp24] == null) ? 0 : 1));
						if (tmp23[tmp24] != null)
						{
							s.addAll(b2B(tmp23[tmp24].serialize()));
						}
					}
				}
			}
		}
		
		// serialize v22
		s.add((byte) ((v22 == null) ? 0 : 1));
		if (v22 != null)
		{
			List<Byte> tmp25 = new ArrayList<>();
			tmp25.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v22.size()).array()));
			while (tmp25.size() > 0 && tmp25.get(tmp25.size() - 1) == 0)
				tmp25.remove(tmp25.size() - 1);
			s.add((byte) tmp25.size());
			s.addAll(tmp25);
			
			for (Map.Entry<String, Child> tmp26 : v22.entrySet())
			{
				s.add((byte) ((tmp26.getKey() == null) ? 0 : 1));
				if (tmp26.getKey() != null)
				{
					List<Byte> tmp27 = new ArrayList<>();
					tmp27.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp26.getKey().length()).array()));
					while (tmp27.size() > 0 && tmp27.get(tmp27.size() - 1) == 0)
						tmp27.remove(tmp27.size() - 1);
					s.add((byte) tmp27.size());
					s.addAll(tmp27);
					
					s.addAll(b2B(tmp26.getKey().getBytes(Charset.forName("ISO-8859-1"))));
				}
				
				s.add((byte) ((tmp26.getValue() == null) ? 0 : 1));
				if (tmp26.getValue() != null)
				{
					s.addAll(b2B(tmp26.getValue().serialize()));
				}
			}
		}
		
		// serialize v23
		s.add((byte) ((v23 == null) ? 0 : 1));
		if (v23 != null)
		{
			for (int tmp28 = 0; tmp28 < 5; tmp28++)
			{
				for (int tmp29 = 0; tmp29 < 10; tmp29++)
				{
					s.add((byte) ((v23[tmp28][tmp29] == null) ? 0 : 1));
					if (v23[tmp28][tmp29] != null)
					{
						s.addAll(b2B(v23[tmp28][tmp29].serialize()));
					}
				}
			}
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize v0
		byte tmp30;
		tmp30 = s[offset];
		offset += Byte.BYTES;
		if (tmp30 == 1)
		{
			v0 = (s[offset] == 0) ? false : true;
			offset += Byte.BYTES;
		}
		else
			v0 = null;
		
		// deserialize v1
		byte tmp31;
		tmp31 = s[offset];
		offset += Byte.BYTES;
		if (tmp31 == 1)
		{
			v1 = (char) s[offset];
			offset += Character.BYTES;
		}
		else
			v1 = null;
		
		// deserialize v2
		byte tmp32;
		tmp32 = s[offset];
		offset += Byte.BYTES;
		if (tmp32 == 1)
		{
			v2 = s[offset];
			offset += Byte.BYTES;
		}
		else
			v2 = null;
		
		// deserialize v3
		byte tmp33;
		tmp33 = s[offset];
		offset += Byte.BYTES;
		if (tmp33 == 1)
		{
			v3 = s[offset];
			offset += Byte.BYTES;
		}
		else
			v3 = null;
		
		// deserialize v4
		byte tmp34;
		tmp34 = s[offset];
		offset += Byte.BYTES;
		if (tmp34 == 1)
		{
			v4 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Short.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getShort();
			offset += Short.BYTES;
		}
		else
			v4 = null;
		
		// deserialize v5
		byte tmp35;
		tmp35 = s[offset];
		offset += Byte.BYTES;
		if (tmp35 == 1)
		{
			v5 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Short.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getShort();
			offset += Short.BYTES;
		}
		else
			v5 = null;
		
		// deserialize v6
		byte tmp36;
		tmp36 = s[offset];
		offset += Byte.BYTES;
		if (tmp36 == 1)
		{
			v6 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			v6 = null;
		
		// deserialize v7
		byte tmp37;
		tmp37 = s[offset];
		offset += Byte.BYTES;
		if (tmp37 == 1)
		{
			v7 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			v7 = null;
		
		// deserialize v8
		byte tmp38;
		tmp38 = s[offset];
		offset += Byte.BYTES;
		if (tmp38 == 1)
		{
			v8 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Long.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getLong();
			offset += Long.BYTES;
		}
		else
			v8 = null;
		
		// deserialize v9
		byte tmp39;
		tmp39 = s[offset];
		offset += Byte.BYTES;
		if (tmp39 == 1)
		{
			v9 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Long.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getLong();
			offset += Long.BYTES;
		}
		else
			v9 = null;
		
		// deserialize v10
		byte tmp40;
		tmp40 = s[offset];
		offset += Byte.BYTES;
		if (tmp40 == 1)
		{
			v10 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
			offset += Float.BYTES;
		}
		else
			v10 = null;
		
		// deserialize v11
		byte tmp41;
		tmp41 = s[offset];
		offset += Byte.BYTES;
		if (tmp41 == 1)
		{
			v11 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Double.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getDouble();
			offset += Double.BYTES;
		}
		else
			v11 = null;
		
		// deserialize v12
		byte tmp42;
		tmp42 = s[offset];
		offset += Byte.BYTES;
		if (tmp42 == 1)
		{
			byte tmp43;
			tmp43 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp44 = Arrays.copyOfRange(s, offset, offset + tmp43);
			offset += tmp43;
			int tmp45;
			tmp45 = ByteBuffer.wrap(Arrays.copyOfRange(tmp44, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			v12 = new String(s, offset, tmp45, Charset.forName("ISO-8859-1"));
			offset += tmp45;
		}
		else
			v12 = null;
		
		// deserialize v13
		byte tmp46;
		tmp46 = s[offset];
		offset += Byte.BYTES;
		if (tmp46 == 1)
		{
			byte tmp47;
			tmp47 = s[offset];
			offset += Byte.BYTES;
			v13 = EColor.of(tmp47);
		}
		else
			v13 = null;
		
		// deserialize v14
		byte tmp48;
		tmp48 = s[offset];
		offset += Byte.BYTES;
		if (tmp48 == 1)
		{
			v14 = new Child();
			offset = v14.deserialize(s, offset);
		}
		else
			v14 = null;
		
		// deserialize v15
		byte tmp49;
		tmp49 = s[offset];
		offset += Byte.BYTES;
		if (tmp49 == 1)
		{
			byte tmp50;
			tmp50 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp51 = Arrays.copyOfRange(s, offset, offset + tmp50);
			offset += tmp50;
			int tmp52;
			tmp52 = ByteBuffer.wrap(Arrays.copyOfRange(tmp51, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			v15 = new ArrayList<>();
			for (int tmp53 = 0; tmp53 < tmp52; tmp53++)
			{
				Integer tmp54;
				byte tmp55;
				tmp55 = s[offset];
				offset += Byte.BYTES;
				if (tmp55 == 1)
				{
					tmp54 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					offset += Integer.BYTES;
				}
				else
					tmp54 = null;
				v15.add(tmp54);
			}
		}
		else
			v15 = null;
		
		// deserialize v16
		byte tmp56;
		tmp56 = s[offset];
		offset += Byte.BYTES;
		if (tmp56 == 1)
		{
			byte tmp57;
			tmp57 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp58 = Arrays.copyOfRange(s, offset, offset + tmp57);
			offset += tmp57;
			int tmp59;
			tmp59 = ByteBuffer.wrap(Arrays.copyOfRange(tmp58, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			v16 = new ArrayList<>();
			for (int tmp60 = 0; tmp60 < tmp59; tmp60++)
			{
				List<Character> tmp61;
				byte tmp62;
				tmp62 = s[offset];
				offset += Byte.BYTES;
				if (tmp62 == 1)
				{
					byte tmp63;
					tmp63 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp64 = Arrays.copyOfRange(s, offset, offset + tmp63);
					offset += tmp63;
					int tmp65;
					tmp65 = ByteBuffer.wrap(Arrays.copyOfRange(tmp64, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp61 = new ArrayList<>();
					for (int tmp66 = 0; tmp66 < tmp65; tmp66++)
					{
						Character tmp67;
						byte tmp68;
						tmp68 = s[offset];
						offset += Byte.BYTES;
						if (tmp68 == 1)
						{
							tmp67 = (char) s[offset];
							offset += Character.BYTES;
						}
						else
							tmp67 = null;
						tmp61.add(tmp67);
					}
				}
				else
					tmp61 = null;
				v16.add(tmp61);
			}
		}
		else
			v16 = null;
		
		// deserialize v17
		byte tmp69;
		tmp69 = s[offset];
		offset += Byte.BYTES;
		if (tmp69 == 1)
		{
			byte tmp70;
			tmp70 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp71 = Arrays.copyOfRange(s, offset, offset + tmp70);
			offset += tmp70;
			int tmp72;
			tmp72 = ByteBuffer.wrap(Arrays.copyOfRange(tmp71, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			v17 = new HashMap<>();
			for (int tmp73 = 0; tmp73 < tmp72; tmp73++)
			{
				String tmp74;
				byte tmp76;
				tmp76 = s[offset];
				offset += Byte.BYTES;
				if (tmp76 == 1)
				{
					byte tmp77;
					tmp77 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp78 = Arrays.copyOfRange(s, offset, offset + tmp77);
					offset += tmp77;
					int tmp79;
					tmp79 = ByteBuffer.wrap(Arrays.copyOfRange(tmp78, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp74 = new String(s, offset, tmp79, Charset.forName("ISO-8859-1"));
					offset += tmp79;
				}
				else
					tmp74 = null;
				
				Integer tmp75;
				byte tmp80;
				tmp80 = s[offset];
				offset += Byte.BYTES;
				if (tmp80 == 1)
				{
					tmp75 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					offset += Integer.BYTES;
				}
				else
					tmp75 = null;
				
				v17.put(tmp74, tmp75);
			}
		}
		else
			v17 = null;
		
		// deserialize v18
		byte tmp81;
		tmp81 = s[offset];
		offset += Byte.BYTES;
		if (tmp81 == 1)
		{
			byte tmp82;
			tmp82 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp83 = Arrays.copyOfRange(s, offset, offset + tmp82);
			offset += tmp82;
			int tmp84;
			tmp84 = ByteBuffer.wrap(Arrays.copyOfRange(tmp83, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			v18 = new HashMap<>();
			for (int tmp85 = 0; tmp85 < tmp84; tmp85++)
			{
				Character tmp86;
				byte tmp88;
				tmp88 = s[offset];
				offset += Byte.BYTES;
				if (tmp88 == 1)
				{
					tmp86 = (char) s[offset];
					offset += Character.BYTES;
				}
				else
					tmp86 = null;
				
				List<Map<Double, EColor>> tmp87;
				byte tmp89;
				tmp89 = s[offset];
				offset += Byte.BYTES;
				if (tmp89 == 1)
				{
					byte tmp90;
					tmp90 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp91 = Arrays.copyOfRange(s, offset, offset + tmp90);
					offset += tmp90;
					int tmp92;
					tmp92 = ByteBuffer.wrap(Arrays.copyOfRange(tmp91, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp87 = new ArrayList<>();
					for (int tmp93 = 0; tmp93 < tmp92; tmp93++)
					{
						Map<Double, EColor> tmp94;
						byte tmp95;
						tmp95 = s[offset];
						offset += Byte.BYTES;
						if (tmp95 == 1)
						{
							byte tmp96;
							tmp96 = s[offset];
							offset += Byte.BYTES;
							byte[] tmp97 = Arrays.copyOfRange(s, offset, offset + tmp96);
							offset += tmp96;
							int tmp98;
							tmp98 = ByteBuffer.wrap(Arrays.copyOfRange(tmp97, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
							
							tmp94 = new HashMap<>();
							for (int tmp99 = 0; tmp99 < tmp98; tmp99++)
							{
								Double tmp100;
								byte tmp102;
								tmp102 = s[offset];
								offset += Byte.BYTES;
								if (tmp102 == 1)
								{
									tmp100 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Double.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getDouble();
									offset += Double.BYTES;
								}
								else
									tmp100 = null;
								
								EColor tmp101;
								byte tmp103;
								tmp103 = s[offset];
								offset += Byte.BYTES;
								if (tmp103 == 1)
								{
									byte tmp104;
									tmp104 = s[offset];
									offset += Byte.BYTES;
									tmp101 = EColor.of(tmp104);
								}
								else
									tmp101 = null;
								
								tmp94.put(tmp100, tmp101);
							}
						}
						else
							tmp94 = null;
						tmp87.add(tmp94);
					}
				}
				else
					tmp87 = null;
				
				v18.put(tmp86, tmp87);
			}
		}
		else
			v18 = null;
		
		// deserialize v19
		byte tmp105;
		tmp105 = s[offset];
		offset += Byte.BYTES;
		if (tmp105 == 1)
		{
			v19 = new Byte[10];
			for (int tmp106 = 0; tmp106 < 10; tmp106++)
			{
				byte tmp107;
				tmp107 = s[offset];
				offset += Byte.BYTES;
				if (tmp107 == 1)
				{
					v19[tmp106] = s[offset];
					offset += Byte.BYTES;
				}
				else
					v19[tmp106] = null;
			}
		}
		else
			v19 = null;
		
		// deserialize v20
		byte tmp108;
		tmp108 = s[offset];
		offset += Byte.BYTES;
		if (tmp108 == 1)
		{
			v20 = new ArrayList[10][20];
			for (int tmp109 = 0; tmp109 < 10; tmp109++)
			{
				for (int tmp110 = 0; tmp110 < 20; tmp110++)
				{
					byte tmp111;
					tmp111 = s[offset];
					offset += Byte.BYTES;
					if (tmp111 == 1)
					{
						byte tmp112;
						tmp112 = s[offset];
						offset += Byte.BYTES;
						byte[] tmp113 = Arrays.copyOfRange(s, offset, offset + tmp112);
						offset += tmp112;
						int tmp114;
						tmp114 = ByteBuffer.wrap(Arrays.copyOfRange(tmp113, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
						
						v20[tmp109][tmp110] = new ArrayList<>();
						for (int tmp115 = 0; tmp115 < tmp114; tmp115++)
						{
							String tmp116;
							byte tmp117;
							tmp117 = s[offset];
							offset += Byte.BYTES;
							if (tmp117 == 1)
							{
								byte tmp118;
								tmp118 = s[offset];
								offset += Byte.BYTES;
								byte[] tmp119 = Arrays.copyOfRange(s, offset, offset + tmp118);
								offset += tmp118;
								int tmp120;
								tmp120 = ByteBuffer.wrap(Arrays.copyOfRange(tmp119, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
								
								tmp116 = new String(s, offset, tmp120, Charset.forName("ISO-8859-1"));
								offset += tmp120;
							}
							else
								tmp116 = null;
							v20[tmp109][tmp110].add(tmp116);
						}
					}
					else
						v20[tmp109][tmp110] = null;
				}
			}
		}
		else
			v20 = null;
		
		// deserialize v21
		byte tmp121;
		tmp121 = s[offset];
		offset += Byte.BYTES;
		if (tmp121 == 1)
		{
			byte tmp122;
			tmp122 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp123 = Arrays.copyOfRange(s, offset, offset + tmp122);
			offset += tmp122;
			int tmp124;
			tmp124 = ByteBuffer.wrap(Arrays.copyOfRange(tmp123, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			v21 = new ArrayList<>();
			for (int tmp125 = 0; tmp125 < tmp124; tmp125++)
			{
				Child[] tmp126;
				byte tmp127;
				tmp127 = s[offset];
				offset += Byte.BYTES;
				if (tmp127 == 1)
				{
					tmp126 = new Child[4];
					for (int tmp128 = 0; tmp128 < 4; tmp128++)
					{
						byte tmp129;
						tmp129 = s[offset];
						offset += Byte.BYTES;
						if (tmp129 == 1)
						{
							tmp126[tmp128] = new Child();
							offset = tmp126[tmp128].deserialize(s, offset);
						}
						else
							tmp126[tmp128] = null;
					}
				}
				else
					tmp126 = null;
				v21.add(tmp126);
			}
		}
		else
			v21 = null;
		
		// deserialize v22
		byte tmp130;
		tmp130 = s[offset];
		offset += Byte.BYTES;
		if (tmp130 == 1)
		{
			byte tmp131;
			tmp131 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp132 = Arrays.copyOfRange(s, offset, offset + tmp131);
			offset += tmp131;
			int tmp133;
			tmp133 = ByteBuffer.wrap(Arrays.copyOfRange(tmp132, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			v22 = new HashMap<>();
			for (int tmp134 = 0; tmp134 < tmp133; tmp134++)
			{
				String tmp135;
				byte tmp137;
				tmp137 = s[offset];
				offset += Byte.BYTES;
				if (tmp137 == 1)
				{
					byte tmp138;
					tmp138 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp139 = Arrays.copyOfRange(s, offset, offset + tmp138);
					offset += tmp138;
					int tmp140;
					tmp140 = ByteBuffer.wrap(Arrays.copyOfRange(tmp139, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp135 = new String(s, offset, tmp140, Charset.forName("ISO-8859-1"));
					offset += tmp140;
				}
				else
					tmp135 = null;
				
				Child tmp136;
				byte tmp141;
				tmp141 = s[offset];
				offset += Byte.BYTES;
				if (tmp141 == 1)
				{
					tmp136 = new Child();
					offset = tmp136.deserialize(s, offset);
				}
				else
					tmp136 = null;
				
				v22.put(tmp135, tmp136);
			}
		}
		else
			v22 = null;
		
		// deserialize v23
		byte tmp142;
		tmp142 = s[offset];
		offset += Byte.BYTES;
		if (tmp142 == 1)
		{
			v23 = new Child[5][10];
			for (int tmp143 = 0; tmp143 < 5; tmp143++)
			{
				for (int tmp144 = 0; tmp144 < 10; tmp144++)
				{
					byte tmp145;
					tmp145 = s[offset];
					offset += Byte.BYTES;
					if (tmp145 == 1)
					{
						v23[tmp143][tmp144] = new Child();
						offset = v23[tmp143][tmp144].deserialize(s, offset);
					}
					else
						v23[tmp143][tmp144] = null;
				}
			}
		}
		else
			v23 = null;
		
		return offset;
	}
}
