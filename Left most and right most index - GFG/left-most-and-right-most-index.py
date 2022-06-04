#User function Template for python3

class Solution:
    def indexes(self, v, x):
        # Your code goes here
        def bs(flag):
            l = 0
            h = len(v) - 1
        
            while l <= h:
                mid = (l+h) >> 1
            
                if flag == False and v[mid] < x:
                    l = mid + 1
                elif flag == True and v[mid] <= x:
                    l = mid + 1
                else :
                    h = mid - 1
            
            if flag == False:
                return l if 0<= l <len(v) and v[l] == x else -1 
            if flag == True:
                return h if 0<= h<len(v) and v[h] == x else - 1
        
        left = bs(False)
        right = bs(True)
        
        return [left,right]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends