#User function Template for python3

class Solution:
	def fractionToDecimal(self, numerator, denominator):
		# Code here
		ans = []
		st = {}
		if numerator * denominator < 1:
		    ans.append("-")
		    numerator = abs(numerator)
		    denominator = abs(denominator)
		    
		q = numerator//denominator
		r = numerator % denominator
		ans.append(str(q))
		if r == 0:
		    s = ''.join(ans)
		    return s
		else :
		    ans.append(".")
		    
		    while r != 0 and r not in st:
		        st[r] =  len(ans)
		        r = r*10
		        q = r//denominator
		        r = r%denominator
		        ans += str(q)
		        
		    if r in st:
		        ans.insert(st[r],"(")
		        ans.append(")")
		        
		s = ''.join(ans)
		return s 
		        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		numerator, denominator = input().split()
		numerator = int(numerator); denominator = int(denominator)
		ob = Solution()
		ans = ob.fractionToDecimal(numerator, denominator)
		print(ans)
# } Driver Code Ends