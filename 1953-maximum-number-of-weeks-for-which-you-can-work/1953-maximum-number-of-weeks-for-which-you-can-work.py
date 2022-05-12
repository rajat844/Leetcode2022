class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s = sum(milestones)
        m = max(milestones)
        
        if s - m >= m - 1:
            return s
        else:
            return 2*(s-m) + 1