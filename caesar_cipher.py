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
# -- ord() returns the unicode from a given char
# -- chr() returns the character that respresents the specified code
def encrypt_letter(letter, shift):
  cipher = ord(letter) + shift                                  # x + n                                
  return chr(cipher)
    
# function to substract a shift to a letter (backwords)
def decrypt_letter(letter, shift):
  cipher = ord(letter) - shift
  return chr(cipher)

# function to encrypt words using a shift
def encrypt_word(word):
  en_letters = []
  
  for letter in word:
    cipher = encrypt_letter(letter)
    en_letters.append(cipher)
    
  return en_letters
  
  
# function to decrypt words using a shift 

# function to encrypt messages using a shift
# function to decrypt messages using a shift 


# --- TEST CASES ---

# shift by 0 or 26 --> yields the same letter result 
print(encrypt_letter('a', 0))
write_file('enChar', encrypt_letter('a', 0))






