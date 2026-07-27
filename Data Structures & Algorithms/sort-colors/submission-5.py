class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = Counter(nums)
        index = 0
        for num in range(len(count)):        
            freq = count[num]
            while freq > 0:
                nums[index] = num
                index += 1
                freq -= 1
        return nums