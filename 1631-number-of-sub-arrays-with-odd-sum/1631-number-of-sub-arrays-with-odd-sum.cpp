class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int sum = 0;
        int oddPrefixCount = 0;  
        int evenPrefixCount = 0; 
        int mod = 1e9 + 7;

        int ans = 0;  

        for (int i = 0; i < arr.size(); i++) {
            sum = (sum + arr[i]) % mod;                
            if (sum % 2 == 1) {
                ans  = (ans + 1) % mod;
                ans = (ans + evenPrefixCount) % mod;
                oddPrefixCount = (oddPrefixCount + 1) % mod;
            } else {
                ans = (ans + oddPrefixCount) % mod;
                evenPrefixCount = (evenPrefixCount +  1) % mod;
            }
        }

        return ans % mod;
    }
};