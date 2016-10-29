
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 : return ''
        if len(strs) == 1 : return strs[0]
        res = ''
        #找出第一组最长前缀，然后两两比较，之后的只能比第一组的小
        l = min(len(strs[0]), len(strs[1]))
        for j in range(l):
            if strs[0][j] != strs[1][j]:
                break;
            res += strs[0][j]
        for i in range(1, len(strs) -1):
            temp = ''
            l = min(len(strs[i]), len(strs[i+1]))
            for j in range(l):
                if strs[i][j] != strs[i+1][j]:
                    break;
                temp += strs[i][j]
            if len(temp) < len(res):
                res = temp
        
        return res
