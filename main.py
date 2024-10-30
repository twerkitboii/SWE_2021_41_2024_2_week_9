from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    raise ValueError('No solution to given problem')# SWE_2021_41_2024_2_week_9