class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        for key in count:
            freq=count[key]
            res.append([freq,key])
        res.sort(reverse=True)
        ans=[]
        for i in range(k):
            ans.append(res[i][1])
        return ans