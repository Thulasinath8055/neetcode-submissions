class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        
        for i in range(len(nums)-k+1):
            currSum = float('-inf')
            for j in range(i,k+i):
                currSum = max(currSum,nums[j])
            output.append(currSum)
        return output