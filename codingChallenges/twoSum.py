from typing import List
import time


# 2.5987625122070312e-05
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 1.71661376953125e-05
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n log n)
        sortedList = sorted(nums)

        lIndex, rIndex = 0, len(sortedList)-1

        # O(n)
        while lIndex != rIndex:
            sum = sortedList[lIndex] + sortedList[rIndex]
            if sum == target:
                l = nums.index(sortedList[lIndex])
                r = len(nums) - 1 - nums[::-1].index(sortedList[rIndex])
                if l < r:
                    return [l, r]
                else:
                    return [r, l]
            elif sum > target:
                rIndex -= 1
            else:
                lIndex += 1

        return None


# 1.2159347534179688e-05
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        distanceToIndex = {}
        for idx, n in enumerate(nums):
            if n in distanceToIndex:
                return [distanceToIndex[n], idx]
            distanceToIndex[target - n] = idx

        return None


start = time.time()
s = Solution3()
assert(s.twoSum([2, 7, 11, 15], 9) == [0, 1])
assert(s.twoSum([2, 11, 15, 32, 0, 1], 16) == [2, 5])
assert(s.twoSum([1, 8], 9) == [0, 1])
assert(s.twoSum([1, 8, 19], 16) == None)
assert(s.twoSum([43, 12, 65, 87, 33, 65, 43, 11, 76, 88, 99,
                 88, 99, 87, 12, 34, 12, 43, 1002], 1013) == [7, 18])
assert(s.twoSum([3, 3], 6) == [0, 1])
end = time.time()
print(end - start)
