"""
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

"""

import collections

def findOriginalArray(changed):
    d = collections.Counter(changed)
    original = []
    for key in d.keys():
        if key == 0:
            if d[key] % 2 == 1:
                return []
            original += [0] * (d[key] // 2)
            d[key] = 0
        else:
            num = key
            while num % 2 == 0 and num // 2 in d:
                num = num // 2
            while num in d:
                if d[num] > 0:
                    if d[num] > d[num + num]:
                        return []
                    original += [num] * d[num]
                    d[num + num] -= d[num]
                    d[num] = 0
                num = num + num
    return original
