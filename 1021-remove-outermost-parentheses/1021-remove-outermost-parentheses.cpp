class Solution {
public:
    string removeOuterParentheses(string s) {
        int count = 0;
        
        string ans;
        
        for(char x : s){
            if(x == '(' ){
                if(!count == 0){
                    ans += '(';
                }
                count++;
            }
            else {
                count--;
                if(!count == 0){
                    ans += ')';
                }
            }
        }
        
        return ans;
        
    }
};