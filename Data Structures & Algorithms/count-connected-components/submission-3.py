class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if i run through the graph once
        # connected components shud be n - len(visit)

        # map connected nodes to each other in both directions
        treeMap = {i:[] for i in range(n)}
        for v1, v2 in edges:
            treeMap[v1].append(v2)
            treeMap[v2].append(v1)
        
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            
            visit.add(i)
            for neighbor in treeMap[i]:
                dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        
        return count

        
            







