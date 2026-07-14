class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        missing =0
        for num in nums:
            if num<missing:
                continue
            if num==missing:
                missing+=1
            if num>missing:
                return missing
        return missing
