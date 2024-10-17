class KthLargest {
    struct comp{
        bool operator()(int a, int b){
            return a > b;
        }
    };
public:
    priority_queue<int,vector<int>,comp> pq;
    int size;
    KthLargest(int k, vector<int>& nums) {
        size = k;
        for(int x : nums){
            pq.push(x);
        }
        
        while(pq.size() > size){
            pq.pop();
        }
        
    }
    
    int add(int val) {
        pq.push(val);
        
        if(pq.size() > size){
            pq.pop();
        }
        
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */