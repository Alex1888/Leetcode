```
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0: return 0
        res = 0
        cnt = {}
        #只检查出现过的字母，不全检查
        for se in s:
            cnt[se] = True

        for cn in cnt:
            start, end = 0,0;
            usedk = 0
            # 整体思路是end往前走，碰到不一样的字母就用k的额度去换，直到额度用完；只有当碰到不一样的而且额度也用完了，才滑动窗口
            while end < len(s):
                if(s[end] == cn or usedk < k):
                    if s[end] != cn:
                        usedk += 1
                    res = max(res, end - start + 1)
                    end += 1
                else:
                    #当前长度不够了，需要调整头部，把头部往前推，并且已经替换的也减掉
                    if(s[start] != cn): # 因为上一步有可能是因为usedk==k才跳进这步的，这时候不需要减;
                         usedk -= 1
                    start += 1
        return res

