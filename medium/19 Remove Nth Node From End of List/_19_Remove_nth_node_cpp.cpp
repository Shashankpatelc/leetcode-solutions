// Problem Name : Remove Nth Node From End of List
// Difficulty : Medium
// Problem : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
// Solution : https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/6950247/19-remove-nth-node-from-end-of-list-in-c-6a2m
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

    struct ListNode* node = head;
    int i = 1,k = 1;

    if(n == 0){
        return head;
    }

    while (node->next != NULL){
        node = node->next;
        i++;
    }
    
    if(n == i){
        head=head->next;
        return head;
    }

    node = head;
    
    while(k < i - n){
        node = node->next;
        k++;
    }
    
    node->next = node->next->next;
    
    return head;
    }
};

