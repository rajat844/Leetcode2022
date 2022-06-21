class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            tempans = ""
            if i%3 == 0:
                tempans += "Fizz"
            if i%5 == 0:
                tempans += "Buzz"
            if tempans == "":
                tempans += str(i)
            ans.append(tempans)
        
        return ans
                
        