class Solution {
public:
    string frequencySort(string s) {
        map<char,int> st;
        
        for(char x : s){
            st[x] += 1;
        }
        
        map<int,vector<char>> bucket;
        
        for(auto const &[key,val] : st){
            bucket[val].push_back(key);
        }
        
        string ans;
        
        for(int i = s.size(); i > 0; i--){
            if(bucket.find(i) != bucket.end()){
                for(char x : bucket[i]){
                    ans += string(i,x);
                }
            }
        }
        
        return ans;
    }
};