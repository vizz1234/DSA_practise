import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # code here
        if len(meetings) == 0 or n == 0:
            return -1
        
        meetings = sorted(meetings, key = lambda x : x[0])
        
        available_room = list(range(n))
        heapq.heapify(available_room)
        meeting_end = []
        room_count = [0] * n
        
        for s, e in meetings:
            
            duration = e - s
            
            while meeting_end and s >= meeting_end[0][0]:
                _, room = heapq.heappop(meeting_end)
                heapq.heappush(available_room, room)
            
            if available_room:
                room = heapq.heappop(available_room)
                heapq.heappush(meeting_end, (e, room))
            
            else:
                d_end, room = heapq.heappop(meeting_end)
                heapq.heappush(meeting_end, (d_end + duration, room))
            
            room_count[room] += 1
        
        max_room = max(room_count)
        return room_count.index(max_room)
        
sol = Solution()
print(sol.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
print(sol.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 19]]))  