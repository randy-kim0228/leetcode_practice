"""
Given an array of integers num and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
    Input: nums = [1, 1, 1], k = 2
    Output: 2 
    Explanation: [1, 1] (index 0 & 1) and [1, 1] (index 1 & 2)

Example 2:
    Input: nums[1, 2, 3], k = 3
    Output: 2
    Explanation: [1, 2], [3]

1) Brute Force: Get all possible subarrays of the array in O(N^2) and get each subarray's sum O(N) 
    TC: O(N^3)
    SC: O(1)

2) Prefix sum table: build table then use nested loop to find the prefixSum of right pointer subtracts prefixSum of left pointer equal to k
    TC: O(N^2)
    SC: O(N)

3) Use prefix sum & hash table: keep the cumulative sum and find if cumulativeSum - k exists in the hash table
    If exists, count = count + hashTable[cumulativeSum - k]
    TC: O(N)
    SC: O(N)
"""

# approach 2
def usePrefixTable(nums, k):
    count = 0
    sums = [0] * (len(nums) + 1) # to account for the fist prefix sum equals k
    
    for i in range(1, len(nums) + 1):
        sums[i] = sums[i - 1] + nums[i - 1]
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if sums[j] - sums[i] == k:
                count += 1

    print(count)
    
    return count

# approach 3
def useHashTable(nums, k):
    count = 0
    d = {0: 1} # to account for the first prefix sum equals k
    prefix_sums = 0
    
    for num in nums:
        prefix_sums += num
        if prefix_sums - k in d:
            count += d[prefix_sums - k]
        d[prefix_sums] = d.get(prefix_sums, 0) + 1
        
    return count
