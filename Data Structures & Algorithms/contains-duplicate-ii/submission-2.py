class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]==nums[r] and r-l<=k:
                return True
            r-=1
        return False
