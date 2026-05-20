class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        output = []
        flag = 0
        for num in nums:
            hashmap[num]+=1
        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1]))
        for i in range(len(sorted_dict)-1,-1,-1):
            flag+=1
            if flag>k:
                break
            output.append(list(sorted_dict.keys())[i])
        return output