class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st = {}
        
        for i in range(len(nums)):
            if target - nums[i] in st:
                x = st[target-nums[i]]
                return [x,i]
            
            st[nums[i]] = i
            
        return []
        