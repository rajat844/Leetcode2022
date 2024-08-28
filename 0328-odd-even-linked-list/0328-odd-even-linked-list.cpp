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
    ListNode* oddEvenList(ListNode* head) {
        ListNode* odd = new ListNode();
        ListNode* odd_curr = odd;
        
        ListNode* even = new ListNode();
        ListNode* even_curr = even;
        
        bool flag = true;
        while(head != nullptr){
            ListNode* nextNode = head->next;
            head->next = nullptr;
            if(!flag){
                even_curr->next = head;
                even_curr = even_curr->next;
            }
            else{
                odd_curr->next = head;
                odd_curr = odd_curr->next;
            }
            head = nextNode;
            flag = !flag;
        }
        
        odd_curr->next = even->next;
        return odd->next;
        
    }
};