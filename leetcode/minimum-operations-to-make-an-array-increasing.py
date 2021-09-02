# Link to Question https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums):
        answer = 0
        for i in range(1, len(nums)):
            previous = nums[i]
            nums[i] = max(nums[i-1]+1, nums[i])
            answer += nums[i]-previous
        return answer


sol = Solution()
print(sol.minOperations([1, 1, 1]))
print(sol.minOperations([1, 5, 2, 4, 1]))
