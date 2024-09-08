class Solution {
public:
    bool isPalindrome(string s){
        int n = s.size();
        
        for(int i = 0; i < n/2; i++){
            if(s[i] != s[n-i-1]){
                return false;
            }
        }
        return true;
    }
    
    void getPartition(int idx, vector<vector<string>> &ans,string s, vector<string> &temp){
        if(idx == s.size()){
            ans.push_back(temp);
            return;
        }
        
        string r = "";
        for(int i = idx; i < s.size(); i++) {
            r += s[i];
            if(isPalindrome(r)){
                temp.push_back(r);
                getPartition(i+1,ans,s,temp);
                temp.pop_back();
            }
        }
    }
    
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> temp;
        
        getPartition(0,ans,s,temp);
        return ans;
    }
};