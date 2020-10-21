def reverseWords(s):
    ans = ""
    #Split string into array of words
    strSpl = s.split()
    #Iterate through array of words
    for i in range (0, len(strSpl)):
        if i < len(strSpl) - 1:
            #Add the word of last index - i - 1 to array plus a space
            ans += strSpl[len(strSpl) - i - 1] + " "
        else:
            #At the end of the iteration (beginning of array) add word without a space
            ans += strSpl[len(strSpl) - i - 1]
    return ans