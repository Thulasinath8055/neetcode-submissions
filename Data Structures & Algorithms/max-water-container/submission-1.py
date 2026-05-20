class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        l, r = 0, len(heights)-1
        while l < r:
            height = min(heights[l], heights[r])
            width = r-l
            area = height * width
            output = max(area,output)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return output