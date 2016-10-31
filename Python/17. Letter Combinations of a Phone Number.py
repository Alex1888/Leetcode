"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        length = len(digits)
        digmp = {'1':['*'],
                 '2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'], 
                 '5':['j','k','l'], 
                 '6':['m','n','o'],
                 '7':['p','q','r','s'], 
                 '8':['t','u','v'],
                 '9':['w','x','y','z'], 
                 '0':[' ']}
        #index时digits的索引，递归回溯把所有的可能都打印出来，每次增加一个字母
        def findcomb(string, index, res):
            if index == length:
                res.append(string)
                return
            for letter in digmp[digits[index]]:
                findcomb(string+letter, index+1, res)
            
        
        res = []
        findcomb('', 0, res)
        
        return res
