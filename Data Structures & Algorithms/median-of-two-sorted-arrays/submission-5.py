class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = (len(nums1) + len(nums2)) // 2
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = m - i - 2
            n1left = nums1[i] if i >= 0 else -math.inf
            n1right = nums1[i + 1] if (i + 1) < len(nums1) else math.inf
            n2left = nums2[j] if j >= 0 else -math.inf
            n2right = nums2[j + 1] if (j + 1) < len(nums2) else math.inf
            if n1left <= n2right and n2left <= n1right:
                if (len(nums1) + len(nums2)) % 2:
                    return min(n1right, n2right)
                return (max(n1left, n2left) + min(n1right, n2right)) / 2
            elif n1left > n2right:
                r = i - 1
            else:
                l = i + 1