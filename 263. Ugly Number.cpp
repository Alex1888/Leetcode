// 263. Ugly Number.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>


class Solution {
public:
	bool isUgly(int num) {
		int t = num;
		while (t % 5 == 0)
		{
			t /= 5;
		}

		while (t % 3 == 0)
		{
			t /= 3;
		}

		while (t % 2 == 0)
		{
			t /= 2;
		}

		return t == 1;
	}
};


int main()
{
	Solution s;
	std::cout << s.isUgly(8) << '\n';
	std::cout << s.isUgly(9) << '\n';
	std::cout << s.isUgly(14) << '\n';
	std::cout << s.isUgly(16) << '\n';
	std::cout << s.isUgly(26) << '\n';
    return 0;
}

