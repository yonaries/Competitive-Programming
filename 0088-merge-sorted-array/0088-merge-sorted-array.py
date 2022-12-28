class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            j=0
            for i in range(m,len(nums1)):
                nums1[i]=nums2[j]
                j+=1
            
        else:
            j=0
            for i in range(m,len(nums1)):
                nums1[i]=nums2[j]
                j+=1
            nums1.sort()

        