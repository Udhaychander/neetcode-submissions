class Solution:
    def search(self, nums: List[int], target: int) -> int:
        store=defaultdict(int)
        for i,n in enumerate(nums):
            if target in store:
                return store[target]
            store[n]=i
        return -1