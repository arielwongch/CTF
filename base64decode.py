def Base64Decode(encoded_msg):

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    map = {char: index for index, char in enumerate(base64_chars)}

    result = ""
    binary = ""

    num_of_padding = 0

    for char in encoded_msg:

        if char == '=':
            num_of_padding += 1
            continue
        elif char in map.keys():
            binary += f"{map[char]:06b}"
        else:
            continue
    
    num_of_padding = num_of_padding % 3
    
    padding = num_of_padding * 2

    for i in range(0, len(binary)-padding, 8):

        byte_str = binary[i:i+8]

        letter = chr(int(byte_str,2))

        result += letter

    return result


encoded = input("What is the encoded msg?")
decoded = Base64Decode(encoded)
print(decoded)

