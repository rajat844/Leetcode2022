class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(start1,start2,end):
            temp = []
            i = start1
            j = start2
            
            while i < start2 and j <= end:
                if arr[i][0] > arr[j][0]:
                    ans[arr[i][1]] += end - j + 1
                    temp.append(arr[i])
                    i += 1
                else :
                    temp.append(arr[j])
                    j += 1
                    
            while i < start2:
                temp.append(arr[i])
                i += 1
            while j <= end:
                temp.append(arr[j])
                j += 1
            
            a = 0
            for i in range(start1,end+1):
                arr[i] = temp[a]
                a += 1
                    
        def mergeSort(start,end):
            if start < end:
                mid = (start+end) >> 1
                mergeSort(start,mid)
                mergeSort(mid+1,end)
                
                merge(start,mid+1,end)
                
        ans = [0 for i in range(len(nums))]
        n = len(nums)
        
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i],i))
        
        mergeSort(0,len(nums) - 1)
        return ans