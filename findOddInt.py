def find_it(seq):
    #Get length of array
    length = len(seq)
    #Sort array
    seq.sort()
    #Initialize counter
    counter = 0
    #Nested for loop to compare numbers in the list
    for i in range (0, length):
        for j in range (0, length):
            if seq[i] == seq[j]:
                #Increment counter
                counter += 1
        #Return number if it is listed an odd number of times
        if counter % 2 != 0:
            return seq[i] 
    counter = 0