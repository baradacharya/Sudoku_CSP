#https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/solution/
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        W = []  # array of sums of windows
        sum_ = 0

        # sum of each windows
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K:
                sum_ -= nums[i - K]
            if i >= K - 1:
                W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):  # max sum from left upto that index
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):  # max sum from right after this index
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        max_sum = 0
        #i,j,k staring index of substring with K length
        for j in xrange(K, len(W) - K):  # find middle j so that both and right will max
            i, k = left[j - K], right[j + K]
            if ans is None or (W[i] + W[j] + W[k] > max_sum):
                ans = i, j, k
                max_sum = W[ans[0]] + W[ans[1]] + W[ans[2]]
        return ans

s = Solution()
print s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)