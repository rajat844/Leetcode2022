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
        
        while(n){
            temp = temp->next;
            n -= 1;
        }
        
        if(temp == nullptr) return head->next;
        
        ListNode* curr = head;
        
        while(temp->next){
            temp = temp->next;
            curr = curr->next;
        }
        
        if(curr->next->next){
            curr->next = curr->next->next;
        }
        else{
            curr->next = nullptr;
        }
        
        return head;
    }
};