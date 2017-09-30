#ifndef _KS_FULL_H_
#define _KS_FULL_H_

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


namespace full
{

enum class EColor
{
	white = 0,
	red = 3,
	green = 4,
	blue = -2,
	black = -1,
};


class Parent1 : public KSObject
{

protected:

	unsigned int __p1;

	bool __has_p1;


public: // getters

	inline unsigned int p1() const
	{
		return __p1;
	}
	

public: // reference getters

	inline unsigned int &ref_p1() const
	{
		return (unsigned int&) __p1;
	}
	

public: // setters

	inline void p1(const unsigned int &p1)
	{
		__p1 = p1;
		has_p1(true);
	}
	

public: // has_attribute getters

	inline bool has_p1() const
	{
		return __has_p1;
	}
	

public: // has_attribute setters

	inline void has_p1(const bool &has_p1)
	{
		__has_p1 = has_p1;
	}
	

public:

	Parent1()
	{
		has_p1(false);
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
		
		// serialize p1
		s += __has_p1;
		if (__has_p1)
		{
			unsigned int tmp1 = __p1;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(unsigned int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize p1
		__has_p1 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_p1)
		{
			__p1 = *((unsigned int*) (&s[offset]));
			offset += sizeof(unsigned int);
		}
		
		return offset;
	}
};


class Parent2 : public KSObject
{

protected:

	long long __p2;

	bool __has_p2;


public: // getters

	inline long long p2() const
	{
		return __p2;
	}
	

public: // reference getters

	inline long long &ref_p2() const
	{
		return (long long&) __p2;
	}
	

public: // setters

	inline void p2(const long long &p2)
	{
		__p2 = p2;
		has_p2(true);
	}
	

public: // has_attribute getters

	inline bool has_p2() const
	{
		return __has_p2;
	}
	

public: // has_attribute setters

	inline void has_p2(const bool &has_p2)
	{
		__has_p2 = has_p2;
	}
	

public:

	Parent2()
	{
		has_p2(false);
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
		
		// serialize p2
		s += __has_p2;
		if (__has_p2)
		{
			long long tmp4 = __p2;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(long long));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize p2
		__has_p2 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_p2)
		{
			__p2 = *((long long*) (&s[offset]));
			offset += sizeof(long long);
		}
		
		return offset;
	}
};


class Child : public Parent1, Parent2
{

protected:

	std::string __c;

	bool __has_c;


public: // getters

	inline std::string c() const
	{
		return __c;
	}
	

public: // reference getters

	inline std::string &ref_c() const
	{
		return (std::string&) __c;
	}
	

public: // setters

	inline void c(const std::string &c)
	{
		__c = c;
		has_c(true);
	}
	

public: // has_attribute getters

	inline bool has_c() const
	{
		return __has_c;
	}
	

public: // has_attribute setters

	inline void has_c(const bool &has_c)
	{
		__has_c = has_c;
	}
	

public:

	Child()
	{
		has_c(false);
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
		
		// serialize c
		s += __has_c;
		if (__has_c)
		{
			std::string tmp6 = "";
			unsigned int tmp8 = __c.size();
			auto tmp9 = reinterpret_cast<char*>(&tmp8);
			tmp6 += std::string(tmp9, sizeof(unsigned int));
			while (tmp6.size() && tmp6.back() == 0)
				tmp6.pop_back();
			unsigned char tmp11 = tmp6.size();
			auto tmp12 = reinterpret_cast<char*>(&tmp11);
			s += std::string(tmp12, sizeof(unsigned char));
			s += tmp6;
			
			s += __c;
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Parent1::deserialize(s, offset);
		offset = Parent2::deserialize(s, offset);
		
		// deserialize c
		__has_c = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_c)
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
			
			__c = s.substr(offset, tmp15);
			offset += tmp15;
		}
		
		return offset;
	}
};


class Test : public KSObject
{

protected:

	bool __v0;
	char __v1;
	char __v2;
	unsigned char __v3;
	short __v4;
	unsigned short __v5;
	int __v6;
	unsigned int __v7;
	long long __v8;
	unsigned long long __v9;
	float __v10;
	double __v11;
	std::string __v12;
	EColor __v13;
	Child __v14;
	std::vector<int> __v15;
	std::vector<std::vector<char>> __v16;
	std::map<std::string, int> __v17;
	std::map<char, std::vector<std::map<double, EColor>>> __v18;
	std::array<char, 10> __v19;
	std::array<std::array<std::vector<std::string>, 20>, 10> __v20;
	std::vector<Child> __v21;
	std::map<std::string, Child> __v22;
	std::array<std::array<Child, 10>, 5> __v23;

	bool __has_v0;
	bool __has_v1;
	bool __has_v2;
	bool __has_v3;
	bool __has_v4;
	bool __has_v5;
	bool __has_v6;
	bool __has_v7;
	bool __has_v8;
	bool __has_v9;
	bool __has_v10;
	bool __has_v11;
	bool __has_v12;
	bool __has_v13;
	bool __has_v14;
	bool __has_v15;
	bool __has_v16;
	bool __has_v17;
	bool __has_v18;
	bool __has_v19;
	bool __has_v20;
	bool __has_v21;
	bool __has_v22;
	bool __has_v23;


public: // getters

	inline bool v0() const
	{
		return __v0;
	}
	
	inline char v1() const
	{
		return __v1;
	}
	
	inline char v2() const
	{
		return __v2;
	}
	
	inline unsigned char v3() const
	{
		return __v3;
	}
	
	inline short v4() const
	{
		return __v4;
	}
	
	inline unsigned short v5() const
	{
		return __v5;
	}
	
	inline int v6() const
	{
		return __v6;
	}
	
	inline unsigned int v7() const
	{
		return __v7;
	}
	
	inline long long v8() const
	{
		return __v8;
	}
	
	inline unsigned long long v9() const
	{
		return __v9;
	}
	
	inline float v10() const
	{
		return __v10;
	}
	
	inline double v11() const
	{
		return __v11;
	}
	
	inline std::string v12() const
	{
		return __v12;
	}
	
	inline EColor v13() const
	{
		return __v13;
	}
	
	inline Child v14() const
	{
		return __v14;
	}
	
	inline std::vector<int> v15() const
	{
		return __v15;
	}
	
	inline std::vector<std::vector<char>> v16() const
	{
		return __v16;
	}
	
	inline std::map<std::string, int> v17() const
	{
		return __v17;
	}
	
	inline std::map<char, std::vector<std::map<double, EColor>>> v18() const
	{
		return __v18;
	}
	
	inline std::array<char, 10> v19() const
	{
		return __v19;
	}
	
	inline std::array<std::array<std::vector<std::string>, 20>, 10> v20() const
	{
		return __v20;
	}
	
	inline std::vector<Child> v21() const
	{
		return __v21;
	}
	
	inline std::map<std::string, Child> v22() const
	{
		return __v22;
	}
	
	inline std::array<std::array<Child, 10>, 5> v23() const
	{
		return __v23;
	}
	

public: // reference getters

	inline bool &ref_v0() const
	{
		return (bool&) __v0;
	}
	
	inline char &ref_v1() const
	{
		return (char&) __v1;
	}
	
	inline char &ref_v2() const
	{
		return (char&) __v2;
	}
	
	inline unsigned char &ref_v3() const
	{
		return (unsigned char&) __v3;
	}
	
	inline short &ref_v4() const
	{
		return (short&) __v4;
	}
	
	inline unsigned short &ref_v5() const
	{
		return (unsigned short&) __v5;
	}
	
	inline int &ref_v6() const
	{
		return (int&) __v6;
	}
	
	inline unsigned int &ref_v7() const
	{
		return (unsigned int&) __v7;
	}
	
	inline long long &ref_v8() const
	{
		return (long long&) __v8;
	}
	
	inline unsigned long long &ref_v9() const
	{
		return (unsigned long long&) __v9;
	}
	
	inline float &ref_v10() const
	{
		return (float&) __v10;
	}
	
	inline double &ref_v11() const
	{
		return (double&) __v11;
	}
	
	inline std::string &ref_v12() const
	{
		return (std::string&) __v12;
	}
	
	inline EColor &ref_v13() const
	{
		return (EColor&) __v13;
	}
	
	inline Child &ref_v14() const
	{
		return (Child&) __v14;
	}
	
	inline std::vector<int> &ref_v15() const
	{
		return (std::vector<int>&) __v15;
	}
	
	inline std::vector<std::vector<char>> &ref_v16() const
	{
		return (std::vector<std::vector<char>>&) __v16;
	}
	
	inline std::map<std::string, int> &ref_v17() const
	{
		return (std::map<std::string, int>&) __v17;
	}
	
	inline std::map<char, std::vector<std::map<double, EColor>>> &ref_v18() const
	{
		return (std::map<char, std::vector<std::map<double, EColor>>>&) __v18;
	}
	
	inline std::array<char, 10> &ref_v19() const
	{
		return (std::array<char, 10>&) __v19;
	}
	
	inline std::array<std::array<std::vector<std::string>, 20>, 10> &ref_v20() const
	{
		return (std::array<std::array<std::vector<std::string>, 20>, 10>&) __v20;
	}
	
	inline std::vector<Child> &ref_v21() const
	{
		return (std::vector<Child>&) __v21;
	}
	
	inline std::map<std::string, Child> &ref_v22() const
	{
		return (std::map<std::string, Child>&) __v22;
	}
	
	inline std::array<std::array<Child, 10>, 5> &ref_v23() const
	{
		return (std::array<std::array<Child, 10>, 5>&) __v23;
	}
	

public: // setters

	inline void v0(const bool &v0)
	{
		__v0 = v0;
		has_v0(true);
	}
	
	inline void v1(const char &v1)
	{
		__v1 = v1;
		has_v1(true);
	}
	
	inline void v2(const char &v2)
	{
		__v2 = v2;
		has_v2(true);
	}
	
	inline void v3(const unsigned char &v3)
	{
		__v3 = v3;
		has_v3(true);
	}
	
	inline void v4(const short &v4)
	{
		__v4 = v4;
		has_v4(true);
	}
	
	inline void v5(const unsigned short &v5)
	{
		__v5 = v5;
		has_v5(true);
	}
	
	inline void v6(const int &v6)
	{
		__v6 = v6;
		has_v6(true);
	}
	
	inline void v7(const unsigned int &v7)
	{
		__v7 = v7;
		has_v7(true);
	}
	
	inline void v8(const long long &v8)
	{
		__v8 = v8;
		has_v8(true);
	}
	
	inline void v9(const unsigned long long &v9)
	{
		__v9 = v9;
		has_v9(true);
	}
	
	inline void v10(const float &v10)
	{
		__v10 = v10;
		has_v10(true);
	}
	
	inline void v11(const double &v11)
	{
		__v11 = v11;
		has_v11(true);
	}
	
	inline void v12(const std::string &v12)
	{
		__v12 = v12;
		has_v12(true);
	}
	
	inline void v13(const EColor &v13)
	{
		__v13 = v13;
		has_v13(true);
	}
	
	inline void v14(const Child &v14)
	{
		__v14 = v14;
		has_v14(true);
	}
	
	inline void v15(const std::vector<int> &v15)
	{
		__v15 = v15;
		has_v15(true);
	}
	
	inline void v16(const std::vector<std::vector<char>> &v16)
	{
		__v16 = v16;
		has_v16(true);
	}
	
	inline void v17(const std::map<std::string, int> &v17)
	{
		__v17 = v17;
		has_v17(true);
	}
	
	inline void v18(const std::map<char, std::vector<std::map<double, EColor>>> &v18)
	{
		__v18 = v18;
		has_v18(true);
	}
	
	inline void v19(const std::array<char, 10> &v19)
	{
		__v19 = v19;
		has_v19(true);
	}
	
	inline void v20(const std::array<std::array<std::vector<std::string>, 20>, 10> &v20)
	{
		__v20 = v20;
		has_v20(true);
	}
	
	inline void v21(const std::vector<Child> &v21)
	{
		__v21 = v21;
		has_v21(true);
	}
	
	inline void v22(const std::map<std::string, Child> &v22)
	{
		__v22 = v22;
		has_v22(true);
	}
	
	inline void v23(const std::array<std::array<Child, 10>, 5> &v23)
	{
		__v23 = v23;
		has_v23(true);
	}
	

public: // has_attribute getters

	inline bool has_v0() const
	{
		return __has_v0;
	}
	
	inline bool has_v1() const
	{
		return __has_v1;
	}
	
	inline bool has_v2() const
	{
		return __has_v2;
	}
	
	inline bool has_v3() const
	{
		return __has_v3;
	}
	
	inline bool has_v4() const
	{
		return __has_v4;
	}
	
	inline bool has_v5() const
	{
		return __has_v5;
	}
	
	inline bool has_v6() const
	{
		return __has_v6;
	}
	
	inline bool has_v7() const
	{
		return __has_v7;
	}
	
	inline bool has_v8() const
	{
		return __has_v8;
	}
	
	inline bool has_v9() const
	{
		return __has_v9;
	}
	
	inline bool has_v10() const
	{
		return __has_v10;
	}
	
	inline bool has_v11() const
	{
		return __has_v11;
	}
	
	inline bool has_v12() const
	{
		return __has_v12;
	}
	
	inline bool has_v13() const
	{
		return __has_v13;
	}
	
	inline bool has_v14() const
	{
		return __has_v14;
	}
	
	inline bool has_v15() const
	{
		return __has_v15;
	}
	
	inline bool has_v16() const
	{
		return __has_v16;
	}
	
	inline bool has_v17() const
	{
		return __has_v17;
	}
	
	inline bool has_v18() const
	{
		return __has_v18;
	}
	
	inline bool has_v19() const
	{
		return __has_v19;
	}
	
	inline bool has_v20() const
	{
		return __has_v20;
	}
	
	inline bool has_v21() const
	{
		return __has_v21;
	}
	
	inline bool has_v22() const
	{
		return __has_v22;
	}
	
	inline bool has_v23() const
	{
		return __has_v23;
	}
	

public: // has_attribute setters

	inline void has_v0(const bool &has_v0)
	{
		__has_v0 = has_v0;
	}
	
	inline void has_v1(const bool &has_v1)
	{
		__has_v1 = has_v1;
	}
	
	inline void has_v2(const bool &has_v2)
	{
		__has_v2 = has_v2;
	}
	
	inline void has_v3(const bool &has_v3)
	{
		__has_v3 = has_v3;
	}
	
	inline void has_v4(const bool &has_v4)
	{
		__has_v4 = has_v4;
	}
	
	inline void has_v5(const bool &has_v5)
	{
		__has_v5 = has_v5;
	}
	
	inline void has_v6(const bool &has_v6)
	{
		__has_v6 = has_v6;
	}
	
	inline void has_v7(const bool &has_v7)
	{
		__has_v7 = has_v7;
	}
	
	inline void has_v8(const bool &has_v8)
	{
		__has_v8 = has_v8;
	}
	
	inline void has_v9(const bool &has_v9)
	{
		__has_v9 = has_v9;
	}
	
	inline void has_v10(const bool &has_v10)
	{
		__has_v10 = has_v10;
	}
	
	inline void has_v11(const bool &has_v11)
	{
		__has_v11 = has_v11;
	}
	
	inline void has_v12(const bool &has_v12)
	{
		__has_v12 = has_v12;
	}
	
	inline void has_v13(const bool &has_v13)
	{
		__has_v13 = has_v13;
	}
	
	inline void has_v14(const bool &has_v14)
	{
		__has_v14 = has_v14;
	}
	
	inline void has_v15(const bool &has_v15)
	{
		__has_v15 = has_v15;
	}
	
	inline void has_v16(const bool &has_v16)
	{
		__has_v16 = has_v16;
	}
	
	inline void has_v17(const bool &has_v17)
	{
		__has_v17 = has_v17;
	}
	
	inline void has_v18(const bool &has_v18)
	{
		__has_v18 = has_v18;
	}
	
	inline void has_v19(const bool &has_v19)
	{
		__has_v19 = has_v19;
	}
	
	inline void has_v20(const bool &has_v20)
	{
		__has_v20 = has_v20;
	}
	
	inline void has_v21(const bool &has_v21)
	{
		__has_v21 = has_v21;
	}
	
	inline void has_v22(const bool &has_v22)
	{
		__has_v22 = has_v22;
	}
	
	inline void has_v23(const bool &has_v23)
	{
		__has_v23 = has_v23;
	}
	

public:

	Test()
	{
		has_v0(false);
		has_v1(false);
		has_v2(false);
		has_v3(false);
		has_v4(false);
		has_v5(false);
		has_v6(false);
		has_v7(false);
		has_v8(false);
		has_v9(false);
		has_v10(false);
		has_v11(false);
		has_v12(false);
		has_v13(false);
		has_v14(false);
		has_v15(false);
		has_v16(false);
		has_v17(false);
		has_v18(false);
		has_v19(false);
		has_v20(false);
		has_v21(false);
		has_v22(false);
		has_v23(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Test";
	}
	
	virtual inline const std::string name() const
	{
		return "Test";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize v0
		s += __has_v0;
		if (__has_v0)
		{
			bool tmp17 = __v0;
			auto tmp18 = reinterpret_cast<char*>(&tmp17);
			s += std::string(tmp18, sizeof(bool));
		}
		
		// serialize v1
		s += __has_v1;
		if (__has_v1)
		{
			char tmp20 = __v1;
			auto tmp21 = reinterpret_cast<char*>(&tmp20);
			s += std::string(tmp21, sizeof(char));
		}
		
		// serialize v2
		s += __has_v2;
		if (__has_v2)
		{
			char tmp23 = __v2;
			auto tmp24 = reinterpret_cast<char*>(&tmp23);
			s += std::string(tmp24, sizeof(char));
		}
		
		// serialize v3
		s += __has_v3;
		if (__has_v3)
		{
			unsigned char tmp26 = __v3;
			auto tmp27 = reinterpret_cast<char*>(&tmp26);
			s += std::string(tmp27, sizeof(unsigned char));
		}
		
		// serialize v4
		s += __has_v4;
		if (__has_v4)
		{
			short tmp29 = __v4;
			auto tmp30 = reinterpret_cast<char*>(&tmp29);
			s += std::string(tmp30, sizeof(short));
		}
		
		// serialize v5
		s += __has_v5;
		if (__has_v5)
		{
			unsigned short tmp32 = __v5;
			auto tmp33 = reinterpret_cast<char*>(&tmp32);
			s += std::string(tmp33, sizeof(unsigned short));
		}
		
		// serialize v6
		s += __has_v6;
		if (__has_v6)
		{
			int tmp35 = __v6;
			auto tmp36 = reinterpret_cast<char*>(&tmp35);
			s += std::string(tmp36, sizeof(int));
		}
		
		// serialize v7
		s += __has_v7;
		if (__has_v7)
		{
			unsigned int tmp38 = __v7;
			auto tmp39 = reinterpret_cast<char*>(&tmp38);
			s += std::string(tmp39, sizeof(unsigned int));
		}
		
		// serialize v8
		s += __has_v8;
		if (__has_v8)
		{
			long long tmp41 = __v8;
			auto tmp42 = reinterpret_cast<char*>(&tmp41);
			s += std::string(tmp42, sizeof(long long));
		}
		
		// serialize v9
		s += __has_v9;
		if (__has_v9)
		{
			unsigned long long tmp44 = __v9;
			auto tmp45 = reinterpret_cast<char*>(&tmp44);
			s += std::string(tmp45, sizeof(unsigned long long));
		}
		
		// serialize v10
		s += __has_v10;
		if (__has_v10)
		{
			float tmp47 = __v10;
			auto tmp48 = reinterpret_cast<char*>(&tmp47);
			s += std::string(tmp48, sizeof(float));
		}
		
		// serialize v11
		s += __has_v11;
		if (__has_v11)
		{
			double tmp50 = __v11;
			auto tmp51 = reinterpret_cast<char*>(&tmp50);
			s += std::string(tmp51, sizeof(double));
		}
		
		// serialize v12
		s += __has_v12;
		if (__has_v12)
		{
			std::string tmp52 = "";
			unsigned int tmp54 = __v12.size();
			auto tmp55 = reinterpret_cast<char*>(&tmp54);
			tmp52 += std::string(tmp55, sizeof(unsigned int));
			while (tmp52.size() && tmp52.back() == 0)
				tmp52.pop_back();
			unsigned char tmp57 = tmp52.size();
			auto tmp58 = reinterpret_cast<char*>(&tmp57);
			s += std::string(tmp58, sizeof(unsigned char));
			s += tmp52;
			
			s += __v12;
		}
		
		// serialize v13
		s += __has_v13;
		if (__has_v13)
		{
			char tmp60 = (char) __v13;
			auto tmp61 = reinterpret_cast<char*>(&tmp60);
			s += std::string(tmp61, sizeof(char));
		}
		
		// serialize v14
		s += __has_v14;
		if (__has_v14)
		{
			s += __v14.serialize();
		}
		
		// serialize v15
		s += __has_v15;
		if (__has_v15)
		{
			std::string tmp62 = "";
			unsigned int tmp64 = __v15.size();
			auto tmp65 = reinterpret_cast<char*>(&tmp64);
			tmp62 += std::string(tmp65, sizeof(unsigned int));
			while (tmp62.size() && tmp62.back() == 0)
				tmp62.pop_back();
			unsigned char tmp67 = tmp62.size();
			auto tmp68 = reinterpret_cast<char*>(&tmp67);
			s += std::string(tmp68, sizeof(unsigned char));
			s += tmp62;
			
			for (auto &tmp69 : __v15)
			{
				s += '\x01';
				int tmp71 = tmp69;
				auto tmp72 = reinterpret_cast<char*>(&tmp71);
				s += std::string(tmp72, sizeof(int));
			}
		}
		
		// serialize v16
		s += __has_v16;
		if (__has_v16)
		{
			std::string tmp73 = "";
			unsigned int tmp75 = __v16.size();
			auto tmp76 = reinterpret_cast<char*>(&tmp75);
			tmp73 += std::string(tmp76, sizeof(unsigned int));
			while (tmp73.size() && tmp73.back() == 0)
				tmp73.pop_back();
			unsigned char tmp78 = tmp73.size();
			auto tmp79 = reinterpret_cast<char*>(&tmp78);
			s += std::string(tmp79, sizeof(unsigned char));
			s += tmp73;
			
			for (auto &tmp80 : __v16)
			{
				s += '\x01';
				std::string tmp81 = "";
				unsigned int tmp83 = tmp80.size();
				auto tmp84 = reinterpret_cast<char*>(&tmp83);
				tmp81 += std::string(tmp84, sizeof(unsigned int));
				while (tmp81.size() && tmp81.back() == 0)
					tmp81.pop_back();
				unsigned char tmp86 = tmp81.size();
				auto tmp87 = reinterpret_cast<char*>(&tmp86);
				s += std::string(tmp87, sizeof(unsigned char));
				s += tmp81;
				
				for (auto &tmp88 : tmp80)
				{
					s += '\x01';
					char tmp90 = tmp88;
					auto tmp91 = reinterpret_cast<char*>(&tmp90);
					s += std::string(tmp91, sizeof(char));
				}
			}
		}
		
		// serialize v17
		s += __has_v17;
		if (__has_v17)
		{
			std::string tmp92 = "";
			unsigned int tmp94 = __v17.size();
			auto tmp95 = reinterpret_cast<char*>(&tmp94);
			tmp92 += std::string(tmp95, sizeof(unsigned int));
			while (tmp92.size() && tmp92.back() == 0)
				tmp92.pop_back();
			unsigned char tmp97 = tmp92.size();
			auto tmp98 = reinterpret_cast<char*>(&tmp97);
			s += std::string(tmp98, sizeof(unsigned char));
			s += tmp92;
			
			for (auto &tmp99 : __v17)
			{
				s += '\x01';
				std::string tmp100 = "";
				unsigned int tmp102 = tmp99.first.size();
				auto tmp103 = reinterpret_cast<char*>(&tmp102);
				tmp100 += std::string(tmp103, sizeof(unsigned int));
				while (tmp100.size() && tmp100.back() == 0)
					tmp100.pop_back();
				unsigned char tmp105 = tmp100.size();
				auto tmp106 = reinterpret_cast<char*>(&tmp105);
				s += std::string(tmp106, sizeof(unsigned char));
				s += tmp100;
				
				s += tmp99.first;
				
				s += '\x01';
				int tmp108 = tmp99.second;
				auto tmp109 = reinterpret_cast<char*>(&tmp108);
				s += std::string(tmp109, sizeof(int));
			}
		}
		
		// serialize v18
		s += __has_v18;
		if (__has_v18)
		{
			std::string tmp110 = "";
			unsigned int tmp112 = __v18.size();
			auto tmp113 = reinterpret_cast<char*>(&tmp112);
			tmp110 += std::string(tmp113, sizeof(unsigned int));
			while (tmp110.size() && tmp110.back() == 0)
				tmp110.pop_back();
			unsigned char tmp115 = tmp110.size();
			auto tmp116 = reinterpret_cast<char*>(&tmp115);
			s += std::string(tmp116, sizeof(unsigned char));
			s += tmp110;
			
			for (auto &tmp117 : __v18)
			{
				s += '\x01';
				char tmp119 = tmp117.first;
				auto tmp120 = reinterpret_cast<char*>(&tmp119);
				s += std::string(tmp120, sizeof(char));
				
				s += '\x01';
				std::string tmp121 = "";
				unsigned int tmp123 = tmp117.second.size();
				auto tmp124 = reinterpret_cast<char*>(&tmp123);
				tmp121 += std::string(tmp124, sizeof(unsigned int));
				while (tmp121.size() && tmp121.back() == 0)
					tmp121.pop_back();
				unsigned char tmp126 = tmp121.size();
				auto tmp127 = reinterpret_cast<char*>(&tmp126);
				s += std::string(tmp127, sizeof(unsigned char));
				s += tmp121;
				
				for (auto &tmp128 : tmp117.second)
				{
					s += '\x01';
					std::string tmp129 = "";
					unsigned int tmp131 = tmp128.size();
					auto tmp132 = reinterpret_cast<char*>(&tmp131);
					tmp129 += std::string(tmp132, sizeof(unsigned int));
					while (tmp129.size() && tmp129.back() == 0)
						tmp129.pop_back();
					unsigned char tmp134 = tmp129.size();
					auto tmp135 = reinterpret_cast<char*>(&tmp134);
					s += std::string(tmp135, sizeof(unsigned char));
					s += tmp129;
					
					for (auto &tmp136 : tmp128)
					{
						s += '\x01';
						double tmp138 = tmp136.first;
						auto tmp139 = reinterpret_cast<char*>(&tmp138);
						s += std::string(tmp139, sizeof(double));
						
						s += '\x01';
						char tmp141 = (char) tmp136.second;
						auto tmp142 = reinterpret_cast<char*>(&tmp141);
						s += std::string(tmp142, sizeof(char));
					}
				}
			}
		}
		
		// serialize v19
		s += __has_v19;
		if (__has_v19)
		{
			for (unsigned int tmp143 = 0; tmp143 < 10; tmp143++)
			{
				s += '\x01';
				char tmp145 = __v19[tmp143];
				auto tmp146 = reinterpret_cast<char*>(&tmp145);
				s += std::string(tmp146, sizeof(char));
			}
		}
		
		// serialize v20
		s += __has_v20;
		if (__has_v20)
		{
			for (unsigned int tmp147 = 0; tmp147 < 10; tmp147++)
			{
				for (unsigned int tmp148 = 0; tmp148 < 20; tmp148++)
				{
					s += '\x01';
					std::string tmp149 = "";
					unsigned int tmp151 = __v20[tmp147][tmp148].size();
					auto tmp152 = reinterpret_cast<char*>(&tmp151);
					tmp149 += std::string(tmp152, sizeof(unsigned int));
					while (tmp149.size() && tmp149.back() == 0)
						tmp149.pop_back();
					unsigned char tmp154 = tmp149.size();
					auto tmp155 = reinterpret_cast<char*>(&tmp154);
					s += std::string(tmp155, sizeof(unsigned char));
					s += tmp149;
					
					for (auto &tmp156 : __v20[tmp147][tmp148])
					{
						s += '\x01';
						std::string tmp157 = "";
						unsigned int tmp159 = tmp156.size();
						auto tmp160 = reinterpret_cast<char*>(&tmp159);
						tmp157 += std::string(tmp160, sizeof(unsigned int));
						while (tmp157.size() && tmp157.back() == 0)
							tmp157.pop_back();
						unsigned char tmp162 = tmp157.size();
						auto tmp163 = reinterpret_cast<char*>(&tmp162);
						s += std::string(tmp163, sizeof(unsigned char));
						s += tmp157;
						
						s += tmp156;
					}
				}
			}
		}
		
		// serialize v21
		s += __has_v21;
		if (__has_v21)
		{
			std::string tmp164 = "";
			unsigned int tmp166 = __v21.size();
			auto tmp167 = reinterpret_cast<char*>(&tmp166);
			tmp164 += std::string(tmp167, sizeof(unsigned int));
			while (tmp164.size() && tmp164.back() == 0)
				tmp164.pop_back();
			unsigned char tmp169 = tmp164.size();
			auto tmp170 = reinterpret_cast<char*>(&tmp169);
			s += std::string(tmp170, sizeof(unsigned char));
			s += tmp164;
			
			for (auto &tmp171 : __v21)
			{
				s += '\x01';
				s += tmp171.serialize();
			}
		}
		
		// serialize v22
		s += __has_v22;
		if (__has_v22)
		{
			std::string tmp172 = "";
			unsigned int tmp174 = __v22.size();
			auto tmp175 = reinterpret_cast<char*>(&tmp174);
			tmp172 += std::string(tmp175, sizeof(unsigned int));
			while (tmp172.size() && tmp172.back() == 0)
				tmp172.pop_back();
			unsigned char tmp177 = tmp172.size();
			auto tmp178 = reinterpret_cast<char*>(&tmp177);
			s += std::string(tmp178, sizeof(unsigned char));
			s += tmp172;
			
			for (auto &tmp179 : __v22)
			{
				s += '\x01';
				std::string tmp180 = "";
				unsigned int tmp182 = tmp179.first.size();
				auto tmp183 = reinterpret_cast<char*>(&tmp182);
				tmp180 += std::string(tmp183, sizeof(unsigned int));
				while (tmp180.size() && tmp180.back() == 0)
					tmp180.pop_back();
				unsigned char tmp185 = tmp180.size();
				auto tmp186 = reinterpret_cast<char*>(&tmp185);
				s += std::string(tmp186, sizeof(unsigned char));
				s += tmp180;
				
				s += tmp179.first;
				
				s += '\x01';
				s += tmp179.second.serialize();
			}
		}
		
		// serialize v23
		s += __has_v23;
		if (__has_v23)
		{
			for (unsigned int tmp187 = 0; tmp187 < 5; tmp187++)
			{
				for (unsigned int tmp188 = 0; tmp188 < 10; tmp188++)
				{
					s += '\x01';
					s += __v23[tmp187][tmp188].serialize();
				}
			}
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize v0
		__has_v0 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v0)
		{
			__v0 = *((bool*) (&s[offset]));
			offset += sizeof(bool);
		}
		
		// deserialize v1
		__has_v1 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v1)
		{
			__v1 = *((char*) (&s[offset]));
			offset += sizeof(char);
		}
		
		// deserialize v2
		__has_v2 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v2)
		{
			__v2 = *((char*) (&s[offset]));
			offset += sizeof(char);
		}
		
		// deserialize v3
		__has_v3 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v3)
		{
			__v3 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
		}
		
		// deserialize v4
		__has_v4 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v4)
		{
			__v4 = *((short*) (&s[offset]));
			offset += sizeof(short);
		}
		
		// deserialize v5
		__has_v5 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v5)
		{
			__v5 = *((unsigned short*) (&s[offset]));
			offset += sizeof(unsigned short);
		}
		
		// deserialize v6
		__has_v6 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v6)
		{
			__v6 = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize v7
		__has_v7 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v7)
		{
			__v7 = *((unsigned int*) (&s[offset]));
			offset += sizeof(unsigned int);
		}
		
		// deserialize v8
		__has_v8 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v8)
		{
			__v8 = *((long long*) (&s[offset]));
			offset += sizeof(long long);
		}
		
		// deserialize v9
		__has_v9 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v9)
		{
			__v9 = *((unsigned long long*) (&s[offset]));
			offset += sizeof(unsigned long long);
		}
		
		// deserialize v10
		__has_v10 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v10)
		{
			__v10 = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize v11
		__has_v11 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v11)
		{
			__v11 = *((double*) (&s[offset]));
			offset += sizeof(double);
		}
		
		// deserialize v12
		__has_v12 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v12)
		{
			unsigned char tmp189;
			tmp189 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp190 = std::string(&s[offset], tmp189);
			offset += tmp189;
			while (tmp190.size() < sizeof(unsigned int))
				tmp190 += '\x00';
			unsigned int tmp191;
			tmp191 = *((unsigned int*) (&tmp190[0]));
			
			__v12 = s.substr(offset, tmp191);
			offset += tmp191;
		}
		
		// deserialize v13
		__has_v13 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v13)
		{
			char tmp192;
			tmp192 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__v13 = (EColor) tmp192;
		}
		
		// deserialize v14
		__has_v14 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v14)
		{
			offset = __v14.deserialize(s, offset);
		}
		
		// deserialize v15
		__has_v15 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v15)
		{
			unsigned char tmp193;
			tmp193 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp194 = std::string(&s[offset], tmp193);
			offset += tmp193;
			while (tmp194.size() < sizeof(unsigned int))
				tmp194 += '\x00';
			unsigned int tmp195;
			tmp195 = *((unsigned int*) (&tmp194[0]));
			
			__v15.clear();
			for (unsigned int tmp196 = 0; tmp196 < tmp195; tmp196++)
			{
				int tmp197;
				offset++;
				tmp197 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__v15.push_back(tmp197);
			}
		}
		
		// deserialize v16
		__has_v16 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v16)
		{
			unsigned char tmp198;
			tmp198 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp199 = std::string(&s[offset], tmp198);
			offset += tmp198;
			while (tmp199.size() < sizeof(unsigned int))
				tmp199 += '\x00';
			unsigned int tmp200;
			tmp200 = *((unsigned int*) (&tmp199[0]));
			
			__v16.clear();
			for (unsigned int tmp201 = 0; tmp201 < tmp200; tmp201++)
			{
				std::vector<char> tmp202;
				offset++;
				unsigned char tmp203;
				tmp203 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp204 = std::string(&s[offset], tmp203);
				offset += tmp203;
				while (tmp204.size() < sizeof(unsigned int))
					tmp204 += '\x00';
				unsigned int tmp205;
				tmp205 = *((unsigned int*) (&tmp204[0]));
				
				tmp202.clear();
				for (unsigned int tmp206 = 0; tmp206 < tmp205; tmp206++)
				{
					char tmp207;
					offset++;
					tmp207 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp202.push_back(tmp207);
				}
				__v16.push_back(tmp202);
			}
		}
		
		// deserialize v17
		__has_v17 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v17)
		{
			unsigned char tmp208;
			tmp208 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp209 = std::string(&s[offset], tmp208);
			offset += tmp208;
			while (tmp209.size() < sizeof(unsigned int))
				tmp209 += '\x00';
			unsigned int tmp210;
			tmp210 = *((unsigned int*) (&tmp209[0]));
			
			__v17.clear();
			for (unsigned int tmp211 = 0; tmp211 < tmp210; tmp211++)
			{
				std::string tmp212;
				offset++;
				unsigned char tmp214;
				tmp214 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp215 = std::string(&s[offset], tmp214);
				offset += tmp214;
				while (tmp215.size() < sizeof(unsigned int))
					tmp215 += '\x00';
				unsigned int tmp216;
				tmp216 = *((unsigned int*) (&tmp215[0]));
				
				tmp212 = s.substr(offset, tmp216);
				offset += tmp216;
				
				int tmp213;
				offset++;
				tmp213 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__v17[tmp212] = tmp213;
			}
		}
		
		// deserialize v18
		__has_v18 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v18)
		{
			unsigned char tmp217;
			tmp217 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp218 = std::string(&s[offset], tmp217);
			offset += tmp217;
			while (tmp218.size() < sizeof(unsigned int))
				tmp218 += '\x00';
			unsigned int tmp219;
			tmp219 = *((unsigned int*) (&tmp218[0]));
			
			__v18.clear();
			for (unsigned int tmp220 = 0; tmp220 < tmp219; tmp220++)
			{
				char tmp221;
				offset++;
				tmp221 = *((char*) (&s[offset]));
				offset += sizeof(char);
				
				std::vector<std::map<double, EColor>> tmp222;
				offset++;
				unsigned char tmp223;
				tmp223 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp224 = std::string(&s[offset], tmp223);
				offset += tmp223;
				while (tmp224.size() < sizeof(unsigned int))
					tmp224 += '\x00';
				unsigned int tmp225;
				tmp225 = *((unsigned int*) (&tmp224[0]));
				
				tmp222.clear();
				for (unsigned int tmp226 = 0; tmp226 < tmp225; tmp226++)
				{
					std::map<double, EColor> tmp227;
					offset++;
					unsigned char tmp228;
					tmp228 = *((unsigned char*) (&s[offset]));
					offset += sizeof(unsigned char);
					std::string tmp229 = std::string(&s[offset], tmp228);
					offset += tmp228;
					while (tmp229.size() < sizeof(unsigned int))
						tmp229 += '\x00';
					unsigned int tmp230;
					tmp230 = *((unsigned int*) (&tmp229[0]));
					
					tmp227.clear();
					for (unsigned int tmp231 = 0; tmp231 < tmp230; tmp231++)
					{
						double tmp232;
						offset++;
						tmp232 = *((double*) (&s[offset]));
						offset += sizeof(double);
						
						EColor tmp233;
						offset++;
						char tmp234;
						tmp234 = *((char*) (&s[offset]));
						offset += sizeof(char);
						tmp233 = (EColor) tmp234;
						
						tmp227[tmp232] = tmp233;
					}
					tmp222.push_back(tmp227);
				}
				
				__v18[tmp221] = tmp222;
			}
		}
		
		// deserialize v19
		__has_v19 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v19)
		{
			for (unsigned int tmp235 = 0; tmp235 < 10; tmp235++)
			{
				offset++;
				__v19[tmp235] = *((char*) (&s[offset]));
				offset += sizeof(char);
			}
		}
		
		// deserialize v20
		__has_v20 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v20)
		{
			for (unsigned int tmp236 = 0; tmp236 < 10; tmp236++)
			{
				for (unsigned int tmp237 = 0; tmp237 < 20; tmp237++)
				{
					offset++;
					unsigned char tmp238;
					tmp238 = *((unsigned char*) (&s[offset]));
					offset += sizeof(unsigned char);
					std::string tmp239 = std::string(&s[offset], tmp238);
					offset += tmp238;
					while (tmp239.size() < sizeof(unsigned int))
						tmp239 += '\x00';
					unsigned int tmp240;
					tmp240 = *((unsigned int*) (&tmp239[0]));
					
					__v20[tmp236][tmp237].clear();
					for (unsigned int tmp241 = 0; tmp241 < tmp240; tmp241++)
					{
						std::string tmp242;
						offset++;
						unsigned char tmp243;
						tmp243 = *((unsigned char*) (&s[offset]));
						offset += sizeof(unsigned char);
						std::string tmp244 = std::string(&s[offset], tmp243);
						offset += tmp243;
						while (tmp244.size() < sizeof(unsigned int))
							tmp244 += '\x00';
						unsigned int tmp245;
						tmp245 = *((unsigned int*) (&tmp244[0]));
						
						tmp242 = s.substr(offset, tmp245);
						offset += tmp245;
						__v20[tmp236][tmp237].push_back(tmp242);
					}
				}
			}
		}
		
		// deserialize v21
		__has_v21 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v21)
		{
			unsigned char tmp246;
			tmp246 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp247 = std::string(&s[offset], tmp246);
			offset += tmp246;
			while (tmp247.size() < sizeof(unsigned int))
				tmp247 += '\x00';
			unsigned int tmp248;
			tmp248 = *((unsigned int*) (&tmp247[0]));
			
			__v21.clear();
			for (unsigned int tmp249 = 0; tmp249 < tmp248; tmp249++)
			{
				Child tmp250;
				offset++;
				offset = tmp250.deserialize(s, offset);
				__v21.push_back(tmp250);
			}
		}
		
		// deserialize v22
		__has_v22 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v22)
		{
			unsigned char tmp251;
			tmp251 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp252 = std::string(&s[offset], tmp251);
			offset += tmp251;
			while (tmp252.size() < sizeof(unsigned int))
				tmp252 += '\x00';
			unsigned int tmp253;
			tmp253 = *((unsigned int*) (&tmp252[0]));
			
			__v22.clear();
			for (unsigned int tmp254 = 0; tmp254 < tmp253; tmp254++)
			{
				std::string tmp255;
				offset++;
				unsigned char tmp257;
				tmp257 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp258 = std::string(&s[offset], tmp257);
				offset += tmp257;
				while (tmp258.size() < sizeof(unsigned int))
					tmp258 += '\x00';
				unsigned int tmp259;
				tmp259 = *((unsigned int*) (&tmp258[0]));
				
				tmp255 = s.substr(offset, tmp259);
				offset += tmp259;
				
				Child tmp256;
				offset++;
				offset = tmp256.deserialize(s, offset);
				
				__v22[tmp255] = tmp256;
			}
		}
		
		// deserialize v23
		__has_v23 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v23)
		{
			for (unsigned int tmp260 = 0; tmp260 < 5; tmp260++)
			{
				for (unsigned int tmp261 = 0; tmp261 < 10; tmp261++)
				{
					offset++;
					offset = __v23[tmp260][tmp261].deserialize(s, offset);
				}
			}
		}
		
		return offset;
	}
};

} // namespace full

} // namespace ks

#endif // _KS_FULL_H_
