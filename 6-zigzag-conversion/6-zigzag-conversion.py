class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [[] for i in range(numRows)]
        
        i = 0        
        x = 0
        uptodown = True
        
        while x < len(s):
            if uptodown == True:
                arr[i].append(s[x])
                i += 1
                if i == numRows:
                    uptodown = False
                    i = numRows - 2
            else:
                arr[i].append(s[x])
                i -= 1
                if i == -1:
                    uptodown = True
                    i = 1
            x += 1
        s = ''
        for i in range(numRows):
            x = ''.join(arr[i])
            s += x
        
        return s
            
                    
        