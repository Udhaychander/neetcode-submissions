class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        for key, freq in Counter(nums).items(): 
            if freq > len(nums) // 3:
                res.append(key)
        return res