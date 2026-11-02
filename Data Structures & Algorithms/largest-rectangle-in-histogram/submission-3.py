class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        res = []  
        for i, h in enumerate(heights):
            start = i
            while res and res[-1][1] > h:
                index, height = res.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            res.append((start, h))
        for i, h in res:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea