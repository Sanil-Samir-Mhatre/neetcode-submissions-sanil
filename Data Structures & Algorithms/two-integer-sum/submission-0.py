class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force or Array method with 2 For loops
        
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
        