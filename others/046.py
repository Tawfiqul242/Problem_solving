# Sort dictionary by value

students = {
    "Rahim": 75,
    "Karim": 92,
    "Hasan": 68,
    "Nadia": 85,
    "Sadia": 78
}
sorted_list = dict(sorted(students.items(), key = lambda item: item[1]))
print(sorted_list)