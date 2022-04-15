#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        if len(a) != len(b):
            return False
        n = len(a)
        #code here
        st = [0]*256
        for i in range(n):
            st[ord(a[i])] += 1
            st[ord(b[i])] -= 1
        
        for i in range(len(st)):
            if st[i] != 0:
                return False
        
        return True
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends