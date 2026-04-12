class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Store each number in a hash map, maybe sort the array first 
    # needs to return the pair with smaller -> bigger number
    # use the target - that number to find the other number
    # if that number exist in the array -> return the indexs' pair
        prev_sum = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prev_sum:
                return [prev_sum[diff], idx]
            prev_sum[val] = idx
