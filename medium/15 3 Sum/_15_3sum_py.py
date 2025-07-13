# Problem Name : 3Sum 
# Difficulty : Medium
# Problem : https://leetcode.com/problems/3sum/description/
# Solution : https://leetcode.com/problems/3sum/solutions/6863679/15-3sum-by-shashankpatelc-nfk8
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
