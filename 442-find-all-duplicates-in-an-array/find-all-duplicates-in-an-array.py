class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map = {}
        arr = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i]+=1
        for i in map:
            if map[i] == 2:
                arr.append(i)
        return arr