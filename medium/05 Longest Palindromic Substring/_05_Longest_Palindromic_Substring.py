# Problem Name: Two Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-palindromic-substring/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s) == 1:
            return s
        
        def fun(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return s[left+1:right]
        
        string = s[0]

        for i in range(len(s)):
            
            odd = fun(i,i)
            even = fun(i,i+1)

            if len(odd) > len(string):
                string = odd
            if len(even) > len(string):
                string = even
        
        return string
