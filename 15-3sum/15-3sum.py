class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            tf = 0 - nums[i]
            x = i+1
            y = len(nums)-1
            
            while( x < y):
                if nums[x] + nums[y] == tf:
                    ans.append([nums[i],nums[x],nums[y]])
                    temp = nums[x] 
                    while nums[x] == temp and x < y:
                        x += 1
                    temp = nums[y]
                    while nums[y] == temp and y > x:
                        y -= 1
                elif nums[x] + nums[y] > tf:
                    y -= 1
                else:
                    x += 1
                        
        return ans
                    
                    
            
        