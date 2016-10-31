"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        minsum = sys.maxint
        nums.sort()
        for i in range(len(nums)-2):
            #和3Sum的思路差不多，只不过不是找0-num[i], 而是找2Sum和target-nums[i]的关系，每次记录最小的minsum和对应的result
            start, end = i+1,len(nums) -1
            while start < end:
                if nums[start] + nums[end]+ nums[i] < target:
                    if minsum > abs(target - (nums[start] + nums[end] + nums[i])):
                        minsum = abs(target - (nums[start] + nums[end] + nums[i]))
                        result = nums[start] + nums[end] + nums[i]
                    start += 1
                elif nums[start] + nums[end] + nums[i] == target:
                    return target
                elif nums[start] + nums[end] + nums[i] > target:
                    if minsum > abs(target - (nums[start] + nums[end] + nums[i])):
                        minsum = abs(target - (nums[start] + nums[end] + nums[i]))
                        result = nums[start] + nums[end] + nums[i]
                    end -= 1
        return result
