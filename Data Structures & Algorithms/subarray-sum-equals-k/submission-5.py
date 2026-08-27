class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = {} 
        for num in nums:
            curSum += num
            if curSum == k:
                res += 1
            diff = curSum - k
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            res += prefixSums.get(diff, 0)
        return res