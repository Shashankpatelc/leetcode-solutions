# Problem Name: Two Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1 = 0
        ss = []

        for i in s:
            if i not in ss:
                ss.append(i)
                if l1 < len(ss):
                    l1 = len(ss)
            else:
                del ss[:ss.index(i)+1]
                ss.append(i)
                if l1 < len(ss):
                    l1 = len(ss)
        return l1
    
