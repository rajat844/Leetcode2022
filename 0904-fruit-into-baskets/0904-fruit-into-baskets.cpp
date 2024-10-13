class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int ans = 0;
        map<int,int> mp;
        int start = 0;
        
        for(int i = 0; i < fruits.size(); i++){
            if(mp.find(fruits[i]) == mp.end()){
                while(mp.size() > 1){
                    mp[fruits[start]] -= 1;
                    if(mp[fruits[start]] == 0){
                        mp.erase(fruits[start]);
                    }
                    start++;
                }
            }
            mp[fruits[i]] ++;
            ans = max(ans,i-start + 1);
        }
        
        return ans;
        
    }
};