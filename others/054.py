# Replace negative numbers with 0
sample = [-11, -45, 3, 7]

result = [0 if i<0 else i for i in sample]

print(result)