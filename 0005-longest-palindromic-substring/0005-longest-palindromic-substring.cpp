class Solution {
public:
    string longestPalindrome(string s) {
        string ans;
        
        for(int i = 0; i < s.size(); i++){
            int j = i;
            int k = i;
            
            while(j-1 >= 0 && s[j-1] == s[i]){
                j--;
            }
            
            while(k+1 < s.size() && s[k+1] == s[i]){
                k++;
            }
            
            while(j-1 >= 0 && k+1 < s.size() && s[j-1] == s[k+1]){
                j--;
                k++;
            }
            
            if(ans.size() <= k-j+1){
                ans = s.substr(j,k-j+1);
            }
        }
        
        return ans;
        
    }
};