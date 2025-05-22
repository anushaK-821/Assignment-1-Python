with open('file.txt','r') as f:
    lines = f.readlines()

words=0
chars=0
line_count=len(lines)

for i in lines:
    chars += len(i)
    words += len(i.split())

print("Total Lines:", line_count)
print("Total Words:", words)
print("Total Characters:", chars)

              
