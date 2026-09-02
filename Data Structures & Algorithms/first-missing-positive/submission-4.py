class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing=1
        nums.sort()
        for num in nums:
            if num==missing:
                missing+=1
        return missing