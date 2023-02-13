class Solution {
    public int calculate(int i,boolean isSell,int[] prices,int[][] st){
        if(i == prices.length){
            return 0;
        }
        if(isSell){
            return st[i][1] =  Math.max(prices[i] + calculate(i+1,false,prices,st), calculate(i+1,true,prices,st));
        }
        else{
            return st[i][0] = Math.max(-prices[i] + calculate(i+1,true,prices,st),calculate(i+1,false,prices,st));
        }
        
        
    }
    
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] st = new int[n+1][2];
        
        st[n][0] = 0; st[n][1] = 0;
        
        for(int i = n-1; i > -1; i--){
            st[i][0] = Math.max(-prices[i] + st[i+1][1],st[i+1][0]);
            st[i][1] = Math.max(prices[i] + st[i+1][0],st[i+1][1]); 
        }
        return st[0][0];
        
    }
}