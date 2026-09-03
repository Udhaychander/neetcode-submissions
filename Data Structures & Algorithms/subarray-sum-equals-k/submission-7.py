class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store=defaultdict(int)
        res=cursum=0
        for num in nums:
            cursum+=num
            if cursum ==k:
                res+=1
            diff=cursum-k
            res+=store[diff]
            store[cursum]+=1
        return res