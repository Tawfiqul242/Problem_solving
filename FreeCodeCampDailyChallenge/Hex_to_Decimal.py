def hex_to_decimal(hex):
    result=0
    length = len(hex)
    for i in range(length):
        char = hex[i].upper()
        if '0' <= char <= '9':
            value = int(char)
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10

        result += int(value)* 16**(length - i -1)
        
    return result