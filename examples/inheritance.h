#ifndef _KS_INHERITANCE_H_
#define _KS_INHERITANCE_H_

#include <string>
#include <vector>
#include <map>
#include <array>


namespace ks
{

#ifndef _KS_OBJECT_
#define _KS_OBJECT_

class KSObject
{
public:
	static inline const std::string nameStatic() { return ""; }
	virtual inline const std::string name() const = 0;
	virtual std::string serialize() const = 0;
	virtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;
};

#endif // _KS_OBJECT_


namespace inheritance
{

class Parent1 : public KSObject
{

protected:

	unsigned int __count;

	bool __has_count;


public: // getters

	inline unsigned int count() const
	{
		return __count;
	}
	

public: // reference getters

	inline unsigned int &ref_count() const
	{
		return (unsigned int&) __count;
	}
	

public: // setters

	inline void count(const unsigned int &count)
	{
		__count = count;
		has_count(true);
	}
	

public: // has_attribute getters

	inline bool has_count() const
	{
		return __has_count;
	}
	

public: // has_attribute setters

	inline void has_count(const bool &has_count)
	{
		__has_count = has_count;
	}
	

public:

	Parent1()
	{
		has_count(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Parent1";
	}
	
	virtual inline const std::string name() const
	{
		return "Parent1";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize count
		s += __has_count;
		if (__has_count)
		{
			unsigned int tmp1 = __count;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(unsigned int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize count
		__has_count = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_count)
		{
			__count = *((unsigned int*) (&s[offset]));
			offset += sizeof(unsigned int);
		}
		
		return offset;
	}
};


class Parent2 : public KSObject
{

protected:

	long long __number;

	bool __has_number;


public: // getters

	inline long long number() const
	{
		return __number;
	}
	

public: // reference getters

	inline long long &ref_number() const
	{
		return (long long&) __number;
	}
	

public: // setters

	inline void number(const long long &number)
	{
		__number = number;
		has_number(true);
	}
	

public: // has_attribute getters

	inline bool has_number() const
	{
		return __has_number;
	}
	

public: // has_attribute setters

	inline void has_number(const bool &has_number)
	{
		__has_number = has_number;
	}
	

public:

	Parent2()
	{
		has_number(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Parent2";
	}
	
	virtual inline const std::string name() const
	{
		return "Parent2";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize number
		s += __has_number;
		if (__has_number)
		{
			long long tmp4 = __number;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(long long));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize number
		__has_number = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_number)
		{
			__number = *((long long*) (&s[offset]));
			offset += sizeof(long long);
		}
		
		return offset;
	}
};


class Child : public Parent1, Parent2
{

protected:

	std::string __name;

	bool __has_name;


public: // getters

	inline std::string name() const
	{
		return __name;
	}
	

public: // reference getters

	inline std::string &ref_name() const
	{
		return (std::string&) __name;
	}
	

public: // setters

	inline void name(const std::string &name)
	{
		__name = name;
		has_name(true);
	}
	

public: // has_attribute getters

	inline bool has_name() const
	{
		return __has_name;
	}
	

public: // has_attribute setters

	inline void has_name(const bool &has_name)
	{
		__has_name = has_name;
	}
	

public:

	Child()
	{
		has_name(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Child";
	}
	
	virtual inline const std::string name() const
	{
		return "Child";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize parents
		s += Parent1::serialize();
		s += Parent2::serialize();
		
		// serialize name
		s += __has_name;
		if (__has_name)
		{
			std::string tmp6 = "";
			unsigned int tmp8 = __name.size();
			auto tmp9 = reinterpret_cast<char*>(&tmp8);
			tmp6 += std::string(tmp9, sizeof(unsigned int));
			while (tmp6.size() && tmp6.back() == 0)
				tmp6.pop_back();
			unsigned char tmp11 = tmp6.size();
			auto tmp12 = reinterpret_cast<char*>(&tmp11);
			s += std::string(tmp12, sizeof(unsigned char));
			s += tmp6;
			
			s += __name;
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Parent1::deserialize(s, offset);
		offset = Parent2::deserialize(s, offset);
		
		// deserialize name
		__has_name = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_name)
		{
			unsigned char tmp13;
			tmp13 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp14 = std::string(&s[offset], tmp13);
			offset += tmp13;
			while (tmp14.size() < sizeof(unsigned int))
				tmp14 += '\x00';
			unsigned int tmp15;
			tmp15 = *((unsigned int*) (&tmp14[0]));
			
			__name = s.substr(offset, tmp15);
			offset += tmp15;
		}
		
		return offset;
	}
};

} // namespace inheritance

} // namespace ks

#endif // _KS_INHERITANCE_H_
