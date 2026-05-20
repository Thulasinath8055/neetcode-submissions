class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output=[]

        for i,num in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            target = -num

            while l < r:

                curr = nums[l] + nums[r]

                if curr > target:
                    r -= 1

                elif curr < target:
                    l += 1

                else:
                    output.append([num,nums[l],nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l +=1

                    while l<r and nums[r]==nums[r-1]:
                        r -=1

                    l +=1
                    r -=1

        return output