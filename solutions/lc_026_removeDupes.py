class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        cur = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == cur:
                nums.pop(i)
            else:
                cur = nums[i]
                i += 1
        return len(nums)
