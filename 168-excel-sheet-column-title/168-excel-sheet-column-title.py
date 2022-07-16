class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0 :
            x = (columnNumber - 1) % 26
            ans += chr(65+x)
            columnNumber = (columnNumber - 1) // 26
        
        return ans[::-1]