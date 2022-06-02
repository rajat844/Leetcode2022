#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        neg = []
        pst = []
        for i in range(n):
            if arr[i] < 0:
                neg.append(arr[i])
            else :
                pst.append(arr[i])
                
        p_ind= 0
        n_ind = 0
        
        
        for i in range(n):
            if i%2 == 0:
                if p_ind < len(pst):
                    arr[i] = pst[p_ind]
                    p_ind += 1
                else:
                    arr[i] = neg[n_ind]
                    n_ind += 1
            else :
                if n_ind < len(neg):
                    arr[i] = neg[n_ind]
                    n_ind += 1
                else :
                    arr[i] = pst[p_ind]
                    p_ind += 1
        
        return arr

                
                
                
                
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends