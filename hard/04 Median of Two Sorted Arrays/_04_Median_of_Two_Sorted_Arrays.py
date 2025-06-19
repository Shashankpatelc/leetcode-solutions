# Problem Name: Two Sum
# Difficulty: Hard
# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])
        l = len(arr)
        if(l%2==0):
            return (arr[l//2]+arr[(l//2)-1])/2
        else:
            return (arr[l//2])
        
        