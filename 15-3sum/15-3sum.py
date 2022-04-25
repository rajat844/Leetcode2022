class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            x = 0 - nums[i]
            
            a = i+1
            b = len(nums) - 1
            
            while a < b:
                if nums[a] + nums[b] == x:
                    ans.append([nums[i],nums[b],nums[a]])
                    temp = nums[a]
                    while a < b and nums[a] == temp:
                        a += 1
                    temp = nums[b]
                    while b > a and nums[b] == temp:
                        b -= 1
                        
                elif nums[a] + nums[b] > x:
                    b -=1
                else :
                    a += 1
                
        return ans
                
                    
                    
                    
            
        