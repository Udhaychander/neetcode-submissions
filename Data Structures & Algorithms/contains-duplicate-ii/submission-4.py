class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store=Counter()
        for i,n in enumerate(nums):
            if n in store and i-store[n]<=k:
                return True
            store[n]=i
        return False