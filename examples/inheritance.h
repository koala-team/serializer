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


class Parent3 : public KSObject
{

protected:




public: // getters


public: // reference getters


public: // setters


public: // has_attribute getters


public: // has_attribute setters


public:

	Parent3()
	{
	}
	
	static inline const std::string nameStatic()
	{
		return "Parent3";
	}
	
	virtual inline const std::string name() const
	{
		return "Parent3";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		return offset;
	}
};


class Child : public Parent1, Parent2
{

protected:

	std::string __firstname;

	bool __has_firstname;


public: // getters

	inline std::string firstname() const
	{
		return __firstname;
	}
	

public: // reference getters

	inline std::string &ref_firstname() const
	{
		return (std::string&) __firstname;
	}
	

public: // setters

	inline void firstname(const std::string &firstname)
	{
		__firstname = firstname;
		has_firstname(true);
	}
	

public: // has_attribute getters

	inline bool has_firstname() const
	{
		return __has_firstname;
	}
	

public: // has_attribute setters

	inline void has_firstname(const bool &has_firstname)
	{
		__has_firstname = has_firstname;
	}
	

public:

	Child()
	{
		has_firstname(false);
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
		
		// serialize firstname
		s += __has_firstname;
		if (__has_firstname)
		{
			std::string tmp6 = "";
			unsigned int tmp8 = __firstname.size();
			auto tmp9 = reinterpret_cast<char*>(&tmp8);
			tmp6 += std::string(tmp9, sizeof(unsigned int));
			while (tmp6.size() && tmp6.back() == 0)
				tmp6.pop_back();
			unsigned char tmp11 = tmp6.size();
			auto tmp12 = reinterpret_cast<char*>(&tmp11);
			s += std::string(tmp12, sizeof(unsigned char));
			s += tmp6;
			
			s += __firstname;
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Parent1::deserialize(s, offset);
		offset = Parent2::deserialize(s, offset);
		
		// deserialize firstname
		__has_firstname = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_firstname)
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
			
			__firstname = s.substr(offset, tmp15);
			offset += tmp15;
		}
		
		return offset;
	}
};


class GrandChild : public Child, Parent3
{

protected:

	float __height;

	bool __has_height;


public: // getters

	inline float height() const
	{
		return __height;
	}
	

public: // reference getters

	inline float &ref_height() const
	{
		return (float&) __height;
	}
	

public: // setters

	inline void height(const float &height)
	{
		__height = height;
		has_height(true);
	}
	

public: // has_attribute getters

	inline bool has_height() const
	{
		return __has_height;
	}
	

public: // has_attribute setters

	inline void has_height(const bool &has_height)
	{
		__has_height = has_height;
	}
	

public:

	GrandChild()
	{
		has_height(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "GrandChild";
	}
	
	virtual inline const std::string name() const
	{
		return "GrandChild";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize parents
		s += Child::serialize();
		s += Parent3::serialize();
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			float tmp17 = __height;
			auto tmp18 = reinterpret_cast<char*>(&tmp17);
			s += std::string(tmp18, sizeof(float));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Child::deserialize(s, offset);
		offset = Parent3::deserialize(s, offset);
		
		// deserialize height
		__has_height = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_height)
		{
			__height = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		return offset;
	}
};

} // namespace inheritance

} // namespace ks

#endif // _KS_INHERITANCE_H_
