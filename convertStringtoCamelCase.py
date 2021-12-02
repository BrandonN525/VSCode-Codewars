def to_camel_case(text):
    #Declare variables
    answer = ''
    nextchar = False
    #Iterate through input string
    for i in range (0, len(text)):
        #If character is a dash or underscore set nextchar to True
        if text[i] == '-' or text[i] == '_':
            nextchar = True
        #If character is not a dash or underscore and nextchar is False then add character to answer string    
        elif nextchar == False:
            answer += text[i]
        #If nextchar is False then add character in Uppercase to answer string
        else:
            answer += text[i].upper()
            nextchar = False
            
    return answer