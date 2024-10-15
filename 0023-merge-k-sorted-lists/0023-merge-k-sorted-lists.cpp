class Comp{
    public:
    bool operator()(ListNode* node1, ListNode*node2){
        return node1->val > node2->val;
    }
};

class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.size() == 0) return nullptr;

        priority_queue<ListNode *, vector<ListNode *>, Comp> pq;

        for (ListNode* list: lists) {
            if(list != nullptr) pq.push(list);
        }

        ListNode* head = new ListNode(0);
        ListNode* tail = head;

        while (!pq.empty()) {
            auto temp = pq.top();
            pq.pop();
            if(temp->next != nullptr) pq.push(temp->next);
            tail->next = temp;
            tail = tail->next;
        }

        tail->next = NULL;
        return head->next;
    }
};