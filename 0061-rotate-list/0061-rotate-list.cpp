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
    int findSize(ListNode* head){
        if(!head) return 0;
        ListNode* curr = head;
        int size = 1;
        
        while(curr->next){
            curr = curr->next;
            size += 1;
        }
        
        return size;
    }
    
    ListNode* findKthNode(ListNode* head, int k){
        ListNode* curr = head;
        
        while(k > 1){
            k--;
            curr = curr->next;
        }
        return curr;
    }
    
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !head->next) return head;
        int size = findSize(head);
        ListNode* curr = head;

        k = k % size;
        if(k == size) return head;
        
        ListNode* lastNode = findKthNode(head,size);
        lastNode->next = head;
        
        ListNode* kthNode = findKthNode(head,size-k);
        ListNode* nextNode = kthNode->next;
        kthNode->next = nullptr;
        
        return nextNode;     
        
    }
};