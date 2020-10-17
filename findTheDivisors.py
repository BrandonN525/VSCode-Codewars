def divisors(integer):
    finArray = []
    
    #Iterate through list of numbers between 2 and integer less 1
    #We don't need to check 1 or integer because they will always be divisors
    for i in range (2, integer - 1):
        #If i is a divisor add it to the array
        if integer % i == 0:
            finArray.append(i)
            
    #If finArray is empty, return integer is prime
    if not finArray:
        return str(integer) + " is prime"
    #Else return finArray
    else: 
        return finArray