# 1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

# SOLUTION 1:

```python 3.0
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums)-1):
            for y in range (x+1, len(nums)):
                if (nums[x] + nums[y] == target):
                    return (x,y)
```
# SOLUTION 2:
More optimised

```python 3.0
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = nums.copy()
        new_nums.sort()
        i = 0
        j = len(nums)-1

        while (i < j):
            if (new_nums[i] + new_nums[j] == target):
                if (new_nums[i] == new_nums[j]):
                    return[nums.index(new_nums[i]), nums.index(new_nums[j],nums.index(new_nums[i])+1)]
                else:
                    return[nums.index(new_nums[i]), nums.index(new_nums[j])]
            elif (new_nums[i] + new_nums[j] < target):
                i += 1
            else:
                j -= 1
```                
