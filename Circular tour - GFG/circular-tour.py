'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        balance = 0
        start = 0
        defecit = 0
        
        for i in range(len(lis)):
            petrol = balance + lis[i][0]
            distance = lis[i][1]
            
            if (petrol >= distance):
                balance = petrol - distance
            
            else :
                balance = 0
                start = i+1
                defecit += distance - petrol
                
        
        if balance >= defecit :
            return start
        else:
            return -1
#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends