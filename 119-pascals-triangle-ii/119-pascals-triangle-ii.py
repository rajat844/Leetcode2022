class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        
        for i in range(rowIndex):
            temp = [0] + ans + [0]
            res = []
            for j in range(len(ans) + 1):
                res.append(temp[j] + temp[j+1])
            ans = res
        return ans
        