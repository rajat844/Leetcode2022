class Solution {
public:
    int characterReplacement(string s, int k) {
        int ans = 0;
        map<char,int> mp;
        int maxfreq = 0;
        int start = 0;
        
        for(int i = 0; i < s.size(); i++){
            mp[s[i]]++;
            maxfreq = max(maxfreq,mp[s[i]]);
            
            while((i - start + 1 - maxfreq) > k){
                mp[s[start]]--;
                start++;
            }
            
            ans = max(ans,i-start+1);
        }
        return ans;
        
    }
};