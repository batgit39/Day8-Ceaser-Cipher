from art import logo
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(f_text , f_shift, f_direction):
    text = "" 
    if (f_direction == "decode"):
        f_shift *= -1
        

    for letters in f_text:  
        if ( ord(letters) + f_shift ) > 122:
            letters = chr( ord(letters) - 26)

        elif ( ord(letters) + f_shift ) < 97:
            letters = chr( ord(letters) + 26) 

        text += chr( ord(letters) + f_shift)
        
    print("The " + f_direction +  "d text is " + text)

end_game = True

while end_game:    
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt your text :\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #to counter numbers bigger than 26
    if shift > 26:
        shift %= 26

    ceaser(text, shift, direction)

    restart = input("Type 'yes' to restart or any button to end the session - ")

    if restart != "yes":
        end_game = False

#old code changed for proficiency :)
#def encrypt(f_text, f_shift):
#    encrypted_text = "" 
#    for letters in f_text:  
#        #conversion by ascii a = 97, z = 122
#        if ( ord(letters) + f_shift ) > 122:
 #           letters = chr( ord(letters) - 26)
#        encrypted_text += chr( ord(letters) + f_shift)
#    print("The encoded text is " + encrypted_text)

#def decrypt(f_text, f_shift):
#    decrypted_text = "" 
#    for letters in f_text:  
#        if ( ord(letters) - f_shift ) < 97:
#            letters = chr( ord(letters) + 26) 
#        decrypted_text += chr( ord(letters) - f_shift)     
#    print("The decoded text is " + decrypted_text)

#if (direction == "encode"): 
#    text = input("Type your message:\n").lower()
#    shift = int(input("Type the shift number:\n"))
#    encrypt(text, shift)

#elif (direction == "decode"): 
#    text = input("Type your message:\n").lower()
#    shift = int(input("Type the shift number:\n"))
#    decrypt(text, shift)

#else:
#    print("Wrong input try again!")
