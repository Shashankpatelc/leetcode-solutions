// Problem Name: Two Sum
// Difficulty: Easy
// Problem: https://leetcode.com/problems/two-sum/
// Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0 ; i < nums.size() ; i++ ){
            for (int j = i + 1 ; j < nums.size(); j++){
                if (nums[i] + nums[j] == target){
                    return{i,j};
                }
            }
        }
        return {};
    }
};

// or 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sum;
        vector<int> v;
        for(int i = 0;i < size(nums) - 1; i++){
            for(int j = i+1; j < size(nums); j++){
                sum = nums[i] + nums[j];
                if(sum == target){
                    v.push_back(i);
                    v.push_back(j);
                }
            }
        }
        return v;
    }  
};

