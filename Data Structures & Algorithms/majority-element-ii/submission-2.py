class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        for num in count:
            if count[num]>len(nums)/3:
                ans.append(num)
        return ans