#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        prd = 1
        z_count = 0
        
        for i in range(n):
            if nums[i] == 0:
                z_count += 1
                if z_count == 2:
                    return [0] * n
            else :
                prd *= nums[i]
                
        for i in range(n):
            if z_count == 1:
                if nums[i] != 0:
                    arr[i] = 0
                else :
                    arr[i] = prd
            else :
                arr[i] = prd//arr[i]
        
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends