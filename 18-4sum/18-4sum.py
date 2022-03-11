class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(len(nums)-3):
            while i > 0 and i < n-3 and nums[i] == nums[i-1]:
                i += 1
            for j in range(i+1,len(nums)-2):
                while j > i+1 and j < n-2 and nums[j] == nums[j-1]:
                    j += 1
                tf = target - nums[i] - nums[j]
                x = j+1
                y = len(nums)-1
                while x < y:
                    if nums[x] + nums[y] == tf:
                        m = [nums[i], nums[j], nums[x], nums[y]] 
                        if m not in ans:
                            ans.append(m)
                        x += 1
                        y -= 1
                    elif nums[x] + nums[y] > tf:
                        y -= 1
                    else:
                        x +=1
            
        return ans
                                
                    
                    