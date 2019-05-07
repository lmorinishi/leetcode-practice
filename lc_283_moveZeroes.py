class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # max_len = len(nums)
        # i = 0
        # while i < max_len:
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))
        #         max_len -= 1
        #     else:
        #         i += 1

        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i-zero_count] = nums[i]
        for i in range(len(nums)-zero_count, len(nums)):
            nums[i] = 0
