class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = numsDivide[0]
        for i in range(len(numsDivide)):
            g = gcd(g,numsDivide[i])
        
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] <= g :
                if g % nums[i] == 0:
                    return i
            else:
                break
        return -1
                
            
        