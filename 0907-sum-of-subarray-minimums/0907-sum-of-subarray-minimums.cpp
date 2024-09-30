class Solution {
public:
    vector<int> findPsee(vector<int> & arr){
        vector<int> ans(arr.size(),-1);
        stack<int> st;
        
        for(int i = 0; i < arr.size(); i++){
            while(!st.empty() && arr[st.top()] > arr[i]) st.pop(); 
            ans[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        
        return ans;
    }
    
    vector<int> findNse(vector<int>& arr){
        int n = arr.size();
        vector<int> ans(n,n);
        stack<int> st;
        
        for(int i = n-1; i >= 0; i--){
            while(!st.empty() && arr[st.top()] >= arr[i]) st.pop();
            ans[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        return ans;
    }
    
    int sumSubarrayMins(vector<int>& arr) {
        vector<int> psee = findPsee(arr);
        vector<int> nse = findNse(arr);
        
        long sum = 0;
        int mod = 1000000007;
        
        for(int i = 0; i < arr.size(); i++){
            long left = i - psee[i];
            long right = nse[i] - i;
            
            sum = (sum + (((arr[i] * left) % mod) * right) % mod) % mod; 
        }
        
        return sum % mod;
    }
};