class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Thinking process: traverse through the array -> store the character as key, 
        # the number of occurence as value ->if t has the same values-key=>true ELSE false

        # Easy, dirty way - might get banned ^^
        # return Counter(s)== Counter(t)

        # Official way
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i], 0)
            countT[t[i]] = 1+ countT.get(t[i], 0)

        return countS == countT
        