import string
def generate_hashtag(s):
    #Capitalize the first letter in each word
    sNew = string.capwords(s)
    #Remove spaces in between words and add hashtag to string
    result = "#" + sNew.replace(" ", "")
    
    #If result is greater than 140 characters return false
    if len(result) > 140:
        return False
    #If either input or result is empty return false 
    if not s or not result:
        return False
    
    return result