def is_isogram(string):
    
    # First turn the input string into all lowercase to disregard letter case
    string = string.lower()
    
    # Grab the length of the string
    length = len(string)
    
    # Create a list so that we can add all letters in and compare
    my_list = []
    
    # For list to do the comparison of letters
    for i in range (0, length):
        
        # If a letter in the string is already in the list the test fails
        if string[i] in my_list:
            return False
        
        # Otherwise add letter to list and continue comparing
        else:
            my_list.append(string[i])
    # If the test did not fail then all letters are different and the string is an isogram, hence it passes        
    return True