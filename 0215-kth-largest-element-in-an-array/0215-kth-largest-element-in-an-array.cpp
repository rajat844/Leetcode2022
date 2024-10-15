class Solution {
    struct Custom{
        bool operator()(int lhs,int rhs){
            return lhs > rhs;
        }
    };
    
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,Custom> pq;
        for(int x: nums){
            pq.push(x);
            if(pq.size() > k){
                pq.pop();
            }
        }
        
        return pq.top();
    }
};