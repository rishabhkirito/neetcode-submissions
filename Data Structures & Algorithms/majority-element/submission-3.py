class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checker = {}
        nums.sort()
        res = maxCount = 0

        for i in range(len(nums)):
            checker[nums[i]] = checker.get(nums[i],0)+1
            if maxCount < checker[nums[i]]:
                res = nums[i]
                maxCount = checker[nums[i]]
        return res
        