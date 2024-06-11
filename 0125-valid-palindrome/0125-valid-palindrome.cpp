class Solution {
public:
    bool isPalindrome(string s) {
        string mystr = "";
        
        for(int i = 0; i< s.length(); i++){
            if(isalnum(s[i])) mystr += tolower(s[i]);
        }
        cout << mystr;
        
        int size = mystr.length();
        for(int i = 0; i < size/2; i++){
            if(mystr[i] != mystr[size-i-1]) return false;
        }
        return true;
    }
};