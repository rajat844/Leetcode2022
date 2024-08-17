class Solution {
public:
    int beautySum(string s) {
        int ans = 0;
        
        
        for(int i = 0; i < s.size(); i++){
            map<char,int> st;
            
            for(int j = i; j < s.size(); j++){
                st[s[j]]++;
                
                int mx = INT_MIN;
                int mn = INT_MAX;
                
                for(auto const& [key,val] : st){
                    mx = max(val,mx);
                    mn = min(val,mn);
                }
                
                ans += mx-mn;
            }
        }
        
        return ans;
        
    }
};