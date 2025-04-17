class Solution:
    
    def kClosest(self, points, k):
        # Your code here
        import heapq
        maxH = []
        for point in points:
            d = point[0] ** 2 + point[1] ** 2
            d *= -1
            if len(maxH) < k:
                heapq.heappush(maxH, (d, point))
            
            else:
                if d > maxH[0][0]:
                    heapq.heapreplace(maxH, (d, point))
        return [i[1] for i in maxH]