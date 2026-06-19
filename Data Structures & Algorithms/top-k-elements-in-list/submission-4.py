class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        arr = []
        for num, cnt in count.items():
            arr.append([num, cnt])
        def get_second(a):
            return a[1]
        arr.sort(key=get_second)

        res = []
        while k>len(res):
            res.append(arr.pop()[0])
        return res