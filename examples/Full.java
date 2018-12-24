package ks.full;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.*;

public class Full
{
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
	
	public static class Parent extends KSObject
	{
		public String firstName;
		public String _lastName_;
		

		public Parent()
		{
		}
		
		public static final String NameStatic = "Parent";
		
		@Override
		public String Name() { return "Parent"; }
		
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
	
	public static class Child extends Parent
	{
		public String c;
		

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
			
			// serialize c
			s.add((byte) ((c == null) ? 0 : 1));
			if (c != null)
			{
				List<Byte> tmp10 = new ArrayList<>();
				tmp10.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(c.length()).array()));
				while (tmp10.size() > 0 && tmp10.get(tmp10.size() - 1) == 0)
					tmp10.remove(tmp10.size() - 1);
				s.add((byte) tmp10.size());
				s.addAll(tmp10);
				
				s.addAll(b2B(c.getBytes(Charset.forName("ISO-8859-1"))));
			}
			
			return B2b(s);
		}
		
		@Override
		protected int deserialize(byte[] s, int offset)
		{
			// deserialize parents
			offset = super.deserialize(s, offset);
			
			// deserialize c
			byte tmp11;
			tmp11 = s[offset];
			offset += Byte.BYTES;
			if (tmp11 == 1)
			{
				byte tmp12;
				tmp12 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp13 = Arrays.copyOfRange(s, offset, offset + tmp12);
				offset += tmp12;
				int tmp14;
				tmp14 = ByteBuffer.wrap(Arrays.copyOfRange(tmp13, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				c = new String(s, offset, tmp14, Charset.forName("ISO-8859-1"));
				offset += tmp14;
			}
			else
				c = null;
			
			return offset;
		}
	}
	
	public static class Test extends KSObject
	{
		public Boolean v0;
		public Character v1;
		public Byte v2;
		public Byte v3;
		public Short v4;
		public Short v5;
		public Integer v6;
		public Integer v7;
		public Long v8;
		public Long v9;
		public Float v10;
		public Double v11;
		public String v12;
		public EColor v13;
		public Child v14;
		public List<Integer> v15;
		public List<List<Character>> v16;
		public Map<String, Integer> v17;
		public Map<Character, List<Map<Double, EColor>>> v18;
		public Byte[] v19;
		public List<String>[][] v20;
		public List<Child[]> v21;
		public Map<String, Child> v22;
		public Child[][] v23;
		

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
				List<Byte> tmp15 = new ArrayList<>();
				tmp15.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v12.length()).array()));
				while (tmp15.size() > 0 && tmp15.get(tmp15.size() - 1) == 0)
					tmp15.remove(tmp15.size() - 1);
				s.add((byte) tmp15.size());
				s.addAll(tmp15);
				
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
				List<Byte> tmp16 = new ArrayList<>();
				tmp16.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v15.size()).array()));
				while (tmp16.size() > 0 && tmp16.get(tmp16.size() - 1) == 0)
					tmp16.remove(tmp16.size() - 1);
				s.add((byte) tmp16.size());
				s.addAll(tmp16);
				
				for (Integer tmp17 : v15)
				{
					s.add((byte) ((tmp17 == null) ? 0 : 1));
					if (tmp17 != null)
					{
						s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp17).array()));
					}
				}
			}
			
			// serialize v16
			s.add((byte) ((v16 == null) ? 0 : 1));
			if (v16 != null)
			{
				List<Byte> tmp18 = new ArrayList<>();
				tmp18.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v16.size()).array()));
				while (tmp18.size() > 0 && tmp18.get(tmp18.size() - 1) == 0)
					tmp18.remove(tmp18.size() - 1);
				s.add((byte) tmp18.size());
				s.addAll(tmp18);
				
				for (List<Character> tmp19 : v16)
				{
					s.add((byte) ((tmp19 == null) ? 0 : 1));
					if (tmp19 != null)
					{
						List<Byte> tmp20 = new ArrayList<>();
						tmp20.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp19.size()).array()));
						while (tmp20.size() > 0 && tmp20.get(tmp20.size() - 1) == 0)
							tmp20.remove(tmp20.size() - 1);
						s.add((byte) tmp20.size());
						s.addAll(tmp20);
						
						for (Character tmp21 : tmp19)
						{
							s.add((byte) ((tmp21 == null) ? 0 : 1));
							if (tmp21 != null)
							{
								s.add((byte) (char) tmp21);
							}
						}
					}
				}
			}
			
			// serialize v17
			s.add((byte) ((v17 == null) ? 0 : 1));
			if (v17 != null)
			{
				List<Byte> tmp22 = new ArrayList<>();
				tmp22.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v17.size()).array()));
				while (tmp22.size() > 0 && tmp22.get(tmp22.size() - 1) == 0)
					tmp22.remove(tmp22.size() - 1);
				s.add((byte) tmp22.size());
				s.addAll(tmp22);
				
				for (Map.Entry<String, Integer> tmp23 : v17.entrySet())
				{
					s.add((byte) ((tmp23.getKey() == null) ? 0 : 1));
					if (tmp23.getKey() != null)
					{
						List<Byte> tmp24 = new ArrayList<>();
						tmp24.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp23.getKey().length()).array()));
						while (tmp24.size() > 0 && tmp24.get(tmp24.size() - 1) == 0)
							tmp24.remove(tmp24.size() - 1);
						s.add((byte) tmp24.size());
						s.addAll(tmp24);
						
						s.addAll(b2B(tmp23.getKey().getBytes(Charset.forName("ISO-8859-1"))));
					}
					
					s.add((byte) ((tmp23.getValue() == null) ? 0 : 1));
					if (tmp23.getValue() != null)
					{
						s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp23.getValue()).array()));
					}
				}
			}
			
			// serialize v18
			s.add((byte) ((v18 == null) ? 0 : 1));
			if (v18 != null)
			{
				List<Byte> tmp25 = new ArrayList<>();
				tmp25.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v18.size()).array()));
				while (tmp25.size() > 0 && tmp25.get(tmp25.size() - 1) == 0)
					tmp25.remove(tmp25.size() - 1);
				s.add((byte) tmp25.size());
				s.addAll(tmp25);
				
				for (Map.Entry<Character, List<Map<Double, EColor>>> tmp26 : v18.entrySet())
				{
					s.add((byte) ((tmp26.getKey() == null) ? 0 : 1));
					if (tmp26.getKey() != null)
					{
						s.add((byte) (char) tmp26.getKey());
					}
					
					s.add((byte) ((tmp26.getValue() == null) ? 0 : 1));
					if (tmp26.getValue() != null)
					{
						List<Byte> tmp27 = new ArrayList<>();
						tmp27.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp26.getValue().size()).array()));
						while (tmp27.size() > 0 && tmp27.get(tmp27.size() - 1) == 0)
							tmp27.remove(tmp27.size() - 1);
						s.add((byte) tmp27.size());
						s.addAll(tmp27);
						
						for (Map<Double, EColor> tmp28 : tmp26.getValue())
						{
							s.add((byte) ((tmp28 == null) ? 0 : 1));
							if (tmp28 != null)
							{
								List<Byte> tmp29 = new ArrayList<>();
								tmp29.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp28.size()).array()));
								while (tmp29.size() > 0 && tmp29.get(tmp29.size() - 1) == 0)
									tmp29.remove(tmp29.size() - 1);
								s.add((byte) tmp29.size());
								s.addAll(tmp29);
								
								for (Map.Entry<Double, EColor> tmp30 : tmp28.entrySet())
								{
									s.add((byte) ((tmp30.getKey() == null) ? 0 : 1));
									if (tmp30.getKey() != null)
									{
										s.addAll(b2B(ByteBuffer.allocate(Double.BYTES).order(ByteOrder.LITTLE_ENDIAN).putDouble(tmp30.getKey()).array()));
									}
									
									s.add((byte) ((tmp30.getValue() == null) ? 0 : 1));
									if (tmp30.getValue() != null)
									{
										s.add((byte) (tmp30.getValue().getValue()));
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
				for (int tmp31 = 0; tmp31 < 10; tmp31++)
				{
					s.add((byte) ((v19[tmp31] == null) ? 0 : 1));
					if (v19[tmp31] != null)
					{
						s.add((byte) v19[tmp31]);
					}
				}
			}
			
			// serialize v20
			s.add((byte) ((v20 == null) ? 0 : 1));
			if (v20 != null)
			{
				for (int tmp32 = 0; tmp32 < 10; tmp32++)
				{
					for (int tmp33 = 0; tmp33 < 20; tmp33++)
					{
						s.add((byte) ((v20[tmp32][tmp33] == null) ? 0 : 1));
						if (v20[tmp32][tmp33] != null)
						{
							List<Byte> tmp34 = new ArrayList<>();
							tmp34.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v20[tmp32][tmp33].size()).array()));
							while (tmp34.size() > 0 && tmp34.get(tmp34.size() - 1) == 0)
								tmp34.remove(tmp34.size() - 1);
							s.add((byte) tmp34.size());
							s.addAll(tmp34);
							
							for (String tmp35 : v20[tmp32][tmp33])
							{
								s.add((byte) ((tmp35 == null) ? 0 : 1));
								if (tmp35 != null)
								{
									List<Byte> tmp36 = new ArrayList<>();
									tmp36.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp35.length()).array()));
									while (tmp36.size() > 0 && tmp36.get(tmp36.size() - 1) == 0)
										tmp36.remove(tmp36.size() - 1);
									s.add((byte) tmp36.size());
									s.addAll(tmp36);
									
									s.addAll(b2B(tmp35.getBytes(Charset.forName("ISO-8859-1"))));
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
				List<Byte> tmp37 = new ArrayList<>();
				tmp37.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v21.size()).array()));
				while (tmp37.size() > 0 && tmp37.get(tmp37.size() - 1) == 0)
					tmp37.remove(tmp37.size() - 1);
				s.add((byte) tmp37.size());
				s.addAll(tmp37);
				
				for (Child[] tmp38 : v21)
				{
					s.add((byte) ((tmp38 == null) ? 0 : 1));
					if (tmp38 != null)
					{
						for (int tmp39 = 0; tmp39 < 4; tmp39++)
						{
							s.add((byte) ((tmp38[tmp39] == null) ? 0 : 1));
							if (tmp38[tmp39] != null)
							{
								s.addAll(b2B(tmp38[tmp39].serialize()));
							}
						}
					}
				}
			}
			
			// serialize v22
			s.add((byte) ((v22 == null) ? 0 : 1));
			if (v22 != null)
			{
				List<Byte> tmp40 = new ArrayList<>();
				tmp40.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(v22.size()).array()));
				while (tmp40.size() > 0 && tmp40.get(tmp40.size() - 1) == 0)
					tmp40.remove(tmp40.size() - 1);
				s.add((byte) tmp40.size());
				s.addAll(tmp40);
				
				for (Map.Entry<String, Child> tmp41 : v22.entrySet())
				{
					s.add((byte) ((tmp41.getKey() == null) ? 0 : 1));
					if (tmp41.getKey() != null)
					{
						List<Byte> tmp42 = new ArrayList<>();
						tmp42.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp41.getKey().length()).array()));
						while (tmp42.size() > 0 && tmp42.get(tmp42.size() - 1) == 0)
							tmp42.remove(tmp42.size() - 1);
						s.add((byte) tmp42.size());
						s.addAll(tmp42);
						
						s.addAll(b2B(tmp41.getKey().getBytes(Charset.forName("ISO-8859-1"))));
					}
					
					s.add((byte) ((tmp41.getValue() == null) ? 0 : 1));
					if (tmp41.getValue() != null)
					{
						s.addAll(b2B(tmp41.getValue().serialize()));
					}
				}
			}
			
			// serialize v23
			s.add((byte) ((v23 == null) ? 0 : 1));
			if (v23 != null)
			{
				for (int tmp43 = 0; tmp43 < 5; tmp43++)
				{
					for (int tmp44 = 0; tmp44 < 10; tmp44++)
					{
						s.add((byte) ((v23[tmp43][tmp44] == null) ? 0 : 1));
						if (v23[tmp43][tmp44] != null)
						{
							s.addAll(b2B(v23[tmp43][tmp44].serialize()));
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
			byte tmp45;
			tmp45 = s[offset];
			offset += Byte.BYTES;
			if (tmp45 == 1)
			{
				v0 = (s[offset] == 0) ? false : true;
				offset += Byte.BYTES;
			}
			else
				v0 = null;
			
			// deserialize v1
			byte tmp46;
			tmp46 = s[offset];
			offset += Byte.BYTES;
			if (tmp46 == 1)
			{
				v1 = (char) s[offset];
				offset += Character.BYTES;
			}
			else
				v1 = null;
			
			// deserialize v2
			byte tmp47;
			tmp47 = s[offset];
			offset += Byte.BYTES;
			if (tmp47 == 1)
			{
				v2 = s[offset];
				offset += Byte.BYTES;
			}
			else
				v2 = null;
			
			// deserialize v3
			byte tmp48;
			tmp48 = s[offset];
			offset += Byte.BYTES;
			if (tmp48 == 1)
			{
				v3 = s[offset];
				offset += Byte.BYTES;
			}
			else
				v3 = null;
			
			// deserialize v4
			byte tmp49;
			tmp49 = s[offset];
			offset += Byte.BYTES;
			if (tmp49 == 1)
			{
				v4 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Short.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getShort();
				offset += Short.BYTES;
			}
			else
				v4 = null;
			
			// deserialize v5
			byte tmp50;
			tmp50 = s[offset];
			offset += Byte.BYTES;
			if (tmp50 == 1)
			{
				v5 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Short.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getShort();
				offset += Short.BYTES;
			}
			else
				v5 = null;
			
			// deserialize v6
			byte tmp51;
			tmp51 = s[offset];
			offset += Byte.BYTES;
			if (tmp51 == 1)
			{
				v6 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				offset += Integer.BYTES;
			}
			else
				v6 = null;
			
			// deserialize v7
			byte tmp52;
			tmp52 = s[offset];
			offset += Byte.BYTES;
			if (tmp52 == 1)
			{
				v7 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				offset += Integer.BYTES;
			}
			else
				v7 = null;
			
			// deserialize v8
			byte tmp53;
			tmp53 = s[offset];
			offset += Byte.BYTES;
			if (tmp53 == 1)
			{
				v8 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Long.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getLong();
				offset += Long.BYTES;
			}
			else
				v8 = null;
			
			// deserialize v9
			byte tmp54;
			tmp54 = s[offset];
			offset += Byte.BYTES;
			if (tmp54 == 1)
			{
				v9 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Long.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getLong();
				offset += Long.BYTES;
			}
			else
				v9 = null;
			
			// deserialize v10
			byte tmp55;
			tmp55 = s[offset];
			offset += Byte.BYTES;
			if (tmp55 == 1)
			{
				v10 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
				offset += Float.BYTES;
			}
			else
				v10 = null;
			
			// deserialize v11
			byte tmp56;
			tmp56 = s[offset];
			offset += Byte.BYTES;
			if (tmp56 == 1)
			{
				v11 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Double.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getDouble();
				offset += Double.BYTES;
			}
			else
				v11 = null;
			
			// deserialize v12
			byte tmp57;
			tmp57 = s[offset];
			offset += Byte.BYTES;
			if (tmp57 == 1)
			{
				byte tmp58;
				tmp58 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp59 = Arrays.copyOfRange(s, offset, offset + tmp58);
				offset += tmp58;
				int tmp60;
				tmp60 = ByteBuffer.wrap(Arrays.copyOfRange(tmp59, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				v12 = new String(s, offset, tmp60, Charset.forName("ISO-8859-1"));
				offset += tmp60;
			}
			else
				v12 = null;
			
			// deserialize v13
			byte tmp61;
			tmp61 = s[offset];
			offset += Byte.BYTES;
			if (tmp61 == 1)
			{
				byte tmp62;
				tmp62 = s[offset];
				offset += Byte.BYTES;
				v13 = EColor.of(tmp62);
			}
			else
				v13 = null;
			
			// deserialize v14
			byte tmp63;
			tmp63 = s[offset];
			offset += Byte.BYTES;
			if (tmp63 == 1)
			{
				v14 = new Child();
				offset = v14.deserialize(s, offset);
			}
			else
				v14 = null;
			
			// deserialize v15
			byte tmp64;
			tmp64 = s[offset];
			offset += Byte.BYTES;
			if (tmp64 == 1)
			{
				byte tmp65;
				tmp65 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp66 = Arrays.copyOfRange(s, offset, offset + tmp65);
				offset += tmp65;
				int tmp67;
				tmp67 = ByteBuffer.wrap(Arrays.copyOfRange(tmp66, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				v15 = new ArrayList<>();
				for (int tmp68 = 0; tmp68 < tmp67; tmp68++)
				{
					Integer tmp69;
					byte tmp70;
					tmp70 = s[offset];
					offset += Byte.BYTES;
					if (tmp70 == 1)
					{
						tmp69 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
						offset += Integer.BYTES;
					}
					else
						tmp69 = null;
					v15.add(tmp69);
				}
			}
			else
				v15 = null;
			
			// deserialize v16
			byte tmp71;
			tmp71 = s[offset];
			offset += Byte.BYTES;
			if (tmp71 == 1)
			{
				byte tmp72;
				tmp72 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp73 = Arrays.copyOfRange(s, offset, offset + tmp72);
				offset += tmp72;
				int tmp74;
				tmp74 = ByteBuffer.wrap(Arrays.copyOfRange(tmp73, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				v16 = new ArrayList<>();
				for (int tmp75 = 0; tmp75 < tmp74; tmp75++)
				{
					List<Character> tmp76;
					byte tmp77;
					tmp77 = s[offset];
					offset += Byte.BYTES;
					if (tmp77 == 1)
					{
						byte tmp78;
						tmp78 = s[offset];
						offset += Byte.BYTES;
						byte[] tmp79 = Arrays.copyOfRange(s, offset, offset + tmp78);
						offset += tmp78;
						int tmp80;
						tmp80 = ByteBuffer.wrap(Arrays.copyOfRange(tmp79, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
						
						tmp76 = new ArrayList<>();
						for (int tmp81 = 0; tmp81 < tmp80; tmp81++)
						{
							Character tmp82;
							byte tmp83;
							tmp83 = s[offset];
							offset += Byte.BYTES;
							if (tmp83 == 1)
							{
								tmp82 = (char) s[offset];
								offset += Character.BYTES;
							}
							else
								tmp82 = null;
							tmp76.add(tmp82);
						}
					}
					else
						tmp76 = null;
					v16.add(tmp76);
				}
			}
			else
				v16 = null;
			
			// deserialize v17
			byte tmp84;
			tmp84 = s[offset];
			offset += Byte.BYTES;
			if (tmp84 == 1)
			{
				byte tmp85;
				tmp85 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp86 = Arrays.copyOfRange(s, offset, offset + tmp85);
				offset += tmp85;
				int tmp87;
				tmp87 = ByteBuffer.wrap(Arrays.copyOfRange(tmp86, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				v17 = new HashMap<>();
				for (int tmp88 = 0; tmp88 < tmp87; tmp88++)
				{
					String tmp89;
					byte tmp91;
					tmp91 = s[offset];
					offset += Byte.BYTES;
					if (tmp91 == 1)
					{
						byte tmp92;
						tmp92 = s[offset];
						offset += Byte.BYTES;
						byte[] tmp93 = Arrays.copyOfRange(s, offset, offset + tmp92);
						offset += tmp92;
						int tmp94;
						tmp94 = ByteBuffer.wrap(Arrays.copyOfRange(tmp93, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
						
						tmp89 = new String(s, offset, tmp94, Charset.forName("ISO-8859-1"));
						offset += tmp94;
					}
					else
						tmp89 = null;
					
					Integer tmp90;
					byte tmp95;
					tmp95 = s[offset];
					offset += Byte.BYTES;
					if (tmp95 == 1)
					{
						tmp90 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
						offset += Integer.BYTES;
					}
					else
						tmp90 = null;
					
					v17.put(tmp89, tmp90);
				}
			}
			else
				v17 = null;
			
			// deserialize v18
			byte tmp96;
			tmp96 = s[offset];
			offset += Byte.BYTES;
			if (tmp96 == 1)
			{
				byte tmp97;
				tmp97 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp98 = Arrays.copyOfRange(s, offset, offset + tmp97);
				offset += tmp97;
				int tmp99;
				tmp99 = ByteBuffer.wrap(Arrays.copyOfRange(tmp98, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				v18 = new HashMap<>();
				for (int tmp100 = 0; tmp100 < tmp99; tmp100++)
				{
					Character tmp101;
					byte tmp103;
					tmp103 = s[offset];
					offset += Byte.BYTES;
					if (tmp103 == 1)
					{
						tmp101 = (char) s[offset];
						offset += Character.BYTES;
					}
					else
						tmp101 = null;
					
					List<Map<Double, EColor>> tmp102;
					byte tmp104;
					tmp104 = s[offset];
					offset += Byte.BYTES;
					if (tmp104 == 1)
					{
						byte tmp105;
						tmp105 = s[offset];
						offset += Byte.BYTES;
						byte[] tmp106 = Arrays.copyOfRange(s, offset, offset + tmp105);
						offset += tmp105;
						int tmp107;
						tmp107 = ByteBuffer.wrap(Arrays.copyOfRange(tmp106, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
						
						tmp102 = new ArrayList<>();
						for (int tmp108 = 0; tmp108 < tmp107; tmp108++)
						{
							Map<Double, EColor> tmp109;
							byte tmp110;
							tmp110 = s[offset];
							offset += Byte.BYTES;
							if (tmp110 == 1)
							{
								byte tmp111;
								tmp111 = s[offset];
								offset += Byte.BYTES;
								byte[] tmp112 = Arrays.copyOfRange(s, offset, offset + tmp111);
								offset += tmp111;
								int tmp113;
								tmp113 = ByteBuffer.wrap(Arrays.copyOfRange(tmp112, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
								
								tmp109 = new HashMap<>();
								for (int tmp114 = 0; tmp114 < tmp113; tmp114++)
								{
									Double tmp115;
									byte tmp117;
									tmp117 = s[offset];
									offset += Byte.BYTES;
									if (tmp117 == 1)
									{
										tmp115 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Double.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getDouble();
										offset += Double.BYTES;
									}
									else
										tmp115 = null;
									
									EColor tmp116;
									byte tmp118;
									tmp118 = s[offset];
									offset += Byte.BYTES;
									if (tmp118 == 1)
									{
										byte tmp119;
										tmp119 = s[offset];
										offset += Byte.BYTES;
										tmp116 = EColor.of(tmp119);
									}
									else
										tmp116 = null;
									
									tmp109.put(tmp115, tmp116);
								}
							}
							else
								tmp109 = null;
							tmp102.add(tmp109);
						}
					}
					else
						tmp102 = null;
					
					v18.put(tmp101, tmp102);
				}
			}
			else
				v18 = null;
			
			// deserialize v19
			byte tmp120;
			tmp120 = s[offset];
			offset += Byte.BYTES;
			if (tmp120 == 1)
			{
				v19 = new Byte[10];
				for (int tmp121 = 0; tmp121 < 10; tmp121++)
				{
					byte tmp122;
					tmp122 = s[offset];
					offset += Byte.BYTES;
					if (tmp122 == 1)
					{
						v19[tmp121] = s[offset];
						offset += Byte.BYTES;
					}
					else
						v19[tmp121] = null;
				}
			}
			else
				v19 = null;
			
			// deserialize v20
			byte tmp123;
			tmp123 = s[offset];
			offset += Byte.BYTES;
			if (tmp123 == 1)
			{
				v20 = new ArrayList[10][20];
				for (int tmp124 = 0; tmp124 < 10; tmp124++)
				{
					for (int tmp125 = 0; tmp125 < 20; tmp125++)
					{
						byte tmp126;
						tmp126 = s[offset];
						offset += Byte.BYTES;
						if (tmp126 == 1)
						{
							byte tmp127;
							tmp127 = s[offset];
							offset += Byte.BYTES;
							byte[] tmp128 = Arrays.copyOfRange(s, offset, offset + tmp127);
							offset += tmp127;
							int tmp129;
							tmp129 = ByteBuffer.wrap(Arrays.copyOfRange(tmp128, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
							
							v20[tmp124][tmp125] = new ArrayList<>();
							for (int tmp130 = 0; tmp130 < tmp129; tmp130++)
							{
								String tmp131;
								byte tmp132;
								tmp132 = s[offset];
								offset += Byte.BYTES;
								if (tmp132 == 1)
								{
									byte tmp133;
									tmp133 = s[offset];
									offset += Byte.BYTES;
									byte[] tmp134 = Arrays.copyOfRange(s, offset, offset + tmp133);
									offset += tmp133;
									int tmp135;
									tmp135 = ByteBuffer.wrap(Arrays.copyOfRange(tmp134, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
									
									tmp131 = new String(s, offset, tmp135, Charset.forName("ISO-8859-1"));
									offset += tmp135;
								}
								else
									tmp131 = null;
								v20[tmp124][tmp125].add(tmp131);
							}
						}
						else
							v20[tmp124][tmp125] = null;
					}
				}
			}
			else
				v20 = null;
			
			// deserialize v21
			byte tmp136;
			tmp136 = s[offset];
			offset += Byte.BYTES;
			if (tmp136 == 1)
			{
				byte tmp137;
				tmp137 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp138 = Arrays.copyOfRange(s, offset, offset + tmp137);
				offset += tmp137;
				int tmp139;
				tmp139 = ByteBuffer.wrap(Arrays.copyOfRange(tmp138, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				v21 = new ArrayList<>();
				for (int tmp140 = 0; tmp140 < tmp139; tmp140++)
				{
					Child[] tmp141;
					byte tmp142;
					tmp142 = s[offset];
					offset += Byte.BYTES;
					if (tmp142 == 1)
					{
						tmp141 = new Child[4];
						for (int tmp143 = 0; tmp143 < 4; tmp143++)
						{
							byte tmp144;
							tmp144 = s[offset];
							offset += Byte.BYTES;
							if (tmp144 == 1)
							{
								tmp141[tmp143] = new Child();
								offset = tmp141[tmp143].deserialize(s, offset);
							}
							else
								tmp141[tmp143] = null;
						}
					}
					else
						tmp141 = null;
					v21.add(tmp141);
				}
			}
			else
				v21 = null;
			
			// deserialize v22
			byte tmp145;
			tmp145 = s[offset];
			offset += Byte.BYTES;
			if (tmp145 == 1)
			{
				byte tmp146;
				tmp146 = s[offset];
				offset += Byte.BYTES;
				byte[] tmp147 = Arrays.copyOfRange(s, offset, offset + tmp146);
				offset += tmp146;
				int tmp148;
				tmp148 = ByteBuffer.wrap(Arrays.copyOfRange(tmp147, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
				
				v22 = new HashMap<>();
				for (int tmp149 = 0; tmp149 < tmp148; tmp149++)
				{
					String tmp150;
					byte tmp152;
					tmp152 = s[offset];
					offset += Byte.BYTES;
					if (tmp152 == 1)
					{
						byte tmp153;
						tmp153 = s[offset];
						offset += Byte.BYTES;
						byte[] tmp154 = Arrays.copyOfRange(s, offset, offset + tmp153);
						offset += tmp153;
						int tmp155;
						tmp155 = ByteBuffer.wrap(Arrays.copyOfRange(tmp154, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
						
						tmp150 = new String(s, offset, tmp155, Charset.forName("ISO-8859-1"));
						offset += tmp155;
					}
					else
						tmp150 = null;
					
					Child tmp151;
					byte tmp156;
					tmp156 = s[offset];
					offset += Byte.BYTES;
					if (tmp156 == 1)
					{
						tmp151 = new Child();
						offset = tmp151.deserialize(s, offset);
					}
					else
						tmp151 = null;
					
					v22.put(tmp150, tmp151);
				}
			}
			else
				v22 = null;
			
			// deserialize v23
			byte tmp157;
			tmp157 = s[offset];
			offset += Byte.BYTES;
			if (tmp157 == 1)
			{
				v23 = new Child[5][10];
				for (int tmp158 = 0; tmp158 < 5; tmp158++)
				{
					for (int tmp159 = 0; tmp159 < 10; tmp159++)
					{
						byte tmp160;
						tmp160 = s[offset];
						offset += Byte.BYTES;
						if (tmp160 == 1)
						{
							v23[tmp158][tmp159] = new Child();
							offset = v23[tmp158][tmp159].deserialize(s, offset);
						}
						else
							v23[tmp158][tmp159] = null;
					}
				}
			}
			else
				v23 = null;
			
			return offset;
		}
	}
} // Full
