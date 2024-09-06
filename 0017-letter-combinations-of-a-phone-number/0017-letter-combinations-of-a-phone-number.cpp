class Solution {
public:
    void getCombination(string digits,int idx,vector<string>& ans, string temp,map<int,vector<char>> &st){
        if(idx == digits.size()){
            if(temp.size() > 0) ans.push_back(temp);
            return;
        }
        
        for(int i = 0; i < st[digits[idx]].size();i++){
            temp += st[digits[idx]][i];
            getCombination(digits,idx+1,ans,temp,st);
            temp.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        map<int,vector<char>> st {
            {'2',{'a','b','c'}},
            {'3',{'d','e','f'}},
            {'4',{'g','h','i'}},
            {'5',{'j','k','l'}},
            {'6',{'m','n','o'}},
            {'7',{'p','q','r','s'}},
            {'8',{'t','u','v'}},
            {'9',{'w','x','y','z'}}
        };
        
        vector<string> ans;
        getCombination(digits,0,ans,"",st);
        return ans;
    }
    
};