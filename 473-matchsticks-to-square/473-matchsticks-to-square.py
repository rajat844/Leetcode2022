class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4 or sum(matchsticks) % 4:
            return False      
        numSum = sum(matchsticks)
        matchsticks.sort(reverse = True)
        for x in matchsticks:
            if x > numSum // 4:
                return False
        visited = [False] * len(matchsticks)
        return self.dfs(matchsticks, 0, 0, 0, numSum // 4, visited)
        
    def dfs(self, a, made, cur, start, limit, visited):
        if made == 4:
            return True
        if cur == limit:
            return self.dfs(a, made + 1, 0, 0, limit, visited)
        i = start
        while i < len(a):
            if visited[i] or a[i] + cur > limit:
                i += 1
                continue
            visited[i] = True
            if self.dfs(a, made, cur + a[i], i + 1, limit, visited):
                return True
            visited[i] = False
            
            while i + 1 < len(a) and a[i + 1] == a[i]:
                i += 1
            i += 1
        return False
            
            
        