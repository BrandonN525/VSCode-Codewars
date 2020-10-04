import sys

def find_outlier(integers):
    
    #Declare both the counters and booleans we need for solution
    evenNum = 0
    oddNum = 0
    evenList = False
    oddList = False
    
    #For loop to decide whether the list is all odds or all evens
    for i in range (0, len(integers)):
        if integers[i] % 2 == 0:
            evenNum += 1
        else:
            oddNum += 1
            
        if evenNum >= 2:
            evenList = True
            break
        if oddNum >= 2:
            oddList = True
            break
    
    #If the list is all odds, find the even integer and return it
    if oddList == True:
        for i in range (0, len(integers)):
            if integers[i] % 2 == 0:
                return integers[i]
    
    #If the list is all evens, find the odd integer and return it
    if evenList == True:
        for i in range (0, len(integers)):
            if integers[i] % 2 != 0:
                return integers[i]
        
    return None