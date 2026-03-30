class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # source airport : destination airport in tickets
        # original departure is JFK
        # reconstruct the light pack that the person took
        # each ticket used once so try for o(n) iteration
        # tie breaker is lexicographically found

        # we can create an adjacency list containt start : end since one start point can have multiple end points
        tickets.sort()
        adjList = defaultdict(list)
        for src, dst in tickets:
            adjList[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adjList:
                return False
            
            temp = list(adjList[src])
            for i, v in enumerate(temp):
                adjList[src].pop(i)
                res.append(v)

                if dfs(v): return True
                adjList[src].insert(i,v)
                res.pop()
            return False
        
        dfs("JFK")
        return res



        
        



