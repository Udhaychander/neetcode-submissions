class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        res = []
        while len(res) < k:
            res.append(count.popitem()[0])
        return res