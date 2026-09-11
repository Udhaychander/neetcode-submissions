class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while res and temperatures[i] > temperatures[res[-1]]:
                prev = res.pop()
                ans[prev] = i - prev
            res.append(i)
        return ans