class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            for subset in res[:]:
                res.append(subset + [n])
        return res