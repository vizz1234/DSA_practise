from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        line_equations = defaultdict(set)
        max_len = 2

        for i in range(len(points)):

            line1 = points[i]
            x1 = line1[0]
            y1 = line1[1]

            for j in range(i+1, len(points)):

                line2 = points[j]
                x2 = line2[0]
                y2 = line2[1]

                if x2 - x1 == 0:
                    line_eq = f'x = {x1}'
                
                else:
                    m = (y2 - y1) / (x2 - x1)
                    c = -m * x1 + y1
                    line_eq = f'y = {m}x + {c}'

                line_equations[line_eq].update([(x1, y1), (x2, y2)])
                max_len = max(max_len, len(line_equations[line_eq]))
        
        return max_len
        

sol = Solution()
print(sol.maxPoints([[1,1],[2,2],[3,3]]))