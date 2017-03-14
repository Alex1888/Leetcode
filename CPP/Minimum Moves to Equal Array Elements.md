# [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/#/solutions)
*  很无聊的一道数学题，但是一下子想不到还真不好做
> 1. 设原来数组所有和为sum, 数组有n个元素，经过了m步之后，所有元素变为x,原来数组最小的数为minx
> 2. 则最开始有：sum + m \* ( n-1) = x \* n
> 3. 而最关键的有： x = minx + m
> 4. 带入，能解出来：m = sum - minx \* n

* 关于最关键一步：x = minx + m，可以这么想：每一次增加操作，minx都必须参加，要不然就不能保证步数最小了(在所有过程中，minx依然是最小的)

```C++
class Solution {
public:
    int minMoves(vector<int>& nums) {
        int sum = 0, minx = INT_MAX;
        for(auto x : nums){
            sum += x;
            minx = min(minx, x);
        }
        
        return sum - minx*nums.size();
    }
};
```


