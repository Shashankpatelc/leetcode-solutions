// Problem Name: Two Sum
// Difficulty: Medium
// Problem: https://leetcode.com/problems/add-two-numbers/
// Leetcode : https://leetcode.com/u/Shashankpatelc/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* Head = new ListNode(0);
        ListNode* tail = Head;
        int c = 0;

        while (l1 != nullptr || l2 != nullptr || c != 0){
            int d1 = (l1 != nullptr) ? l1->val : 0;
            int d2 = (l2 != nullptr) ? l2->val : 0;

            int sum = d1 + d2 + c;
            int d = sum % 10;
            c = sum / 10;

            ListNode* newNode = new ListNode(d);
            tail->next = newNode;
            tail = tail->next;

            l1 = (l1 != nullptr) ? l1->next : nullptr;
            l2 = (l2 != nullptr) ? l2->next : nullptr;
        }
        ListNode* result = Head->next;
        Head->next = nullptr;
        return result;
    }
};