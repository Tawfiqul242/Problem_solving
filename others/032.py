# Separate positive and negative numbers
list1 = [1, 2, -5, 12, -85, 0]
postive = []
negative = []
for num in list1:
    if num > 0:
        postive.append(num)
    elif num < 0:
        negative.append(num)
print(f"Positive numbers: {postive}")
print(f"Negative numbers: {negative}")