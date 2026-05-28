class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            while s[l].isalnum() != True and l < r:
                l = l + 1
            while s[r].isalnum() != True and l < r:
                r = r - 1

            if s[l].lower() != s[r].lower():
                return False
        
            l = l + 1
            r = r - 1
        return True

