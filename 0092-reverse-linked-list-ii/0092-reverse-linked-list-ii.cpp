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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || !head->next || left == right)
            return head;

        ListNode* dummy = new ListNode(0);
        ListNode* prev = dummy;
        dummy->next = head;

        ListNode* curr = head;

        for(int i = 1; i < left; i++){
            prev = curr;
            curr = curr->next;
        }

        for(int i = left; i < right; i++){
            ListNode* nextNode = curr->next;
            curr->next = nextNode->next;
            nextNode->next = prev->next;
            prev->next = nextNode;
        }

        return dummy->next;
    }
};