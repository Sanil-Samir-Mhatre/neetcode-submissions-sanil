class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #iteration 2 Pass for loop
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans