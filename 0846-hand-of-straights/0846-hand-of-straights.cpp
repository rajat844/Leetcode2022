class Solution {
    struct comp{
      bool operator()(int a, int b){
          return a > b;
      }  
    };
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size() % groupSize != 0) return false;
        
        priority_queue<int,vector<int>,comp> pq;
        
        for(int x : hand){
            pq.push(x);
        }
        
        int currSize = groupSize;
        vector<int> nextGroup;
        int prev = -1;
        
        while(!pq.empty()){
            int curr = pq.top();
            pq.pop();
            
            if(prev == -1 || curr == prev+1){
                prev = curr;
                currSize--;
            }
            else{
                nextGroup.push_back(curr);
            }
            
            if(currSize == 0){
                currSize = groupSize;
                prev = -1;
                while(nextGroup.size() > 0){
                    pq.push(nextGroup.back());
                    nextGroup.pop_back();
                }
            }
        }
        
        if(currSize == groupSize) return true;
        return false;
        
    }
};