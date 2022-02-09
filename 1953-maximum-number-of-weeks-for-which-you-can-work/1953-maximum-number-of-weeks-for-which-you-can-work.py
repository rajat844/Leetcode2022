from queue import PriorityQueue 
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m = max(milestones)
        s = sum(milestones)
        
        if s-2*m < -1:
            return 2*(s-m) +1
        else :
            return s