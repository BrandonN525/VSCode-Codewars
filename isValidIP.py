def is_valid_IP(string):
    str = string.split(".")
    for i in range (0, len(str)):
        if len(str) != 4:
            return False
        elif not str[i]:
            return False
        elif not str[i].isnumeric():
            return False
        elif int(str[i]) > 255:
            return False
        elif str[i].startswith("0") and len(str[i]) > 1:
            return False
    return True