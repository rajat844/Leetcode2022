#User function Template for python3
class Solution:

	def printUnsorted(self,nums, n):
		# code here
		end = 0
        mx = nums[0]
        
        for i in range(1,len(nums)):
            if mx > nums[i]:
                end = i
            else :
                mx = nums[i]
        
        start = 0
        mn = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if mn < nums[i]:
                start = i
            else :
                mn = nums[i]
        return [start,end]

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printUnsorted(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends