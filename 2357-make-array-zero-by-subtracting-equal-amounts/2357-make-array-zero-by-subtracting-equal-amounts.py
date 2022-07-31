class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        st = set(nums)
        if 0 in st:
            return len(st) - 1
        else:
            return len(st)