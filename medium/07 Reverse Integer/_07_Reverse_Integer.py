# Problem Name: Two Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/reverse-integer/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            res = int(str(x*-1)[::-1])*-1

        else:
            res = int(str(x)[::-1])
        
        if not abs(res) < 2**31 and res != 2**31 - 1:
            return 0
        return res
