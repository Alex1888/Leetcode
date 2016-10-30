```
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
#这道题目主要思路是对每一元素i，利用双指针，遍历寻找后面的两个数和等于-i;
#但是，最主要的问题是，它要顺序输出，而且要去重，大部分的时间都是在调试怎么样去重
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            #防止重复，滤过重复的点
            if i > 0 and nums[i] == nums[i -1]:
                continue
            r = 0 - nums[i]
            #从i+1开始寻找2Sum=r,双指针，寻找两数之和等于r
            start, end = i+1,len(nums) -1
            while start < end:
                if nums[start] + nums[end] < r:
                    start += 1
                elif nums[start] + nums[end] == r:
                    re_list = [nums[i], nums[start], nums[end]]
                    result.append(re_list)
                    #一定要有这两句，不能把这两句混到下面的while里去，一旦下面的while不成立，就不能继续循环了
                    start += 1
                    end -= 1
                    #为了防止[0,0,0,0,0]这种情况，或者像[-1,-1,-1,0,0,0,1,1,1,1]这种，当遍历第一个-1时，得到[-1,0,1]后，要把其他的-1和1都滤过；注意这里一定要把start<len(nums)-2放前面，因为有可能start已经越界了，后面的访问会出错；而且一定要向前比较，不能用nums[start] == nums[start+1]，因为后面的值可能是你要用到的值，比如这情况：[-2,0,1,1,2]，都遍历-2时，start=1，end=1时不能滤过
                    while(start < len(nums)-2 and nums[start] == nums[start-1]): start += 1 
                    while(end > 1 and nums[end] == nums[end+1]): end -= 1
                elif nums[start] + nums[end] > r:
                    end -= 1
        return result
