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
        if(!head || !head->next) return head;
        ListNode* curr = head;
        ListNode* prev = nullptr;
        
        while(curr){
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        
        return prev;
    }
    
    ListNode* findKthNode(ListNode* head,int k){
        if(!head || !head->next) return nullptr;
        
        ListNode* curr = head;
        while(curr && k > 1){
            curr = curr->next;
            k--;
        }
        return curr;      
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(!head || !head->next) return head;
        
        ListNode* curr = head;
        ListNode* prev = new ListNode();
        prev->next = head;
        
        while(curr){
            ListNode* kthNode = findKthNode(curr,k);
            if(kthNode){
                ListNode* nextNode = kthNode->next;
                kthNode->next = nullptr;
                ListNode* reverseList = reverse(curr);
                if(head == prev->next){
                    head = reverseList;
                }
                prev->next = reverseList;
                curr->next = nextNode;
                prev = curr;
                curr = nextNode;
            }
            else{
                break;   
            }
        }
        return head;
        
    }
    
};