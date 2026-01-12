import heapq
class Solution:

    # Construct adjacency list using list of lists
    def constructadj(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))
        return adj

    # find shortest path from src to dest
    # while ignoring the edge between source and destination
    def shortestPath(self, V, adj, src, dest):
        # Initialize distance array with infinity
        dist = [float('inf')] * V
        dist[src] = 0

        # Priority queue to store (distance, vertex)
        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)

            # If we already found a better path, skip this one
            if d > dist[u]:
                continue

            # Traverse neighbors
            for v, w in adj[u]:

                # ignored edge from source and destination
                if (u == src and v == dest) or (u == dest and v == src):
                    continue

                # Relaxation step
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist[dest]

    # Returns shortest distances from src to all other vertices
    def findMinCycle(self, V, edges):
        # Build the adjacency list once
        adj = self.constructadj(V, edges)
        minCycle = float('inf')

        # Try removing each edge one by one
        for edge in edges:
            u, v, w = edge
            dist = self.shortestPath(V, adj, u, v)

            # If such a path exists, it forms a cycle with (u, v)
            if dist != float('inf'):
                minCycle = min(minCycle, dist + w)

        # If no cycle found, return -1
        return minCycle
sol = Solution()
V = 5
edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5]]
print(sol.findMinCycle(V, edges))