def CodelandUsernameValidation(strParam):
    if len(strParam) >= 4 and len(strParam) <= 25:  # check for length
        if strParam[0].isalpha():    # check for character
            if strParam.replace("_", "").isalnum(): # can only contain letters, numbers, and underscore
                if strParam[-1] != '_':  # cannot end with an underscore
                    return True
                
    return False
# keep this function call here 
print(CodelandUsernameValidation("aa_123"))


# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.


