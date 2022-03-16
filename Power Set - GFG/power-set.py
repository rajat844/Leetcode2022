#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n = len(s)
		ans = []
		
		for num in range(1<<n):
		    sub = ''
		    for i in range(n):
		        if num & (1<<i):
		            sub += s[i]
		            
		    if len(sub) > 0:
		        ans.append(sub)
		        
		ans.sort()
		return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends