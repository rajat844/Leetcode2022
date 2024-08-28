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
        ListNode* temp = head;
        
        while(n > 0){
            temp = temp->next;
            n -= 1;
        }
        
        if(!temp) return head->next;
        
        ListNode* curr = head;
        while(temp->next != nullptr){
            curr = curr->next;
            temp = temp->next;
        }
        
        
        if(curr->next->next == nullptr){
            curr->next= nullptr;
        }
        else {
            curr->next = curr->next->next;
        }
        
        return head;
        
    }
};