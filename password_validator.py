# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==
    #def function call is_valid
    #Check if the password is longer than or equal to 8 characters
    #test function so far 
    #create a speclist of characters "!", "@", "$", "%", "&"
    #check too see if speclist is in password
    #create relvent if statements
    #call the function through a variable and pass argument
def is_valid(password):
    if len(password) < 8:
        return False
    spec_list = ["!", "@", "$", "%", "&"]
    spec_list_true = any(char in spec_list for char in password)
    if spec_list_true:
        return True
    else:
        return False 
result = is_valid("Elephant!")
print(result)





























