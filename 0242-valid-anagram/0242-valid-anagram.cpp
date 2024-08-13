class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;
        map<char,int> st;
        
        for(char x: s){
            st[x]++;
        }
        
        for(char y: t){
            if(st.find(y) != st.end() && st[y] != 0){
                st[y]--;
            } 
            else return false;
        }
        return true;
    }
};