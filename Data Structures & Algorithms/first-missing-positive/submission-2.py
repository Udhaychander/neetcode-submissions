class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing=1
        for num in nums:
            if num == missing:
                missing +=1
            if num > missing:
                return missing
        return missing