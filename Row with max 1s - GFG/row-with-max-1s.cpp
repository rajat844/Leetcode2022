// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++
class Solution{
public:
    int psn(vector<int> &row){
        int l = 0, h = row.size()-1,m;
        while(l<= h){
            m = (l+h)/2;
            
            if(row[m] == 0) l = m+1;
            else h = m-1;
        }
        int x = row.size() - l;
        return x;
    }
	int rowWithMax1s(vector<vector<int>> arr, int n, int m) {
	    // code here
	    int curr = 0, r = -1;
	    for(int i = 0; i<n; i++){
	        int x = psn(arr[i]);
	        if(curr < x){
	            curr = x;
	            r = i;
	        }
	    }
	    return r;
	}

};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector< vector<int> > arr(n,vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin>>arr[i][j];
            }
        }
        Solution ob;
        auto ans = ob.rowWithMax1s(arr, n, m);
        cout << ans << "\n";
    }
    return 0;
}
  // } Driver Code Ends