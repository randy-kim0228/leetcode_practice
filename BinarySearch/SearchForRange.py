"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109
* nums is a non-decreasing array.
* -109 <= target <= 109
"""

from typing import List


def searchRange(nums: List, target: int) -> List[int]:
    # edge case if given nums is an empty array
    if not nums: return [-1, -1]
    # finding the last one
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    end = left - 1

    if end == -1 or nums[end] != target: return [-1, -1]
    # finding the first one
    left, right = 0, end
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    start = left

    return [start, end]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 7, 8]
    target = 6
    print(searchRange(nums, target))