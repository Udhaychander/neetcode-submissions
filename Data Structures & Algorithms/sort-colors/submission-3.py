class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count= defaultdict(int)
        for num in nums:
            count[num]+=1
        index=0
        for i in sorted(count.keys()):
            freq=count[i]
            while freq>0:
                nums[index]=i
                freq-=1
                index+=1


