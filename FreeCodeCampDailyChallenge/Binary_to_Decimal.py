def to_decimal(binary):
    #  result=0
    #  length = len(binary)
    #  for i in range(length):
    #       result += int(binary[i])* 2**(length - i -1)
    #  return result
    return int(binary, base=2)