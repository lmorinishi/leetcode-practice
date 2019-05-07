class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1).intersection(set(nums2))
        dict1 = {}
        dict2 = {}
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                dict1[nums1[i]] += 1
            else:
                dict1[nums1[i]] = 1

        for j in range(len(nums2)):
            if nums2[j] in dict2:
                dict2[nums2[j]] += 1
            else:
                dict2[nums2[j]] = 1

        small_keys = [k for k in dict1 if k in dict2]  # get common keys
        dict1 = {k: min(dict1[k], dict2[k]) for k in small_keys}  # replace val with min
        my_out = []
        for i in dict1:
            my_out += [i for k in range(dict1[i])]
        return my_out
