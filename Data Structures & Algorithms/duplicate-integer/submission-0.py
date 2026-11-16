class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        DupCheck = set()
        for num in nums:
            if num in DupCheck:
                return True
            else:
                DupCheck.add(num)
        return False