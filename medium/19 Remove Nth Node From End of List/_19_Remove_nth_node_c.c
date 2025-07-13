// Problem Name : Remove Nth Node From End of List
// Difficulty : Medium
// Problem : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
// Solution : https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/6950232/19-remove-nth-node-from-end-of-list-in-c-zgsc
// Leetcode : https://leetcode.com/u/Shashankpatelc/
 
 /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

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

