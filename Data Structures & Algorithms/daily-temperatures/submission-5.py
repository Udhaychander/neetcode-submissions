class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1 ,-1):
            while res and temperatures[res[-1]] <= temperatures[i]:
                res.pop()
            if res:
                ans[i] = res[-1] - i
            res.append(i)
        return ans