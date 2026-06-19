class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        index = 0
        for key in range(len(count.keys())):
            freq = count[key]
            while freq > 0:
                nums[index] = key
                index += 1
                freq -= 1
        return nums