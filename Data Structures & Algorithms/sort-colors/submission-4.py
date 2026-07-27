class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = Counter(nums)
        index = 0
        for key in [0, 1, 2]:        
            freq = count[key]
            while freq > 0:
                nums[index] = key
                index += 1
                freq -= 1
        return nums