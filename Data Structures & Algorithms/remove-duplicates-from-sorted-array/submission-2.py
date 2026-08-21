class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        unique=0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[unique] = num
                unique += 1
        return unique