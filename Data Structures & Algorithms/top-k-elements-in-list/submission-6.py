class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        
        arr = []

        for num, cnt in hashmap.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res