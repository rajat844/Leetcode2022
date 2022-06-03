#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr,n):
    ##Your code here
    currmax = 0
    currmin = 0
    
    maxsum = arr[0]
    minsum = arr[0]
    
    for i in range(n):
        currmax = max(currmax+arr[i],arr[i])
        maxsum = max(currmax,maxsum)
        
        currmin = min(currmin+arr[i],arr[i])
        minsum = min(currmin,minsum)
        
    s = sum(arr)
    
    return max(maxsum,s-minsum) if maxsum > 0 else maxsum
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math
import sys

    
    

if __name__ == "__main__":
    T=int(input())
    while(T>0):
            
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
            
        print(circularSubarraySum(arr,n))
        
        T-=1
    
# } Driver Code Ends