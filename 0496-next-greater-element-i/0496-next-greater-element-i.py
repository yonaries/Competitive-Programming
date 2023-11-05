class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out=list()
        for num in nums1: 
            out.append(-1)
            for j in range(nums2.index(num)+1,len(nums2)):
                if nums2[j]>num: out[-1]=nums2[j]; break
        return out