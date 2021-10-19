"""
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:
Input: arr = [3,1,3,6]
Output: false

Example 2:
Input: arr = [2,1,2,6]
Output: false

Example 3:
Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:
Input: arr = [1,2,4,16,8,4]
Output: false
"""
import collections

def canReorderDoubled(arr):
    d = collections.Counter(arr)
    
    for key in d.keys():
        if key == 0 and d[key]:
            if d[key] % 2:
                return False
            d[key] = 0
        else:
            num = key
            while num % 2 == 0 and num // 2 in d:
                num = num // 2
            while num in d:
                if d[num] > 0:
                    if d[num] > d[num + num]:
                        return False
                    d[num + num] -= d[num]
                    d[num] = 0
                num = num + num
    
    return sum(d.values()) == 0
