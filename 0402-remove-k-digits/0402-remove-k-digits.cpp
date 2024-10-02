class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char> st;
        
        for(char x : num){
            while(st.size() > 0 && st.back() > x && k > 0){
                st.pop_back();
                k--;
            }
            
            if(st.size() == 0 && x == '0')
                continue;
            st.push_back(x);
        }
        
        while(st.size() > 0 && k > 0){
            st.pop_back();
            k--;
        }
        
        string ans;
        
        for(char x : st){
            ans += x;
        }
        
        if(ans.size() == 0) return "0";
        return ans;
        
    }
};