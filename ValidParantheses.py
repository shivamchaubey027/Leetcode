class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closure = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in closure:             
                if stack and stack[-1] == closure[i]:
                    stack.pop()
                else:
                    return False 
            else:               
                stack.append(i)
        return not stack

##Stacks mein if we have nested loops ya we have to do these open close and such things,w e have the best solution with stacks, also in this prblm we just go on to add stuff to the hashmap 
