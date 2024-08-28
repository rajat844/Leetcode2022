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
    ListNode* reverse(ListNode* head){
        if(head == nullptr || head->next == nullptr) return head;
        
        ListNode* curr = head;
        ListNode* prev = nullptr;
        
        while(curr){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        
        return prev;
    }
    
    bool isPalindrome(ListNode* head) {
        if(head == nullptr || head->next == nullptr) return true;
        
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev;
        
        while(fast != nullptr && fast->next != nullptr){
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        
        prev->next = nullptr;
        ListNode* second = reverse(slow);
        
        while(head != nullptr && second != nullptr){
            if(head->val != second->val) return false;
            head = head->next;
            second = second->next;
        }
        
        return true;
    }
};