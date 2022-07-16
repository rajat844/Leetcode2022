class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0 :
            x = (columnNumber-1) % 26
            ans += chr(x+65)
            columnNumber = (columnNumber - 1)//26
        
            
        ans = ans[::-1]
        return ans