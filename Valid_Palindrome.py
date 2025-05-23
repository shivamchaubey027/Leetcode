class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean == clean[::-1]


##Slicing works with Strings I see we just had to remove stuff from it, accha we learnt the methods and the string comprehension in this tho, so worth it
