class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        st = defaultdict(int)
        for i in range(len(nums)):
            st[nums[i]] += 1
        
        x = sorted(st.items(), key = lambda x: x[1],reverse = True)
        ans = []
        for i in range(k):
            ans.append(x[i][0])
        
        return ans