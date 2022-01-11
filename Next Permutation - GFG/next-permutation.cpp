// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    vector<int> nextPermutation(int N, vector<int> arr){
        // code here
        int index1 = N-2;
        while(index1 >= 0 and arr[index1] >= arr[index1+1]) index1--;
        if(index1 != -1){
            int index2 = N-1;
            while(index2 >= 0 and arr[index2] < arr[index1]) index2--;
            swap(arr[index1],arr[index2]);
        }
        reverse(arr.begin()+index1+1,arr.end());
        return arr;

    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0;i < N;i++)
            cin>>arr[i];
        
        Solution ob;
        vector<int> ans = ob.nextPermutation(N, arr);
        for(int u: ans)
            cout<<u<<" ";
        cout<<"\n";
    }
    return 0;
}  // } Driver Code Ends