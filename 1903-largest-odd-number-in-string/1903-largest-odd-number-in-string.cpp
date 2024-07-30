class Solution {
public:
    string largestOddNumber(string num) {
        int right = num.size() - 1;
        
        while(right >= 0){
            if((num[right] - '0')%2 == 0) right--;
            else break;
        }
        cout << right;
        num.resize(right+1);
        return num;
    }
};