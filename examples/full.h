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

	std::string __firstName;
	std::string ___lastName_;

	bool __has_firstName;
	bool __has__lastName_;


public: // getters

	inline std::string firstName() const
	{
		return __firstName;
	}
	
	inline std::string _lastName_() const
	{
		return ___lastName_;
	}
	

public: // reference getters

	inline std::string &ref_firstName() const
	{
		return (std::string&) __firstName;
	}
	
	inline std::string &ref__lastName_() const
	{
		return (std::string&) ___lastName_;
	}
	

public: // setters

	inline void firstName(const std::string &firstName)
	{
		__firstName = firstName;
		has_firstName(true);
	}
	
	inline void _lastName_(const std::string &_lastName_)
	{
		___lastName_ = _lastName_;
		has__lastName_(true);
	}
	

public: // has_attribute getters

	inline bool has_firstName() const
	{
		return __has_firstName;
	}
	
	inline bool has__lastName_() const
	{
		return __has__lastName_;
	}
	

public: // has_attribute setters

	inline void has_firstName(const bool &has_firstName)
	{
		__has_firstName = has_firstName;
	}
	
	inline void has__lastName_(const bool &has__lastName_)
	{
		__has__lastName_ = has__lastName_;
	}
	

public:

	Parent()
	{
		has_firstName(false);
		has__lastName_(false);
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
		
		// serialize firstName
		s += __has_firstName;
		if (__has_firstName)
		{
			std::string tmp0 = "";
			unsigned int tmp2 = __firstName.size();
			auto tmp3 = reinterpret_cast<char*>(&tmp2);
			tmp0 += std::string(tmp3, sizeof(unsigned int));
			while (tmp0.size() && tmp0.back() == 0)
				tmp0.pop_back();
			unsigned char tmp5 = tmp0.size();
			auto tmp6 = reinterpret_cast<char*>(&tmp5);
			s += std::string(tmp6, sizeof(unsigned char));
			s += tmp0;
			
			s += __firstName;
		}
		
		// serialize _lastName_
		s += __has__lastName_;
		if (__has__lastName_)
		{
			std::string tmp7 = "";
			unsigned int tmp9 = ___lastName_.size();
			auto tmp10 = reinterpret_cast<char*>(&tmp9);
			tmp7 += std::string(tmp10, sizeof(unsigned int));
			while (tmp7.size() && tmp7.back() == 0)
				tmp7.pop_back();
			unsigned char tmp12 = tmp7.size();
			auto tmp13 = reinterpret_cast<char*>(&tmp12);
			s += std::string(tmp13, sizeof(unsigned char));
			s += tmp7;
			
			s += ___lastName_;
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize firstName
		__has_firstName = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_firstName)
		{
			unsigned char tmp14;
			tmp14 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp15 = std::string(&s[offset], tmp14);
			offset += tmp14;
			while (tmp15.size() < sizeof(unsigned int))
				tmp15 += '\x00';
			unsigned int tmp16;
			tmp16 = *((unsigned int*) (&tmp15[0]));
			
			__firstName = s.substr(offset, tmp16);
			offset += tmp16;
		}
		
		// deserialize _lastName_
		__has__lastName_ = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has__lastName_)
		{
			unsigned char tmp17;
			tmp17 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp18 = std::string(&s[offset], tmp17);
			offset += tmp17;
			while (tmp18.size() < sizeof(unsigned int))
				tmp18 += '\x00';
			unsigned int tmp19;
			tmp19 = *((unsigned int*) (&tmp18[0]));
			
			___lastName_ = s.substr(offset, tmp19);
			offset += tmp19;
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
			std::string tmp20 = "";
			unsigned int tmp22 = __c.size();
			auto tmp23 = reinterpret_cast<char*>(&tmp22);
			tmp20 += std::string(tmp23, sizeof(unsigned int));
			while (tmp20.size() && tmp20.back() == 0)
				tmp20.pop_back();
			unsigned char tmp25 = tmp20.size();
			auto tmp26 = reinterpret_cast<char*>(&tmp25);
			s += std::string(tmp26, sizeof(unsigned char));
			s += tmp20;
			
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
			unsigned char tmp27;
			tmp27 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp28 = std::string(&s[offset], tmp27);
			offset += tmp27;
			while (tmp28.size() < sizeof(unsigned int))
				tmp28 += '\x00';
			unsigned int tmp29;
			tmp29 = *((unsigned int*) (&tmp28[0]));
			
			__c = s.substr(offset, tmp29);
			offset += tmp29;
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
			bool tmp31 = __v0;
			auto tmp32 = reinterpret_cast<char*>(&tmp31);
			s += std::string(tmp32, sizeof(bool));
		}
		
		// serialize v1
		s += __has_v1;
		if (__has_v1)
		{
			char tmp34 = __v1;
			auto tmp35 = reinterpret_cast<char*>(&tmp34);
			s += std::string(tmp35, sizeof(char));
		}
		
		// serialize v2
		s += __has_v2;
		if (__has_v2)
		{
			char tmp37 = __v2;
			auto tmp38 = reinterpret_cast<char*>(&tmp37);
			s += std::string(tmp38, sizeof(char));
		}
		
		// serialize v3
		s += __has_v3;
		if (__has_v3)
		{
			unsigned char tmp40 = __v3;
			auto tmp41 = reinterpret_cast<char*>(&tmp40);
			s += std::string(tmp41, sizeof(unsigned char));
		}
		
		// serialize v4
		s += __has_v4;
		if (__has_v4)
		{
			short tmp43 = __v4;
			auto tmp44 = reinterpret_cast<char*>(&tmp43);
			s += std::string(tmp44, sizeof(short));
		}
		
		// serialize v5
		s += __has_v5;
		if (__has_v5)
		{
			unsigned short tmp46 = __v5;
			auto tmp47 = reinterpret_cast<char*>(&tmp46);
			s += std::string(tmp47, sizeof(unsigned short));
		}
		
		// serialize v6
		s += __has_v6;
		if (__has_v6)
		{
			int tmp49 = __v6;
			auto tmp50 = reinterpret_cast<char*>(&tmp49);
			s += std::string(tmp50, sizeof(int));
		}
		
		// serialize v7
		s += __has_v7;
		if (__has_v7)
		{
			unsigned int tmp52 = __v7;
			auto tmp53 = reinterpret_cast<char*>(&tmp52);
			s += std::string(tmp53, sizeof(unsigned int));
		}
		
		// serialize v8
		s += __has_v8;
		if (__has_v8)
		{
			long long tmp55 = __v8;
			auto tmp56 = reinterpret_cast<char*>(&tmp55);
			s += std::string(tmp56, sizeof(long long));
		}
		
		// serialize v9
		s += __has_v9;
		if (__has_v9)
		{
			unsigned long long tmp58 = __v9;
			auto tmp59 = reinterpret_cast<char*>(&tmp58);
			s += std::string(tmp59, sizeof(unsigned long long));
		}
		
		// serialize v10
		s += __has_v10;
		if (__has_v10)
		{
			float tmp61 = __v10;
			auto tmp62 = reinterpret_cast<char*>(&tmp61);
			s += std::string(tmp62, sizeof(float));
		}
		
		// serialize v11
		s += __has_v11;
		if (__has_v11)
		{
			double tmp64 = __v11;
			auto tmp65 = reinterpret_cast<char*>(&tmp64);
			s += std::string(tmp65, sizeof(double));
		}
		
		// serialize v12
		s += __has_v12;
		if (__has_v12)
		{
			std::string tmp66 = "";
			unsigned int tmp68 = __v12.size();
			auto tmp69 = reinterpret_cast<char*>(&tmp68);
			tmp66 += std::string(tmp69, sizeof(unsigned int));
			while (tmp66.size() && tmp66.back() == 0)
				tmp66.pop_back();
			unsigned char tmp71 = tmp66.size();
			auto tmp72 = reinterpret_cast<char*>(&tmp71);
			s += std::string(tmp72, sizeof(unsigned char));
			s += tmp66;
			
			s += __v12;
		}
		
		// serialize v13
		s += __has_v13;
		if (__has_v13)
		{
			char tmp74 = (char) __v13;
			auto tmp75 = reinterpret_cast<char*>(&tmp74);
			s += std::string(tmp75, sizeof(char));
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
			std::string tmp76 = "";
			unsigned int tmp78 = __v15.size();
			auto tmp79 = reinterpret_cast<char*>(&tmp78);
			tmp76 += std::string(tmp79, sizeof(unsigned int));
			while (tmp76.size() && tmp76.back() == 0)
				tmp76.pop_back();
			unsigned char tmp81 = tmp76.size();
			auto tmp82 = reinterpret_cast<char*>(&tmp81);
			s += std::string(tmp82, sizeof(unsigned char));
			s += tmp76;
			
			for (auto &tmp83 : __v15)
			{
				s += '\x01';
				int tmp85 = tmp83;
				auto tmp86 = reinterpret_cast<char*>(&tmp85);
				s += std::string(tmp86, sizeof(int));
			}
		}
		
		// serialize v16
		s += __has_v16;
		if (__has_v16)
		{
			std::string tmp87 = "";
			unsigned int tmp89 = __v16.size();
			auto tmp90 = reinterpret_cast<char*>(&tmp89);
			tmp87 += std::string(tmp90, sizeof(unsigned int));
			while (tmp87.size() && tmp87.back() == 0)
				tmp87.pop_back();
			unsigned char tmp92 = tmp87.size();
			auto tmp93 = reinterpret_cast<char*>(&tmp92);
			s += std::string(tmp93, sizeof(unsigned char));
			s += tmp87;
			
			for (auto &tmp94 : __v16)
			{
				s += '\x01';
				std::string tmp95 = "";
				unsigned int tmp97 = tmp94.size();
				auto tmp98 = reinterpret_cast<char*>(&tmp97);
				tmp95 += std::string(tmp98, sizeof(unsigned int));
				while (tmp95.size() && tmp95.back() == 0)
					tmp95.pop_back();
				unsigned char tmp100 = tmp95.size();
				auto tmp101 = reinterpret_cast<char*>(&tmp100);
				s += std::string(tmp101, sizeof(unsigned char));
				s += tmp95;
				
				for (auto &tmp102 : tmp94)
				{
					s += '\x01';
					char tmp104 = tmp102;
					auto tmp105 = reinterpret_cast<char*>(&tmp104);
					s += std::string(tmp105, sizeof(char));
				}
			}
		}
		
		// serialize v17
		s += __has_v17;
		if (__has_v17)
		{
			std::string tmp106 = "";
			unsigned int tmp108 = __v17.size();
			auto tmp109 = reinterpret_cast<char*>(&tmp108);
			tmp106 += std::string(tmp109, sizeof(unsigned int));
			while (tmp106.size() && tmp106.back() == 0)
				tmp106.pop_back();
			unsigned char tmp111 = tmp106.size();
			auto tmp112 = reinterpret_cast<char*>(&tmp111);
			s += std::string(tmp112, sizeof(unsigned char));
			s += tmp106;
			
			for (auto &tmp113 : __v17)
			{
				s += '\x01';
				std::string tmp114 = "";
				unsigned int tmp116 = tmp113.first.size();
				auto tmp117 = reinterpret_cast<char*>(&tmp116);
				tmp114 += std::string(tmp117, sizeof(unsigned int));
				while (tmp114.size() && tmp114.back() == 0)
					tmp114.pop_back();
				unsigned char tmp119 = tmp114.size();
				auto tmp120 = reinterpret_cast<char*>(&tmp119);
				s += std::string(tmp120, sizeof(unsigned char));
				s += tmp114;
				
				s += tmp113.first;
				
				s += '\x01';
				int tmp122 = tmp113.second;
				auto tmp123 = reinterpret_cast<char*>(&tmp122);
				s += std::string(tmp123, sizeof(int));
			}
		}
		
		// serialize v18
		s += __has_v18;
		if (__has_v18)
		{
			std::string tmp124 = "";
			unsigned int tmp126 = __v18.size();
			auto tmp127 = reinterpret_cast<char*>(&tmp126);
			tmp124 += std::string(tmp127, sizeof(unsigned int));
			while (tmp124.size() && tmp124.back() == 0)
				tmp124.pop_back();
			unsigned char tmp129 = tmp124.size();
			auto tmp130 = reinterpret_cast<char*>(&tmp129);
			s += std::string(tmp130, sizeof(unsigned char));
			s += tmp124;
			
			for (auto &tmp131 : __v18)
			{
				s += '\x01';
				char tmp133 = tmp131.first;
				auto tmp134 = reinterpret_cast<char*>(&tmp133);
				s += std::string(tmp134, sizeof(char));
				
				s += '\x01';
				std::string tmp135 = "";
				unsigned int tmp137 = tmp131.second.size();
				auto tmp138 = reinterpret_cast<char*>(&tmp137);
				tmp135 += std::string(tmp138, sizeof(unsigned int));
				while (tmp135.size() && tmp135.back() == 0)
					tmp135.pop_back();
				unsigned char tmp140 = tmp135.size();
				auto tmp141 = reinterpret_cast<char*>(&tmp140);
				s += std::string(tmp141, sizeof(unsigned char));
				s += tmp135;
				
				for (auto &tmp142 : tmp131.second)
				{
					s += '\x01';
					std::string tmp143 = "";
					unsigned int tmp145 = tmp142.size();
					auto tmp146 = reinterpret_cast<char*>(&tmp145);
					tmp143 += std::string(tmp146, sizeof(unsigned int));
					while (tmp143.size() && tmp143.back() == 0)
						tmp143.pop_back();
					unsigned char tmp148 = tmp143.size();
					auto tmp149 = reinterpret_cast<char*>(&tmp148);
					s += std::string(tmp149, sizeof(unsigned char));
					s += tmp143;
					
					for (auto &tmp150 : tmp142)
					{
						s += '\x01';
						double tmp152 = tmp150.first;
						auto tmp153 = reinterpret_cast<char*>(&tmp152);
						s += std::string(tmp153, sizeof(double));
						
						s += '\x01';
						char tmp155 = (char) tmp150.second;
						auto tmp156 = reinterpret_cast<char*>(&tmp155);
						s += std::string(tmp156, sizeof(char));
					}
				}
			}
		}
		
		// serialize v19
		s += __has_v19;
		if (__has_v19)
		{
			for (unsigned int tmp157 = 0; tmp157 < 10; tmp157++)
			{
				s += '\x01';
				char tmp159 = __v19[tmp157];
				auto tmp160 = reinterpret_cast<char*>(&tmp159);
				s += std::string(tmp160, sizeof(char));
			}
		}
		
		// serialize v20
		s += __has_v20;
		if (__has_v20)
		{
			for (unsigned int tmp161 = 0; tmp161 < 10; tmp161++)
			{
				for (unsigned int tmp162 = 0; tmp162 < 20; tmp162++)
				{
					s += '\x01';
					std::string tmp163 = "";
					unsigned int tmp165 = __v20[tmp161][tmp162].size();
					auto tmp166 = reinterpret_cast<char*>(&tmp165);
					tmp163 += std::string(tmp166, sizeof(unsigned int));
					while (tmp163.size() && tmp163.back() == 0)
						tmp163.pop_back();
					unsigned char tmp168 = tmp163.size();
					auto tmp169 = reinterpret_cast<char*>(&tmp168);
					s += std::string(tmp169, sizeof(unsigned char));
					s += tmp163;
					
					for (auto &tmp170 : __v20[tmp161][tmp162])
					{
						s += '\x01';
						std::string tmp171 = "";
						unsigned int tmp173 = tmp170.size();
						auto tmp174 = reinterpret_cast<char*>(&tmp173);
						tmp171 += std::string(tmp174, sizeof(unsigned int));
						while (tmp171.size() && tmp171.back() == 0)
							tmp171.pop_back();
						unsigned char tmp176 = tmp171.size();
						auto tmp177 = reinterpret_cast<char*>(&tmp176);
						s += std::string(tmp177, sizeof(unsigned char));
						s += tmp171;
						
						s += tmp170;
					}
				}
			}
		}
		
		// serialize v21
		s += __has_v21;
		if (__has_v21)
		{
			std::string tmp178 = "";
			unsigned int tmp180 = __v21.size();
			auto tmp181 = reinterpret_cast<char*>(&tmp180);
			tmp178 += std::string(tmp181, sizeof(unsigned int));
			while (tmp178.size() && tmp178.back() == 0)
				tmp178.pop_back();
			unsigned char tmp183 = tmp178.size();
			auto tmp184 = reinterpret_cast<char*>(&tmp183);
			s += std::string(tmp184, sizeof(unsigned char));
			s += tmp178;
			
			for (auto &tmp185 : __v21)
			{
				s += '\x01';
				for (unsigned int tmp186 = 0; tmp186 < 4; tmp186++)
				{
					s += '\x01';
					s += tmp185[tmp186].serialize();
				}
			}
		}
		
		// serialize v22
		s += __has_v22;
		if (__has_v22)
		{
			std::string tmp187 = "";
			unsigned int tmp189 = __v22.size();
			auto tmp190 = reinterpret_cast<char*>(&tmp189);
			tmp187 += std::string(tmp190, sizeof(unsigned int));
			while (tmp187.size() && tmp187.back() == 0)
				tmp187.pop_back();
			unsigned char tmp192 = tmp187.size();
			auto tmp193 = reinterpret_cast<char*>(&tmp192);
			s += std::string(tmp193, sizeof(unsigned char));
			s += tmp187;
			
			for (auto &tmp194 : __v22)
			{
				s += '\x01';
				std::string tmp195 = "";
				unsigned int tmp197 = tmp194.first.size();
				auto tmp198 = reinterpret_cast<char*>(&tmp197);
				tmp195 += std::string(tmp198, sizeof(unsigned int));
				while (tmp195.size() && tmp195.back() == 0)
					tmp195.pop_back();
				unsigned char tmp200 = tmp195.size();
				auto tmp201 = reinterpret_cast<char*>(&tmp200);
				s += std::string(tmp201, sizeof(unsigned char));
				s += tmp195;
				
				s += tmp194.first;
				
				s += '\x01';
				s += tmp194.second.serialize();
			}
		}
		
		// serialize v23
		s += __has_v23;
		if (__has_v23)
		{
			for (unsigned int tmp202 = 0; tmp202 < 5; tmp202++)
			{
				for (unsigned int tmp203 = 0; tmp203 < 10; tmp203++)
				{
					s += '\x01';
					s += __v23[tmp202][tmp203].serialize();
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
			unsigned char tmp204;
			tmp204 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp205 = std::string(&s[offset], tmp204);
			offset += tmp204;
			while (tmp205.size() < sizeof(unsigned int))
				tmp205 += '\x00';
			unsigned int tmp206;
			tmp206 = *((unsigned int*) (&tmp205[0]));
			
			__v12 = s.substr(offset, tmp206);
			offset += tmp206;
		}
		
		// deserialize v13
		__has_v13 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v13)
		{
			char tmp207;
			tmp207 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__v13 = (EColor) tmp207;
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
			unsigned char tmp208;
			tmp208 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp209 = std::string(&s[offset], tmp208);
			offset += tmp208;
			while (tmp209.size() < sizeof(unsigned int))
				tmp209 += '\x00';
			unsigned int tmp210;
			tmp210 = *((unsigned int*) (&tmp209[0]));
			
			__v15.clear();
			for (unsigned int tmp211 = 0; tmp211 < tmp210; tmp211++)
			{
				int tmp212;
				offset++;
				tmp212 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__v15.push_back(tmp212);
			}
		}
		
		// deserialize v16
		__has_v16 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v16)
		{
			unsigned char tmp213;
			tmp213 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp214 = std::string(&s[offset], tmp213);
			offset += tmp213;
			while (tmp214.size() < sizeof(unsigned int))
				tmp214 += '\x00';
			unsigned int tmp215;
			tmp215 = *((unsigned int*) (&tmp214[0]));
			
			__v16.clear();
			for (unsigned int tmp216 = 0; tmp216 < tmp215; tmp216++)
			{
				std::vector<char> tmp217;
				offset++;
				unsigned char tmp218;
				tmp218 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp219 = std::string(&s[offset], tmp218);
				offset += tmp218;
				while (tmp219.size() < sizeof(unsigned int))
					tmp219 += '\x00';
				unsigned int tmp220;
				tmp220 = *((unsigned int*) (&tmp219[0]));
				
				tmp217.clear();
				for (unsigned int tmp221 = 0; tmp221 < tmp220; tmp221++)
				{
					char tmp222;
					offset++;
					tmp222 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp217.push_back(tmp222);
				}
				__v16.push_back(tmp217);
			}
		}
		
		// deserialize v17
		__has_v17 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v17)
		{
			unsigned char tmp223;
			tmp223 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp224 = std::string(&s[offset], tmp223);
			offset += tmp223;
			while (tmp224.size() < sizeof(unsigned int))
				tmp224 += '\x00';
			unsigned int tmp225;
			tmp225 = *((unsigned int*) (&tmp224[0]));
			
			__v17.clear();
			for (unsigned int tmp226 = 0; tmp226 < tmp225; tmp226++)
			{
				std::string tmp227;
				offset++;
				unsigned char tmp229;
				tmp229 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp230 = std::string(&s[offset], tmp229);
				offset += tmp229;
				while (tmp230.size() < sizeof(unsigned int))
					tmp230 += '\x00';
				unsigned int tmp231;
				tmp231 = *((unsigned int*) (&tmp230[0]));
				
				tmp227 = s.substr(offset, tmp231);
				offset += tmp231;
				
				int tmp228;
				offset++;
				tmp228 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__v17[tmp227] = tmp228;
			}
		}
		
		// deserialize v18
		__has_v18 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v18)
		{
			unsigned char tmp232;
			tmp232 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp233 = std::string(&s[offset], tmp232);
			offset += tmp232;
			while (tmp233.size() < sizeof(unsigned int))
				tmp233 += '\x00';
			unsigned int tmp234;
			tmp234 = *((unsigned int*) (&tmp233[0]));
			
			__v18.clear();
			for (unsigned int tmp235 = 0; tmp235 < tmp234; tmp235++)
			{
				char tmp236;
				offset++;
				tmp236 = *((char*) (&s[offset]));
				offset += sizeof(char);
				
				std::vector<std::map<double, EColor>> tmp237;
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
				
				tmp237.clear();
				for (unsigned int tmp241 = 0; tmp241 < tmp240; tmp241++)
				{
					std::map<double, EColor> tmp242;
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
					
					tmp242.clear();
					for (unsigned int tmp246 = 0; tmp246 < tmp245; tmp246++)
					{
						double tmp247;
						offset++;
						tmp247 = *((double*) (&s[offset]));
						offset += sizeof(double);
						
						EColor tmp248;
						offset++;
						char tmp249;
						tmp249 = *((char*) (&s[offset]));
						offset += sizeof(char);
						tmp248 = (EColor) tmp249;
						
						tmp242[tmp247] = tmp248;
					}
					tmp237.push_back(tmp242);
				}
				
				__v18[tmp236] = tmp237;
			}
		}
		
		// deserialize v19
		__has_v19 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v19)
		{
			for (unsigned int tmp250 = 0; tmp250 < 10; tmp250++)
			{
				offset++;
				__v19[tmp250] = *((char*) (&s[offset]));
				offset += sizeof(char);
			}
		}
		
		// deserialize v20
		__has_v20 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v20)
		{
			for (unsigned int tmp251 = 0; tmp251 < 10; tmp251++)
			{
				for (unsigned int tmp252 = 0; tmp252 < 20; tmp252++)
				{
					offset++;
					unsigned char tmp253;
					tmp253 = *((unsigned char*) (&s[offset]));
					offset += sizeof(unsigned char);
					std::string tmp254 = std::string(&s[offset], tmp253);
					offset += tmp253;
					while (tmp254.size() < sizeof(unsigned int))
						tmp254 += '\x00';
					unsigned int tmp255;
					tmp255 = *((unsigned int*) (&tmp254[0]));
					
					__v20[tmp251][tmp252].clear();
					for (unsigned int tmp256 = 0; tmp256 < tmp255; tmp256++)
					{
						std::string tmp257;
						offset++;
						unsigned char tmp258;
						tmp258 = *((unsigned char*) (&s[offset]));
						offset += sizeof(unsigned char);
						std::string tmp259 = std::string(&s[offset], tmp258);
						offset += tmp258;
						while (tmp259.size() < sizeof(unsigned int))
							tmp259 += '\x00';
						unsigned int tmp260;
						tmp260 = *((unsigned int*) (&tmp259[0]));
						
						tmp257 = s.substr(offset, tmp260);
						offset += tmp260;
						__v20[tmp251][tmp252].push_back(tmp257);
					}
				}
			}
		}
		
		// deserialize v21
		__has_v21 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v21)
		{
			unsigned char tmp261;
			tmp261 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp262 = std::string(&s[offset], tmp261);
			offset += tmp261;
			while (tmp262.size() < sizeof(unsigned int))
				tmp262 += '\x00';
			unsigned int tmp263;
			tmp263 = *((unsigned int*) (&tmp262[0]));
			
			__v21.clear();
			for (unsigned int tmp264 = 0; tmp264 < tmp263; tmp264++)
			{
				std::array<Child, 4> tmp265;
				offset++;
				for (unsigned int tmp266 = 0; tmp266 < 4; tmp266++)
				{
					offset++;
					offset = tmp265[tmp266].deserialize(s, offset);
				}
				__v21.push_back(tmp265);
			}
		}
		
		// deserialize v22
		__has_v22 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v22)
		{
			unsigned char tmp267;
			tmp267 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp268 = std::string(&s[offset], tmp267);
			offset += tmp267;
			while (tmp268.size() < sizeof(unsigned int))
				tmp268 += '\x00';
			unsigned int tmp269;
			tmp269 = *((unsigned int*) (&tmp268[0]));
			
			__v22.clear();
			for (unsigned int tmp270 = 0; tmp270 < tmp269; tmp270++)
			{
				std::string tmp271;
				offset++;
				unsigned char tmp273;
				tmp273 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp274 = std::string(&s[offset], tmp273);
				offset += tmp273;
				while (tmp274.size() < sizeof(unsigned int))
					tmp274 += '\x00';
				unsigned int tmp275;
				tmp275 = *((unsigned int*) (&tmp274[0]));
				
				tmp271 = s.substr(offset, tmp275);
				offset += tmp275;
				
				Child tmp272;
				offset++;
				offset = tmp272.deserialize(s, offset);
				
				__v22[tmp271] = tmp272;
			}
		}
		
		// deserialize v23
		__has_v23 = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_v23)
		{
			for (unsigned int tmp276 = 0; tmp276 < 5; tmp276++)
			{
				for (unsigned int tmp277 = 0; tmp277 < 10; tmp277++)
				{
					offset++;
					offset = __v23[tmp276][tmp277].deserialize(s, offset);
				}
			}
		}
		
		return offset;
	}
};

} // namespace full

} // namespace ks

#endif // _KS_FULL_H_
