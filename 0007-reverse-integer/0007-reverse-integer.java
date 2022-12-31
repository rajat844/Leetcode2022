class Solution {
    public int reverse(int x) {
        long ans = 0;
        while(x != 0){
            int lastDigit = x%10;
            x /= 10;
            ans = ans * 10 + lastDigit;
        }
        if(ans >= Integer.MIN_VALUE && ans <= Integer.MAX_VALUE) return (int)ans;
        return 0;
    }
}