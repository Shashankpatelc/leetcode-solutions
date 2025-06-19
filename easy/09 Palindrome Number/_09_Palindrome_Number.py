# Problem Name: Two Sum
# Difficulty: Easy
# Problem: https://leetcode.com/problems/palindrome-number/
# Leetcode : https://leetcode.com/u/Shashankpatelc/

class Solution {
    public boolean isPalindrome(int x) {
        int rem,rev=0,dup = x;
        while( dup > 0 ){
            rem = dup%10;
            rev = (rev*10) + rem;
            dup = dup/10;
        }
        if(x == rev){
            return true;
        }
        else{
            return false;
        }
    }
}