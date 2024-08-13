class Solution {
public:
    int maxDepth(string s) {
        int ans = INT_MIN;
        int temp = 0;
        
        for(char x : s){
            if(x == '('){
                temp++;
            }
            else if(x == ')'){
                temp--;
            }
            ans = max(temp,ans);
        }
        return ans;
        
    }
};