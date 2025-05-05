class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = {i:[] for i in range(N)} # each node in list is [cost, destination node]
        self.populateGraph(graph, points, N)
        return self.prims(graph, N)
    
    def populateGraph(self, graph, points, N):
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([cost, j])
                graph[j].append([cost, i])
    
    def prims(self, graph, N):
        minHeap = [[0,0]]
        visit = set()
        res = 0
        while len(visit) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neigh in graph[node]:
                if neigh[1] not in visit:
                    heapq.heappush(minHeap, neigh)
        return res



        

         

        