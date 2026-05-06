import heapq

class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        if len(start) == 0 or len(start) == 1:
            return len(start)
        
        meeting_time_sorted = sorted(zip(start, end), key = lambda x : x[0])
        
        max_rooms = 1
        heap = []
        heapq.heappush(heap, meeting_time_sorted[0][1])
        
        for i in range(1, len(meeting_time_sorted)):
            
            while heap and meeting_time_sorted[i][0] >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, meeting_time_sorted[i][1])
            max_rooms = max(max_rooms, len(heap))
        
        return max_rooms

sol = Solution()
print(sol.minMeetingRooms([0, 5, 15], [10, 10, 20]))
