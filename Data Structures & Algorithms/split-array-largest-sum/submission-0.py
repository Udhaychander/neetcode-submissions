class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def solve(l, k):
            if k == 1:
                return sum(nums[l:])
            res = float('inf')
            total = 0
            for r in range(l, n - (k - 1)):
                total += nums[r]
                best_rest = solve(r + 1, k - 1)
                res = min(res, max(total, best_rest))
                if total >= res:
                    break
            return res
        return solve(0, k)