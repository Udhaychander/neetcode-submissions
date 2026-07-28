class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        for key in count:
            freq=count[key]
            res.append([freq,key])
        res.sort(reverse=True)
        ans=[]
        i=0
        while i<k:
            ans.append(res[i][1])
            i+=1
        return ans