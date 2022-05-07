class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1]
        
        for i in range(1,rowIndex+1):
            temp = [0]+arr+[0]
            arr = []
            for i in range(len(temp) - 1):
                arr.append(temp[i] + temp[i+1])
            
        
        return arr
        