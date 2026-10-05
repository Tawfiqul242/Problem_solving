# Find duplicate lines
with open("others/test_file.txt", "r") as f:
    lines = []
    for line in f:
        line = line.strip()
        
        if line not in lines:
            lines.append(line)
        else:
            print(f"line: {line}")