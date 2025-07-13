# Problem Name : vaid parantheses
# Difficulty : Easy
# Problem : https://leetcode.com/problems/valid-parentheses/
# Solution : https://leetcode.com/problems/valid-parentheses/solutions/6951466/20-valid-parentheses-in-python-by-shasha-kjbo
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = [ None for _ in range(len(s))]
        top = -1

        if len(s) <= 1:
            return False

        for i in s:
            if i == '(' or i =='{' or i == '[':
                top+=1
                stack[top] = i
            elif i == ')' and stack[top] == '(':
                top-=1
            elif i == ']' and stack[top] == '[':
                top-=1
            elif i == '}' and stack[top] == '{':
                top-=1
            else:
                return False

        if top == -1:
            return True

        return False
        
    
