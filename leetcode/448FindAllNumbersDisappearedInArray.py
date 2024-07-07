class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        numSet = set(nums)
        resList = []
        for i in range(1,len(nums)+1):
            if i not in numSet:
                resList.append(i)

        return resList

