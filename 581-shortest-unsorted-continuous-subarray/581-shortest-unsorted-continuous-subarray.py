class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        mx = arr[0]
        end = -1
        
        for i in range(1,n):
            if arr[i] >= mx:
                mx = arr[i]
            else :
                end = i
                
        mn = arr[-1]
        start = 0
        for i in range(n-2,-1,-1):
            if arr[i] <= mn:
                mn = arr[i]
            else :
                start = i
        
        return end - start + 1
                
        