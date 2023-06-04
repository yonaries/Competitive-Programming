class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(left, right):
                if left > right:
                    return -1
                
                mid = (left+right)//2
                
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] < target:
                    return binSearch(mid+1,right)
                
                else:
                    return binSearch(left,mid-1)
        
        return binSearch(0, len(nums)-1)