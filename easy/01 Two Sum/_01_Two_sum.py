# Problem Name: Two Sum
# Difficulty: Easy
# Problem: https://leetcode.com/problems/two-sum/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if  nums[i]+nums[j] == target:
                    return (i,j)
                    