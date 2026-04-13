class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize 2 pointers: i: start, j: start +1
        # while j < len(numbers) -> sum= numbers[i] + numbers[j]
        # if sum == target -> return true -> else, j+=1

        # sorted array => target - num[i] = __ -> i+=1 
        result = 0
        i = 0
        j = len(numbers)-1
        while i < j:
            result = numbers[i] + numbers[j]
            if result > target:
                j-=1
            elif result < target: 
                i+=1
            else:
                return [i+1, j+1]
        return []
        

