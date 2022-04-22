

class Solution:
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
	    st = [] 
	    for i in range(len(arr)):
	        st.append((arr[i],i))
	        
	    st.sort(key = lambda x : x[0]) #[(2,0),(4,3),(5,3),(8,1)]
	    
	    i = 0
	    ans = 0
	    
	    while i < len(arr): # i = 1
	        if i == st[i][1]: 
	            i += 1
	        else :
	            x = st[i][1]
	            st[i],st[x] = st[x],st[i]
	            ans += 1
	   
	   
	    return ans
	    
		        
		

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends