#Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
#n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        找到min(a[i], a[j])* (j-i)的最大值；记住一点关键：称水的多少是靠小边的决定的。
        双指针问题：双指针的目的就是过滤减少不必要的遍历
        从两边开始向中间遍历，每次挪动较小的边，直到j<i; 假设开始时结尾的j为小边：即使后面有更大的值，也可能是在j的左侧产生，因为i的如果
        右移的话，i减小了，即使a[i-1]比a[i]大，称的水也会减少，因为小边没变。相应的，j向左移动，即使出现比a[j]大的边，我们也能遍历到。
        """
        i, j, res = 0,len(height) - 1, 0
        while i < j:
            res = max(min(height[i], height[j])* (j - i), res)
            if(height[i] <= height[j]):
                i += 1
                res = max(min(height[i], height[j])* (j - i), res)
            else:
                j -= 1
                res = max(min(height[i], height[j])* (j - i), res)
        return res
