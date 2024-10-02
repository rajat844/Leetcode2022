class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char> st;
        
        for(char x : num){
            while(!st.empty() && st.back() > x && k > 0){
                k--;
                st.pop_back();
            }
            
            if(st.size() == 0 && x == '0')
                continue;
            else 
                st.push_back(x);
        }
        while(k > 0 && st.size() > 0){
            st.pop_back();
            k --;
        }
        string ans = "";
        
        for(int i = 0; i < st.size(); i++){
            if(i == 0 && st[i] == '0') continue;
            ans += st[i];
        }
        
        if(ans.size() == 0) return "0";
        return ans;
        
        
    }
};