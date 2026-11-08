class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        store=defaultdict(int)
        for i,n in enumerate(nums):
            store[n]=i
            if target in store:
                return True
        return False