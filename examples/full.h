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


class Parent : public KSObject
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

	Parent()
	{
		has_p1(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Parent";
	}
	
	virtual inline const std::string name() const
	{
		return "Parent";
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


class Child : public Parent
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
		s += Parent::serialize();
		
		// serialize c
		s += __has_c;
		if (__has_c)
		{
			std::string tmp3 = "";
			unsigned int tmp5 = __c.size();
			auto tmp6 = reinterpret_cast<char*>(&tmp5);
			tmp3 += std::string(tmp6, sizeof(unsigned int));
			while (tmp3.size() && tmp3.back() == 0)
				tmp3.pop_back();
			unsigned char tmp8 = tmp3.size();
			auto tmp9 = reinterpret_cast<char*>(&tmp8);
			s += std::string(tmp9, sizeof(unsigned char));
			s += tmp3;
			
			s += __c;
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Parent::deserialize(s, offset);
		
		// deserialize c
		__has_c = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_c)
		{
			unsigned char tmp10;
			tmp10 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp11 = std::string(&s[offset], tmp10);
			offset += tmp10;
			while (tmp11.size() < sizeof(unsigned int))
				tmp11 += '\x00';
			unsigned int tmp12;
			tmp12 = *((unsigned int*) (&tmp11[0]));
			
			__c = s.substr(offset, tmp12);
			offset += tmp12;
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
	std::vector<std::array<Child, 4>> __v21;
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
	
	inline std::vector<std::array<Child, 4>> v21() const
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
	
	inline std::vector<std::array<Child, 4>> &ref_v21() const
	{
		return (std::vector<std::array<Child, 4>>&) __v21;
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
	
	inline void v21(const std::vector<std::array<Child, 4>> &v21)
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
			bool tmp14 = __v0;
			auto tmp15 = reinterpret_cast<char*>(&tmp14);
			s += std::string(tmp15, sizeof(bool));
		}
		
		// serialize v1
		s += __has_v1;
		if (__has_v1)
		{
			char tmp17 = __v1;
			auto tmp18 = reinterpret_cast<char*>(&tmp17);
			s += std::string(tmp18, sizeof(char));
		}
		
		// serialize v2
		s += __has_v2;
		if (__has_v2)
		{
			char tmp20 = __v2;
			auto tmp21 = reinterpret_cast<char*>(&tmp20);
			s += std::string(tmp21, sizeof(char));
		}
		
		// serialize v3
		s += __has_v3;
		if (__has_v3)
		{
			unsigned char tmp23 = __v3;
			auto tmp24 = reinterpret_cast<char*>(&tmp23);
			s += std::string(tmp24, sizeof(unsigned char));
		}
		
		// serialize v4
		s += __has_v4;
		if (__has_v4)
		{
			short tmp26 = __v4;
			auto tmp27 = reinterpret_cast<char*>(&tmp26);
			s += std::string(tmp27, sizeof(short));
		}
		
		// serialize v5
		s += __has_v5;
		if (__has_v5)
		{
			unsigned short tmp29 = __v5;
			auto tmp30 = reinterpret_cast<char*>(&tmp29);
			s += std::string(tmp30, sizeof(unsigned short));
		}
		
		// serialize v6
		s += __has_v6;
		if (__has_v6)
		{
			int tmp32 = __v6;
			auto tmp33 = reinterpret_cast<char*>(&tmp32);
			s += std::string(tmp33, sizeof(int));
		}
		
		// serialize v7
		s += __has_v7;
		if (__has_v7)
		{
			unsigned int tmp35 = __v7;
			auto tmp36 = reinterpret_cast<char*>(&tmp35);
			s += std::string(tmp36, sizeof(unsigned int));
		}
		
		// serialize v8
		s += __has_v8;
		if (__has_v8)
		{
			long long tmp38 = __v8;
			auto tmp39 = reinterpret_cast<char*>(&tmp38);
			s += std::string(tmp39, sizeof(long long));
		}
		
		// serialize v9
		s += __has_v9;
		if (__has_v9)
		{
			unsigned long long tmp41 = __v9;
			auto tmp42 = reinterpret_cast<char*>(&tmp41);
			s += std::string(tmp42, sizeof(unsigned long long));
		}
		
		// serialize v10
		s += __has_v10;
		if (__has_v10)
		{
			float tmp44 = __v10;
			auto tmp45 = reinterpret_cast<char*>(&tmp44);
			s += std::string(tmp45, sizeof(float));
		}
		
		// serialize v11
		s += __has_v11;
		if (__has_v11)
		{
			double tmp47 = __v11;
			auto tmp48 = reinterpret_cast<char*>(&tmp47);
			s += std::string(tmp48, sizeof(double));
		}
		
		// serialize v12
		s += __has_v12;
		if (__has_v12)
		{
			std::string tmp49 = "";
			unsigned int tmp51 = __v12.size();
			auto tmp52 = reinterpret_cast<char*>(&tmp51);
			tmp49 += std::string(tmp52, sizeof(unsigned int));
			while (tmp49.size() && tmp49.back() == 0)
				tmp49.pop_back();
			unsigned char tmp54 = tmp49.size();
			auto tmp55 = reinterpret_cast<char*>(&tmp54);
			s += std::string(tmp55, sizeof(unsigned char));
			s += tmp49;
			
			s += __v12;
		}
		
		// serialize v13
		s += __has_v13;
		if (__has_v13)
		{
			char tmp57 = (char) __v13;
			auto tmp58 = reinterpret_cast<char*>(&tmp57);
			s += std::string(tmp58, sizeof(char));
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
			std::string tmp59 = "";
			unsigned int tmp61 = __v15.size();
			auto tmp62 = reinterpret_cast<char*>(&tmp61);
			tmp59 += std::string(tmp62, sizeof(unsigned int));
			while (tmp59.size() && tmp59.back() == 0)
				tmp59.pop_back();
			unsigned char tmp64 = tmp59.size();
			auto tmp65 = reinterpret_cast<char*>(&tmp64);
			s += std::string(tmp65, sizeof(unsigned char));
			s += tmp59;
			
			for (auto &tmp66 : __v15)
			{
				s += '\x01';
				int tmp68 = tmp66;
				auto tmp69 = reinterpret_cast<char*>(&tmp68);
				s += std::string(tmp69, sizeof(int));
			}
		}
		
		// serialize v16
		s += __has_v16;
		if (__has_v16)
		{
			std::string tmp70 = "";
			unsigned int tmp72 = __v16.size();
			auto tmp73 = reinterpret_cast<char*>(&tmp72);
			tmp70 += std::string(tmp73, sizeof(unsigned int));
			while (tmp70.size() && tmp70.back() == 0)
				tmp70.pop_back();
			unsigned char tmp75 = tmp70.size();
			auto tmp76 = reinterpret_cast<char*>(&tmp75);
			s += std::string(tmp76, sizeof(unsigned char));
			s += tmp70;
			
			for (auto &tmp77 : __v16)
			{
				s += '\x01';
				std::string tmp78 = "";
				unsigned int tmp80 = tmp77.size();
				auto tmp81 = reinterpret_cast<char*>(&tmp80);
				tmp78 += std::string(tmp81, sizeof(unsigned int));
				while (tmp78.size() && tmp78.back() == 0)
					tmp78.pop_back();
				unsigned char tmp83 = tmp78.size();
				auto tmp84 = reinterpret_cast<char*>(&tmp83);
				s += std::string(tmp84, sizeof(unsigned char));
				s += tmp78;
				
				for (auto &tmp85 : tmp77)
				{
					s += '\x01';
					char tmp87 = tmp85;
					auto tmp88 = reinterpret_cast<char*>(&tmp87);
					s += std::string(tmp88, sizeof(char));
				}
			}
		}
		
		// serialize v17
		s += __has_v17;
		if (__has_v17)
		{
			std::string tmp89 = "";
			unsigned int tmp91 = __v17.size();
			auto tmp92 = reinterpret_cast<char*>(&tmp91);
			tmp89 += std::string(tmp92, sizeof(unsigned int));
			while (tmp89.size() && tmp89.back() == 0)
				tmp89.pop_back();
			unsigned char tmp94 = tmp89.size();
			auto tmp95 = reinterpret_cast<char*>(&tmp94);
			s += std::string(tmp95, sizeof(unsigned char));
			s += tmp89;
			
			for (auto &tmp96 : __v17)
			{
				s += '\x01';
				std::string tmp97 = "";
				unsigned int tmp99 = tmp96.first.size();
				auto tmp100 = reinterpret_cast<char*>(&tmp99);
				tmp97 += std::string(tmp100, sizeof(unsigned int));
				while (tmp97.size() && tmp97.back() == 0)
					tmp97.pop_back();
				unsigned char tmp102 = tmp97.size();
				auto tmp103 = reinterpret_cast<char*>(&tmp102);
				s += std::string(tmp103, sizeof(unsigned char));
				s += tmp97;
				
				s += tmp96.first;
				
				s += '\x01';
				int tmp105 = tmp96.second;
				auto tmp106 = reinterpret_cast<char*>(&tmp105);
				s += std::string(tmp106, sizeof(int));
			}
		}
		
		// serialize v18
		s += __has_v18;
		if (__has_v18)
		{
			std::string tmp107 = "";
			unsigned int tmp109 = __v18.size();
			auto tmp110 = reinterpret_cast<char*>(&tmp109);
			tmp107 += std::string(tmp110, sizeof(unsigned int));
			while (tmp107.size() && tmp107.back() == 0)
				tmp107.pop_back();
			unsigned char tmp112 = tmp107.size();
			auto tmp113 = reinterpret_cast<char*>(&tmp112);
			s += std::string(tmp113, sizeof(unsigned char));
			s += tmp107;
			
			for (auto &tmp114 : __v18)
			{
				s += '\x01';
				char tmp116 = tmp114.first;
				auto tmp117 = reinterpret_cast<char*>(&tmp116);
				s += std::string(tmp117, sizeof(char));
				
				s += '\x01';
				std::string tmp118 = "";
				unsigned int tmp120 = tmp114.second.size();
				auto tmp121 = reinterpret_cast<char*>(&tmp120);
				tmp118 += std::string(tmp121, sizeof(unsigned int));
				while (tmp118.size() && tmp118.back() == 0)
					tmp118.pop_back();
				unsigned char tmp123 = tmp118.size();
				auto tmp124 = reinterpret_cast<char*>(&tmp123);
				s += std::string(tmp124, sizeof(unsigned char));
				s += tmp118;
				
				for (auto &tmp125 : tmp114.second)
				{
					s += '\x01';
					std::string tmp126 = "";
					unsigned int tmp128 = tmp125.size();
					auto tmp129 = reinterpret_cast<char*>(&tmp128);
					tmp126 += std::string(tmp129, sizeof(unsigned int));
					while (tmp126.size() && tmp126.back() == 0)
						tmp126.pop_back();
					unsigned char tmp131 = tmp126.size();
					auto tmp132 = reinterpret_cast<char*>(&tmp131);
					s += std::string(tmp132, sizeof(unsigned char));
					s += tmp126;
					
					for (auto &tmp133 : tmp125)
					{
						s += '\x01';
						double tmp135 = tmp133.first;
						auto tmp136 = reinterpret_cast<char*>(&tmp135);
						s += std::string(tmp136, sizeof(double));
						
						s += '\x01';
						char tmp138 = (char) tmp133.second;
						auto tmp139 = reinterpret_cast<char*>(&tmp138);
						s += std::string(tmp139, sizeof(char));
					}
				}
			}
		}
		
		// serialize v19
		s += __has_v19;
		if (__has_v19)
		{
			for (unsigned int tmp140 = 0; tmp140 < 10; tmp140++)
			{
				s += '\x01';
				char tmp142 = __v19[tmp140];
				auto tmp143 = reinterpret_cast<char*>(&tmp142);
				s += std::string(tmp143, sizeof(char));
			}
		}
		
		// serialize v20
		s += __has_v20;
		if (__has_v20)
		{
			for (unsigned int tmp144 = 0; tmp144 < 10; tmp144++)
			{
				for (unsigned int tmp145 = 0; tmp145 < 20; tmp145++)
				{
					s += '\x01';
					std::string tmp146 = "";
					unsigned int tmp148 = __v20[tmp144][tmp145].size();
					auto tmp149 = reinterpret_cast<char*>(&tmp148);
					tmp146 += std::string(tmp149, sizeof(unsigned int));
					while (tmp146.size() && tmp146.back() == 0)
						tmp146.pop_back();
					unsigned char tmp151 = tmp146.size();
					auto tmp152 = reinterpret_cast<char*>(&tmp151);
					s += std::string(tmp152, sizeof(unsigned char));
					s += tmp146;
					
					for (auto &tmp153 : __v20[tmp144][tmp145])
					{
						s += '\x01';
						std::string tmp154 = "";
						unsigned int tmp156 = tmp153.size();
						auto tmp157 = reinterpret_cast<char*>(&tmp156);
						tmp154 += std::string(tmp157, sizeof(unsigned int));
						while (tmp154.size() && tmp154.back() == 0)
							tmp154.pop_back();
						unsigned char tmp159 = tmp154.size();
						auto tmp160 = reinterpret_cast<char*>(&tmp159);
						s += std::string(tmp160, sizeof(unsigned char));
						s += tmp154;
						
						s += tmp153;
					}
				}
			}
		}
		
		// serialize v21
		s += __has_v21;
		if (__has_v21)
		{
			std::string tmp161 = "";
			unsigned int tmp163 = __v21.size();
			auto tmp164 = reinterpret_cast<char*>(&tmp163);
			tmp161 += std::string(tmp164, sizeof(unsigned int));
			while (tmp161.size() && tmp161.back() == 0)
				tmp161.pop_back();
			unsigned char tmp166 = tmp161.size();
			auto tmp167 = reinterpret_cast<char*>(&tmp166);
			s += std::string(tmp167, sizeof(unsigned char));
			s += tmp161;
			
			for (auto &tmp168 : __v21)
			{
				s += '\x01';
				for (unsigned int tmp169 = 0; tmp169 < 4; tmp169++)
				{
					s += '\x01';
					s += tmp168[tmp169].serialize();
				}
			}
		}
		
		// serialize v22
		s += __has_v22;
		if (__has_v22)
		{
			std::string tmp170 = "";
			unsigned int tmp172 = __v22.size();
			auto tmp173 = reinterpret_cast<char*>(&tmp172);
			tmp170 += std::string(tmp173, sizeof(unsigned int));
			while (tmp170.size() && tmp170.back() == 0)
				tmp170.pop_back();
			unsigned char tmp175 = tmp170.size();
			auto tmp176 = reinterpret_cast<char*>(&tmp175);
			s += std::string(tmp176, sizeof(unsigned char));
			s += tmp170;
			
			for (auto &tmp177 : __v22)
			{
				s += '\x01';
				std::string tmp178 = "";
				unsigned int tmp180 = tmp177.first.size();
				auto tmp181 = reinterpret_cast<char*>(&tmp180);
				tmp178 += std::string(tmp181, sizeof(unsigned int));
				while (tmp178.size() && tmp178.back() == 0)
					tmp178.pop_back();
				unsigned char tmp183 = tmp178.size();
				auto tmp184 = reinterpret_cast<char*>(&tmp183);
				s += std::string(tmp184, sizeof(unsigned char));
				s += tmp178;
				
				s += tmp177.first;
				
				s += '\x01';
				s += tmp177.second.serialize();
			}
		}
		
		// serialize v23
		s += __has_v23;
		if (__has_v23)
		{
			for (unsigned int tmp185 = 0; tmp185 < 5; tmp185++)
			{
				for (unsigned int tmp186 = 0; tmp186 < 10; tmp186++)
				{
					s += '\x01';
					s += __v23[tmp185][tmp186].serialize();
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
			unsigned char tmp187;
			tmp187 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp188 = std::string(&s[offset], tmp187);
			offset += tmp187;
			while (tmp188.size() < sizeof(unsigned int))
				tmp188 += '\x00';
			unsigned int tmp189;
			tmp189 = *((unsigned int*) (&tmp188[0]));
			
			__v12 = s.substr(offset, tmp189);
			offset += tmp189;
		}
		
		// deserialize v13
		__has_v13 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v13)
		{
			char tmp190;
			tmp190 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__v13 = (EColor) tmp190;
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
			unsigned char tmp191;
			tmp191 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp192 = std::string(&s[offset], tmp191);
			offset += tmp191;
			while (tmp192.size() < sizeof(unsigned int))
				tmp192 += '\x00';
			unsigned int tmp193;
			tmp193 = *((unsigned int*) (&tmp192[0]));
			
			__v15.clear();
			for (unsigned int tmp194 = 0; tmp194 < tmp193; tmp194++)
			{
				int tmp195;
				offset++;
				tmp195 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__v15.push_back(tmp195);
			}
		}
		
		// deserialize v16
		__has_v16 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v16)
		{
			unsigned char tmp196;
			tmp196 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp197 = std::string(&s[offset], tmp196);
			offset += tmp196;
			while (tmp197.size() < sizeof(unsigned int))
				tmp197 += '\x00';
			unsigned int tmp198;
			tmp198 = *((unsigned int*) (&tmp197[0]));
			
			__v16.clear();
			for (unsigned int tmp199 = 0; tmp199 < tmp198; tmp199++)
			{
				std::vector<char> tmp200;
				offset++;
				unsigned char tmp201;
				tmp201 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp202 = std::string(&s[offset], tmp201);
				offset += tmp201;
				while (tmp202.size() < sizeof(unsigned int))
					tmp202 += '\x00';
				unsigned int tmp203;
				tmp203 = *((unsigned int*) (&tmp202[0]));
				
				tmp200.clear();
				for (unsigned int tmp204 = 0; tmp204 < tmp203; tmp204++)
				{
					char tmp205;
					offset++;
					tmp205 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp200.push_back(tmp205);
				}
				__v16.push_back(tmp200);
			}
		}
		
		// deserialize v17
		__has_v17 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v17)
		{
			unsigned char tmp206;
			tmp206 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp207 = std::string(&s[offset], tmp206);
			offset += tmp206;
			while (tmp207.size() < sizeof(unsigned int))
				tmp207 += '\x00';
			unsigned int tmp208;
			tmp208 = *((unsigned int*) (&tmp207[0]));
			
			__v17.clear();
			for (unsigned int tmp209 = 0; tmp209 < tmp208; tmp209++)
			{
				std::string tmp210;
				offset++;
				unsigned char tmp212;
				tmp212 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp213 = std::string(&s[offset], tmp212);
				offset += tmp212;
				while (tmp213.size() < sizeof(unsigned int))
					tmp213 += '\x00';
				unsigned int tmp214;
				tmp214 = *((unsigned int*) (&tmp213[0]));
				
				tmp210 = s.substr(offset, tmp214);
				offset += tmp214;
				
				int tmp211;
				offset++;
				tmp211 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__v17[tmp210] = tmp211;
			}
		}
		
		// deserialize v18
		__has_v18 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v18)
		{
			unsigned char tmp215;
			tmp215 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp216 = std::string(&s[offset], tmp215);
			offset += tmp215;
			while (tmp216.size() < sizeof(unsigned int))
				tmp216 += '\x00';
			unsigned int tmp217;
			tmp217 = *((unsigned int*) (&tmp216[0]));
			
			__v18.clear();
			for (unsigned int tmp218 = 0; tmp218 < tmp217; tmp218++)
			{
				char tmp219;
				offset++;
				tmp219 = *((char*) (&s[offset]));
				offset += sizeof(char);
				
				std::vector<std::map<double, EColor>> tmp220;
				offset++;
				unsigned char tmp221;
				tmp221 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp222 = std::string(&s[offset], tmp221);
				offset += tmp221;
				while (tmp222.size() < sizeof(unsigned int))
					tmp222 += '\x00';
				unsigned int tmp223;
				tmp223 = *((unsigned int*) (&tmp222[0]));
				
				tmp220.clear();
				for (unsigned int tmp224 = 0; tmp224 < tmp223; tmp224++)
				{
					std::map<double, EColor> tmp225;
					offset++;
					unsigned char tmp226;
					tmp226 = *((unsigned char*) (&s[offset]));
					offset += sizeof(unsigned char);
					std::string tmp227 = std::string(&s[offset], tmp226);
					offset += tmp226;
					while (tmp227.size() < sizeof(unsigned int))
						tmp227 += '\x00';
					unsigned int tmp228;
					tmp228 = *((unsigned int*) (&tmp227[0]));
					
					tmp225.clear();
					for (unsigned int tmp229 = 0; tmp229 < tmp228; tmp229++)
					{
						double tmp230;
						offset++;
						tmp230 = *((double*) (&s[offset]));
						offset += sizeof(double);
						
						EColor tmp231;
						offset++;
						char tmp232;
						tmp232 = *((char*) (&s[offset]));
						offset += sizeof(char);
						tmp231 = (EColor) tmp232;
						
						tmp225[tmp230] = tmp231;
					}
					tmp220.push_back(tmp225);
				}
				
				__v18[tmp219] = tmp220;
			}
		}
		
		// deserialize v19
		__has_v19 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v19)
		{
			for (unsigned int tmp233 = 0; tmp233 < 10; tmp233++)
			{
				offset++;
				__v19[tmp233] = *((char*) (&s[offset]));
				offset += sizeof(char);
			}
		}
		
		// deserialize v20
		__has_v20 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v20)
		{
			for (unsigned int tmp234 = 0; tmp234 < 10; tmp234++)
			{
				for (unsigned int tmp235 = 0; tmp235 < 20; tmp235++)
				{
					offset++;
					unsigned char tmp236;
					tmp236 = *((unsigned char*) (&s[offset]));
					offset += sizeof(unsigned char);
					std::string tmp237 = std::string(&s[offset], tmp236);
					offset += tmp236;
					while (tmp237.size() < sizeof(unsigned int))
						tmp237 += '\x00';
					unsigned int tmp238;
					tmp238 = *((unsigned int*) (&tmp237[0]));
					
					__v20[tmp234][tmp235].clear();
					for (unsigned int tmp239 = 0; tmp239 < tmp238; tmp239++)
					{
						std::string tmp240;
						offset++;
						unsigned char tmp241;
						tmp241 = *((unsigned char*) (&s[offset]));
						offset += sizeof(unsigned char);
						std::string tmp242 = std::string(&s[offset], tmp241);
						offset += tmp241;
						while (tmp242.size() < sizeof(unsigned int))
							tmp242 += '\x00';
						unsigned int tmp243;
						tmp243 = *((unsigned int*) (&tmp242[0]));
						
						tmp240 = s.substr(offset, tmp243);
						offset += tmp243;
						__v20[tmp234][tmp235].push_back(tmp240);
					}
				}
			}
		}
		
		// deserialize v21
		__has_v21 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v21)
		{
			unsigned char tmp244;
			tmp244 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp245 = std::string(&s[offset], tmp244);
			offset += tmp244;
			while (tmp245.size() < sizeof(unsigned int))
				tmp245 += '\x00';
			unsigned int tmp246;
			tmp246 = *((unsigned int*) (&tmp245[0]));
			
			__v21.clear();
			for (unsigned int tmp247 = 0; tmp247 < tmp246; tmp247++)
			{
				std::array<Child, 4> tmp248;
				offset++;
				for (unsigned int tmp249 = 0; tmp249 < 4; tmp249++)
				{
					offset++;
					offset = tmp248[tmp249].deserialize(s, offset);
				}
				__v21.push_back(tmp248);
			}
		}
		
		// deserialize v22
		__has_v22 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v22)
		{
			unsigned char tmp250;
			tmp250 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp251 = std::string(&s[offset], tmp250);
			offset += tmp250;
			while (tmp251.size() < sizeof(unsigned int))
				tmp251 += '\x00';
			unsigned int tmp252;
			tmp252 = *((unsigned int*) (&tmp251[0]));
			
			__v22.clear();
			for (unsigned int tmp253 = 0; tmp253 < tmp252; tmp253++)
			{
				std::string tmp254;
				offset++;
				unsigned char tmp256;
				tmp256 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp257 = std::string(&s[offset], tmp256);
				offset += tmp256;
				while (tmp257.size() < sizeof(unsigned int))
					tmp257 += '\x00';
				unsigned int tmp258;
				tmp258 = *((unsigned int*) (&tmp257[0]));
				
				tmp254 = s.substr(offset, tmp258);
				offset += tmp258;
				
				Child tmp255;
				offset++;
				offset = tmp255.deserialize(s, offset);
				
				__v22[tmp254] = tmp255;
			}
		}
		
		// deserialize v23
		__has_v23 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v23)
		{
			for (unsigned int tmp259 = 0; tmp259 < 5; tmp259++)
			{
				for (unsigned int tmp260 = 0; tmp260 < 10; tmp260++)
				{
					offset++;
					offset = __v23[tmp259][tmp260].deserialize(s, offset);
				}
			}
		}
		
		return offset;
	}
};

} // namespace full

} // namespace ks

#endif // _KS_FULL_H_
