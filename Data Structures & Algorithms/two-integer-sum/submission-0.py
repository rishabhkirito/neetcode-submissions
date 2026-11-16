class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Checker = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in Checker:
                return [Checker[target-num],i]
            else:
                Checker[num] = i
