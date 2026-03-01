import string

def CipherDecode(decoded_msg):

    letters = list(string.ascii_letters)

    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)

    result = []
    temp = ""

    for i in range(26):

        temp = ""

        for char in decoded_msg:

            #not a letter then skip
            if char not in letters:
                temp += char
                continue

            ascii_dec = ord(char)+i

            if char in lowercase:

                if ascii_dec <= ord('z'):
                    letter = chr(ascii_dec)
                else:
                    letter = chr(ascii_dec-26)
                temp += letter

            elif char in uppercase: 

                if ascii_dec <= ord('Z'):
                    letter = chr(ascii_dec)
                else:
                    letter = chr(ascii_dec-26)
                temp += letter

            else:
                
                print("BUGGGGGGGG!!!!!")

        result.append(temp)

    return result

encoded = input("What is the encoded msg?")
decoded = CipherDecode(encoded)
for s in decoded:
    print(s)
