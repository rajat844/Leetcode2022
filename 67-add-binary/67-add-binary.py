class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        i,j= len(a)-1,len(b)-1
        carry = 0
        while i >=0 and j >=0:
            ans += str(int(a[i])^int(b[j]) ^ carry)  
            carry = int(a[i]) & int(b[j]) | int(b[j]) & carry | int(a[i]) & carry
            i -= 1
            j -= 1
        
        while i >= 0:
            ans += str(int(a[i]) ^ carry)
            carry = int(a[i]) & carry
            i -= 1
            
        while j >= 0:
            ans += str(int(b[j]) ^ carry)
            carry = int(b[j]) & carry
            j -= 1
            
        if carry:
            ans += str(carry)
        
        s = ans[::-1]
        
        return s
            
        