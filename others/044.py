# Find key with maximum value
marks = {
    "Rahim": 80,
    "Karim": 90,
    "Hasan": 85,
    "Abid": 95
}
key = None
maximum = 0
for name, mark in marks.items():
    if maximum < mark:
        maximum = mark
        key = name
print(key)