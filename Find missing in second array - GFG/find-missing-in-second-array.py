#User function Template for python3



def findMissing(A,B,N,M):
    # code here
    x = set()
    for i in range(M):
        x.add(B[i])
        
    ans = []
    for j in range(N):
        if A[j] not in x:
            ans.append(A[j])
    
    return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ans=findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends