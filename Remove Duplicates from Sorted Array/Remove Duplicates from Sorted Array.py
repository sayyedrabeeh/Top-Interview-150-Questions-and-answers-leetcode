from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        for i in range(1,len(nums)):
            if nums[i] != nums[a]:
                a+=1
                nums[a]=nums[i]
                
        return a+1  
         