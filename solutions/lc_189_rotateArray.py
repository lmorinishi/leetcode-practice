class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k is None or k <= 0:
            return
        for i in range(k % len(nums)):
            nums.insert(0, nums[-1])
            nums.pop(-1)
