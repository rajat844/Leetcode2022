class Solution {
public:
    bool canEat(vector<int> &piles, int mid, int h){
        for(int i = 0; i < piles.size(); i++){
            h -= piles[i]/mid;
            if(piles[i] % mid) h--;
        }
        if(h >= 0) return true;
        return false;
    }
    
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxPiles = INT_MIN;
        
        for(int i = 0; i < piles.size(); i++){
            maxPiles = max(piles[i],maxPiles);
        }
        
        if(h == piles.size()) return maxPiles;
        
        int left = 1;
        int right = maxPiles;
        int ans;
        
        while (left <= right){
            int mid = (left + right) >> 1;
            
            if(canEat(piles,mid,h)) {
                ans = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        
        return ans;
    }
};