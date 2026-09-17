class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res=j-i+1
        return res