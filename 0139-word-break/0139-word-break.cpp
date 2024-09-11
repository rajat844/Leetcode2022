class Solution {
public:
    bool isPresent(string temp, vector<string>& wordDict){
        for(int i = 0; i < wordDict.size(); i++){
            if(temp == wordDict[i]) return true;
        }
        return false;
    }
    
//     bool isPossible(string s, vector<string> &wordDict, int idx, vector<int> &dp){
//         if(idx == s.size()){
//             return true;
//         }
        
//         if(dp[idx] != -1) return dp[idx];
        
//         string temp = "";
//         for(int i = idx; i < s.size(); i++){
//             temp += s[i];
//             int val = isPresent(temp,wordDict);
//             if(val != -1){
//                 bool check = isPossible(s,wordDict,i+1,dp);
//                 if(check) return dp[idx] = true;
//             }
//         }
//         return dp[idx] = false;
//     }
    
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(n+1,false);
        
        
        
        dp[n] = true;
        
        for(int i = n-1; i >= 0; i--){
            string temp = "";
            for(int j = i; j < n; j++){
                temp += s[j];
                if(isPresent(temp,wordDict)){
                    bool check = dp[j+1];
                    if(check) dp[i] = true;
                }
            }
        }
        
        return dp[0];
    }
};