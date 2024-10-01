class Solution {
public:
    vector<int> getNse(vector<int> &nums){
        int n = nums.size();
        vector<int> ans(nums.size(),n);
        stack<int> st;
        
        for(int i = n-1; i >= 0; i--){
            while(!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            ans[i] = st.empty() ? n : st.top();
            
            st.push(i);
        }
        
        return ans;
    }
    
    vector<int> getNge(vector<int> &nums){
        int n = nums.size();
        vector<int> ans(nums.size(),n);
        stack<int> st;
        
        for(int i = n-1; i >= 0; i--){
            while(!st.empty() && nums[st.top()] <= nums[i]) st.pop();
            ans[i] = st.empty() ? n : st.top();
            
            st.push(i);
        }
        
        return ans;
    }
    
    vector<int> getPsee(vector<int> &nums){
        int n = nums.size();
        vector<int> ans(nums.size(),-1);
        stack<int> st;
        
        for(int i = 0; i < n; i++){
            while(!st.empty() && nums[st.top()] > nums[i]) st.pop();
            ans[i] = st.empty() ? -1 : st.top();
            
            st.push(i);
        }
        
        return ans;
    }
    
    vector<int> getPgee(vector<int> &nums){
        int n = nums.size();
        vector<int> ans(nums.size(),-1);
        stack<int> st;
        
        for(int i = 0; i < n; i++){
            while(!st.empty() && nums[st.top()] < nums[i]) st.pop();
            ans[i] = st.empty() ? -1 : st.top();
            
            st.push(i);
        }
        
        return ans;
    }
    
    long long subArrayRanges(vector<int>& nums) {
        int n = nums.size();
        vector<int> nse = getNse(nums);
        vector<int> psee = getPsee(nums);
        vector<int> nge = getNge(nums);
        vector<int> pgee = getPgee(nums);
        
        long long sum = 0;
        
        for(int i = 0; i < n; i++){
            long long left1 = i - psee[i];
            long long right1 = nse[i] - i;
            
            long long left2 = i - pgee[i];
            long long right2 = nge[i] - i;
            
            cout << left2 << " " << right2 << endl;
            
            sum += ((left2 * right2) - (left1 * right1) )* nums[i];
        }
        
        return sum; 
    }
};