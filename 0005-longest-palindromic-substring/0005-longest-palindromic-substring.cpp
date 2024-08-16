class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() == 1) return s;
        string ans;
        
        for(int i = 0; i < s.size(); i++){
            int j = i;
            string temp = "";
            
            while(j < s.size() && s[j] == s[i]){
                temp += s[j];
                j++;  
            }
            
            int k = i-1;
            
            while(k >= 0 && j < s.size() && s[j] == s[k]){
                temp = s[k] + temp + s[j];
                j++;
                k--;
            }
            
            if(ans.size() < temp.size()){
                ans = temp;
            }
        }
        
        return ans;
        
    }
};