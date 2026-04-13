class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # sorted_nums = sorted(list(set(nums))) # sort the array in non-decreasing order
        # res = 0 #longest streak
        # curr = sorted_nums[0] # first number
        # streak = 0
        # i = 0 # index

        # while i < len(sorted_nums):
        #     if sorted_nums[i] != curr:
        #         curr = sorted_nums[i]
        #         streak = 0
            
        #     while i < len(sorted_nums) and sorted_nums[i] == curr:
        #         i+=1
        #     streak+=1 
        #     curr+=1
        #     res = max(res, streak)
        # return res

        longest = 0
        num_set = set(nums)
        for num in nums:
            # Check if it's a start
            if (num -1) not in num_set:
                length = 0
                while (num+ length) in num_set:
                    length +=1
                longest = max(length, longest)
        return longest
        


