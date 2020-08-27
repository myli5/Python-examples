"""
 Valid Paranthesis
Given a string of parenthesis characters [] {} <> (), 
find out if the string is valid. The string is valid 
if all the parentheses are paired up properly.
Time complexity: O(n)
Space complexity: stack and pair dictionary
"""
def validate(s):
    stack, pchar = [], {"(": ")", "{": "}", "[": "]", "<": ">"}
    for p in s:
        if p in pchar:
            stack.append(p)
        elif len(stack) == 0 or pchar[stack.pop()] != p:
            return False

    return len(stack) == 0

assert validate("())(())" ) == False
assert validate("())(()" ) == False
assert validate("<[]([<>]{})()>") == True
assert validate("<[>]") == False
assert validate("]<>[") == False