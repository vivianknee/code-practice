class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is valid if
            # no cycles
            # every node reachable from any node
        if not n:
            return True

        #adj list containing nodes and their connected nodes
        adjList = {i:[] for i in range(n)}  
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visit = set() # keep track of visited nodes
        
        def dfs(node, prev):
            if node in visit: # cycle in tree
                return False

            visit.add(node)

            for n in adjList[node]:
                if n == prev:
                    continue
                if dfs(n, node) == False:
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)



