class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,1
        while r<=len(nums)-1:
            if nums[l]==nums[r]:
                nums.pop(l)
            else:
                l+=1
                r+=1
        return len(nums)