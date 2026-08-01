class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cursum = 0
        prefixsum = defaultdict(int)
        for num in nums:
            cursum += num
            if cursum == k:
                res += 1
            diff = cursum - k
            res += prefixsum[diff]
            prefixsum[cursum] += 1
        return res