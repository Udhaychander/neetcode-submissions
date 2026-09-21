class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def countGroups(maxSum):
            groups = 1
            current = 0
            for num in nums:
                if current + num > maxSum:
                    groups += 1
                    current = num
                else:
                    current += num
            return groups
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if countGroups(mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo