# Problem Name: Two Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/zigzag-conversion/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        s1 = [''] * numRows
        i = 0
        dis = False
        for c in s:
            s1[i] += c
            if i == 0 or i == numRows - 1:
                dis = not dis
            i += 1 if dis else -1
        return "".join(s1)

        