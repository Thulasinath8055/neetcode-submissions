class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [1,2,3,4]
        # target = 3
        # output = [1,2]
        # hashmap = {}
        # for i, num in enumerate(numbers):
        #     diff = target - num
        #     if diff in hashmap:
        #         return [hashmap[diff]+1,i+1]
        #     hashmap[num] = i 

        l, r = 0, len(numbers)-1
        while l < r:
            # check if the sum is greater than the target
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1] 