#User function Template for python3

def kthSmallest(mat, n, k): 
    def calmin(arr,x):
        l = 0
        h = len(arr)-1
        
        while l <= h:
            m = (l+h) >> 1
            if arr[m] <= x:
                l = m + 1
            else:
                h = m - 1
        return l
    # Your code goes here
    n = len(mat)
    m = len(mat[0])
    l = mat[0][0]
    h = mat[n-1][m-1]
    
    while l <= h:
        mid = (l+h) >> 1
        
        total = 0
        for i in range(len(mat)):
            total += calmin(mat[i],mid)

        if total >= k:
            h = mid - 1
        else:
            l = mid + 1
    
    return l
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()




# } Driver Code Ends