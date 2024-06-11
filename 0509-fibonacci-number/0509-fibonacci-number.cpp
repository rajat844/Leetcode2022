class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;
        int prev1 = 0;
        int curr = 1;
        for(int i = 2; i<= n; i++){
            int temp = prev1 + curr;
            prev1 = curr;
            curr = temp;
        }
        
        return curr;
    }
};