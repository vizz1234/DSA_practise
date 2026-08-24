class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)
        int_x1 = max(ax1, bx1)
        int_y1 = max(ay1, by1)
        int_x2 = min(ax2, bx2)
        int_y2 = min(ay2, by2)

        int_area = 0

        if int_x1 < int_x2 and int_y1 < int_y2:
            int_area = (int_x2 - int_x1) * (int_y2 - int_y1)
        
        return area_1 + area_2 - int_area

sol = Solution()
print(sol.computeArea(-2,-1,2,2,1,-2,3,3))