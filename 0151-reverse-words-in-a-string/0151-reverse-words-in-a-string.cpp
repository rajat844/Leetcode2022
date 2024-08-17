class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(),s.end());
        
        int left = 0;
        int right = 0;
        int i = 0;
        
        while(i < s.size()){
            while(i < s.size() && s[i] == ' ') i++;
            if(i == s.size()) break;
            
            while(i < s.size() && s[i] != ' ') s[right++] = s[i++];
            reverse(s.begin() + left, s.begin() + right);
            s[right++] = ' ';
            left = right;
            i++;            
        }
        
        s.resize(right - 1);
        return s;
        
    }
};