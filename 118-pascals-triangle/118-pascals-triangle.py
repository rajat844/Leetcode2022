class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [1]
        ans = []
        ans.append(arr[::])
        
        for i in range(1,numRows):
            temp = [0]+arr+[0]
            arr = []
            for i in range(len(temp) - 1):
                arr.append(temp[i] + temp[i+1])
            
            ans.append(arr[::])
        
        return ans
            
        
                
        