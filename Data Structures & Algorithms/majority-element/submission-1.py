class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = maxc = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > maxc:
                res = num
                maxc = count[num]
        return res
