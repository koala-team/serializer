#ifndef _KS_EMPTY_H_
#define _KS_EMPTY_H_

#include <string>
#include <vector>
#include <map>
#include <array>


#ifndef _KS_OBJECT_
#define _KS_OBJECT_

class KSObject
{

public:
	static std::string nameStatic() { return ""; };
	virtual std::string name() const = 0;
	virtual std::string serialize() const = 0;
	virtual unsigned int deserialize(const std::string &, unsigned int) = 0;

};

#endif // _KS_OBJECT_


namespace ks_empty
{

class Parent : public KSObject
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

	Parent()
	{
		has_count(false);
	}
	
	static std::string nameStatic()
	{
		return "Parent";
	}
	
	virtual std::string name() const
	{
		return "Parent";
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


class Child : public Parent
{

protected:




public: // getters


public: // reference getters


public: // setters


public: // has_attribute getters


public: // has_attribute setters


public:

	Child()
	{
	}
	
	static std::string nameStatic()
	{
		return "Child";
	}
	
	virtual std::string name() const
	{
		return "Child";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize parents
		s += Parent::serialize();
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Parent::deserialize(s, offset);
		
		return offset;
	}
};

}

#endif // _KS_EMPTY_H_
