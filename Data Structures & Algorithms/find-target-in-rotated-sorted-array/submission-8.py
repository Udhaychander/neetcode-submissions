class Solution:
    def search(self, nums: List[int], target: int) -> int:
        store=defaultdict(int)
        for i,n in enumerate(nums):
            store[n]=i
            if target in store:
                return store[target]
        return -1