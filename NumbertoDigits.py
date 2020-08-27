"""
Write a function that takes a number and 
returns a list of its digits
Time complexity: O(n) 
Space complexity: O(n)
- Here n is the number of digits 
"""
def digits(input):
    output=[]
    if (input > 0):
        while (input > 0):
            output.append(input%10)
            input = input // 10
    output.reverse()
    return output

assert digits(123) == [1,2,3]
assert digits(400) == [4,0,0]

#solution - 2
def digits(a):
    c =[]
    if a>0:
        b = str(a)    
        for digit in b:
            c.append(int(digit))
            
    return c
    
#solution-3		
from collections import deque
def digits(num):
    if num > 0:
        digits = deque()
        while True:
            num,r = divmod(num,10)
            digits.appendleft(r)
            if num == 0:
                break
        return list(digits)
    else:
        return []

print(digits(123))
#assert digits(123) == [1,2,3]
#assert digits(400) == [4,0,0]
#assert digits(-10) == []