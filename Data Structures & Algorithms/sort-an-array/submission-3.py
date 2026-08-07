class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self._merge_sort(nums)

    def _merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self._merge_sort(nums[:mid])
        right = self._merge_sort(nums[mid:])
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
                continue
            result.append(right[j])
            j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result