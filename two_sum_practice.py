class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        h = {}
        
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
        


nums = [4, 8, 11, 45, 2, 1]
target = 9

out = Solution().twoSum(nums, target)
print(out)
