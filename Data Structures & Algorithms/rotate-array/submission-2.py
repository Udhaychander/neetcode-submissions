class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        while k>0:
            prev=nums[0]
            for i in range(1,len(nums)):
                nums[i], prev= prev, nums[i]
            nums[0]=prev
            k-=1
        return nums

