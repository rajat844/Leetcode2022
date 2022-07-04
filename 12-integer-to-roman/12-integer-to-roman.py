class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],
               ["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        
        ans = ""
        n = len(arr)
        for i in range(n-1,-1,-1):
            x1 = arr[i][0]
            x2 = arr[i][1]
            
            div = num//x2
            num = num % x2
            while div:
                ans +=x1
                div -= 1
        
        return ans
            
            