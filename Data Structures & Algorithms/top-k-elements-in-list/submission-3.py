class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in set(nums):
            d[i] = nums.count(i)
        d = dict(sorted(d.items(),key=lambda x: x[1],reverse = True))
        print(d)
        return list(d.keys())[0:k]

            