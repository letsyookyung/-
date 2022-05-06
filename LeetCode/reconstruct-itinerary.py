class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = collections.defaultdict(list)
        # print(tickets)
        # print(sorted(tickets))
        for a, b in sorted(tickets):
            # print(a,b)
            graph[a].append(b)
            
        print(graph)
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            print(a)
            route.append(a)
        dfs('JFK')
        print(route)
        return route[::-1]



Runtime: 42 ms 
defaultdict(<class 'list'>, {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']})
[]
SFO
ATL
SFO
JFK
ATL
JFK
['SFO', 'ATL', 'SFO', 'JFK', 'ATL', 'JFK']
