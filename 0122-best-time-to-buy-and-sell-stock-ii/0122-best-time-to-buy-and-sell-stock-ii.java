class Solution {
    
    public int maxProfit(int[] prices) {
        int n = prices.length;
        
        int prevbuy = 0; int prevsell = 0;
        
        
        for(int i = n-1; i > -1; i--){
            int currbuy = Math.max(-prices[i] + prevsell,prevbuy);
            int currsell = Math.max(prices[i] + prevbuy,prevsell); 
            
            prevsell = currsell; prevbuy = currbuy;
        }
        return prevbuy;
        
    }
}