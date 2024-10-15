class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> temp = arr;
        sort(temp.begin(), temp.end());
        
        map<int,int> mp;
        
        int rank = 0;
        
        for(int i = 0; i < temp.size(); i++){
            if(i == 0 || temp[i] > temp[i-1]){
                rank++;
                mp[temp[i]] = rank;
            }
        }
        
        vector<int> ans;
        
        for(int x: arr){
           ans.push_back(mp[x]); 
        }
        
        return ans;
    }
};