class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        store=set(nums)
        if target in store:
            return True
        return False