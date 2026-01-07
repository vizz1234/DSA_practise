class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # code here
        r = len(image)
        c = len(image[0])
        oc = image[sr][sc]
        if oc == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            x, y = stack.pop()
            
            if (x < 0 or x >= r) or (y < 0 or y >= c):
                continue
            cc = image[x][y]
            if cc != oc:
                continue
            image[x][y] = newColor
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))
        return image