class Solution:
    def sortColors(self, nums: List[int]) -> None:
        minimum = min(nums)
        maximum = max(nums)
        count = [0] * (maximum - minimum + 1)
        for num in nums:
            count[num - minimum] += 1
        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[index] = i + minimum
                index += 1
                count[i] -= 1