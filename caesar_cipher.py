# Tam Nguyen
# Caesar Cipher Project

"""
encryption and decryption modeled using this formula:
  En(c) = (x + n) mode 26
where x is orginal letter val, n = shift #, mode 26 = resets wheel after 26th letter (end)
Note: shift of 0 or 26 is the same as no encryption 
"""

# function that writes files 
def write_file(filename, data):
    new_file = open(filename, "w")
    for sentence in data:
        for word in sentence:
            new_file.write(word + " ")
        new_file.write("\n")
    new_file.close()


# function to add a shift to a letter (forwards)
# function to substract a shift to a letter (backwords)

# function to encrypt words using a shift
# function to decrypt words using a shift 

# function to encrypt messages using a shift
# function to decrypt messages using a shift 

