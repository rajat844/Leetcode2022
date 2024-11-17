class Solution {
public:
    bool checkValidString(string s) {
        int leftMin = 0;
        int leftMax = 0;
        
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '('){
                leftMin += 1;
                leftMax += 1;
            } 
            else if(s[i] == ')'){
                leftMin -= 1;
                leftMax -= 1;
            }
            else{
                leftMin -= 1;
                leftMax += 1;
            }
            if(leftMax < 0) return false;
            
            if(leftMin < 0) leftMin = 0;
        }
        
        
        return leftMin == 0;
    }
};