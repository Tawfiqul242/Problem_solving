# Find pairs whose sum equals a target
sample = [2, 7, 11, 15]
target = 18

for i in range(len(sample)):
    for j in range(i+1, len(sample)):
        if sample[i]+sample[j] == target:
            print(sample[i], sample[j])
                