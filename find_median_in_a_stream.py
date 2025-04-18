import heapq
class Solution:
    def getMedian(self, arr):
        if len(arr) == 0:
            return []
        firstH = []
        lastH = []
        n = len(arr)
        op = [arr[0]]
        median = arr[0]
        heapq.heappush(firstH, -arr[0])
        for i in range(1, n):
            x = arr[i]
            F = len(firstH)
            L = len(lastH)
            if F > L:
                if x > median:
                    heapq.heappush(lastH, x)
                else:
                    elePop = heapq.heappop(firstH)
                    heapq.heappush(firstH, -x)
                    heapq.heappush(lastH, -elePop)
                median = (-firstH[0] + lastH[0]) / 2
            elif F == L:
                if x > median:
                    heapq.heappush(lastH, x)
                    median = lastH[0]
                else:
                    heapq.heappush(firstH, -x)
                    median = -firstH[0]
            else:
                if x > median:
                    elePop = heapq.heappop(lastH)
                    heapq.heappush(firstH, -elePop)
                    heapq.heappush(lastH, x)
                else:
                    heapq.heappush(firstH, -x)
                median = (-firstH[0] + lastH[0]) / 2
            op.append(median)
        return op