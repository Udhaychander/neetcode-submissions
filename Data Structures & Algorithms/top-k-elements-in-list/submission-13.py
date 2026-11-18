class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        store=[]
        for key,val in count.items():
            store.append([val,key])
        store.sort(reverse=True)
        res=[]
        while k:
            res.append(store[k-1][1])
            k-=1
        return res