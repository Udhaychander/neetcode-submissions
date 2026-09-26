class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store=Counter()
        l=0
        for r,n in enumerate(nums):
            if n in store and r-store[n]<=k:
                return True
            store[n]=r
        return False