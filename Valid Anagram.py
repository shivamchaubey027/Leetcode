class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False;
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
            
        return True

        
        


## The count function does is it checks the appearance of a character for eg in s.count(i) toh a:2 t.count(i) a:2 so it is not false and comes out and is true now 
