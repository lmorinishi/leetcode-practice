class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = i
        return False
