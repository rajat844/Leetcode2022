class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        long long num = x;
        long long rev = 0;
        while (num){
            rev = rev*10 + num%10;
            num /= 10;
        }
        if (rev == x) return true;
        return false;
        
    }
};