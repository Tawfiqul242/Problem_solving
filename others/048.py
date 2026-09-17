# Create a dictionary from two lists
names = ["A", "B", "C"]
marks = [80, 90, 70]

dictionary = {}

for i in range(len(names)):
    dictionary[names[i]] = marks[i]

print(dictionary)

# dictionary = dict(zip(names, marks))
# print(dictionary)