class Solution {
public:
    int singleNonDuplicate(vector<int>& arr) {
         int n = arr.size();
        if( n == 1 ) return arr[0];
        int ele1 = arr[0];
        int ele2 = arr[2];
       
        if(ele1 != arr[1]) return ele1;
        for(int i = 1; i<n-1; i++){
            if(arr[i] != ele1  and arr[i] != ele2) return arr[i];
            else{
                ele1 = arr[i];
                ele2 = arr[i+2];
            }
        }
        return arr[n-1];
        
    }
};