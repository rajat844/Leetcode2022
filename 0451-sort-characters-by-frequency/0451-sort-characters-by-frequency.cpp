class Solution {
public:
    string frequencySort(string s) {
        map<char,int> counter;
    
        for(char x : s){
            counter[x] += 1;
        }
        
        map<int,vector<char>> st;
        
        for(auto const& [key,val] : counter){
            st[val].push_back(key);
        }
        
        string ans;
        
        for(int i = s.size(); i > 0; i--){
            if(st.find(i) != st.end() && st[i].size() != 0){
                for(char x : st[i]){
                    ans += string(i,x);
                }
            }
        }
        
        return ans;
        
        
    }
};