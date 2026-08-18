class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,n = 0,len(nums)-1
        j = 0
        def swap(x,y):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp

        while j<=n:
            if nums[j] == 0:
                swap(i,j)
                i += 1
            elif nums[j]==2:
                swap(j,n)
                n -= 1
                j -= 1
            j += 1
