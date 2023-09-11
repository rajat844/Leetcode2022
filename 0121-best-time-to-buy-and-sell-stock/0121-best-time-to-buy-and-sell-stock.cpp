class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int maxProfitMade = 0;
        
        for(int i = 0; i < prices.size(); i++){
            minPrice = min(prices[i],minPrice);
            maxProfitMade = max(maxProfitMade,prices[i] - minPrice);
        }
        
        return maxProfitMade;
        
    }
};