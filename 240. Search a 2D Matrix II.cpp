using namespace std;
#include <vector>
#include <iostream>

class Solution {
public:
	bool searchMatrix(vector<vector<int>>& matrix, int target) {
		int m = matrix.size();
		int n = matrix[0].size();

		int row = m - 1;
		int line = 0;
		int num = matrix[row][line];

		while (line < n && row >= 0) {
			if (num == target) return true;
			if (num < target) {
				if (line == n - 1) break;
				line++;
				num = matrix[row][line];
				continue;
			}
			if (num > target) {
				if (row == 0) break;
				row--;
				num = matrix[row][line];
				continue;
			}
		}

		return false;
	}
};

int main()
{
	vector<vector<int>> matrix =
	{
		{1,   4,  7, 11, 15},
		{2,   5,  8, 12, 19},
		{3,   7,  9, 16, 22},
		{10, 13, 14, 17, 24},
		{18, 21, 23, 26, 30},
	};

	Solution s;
	bool result = s.searchMatrix(matrix, -2);
	return 0;
}