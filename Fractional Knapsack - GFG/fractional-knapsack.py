#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        storage = []
        
        for i in range(n):
            ratio = Items[i].value/Items[i].weight
            storage.append((ratio,Items[i].value,Items[i].weight))
            
        st = sorted(storage,key = lambda x: x[0], reverse = True)
        
        max_val = 0
        for i in range(n):
            wt,val = st[i][2],st[i][1]
            
            if W > wt:
                W -= wt
                max_val += val
            else :
                 fr = W/wt
                 max_val += val * fr
                 W = 0
                 break
        
        return max_val
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends