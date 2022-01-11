// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution {
  public:
    string longestPalin (string S) {
        // code here
        string ans = "";
        for(int i = 0; i<S.size(); i++){
            int a = i;
            string x = "";
            while(S[i]==S[a] and a<S.size()){
                x += S[a];
                a++;
            }
            int c = i-1;
            while(c>=0 and a<S.size() and S[c] == S[a]){
                x = S[c]+x+S[a];
                a++;
                c--;
            }
            if(ans.size() < x.size()) ans = x;
        }
        return ans;
    }
};

// { Driver Code Starts.

int main()
{
    int t; cin >> t;
    while (t--)
    {
        string S; cin >> S;
        
        Solution ob;
        cout << ob.longestPalin (S) << endl;
    }
}
// Contributed By: Pranay Bansal
  // } Driver Code Ends