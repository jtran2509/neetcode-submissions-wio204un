class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # traverse through the array
        # store the character as key, the number of occurence as value
        # if t has the same values-key => true ELSE false
        # if len(s) != len(t):
        #     return False
        # countS, countT = {}, {}
        return Counter(s)== Counter(t)