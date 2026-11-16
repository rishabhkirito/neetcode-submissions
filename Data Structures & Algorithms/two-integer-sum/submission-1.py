class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Checker = {}
        for i,num in enumerate(nums):
            if target - num in Checker:
                return [Checker[target-num],i]
            else:
                Checker[num] = i
