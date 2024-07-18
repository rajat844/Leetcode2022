class Solution {
public:
    bool ifPossible(vector<int> &bloomDay,int m, int k,int day){
        int cnt = 0;
        for(int i = 0; i < bloomDay.size(); i++){
            if(day >= bloomDay[i])cnt++;
            else {
                m -= cnt/k;
                cnt = 0;
            }
        }
        m -= cnt/k;
        if(m > 0) return false;
        return true;
    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        if(bloomDay.size()/m < k) return -1;
        int mini{INT_MAX},maxi{INT_MIN}, ans;
        
        cout << 1;
        for(int i = 0; i < bloomDay.size(); i++){
            mini = min(bloomDay[i],mini);
            maxi = max(bloomDay[i],maxi);
        }
        
        while (mini <= maxi){
            int mid = (mini+maxi) >> 1;

            if(ifPossible(bloomDay,m,k,mid)){
                ans = mid;
                maxi = mid - 1;
            }
            else {
                mini = mid + 1;
            }
        }
        
        return ans;
        
    }
};