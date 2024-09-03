class Solution {
public:
    int p = 1e9 + 7;
    long long myPow(long long n, int x){
        if(x == 1 || n == 0) return 1;
        if(n == 1) return x;
        
        long long ans = myPow(n/2,x);
        
        if(n % 2 == 0) return (ans * ans) % p;
        else return (((ans*ans) % p) * x) % p; 
        
    }
    
    int countGoodNumbers(long long n) {
        long long even = n/2;
        long long odd = n - even;
        
        return ((myPow(odd,5)) * (myPow(even,4))) % p;
        
    }
};