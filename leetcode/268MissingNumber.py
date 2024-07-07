class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_list = n*(n+1)/2
        res = 0
        for i in range(n):
            res += nums[i] 

        return  int(sum_of_list-res)

