class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(start1,start2,end):
            nonlocal ans
            temp = []
            i = start1
            j = start2
            
            for i in range(i,start2):
                while j<= end and nums[i] > 2*nums[j]:
                    j += 1
                ans += j - start2
                
            i = start1
            j = start2
                
            while i < start2 and j <= end:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else :
                    temp.append(nums[j])
                    j += 1
                    
            while i < start2 :
                temp.append(nums[i])
                i += 1
            
            while j <= end:
                temp.append(nums[j])
                j += 1
            
            
            a = 0
            
            for i in range(start1,end + 1):
                nums[i] = temp[a]
                a += 1
                
                    
        def mergeSort(start,end):
            if start < end:
                mid = (start + end)>> 1
                
                mergeSort(start,mid)
                mergeSort(mid+1,end)
                
                merge(start,mid+1,end)
                
        
        ans = 0                
        mergeSort(0,len(nums) - 1)
        print(nums)
        return ans