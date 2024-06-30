class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end(),[](const vector<int> &a, const vector<int> &b) {
            if(a[0] != b[0]) return a[0] < b[0];
            else return a[1] < b[1];
        });
        
        vector<vector<int>> ans;
        
        int currStart = intervals[0][0];
        int currEnd = intervals[0][1];
        
        for(int i = 1; i < intervals.size(); i++){
            if(currStart <= intervals[i][0] && currEnd >= intervals[i][0]){
                currEnd = max(currEnd,intervals[i][1]);
            }
            else{
                ans.push_back({currStart,currEnd});
                currStart = intervals[i][0];
                currEnd = intervals[i][1];
            }
        }
        
        ans.push_back({currStart,currEnd});
        
        return ans;
        
    }
};