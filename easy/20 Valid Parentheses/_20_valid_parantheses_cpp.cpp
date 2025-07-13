// Problem Name : vaid parantheses
// Difficulty : Easy
// Problem : https://leetcode.com/problems/valid-parentheses/
// Solution : https://leetcode.com/problems/valid-parentheses/solutions/6951600/20-valid-parentheses-in-c-by-shashankpat-lv7w
// Leetcode : https://leetcode.com/u/Shashankpatelc/

#include <stack>
class Solution {
public:
    bool isValid(string s) {
        int i;
        stack<char> st;

        for (i = 0; i < s.size(); i++) {

            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                st.push(s[i]);
            } else if (!st.empty()) {
                if (s[i] == ')' && st.top() == '(') {
                    st.pop();
                } else if (s[i] == ']' && st.top() == '[') {
                    st.pop();
                } else if (s[i] == '}' && st.top() == '{') {
                    st.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }

        if (st.empty()) {
            return true;
        }
        return false;
    }
};

