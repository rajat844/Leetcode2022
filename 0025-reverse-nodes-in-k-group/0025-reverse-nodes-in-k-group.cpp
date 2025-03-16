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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1)
            return head;
        int count = 0;
        ListNode* curr = head;
        while (curr) {
            curr = curr->next;
            count += 1;
        }

        int x = count / k;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        curr = head;

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < k - 1; j++) {
                ListNode* nextNode = curr->next;
                curr->next = nextNode->next;
                nextNode->next = prev->next;
                prev->next = nextNode;
            }
            prev = curr;
            curr = curr->next;
        }

        return dummy->next;
    }
};