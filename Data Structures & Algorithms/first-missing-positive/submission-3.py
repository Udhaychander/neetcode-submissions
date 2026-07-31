class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res=sorted(nums)
        miss =1
        for num in res:
            if num == miss:
                miss+=1
            if num>miss:
                return miss
        return miss