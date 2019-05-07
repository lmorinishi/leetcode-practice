class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1

        if i < len(nums1):
            tmp += nums1[i:]
        if j < len(nums2):
            tmp += nums2[j:]

        quot, remainder = divmod(len(tmp), 2)
        if remainder:
            return float(tmp[quot])
        else:
            return (tmp[quot-1] + tmp[quot])/2
