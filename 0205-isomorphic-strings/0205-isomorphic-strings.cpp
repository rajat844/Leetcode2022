class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.size() != t.size()) return false;
        map<char,char> st1;
        map<char,char> st2;
        
        for(int i = 0; i < s.size(); i++){
            if((st1.find(s[i]) != st1.end() && st1[s[i]] != t[i]) || 
               (st2.find(t[i]) != st2.end() && st2[t[i]] != s[i])) 
                return false;
            st1[s[i]] = t[i];
            st2[t[i]] = s[i];          
            
        }
        return true;
    }
};