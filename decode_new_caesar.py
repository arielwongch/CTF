import string

ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")

encoded = "fegdeogdgecoeocgcgchcfcffccfca"

result = []

for key in ALPHABET:

    enc = ""

    for c in encoded:
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(key) - LOWERCASE_OFFSET
        enc += ALPHABET[(t1 - t2) % len(ALPHABET)]
    
    binary = ""
    half_string = ""

    for c in enc:
        val = ord(c)-LOWERCASE_OFFSET
        binary += f"{val:04b}"
    for i in range(0,len(binary),8):
        byte_string = binary[i:i+8]
        if len(byte_string) == 8:
            half_string += chr(int(byte_string,2))
    result.append(half_string)

for s in result:
    print(s)


