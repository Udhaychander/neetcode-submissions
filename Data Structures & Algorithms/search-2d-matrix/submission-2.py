class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        l,r=0,(r*c)-1
        while l<=r:
            m=(l+r)//2
            if m>target:
                r-=m-1
            elif m<target:
                l+=m+1
            else:
                return True
        return False