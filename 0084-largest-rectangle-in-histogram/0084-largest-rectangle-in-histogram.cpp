class Solution {
public:
//     vector<int> nextSmallerElement(vector<int> & heights){
//         int n = heights.size();
//         stack<int> st;
//         vector<int> ans(n,n);
        
//         for(int i = n-1; i >= 0; i--){
//             while(!st.empty() && heights[st.top()] >= heights[i]) st.pop();
            
//             ans[i] = st.empty() ? n : st.top();
            
//             st.push(i);
//         }
//         return ans;
//     }
    
//     vector<int> previousSmallerElement(vector<int> & heights){
//         int n = heights.size();
//         stack<int> st;
//         vector<int> ans(n,-1);
        
//         for(int i = 0; i < heights.size(); i++){
//             while(!st.empty() && heights[st.top()] >= heights[i]) st.pop();
            
//             ans[i] = st.empty() ? n : st.top();
            
//             st.push(i);
//         }
//         return ans;
//     }
    int largestRectangleArea(vector<int>& heights) {
//         vector<int> pse = previousSmallerElement(heights);
//         vector<int> nse = nextSmallerElement(heights);
        
        int area = 0;
        
        stack<int> st;
        
        for(int i = 0; i <= heights.size(); i++){
            while(!st.empty() && (i == heights.size() || heights[st.top()] > heights[i])) {
                int h = heights[st.top()]; 
                st.pop();
                
                int pse = (st.empty()) ? -1 : st.top();
                int nse = i;
                
                int w = nse - pse -1;
                
                area = max(h*w,area);
            }
            st.push(i);
        }

        return area;
    }
};