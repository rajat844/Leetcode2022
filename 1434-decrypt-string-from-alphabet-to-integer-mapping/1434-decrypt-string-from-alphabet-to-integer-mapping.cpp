class Solution {
public:
    string freqAlphabets(string s) {
        int i = 0;
        string ans = "";

        while(i < s.size()){
            string temp;
            if(i + 2 < s.size() && s[i + 2] == '#'){
                temp = s.substr(i,2);
                i += 3;
            }
            else {
                temp = s[i];
                i += 1;
            }
            cout << temp << endl;
            ans += 'a' + (stoi(temp) - 1);
        }

        return ans;
    }
};