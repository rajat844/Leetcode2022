from typing import List


class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        # code here
        if n %2 == 0:
            x = n
        else:
            x = n-1
        
        for i in range(0,x,2):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        
        IntArray().Print(arr)

#{ 
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)

# } Driver Code Ends