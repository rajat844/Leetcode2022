class Solution {
public:
    // a 0
    
    string minWindow(string s, string t) {
        map<char,int> mp;
        for(char x : t) mp[x]++;
        
        int count = mp.size(); 
        int count1 = 0;
        int start = 0;
        int minLen = INT_MAX;
        int startIdx = -1;
        
        for(int i = 0; i < s.size(); i++){
            mp[s[i]]--;
            if(mp[s[i]] == 0){
                count1 += 1;
            }
            while(count1 == count){
                if(minLen >= i-start+1){
                    minLen = min(minLen,i-start+1);
                    startIdx = start;
                }
                mp[s[start]]++;
                if(mp[s[start]] == 1) count1 -= 1;
                start++;
            }
        }
        if(minLen == INT_MAX) return "";
        return s.substr(startIdx,minLen);
        
    }
};