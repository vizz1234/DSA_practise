class Solution:
    def findOrder(self, words):
        # code here
        indegree = {}
        for word in words:
            for ch in word:
                indegree[ch] = 0
        graph = {ch:[] for ch in indegree}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].append(w2[j])
                        indegree[w2[j]] += 1
                    break
        queue = [ch for ch in indegree if indegree[ch] == 0]
        order = []
        front = 0
        while front < len(queue):
            top = queue[front]
            order.append(top)
            front += 1
            for v in graph[top]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        if len(order) != len(indegree):
            return ""
        
        return "".join(order)
            
sol = Solution()
print(sol.findOrder(["baa", "abcd", "abca", "cab", "cad"]))