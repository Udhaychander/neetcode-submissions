class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        res = []
        prev = (0, "")
        while heap:
            freq, char = heapq.heappop(heap)
            res.append(char)
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            freq += 1
            prev = (freq, char)
        ans = "".join(res)
        return ans if len(ans) == len(s) else ""