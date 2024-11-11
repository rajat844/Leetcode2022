class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        if(s.size() == 0) return 0;
        
        sort(s.begin(),s.end());
        sort(g.begin(),g.end());
        
        int ans = 0;
        
        int i = g.size() - 1;
        int j = s.size() - 1;
        
        while(i >= 0 and j >= 0){
            if(g[i] <= s[j]){
                i--;
                j--;
                ans += 1;
            }
            else{
                i--;
            }
        }
        
        return ans;
        
    }
};