# Check whether two lists are equal
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

if len(list1) != len(list2):
    print("Not Equal")

else:
    equal = True
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            equal = False
            break

    if equal:
        print("Equal")
    else:
        print("Not Equal")