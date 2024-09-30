class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> ans;
        
        for(int x : asteroids){
            if(x > 0) ans.push_back(x);
            else{
                while(ans.size() > 0 && ans.back() > 0 && ans.back() < abs(x))ans.pop_back();
                if(ans.size() > 0 && ans.back() == abs(x)) ans.pop_back();
                else if(ans.size() == 0 || ans.back() < 0) ans.push_back(x);
            }
        }
        
        return ans;
        
    }
};