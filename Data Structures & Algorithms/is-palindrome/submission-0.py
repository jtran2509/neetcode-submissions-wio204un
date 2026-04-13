class Solution:
    def isPalindrome(self, s: str) -> bool:
       # Remove whitespace
       # Use 2 pointes: one - start, one - end
       # run at the same time: if s[i] = s[j] => return true 
       # otherwise - return False
       clean_s = "".join([char.lower() for char in s if char.isalnum()])
       i = 0
       j = len(clean_s) - 1
       while i < j:
        if clean_s[i] != clean_s[j]:
            return False
        i+=1
        j-=1
       return True