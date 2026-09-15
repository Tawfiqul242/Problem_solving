# Check whether a key exists
dictionary = {"first":1, "second":2, "third":3, "fourth":4}
# for key in dictionary.keys():
#     if key == "second":
#         k = 1
#         break
#     else: k = 0

# if k == 1:  
#     print("Key exists")
# else:
#     print("Key does not exists")


if "second" in dictionary:
    print("Key exists")
else:
    print("Key does not exists")