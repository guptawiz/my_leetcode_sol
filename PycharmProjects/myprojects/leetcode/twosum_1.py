# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         i = 0
#         j = i + 1
#         while i < len(nums):
#             print("#")
#             print(i)
#             while j < len(nums-1):
#                 print("$")
#                 print(j)
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
#                 else:
#                     j = j+1
#             i = i + 1
#             j = i + 1
#         raise Exception("no match")
#
# if name == __Solution__:
#     twoSum([1,2,3], 3)

class Solution:
    def twosum(self, nums, target):
        match = {}
        for i,v in enumerate(nums):
            rem = target - v
            if rem in match:
                return [match[rem], i]
            match[v] = i
        return []


print(Solution().twosum([1,2,3], 4))