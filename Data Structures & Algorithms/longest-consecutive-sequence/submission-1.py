class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = []
        if len(nums) == 0:
            return 0
        counter = [1]
        default = 1
        for i in nums:
            if i-1 not in nums and i+1 in nums:
                l.append(i)
        
        for i in l:
            count = 0
            k = i
            while k in nums:
                count+=1
                k+=1
            counter.append(count)
        return max(counter)

