class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int length = cardPoints.size() - k;
        int sum = 0;
        int start = 0;
        int ans = INT_MAX;
        
        for(int i = 0; i < cardPoints.size(); i++){
            sum += cardPoints[i];
            
            if(i - start + 1 > length){
                sum -= cardPoints[start];
                start++;
            }
            
            if(i - start + 1 == length){
                ans = min(ans,sum);
            }
        }
        
        int res = 0;
        for(int x : cardPoints){
            res += x;
        }
        
        if(ans != INT_MAX)  return res - ans;
        else return res;
        
    }
};