class Solution {
public:
    int romanToInt(string s) {
        map<char,int> st;
        st['I'] = 1;
        st['V'] = 5;
        st['X'] = 10;
        st['L'] = 50;
        st['C'] = 100;
        st['D'] = 500;
        st['M'] = 1000;
        
        int ans = 0;
        
        for(int i = 0; i < s.size(); i++){
            if(i < s.size() - 1 && st[s[i]] < st[s[i+1]] ) ans -= st[s[i]];
            else ans += st[s[i]];
        }
        
        return ans;
    }
};