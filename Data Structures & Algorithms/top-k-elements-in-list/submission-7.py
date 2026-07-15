class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res,i=[],0
        for num in count.most_common():
            if i==k:
                break
            res.append(num[0])
            i+=1
        return res
