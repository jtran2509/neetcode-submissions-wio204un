class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Initialize a hash map
    # Iterate through the array and keeping track of the times each number occurs
    # .values() => max
    # append them to the result
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
