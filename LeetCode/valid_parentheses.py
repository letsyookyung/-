class Solution:
    def isValid(self, s: str) -> bool:
        
        s_list = list(s)
        brackets = { ')':'(',
                      '}':'{', 
                      ']':'['}
        opening = [s for s in s_list if s in brackets.values()]   
        closing = [s for s in s_list if s in brackets.keys()]
        # print(opening)
        # print(closing)
        # print("")
        
        stack =[]
        for s in s_list[:] :
            if s in opening :
                print('#opening:',s)
                stack.append(s)
            if s in closing: 
                print('#closing:',s)
                if not stack:
                    return False
                elif stack.pop() != brackets[s] :
                    return False
                else :
                    continue
                    
        if not stack:
            return True
        else :
            return False
