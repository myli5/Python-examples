"""    
Write a function to create subset of all elements in a list like
[a,b,c]=[(a),(b),(c),(a,b),(a,c),(b,c),(a,b,c)]
"""
# write a function to check whether a list contains a sublist
def subsetList(ls):
    s = ''.join(ls)  
    n = len(s);  
#For holding all the formed substrings  
    sublist = [];  
   
#This loop maintains the starting character  
    for i in range(0,n):  
        #This loop will add a character to start character one by one till the end is reached  
        for j in range(i,n):  
            sublist.append(tuple(s[i:(j+1)]));  
   
    return tuple(sublist)
           
subsetList(['a','b','c'])