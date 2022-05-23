#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    def helper(i,j):
        if dp[i][j] != None:
            return dp[i][j]
        if i > j :
            dp[i][j] = False
            return False
            
        if line[i:j+1] in dictionary:
            dp[i][j] = True
            return dp[i][j]
            
        dp[i][j] = False
        
        for k in range(i,j):
            if line[i:k+1] in dictionary:
                case1 = dp[i][k] if dp[i][k] != None else helper(i,k)
                case2 = dp[k+1][j] if dp[k+1][j] != None else helper(k+1,j)
            
                if case1 and case2:
                    dp[i][j] = True
                    break
        
        return dp[i][j]
    
    dp = [[None for i in range(len(line))]for j in range(len(line))]
    return helper(0,len(line) - 1)
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends