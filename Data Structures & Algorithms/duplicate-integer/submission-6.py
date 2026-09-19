class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #practice Sorting using optimal method  time:o(nlogn)   space:o(1) or o(n)
        nums.sort()  #very crucial to sort
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False