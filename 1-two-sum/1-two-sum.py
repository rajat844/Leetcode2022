class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        arr =  []
        
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dic:
                arr.append(dic[x])
                arr.append(i)
                return arr
            dic[nums[i]] = i
            
        return arr
                
                
            
                
        