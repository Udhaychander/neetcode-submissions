class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        while k:
            prev = nums[0]              
            for i in range(1, n):        
                nums[i], prev = prev, nums[i]
            nums[0] = prev
            k -= 1