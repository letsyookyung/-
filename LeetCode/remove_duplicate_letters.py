class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        print(s)
        strset = set(s)
        stack, counter = [], collections.Counter(s)
        print(stack, counter)
        for char in s:
            counter[char] -= 1
            print(char, counter[char])
            if char in stack :
                print('-pass', char, stack)
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                print(char, stack[-1], counter[stack[-1]])
                stack.pop()
                print('-pop', stack)
            stack.append(char)
            
            print(stack,'\n')
            
        return ''.join(stack)
