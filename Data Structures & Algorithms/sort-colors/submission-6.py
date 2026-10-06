class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=Counter(nums)
        index=0
        for n in range(len(count)):
            freq=count[values]
            while freq:
                nums[index]=n
                freq-=1
                index+=1
        return nums