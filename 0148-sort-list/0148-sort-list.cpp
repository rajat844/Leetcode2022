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
    ListNode* mergeList(ListNode* left,ListNode* right){
        ListNode* head = new ListNode();
        ListNode* curr = head;
        
        while(left && right){
            if(left->val <= right->val){
                curr->next = left;
                left = left->next;
            }
            else{
                curr->next = right;
                right = right->next;
            }
            curr = curr->next;
        }
        
        if(left) curr->next = left;
        if(right) curr->next = right;
        
        return head->next;        
    }
    
    ListNode* findMiddle(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head;
        
        while(fast->next != nullptr && fast->next->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    
    ListNode* sortList(ListNode* head) {
        if(head == nullptr || head->next == nullptr) return head;
        
        ListNode* middle = findMiddle(head);
        
        ListNode* rightList = middle->next;
        middle->next = nullptr;
        ListNode* leftList = head;
        
        rightList = sortList(rightList);
        leftList = sortList(leftList);
        
        return mergeList(leftList,rightList);
    }
};