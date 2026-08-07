class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 
        def merge_sort(nums):
            n = len(nums)
            if n == 1 or n == 0:
                return nums
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]
            L = merge_sort(L)
            R = merge_sort(R)
            i = 0 
            l,r = 0,0
            sorted_arr = [0] * n
            while l < len(L) and r < len(R):
                if L[l] < R[r]:
                    sorted_arr[i] = L[l]
                    l += 1
                else:
                    sorted_arr[i] = R[r]
                    r += 1
                i += 1
            while l < len(L):
                sorted_arr[i] = L[l]
                i += 1
                l += 1
            while r < len(R):
                sorted_arr[i] = R[r]
                r += 1
                i += 1
            return sorted_arr
        return merge_sort(nums)