class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = [0]
        temp = 0
        for i in range(n):
            temp += nums[i]
            s.append(temp)
        
        res = []
        for i in range(n):
            ans = 0
            if i > 0:
                ans += i*nums[i] - s[i]
            
            x = s[-1] - s[i+1]
            ans += x - ((n-i-1) *nums[i])
            
            res.append(ans)
        
        return res
                
                
                

        