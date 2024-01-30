class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if ((nums[i] + nums[j]) == target):
                    return [i, j]
        return [-1 , -1]
        """
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [i, numMap[complement]]
            numMap[nums[i]] = i
        return [-1, -1]