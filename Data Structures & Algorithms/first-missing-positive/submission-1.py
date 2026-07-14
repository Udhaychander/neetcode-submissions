class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        missing = 1
        for num in nums:
            if num<missing:
                continue
            if missing == num:
                missing += 1
            if num>missing:
                return missing
        return missing