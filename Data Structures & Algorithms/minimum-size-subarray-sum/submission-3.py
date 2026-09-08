class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        cur = 0
        for r, n in enumerate(nums):
            cur += n
            while cur >= target:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
        return res if res!=float('inf') else 0