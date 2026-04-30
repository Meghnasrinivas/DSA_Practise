# Merge Two Sorted Arrays

def merge_arrays(nums1,nums2):
    return sorted(nums1+nums2)
nums1 = list(map(int,input('enter first array:').split()))
nums2 = list(map(int,input('enter second array:').split()))
print(merge_arrays(nums1,nums2))