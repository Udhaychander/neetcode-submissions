class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i,num1 in enumerate(temperatures):
            temp=0
            for j in range(i+1,len(temperatures)):
                if num1<temperatures[j]:
                    temp=j-i
                    break
            if temp==float("inf"):
                res.append(0)
            else:
                res.append(temp)
        return res