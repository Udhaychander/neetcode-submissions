class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            count=0
            while num in nums:
                num+=1
                count+=1
            res=max(res,count)
        return res