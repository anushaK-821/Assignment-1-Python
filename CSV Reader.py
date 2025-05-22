
print(f'Sudents scoring above 75: ')
with open('students.csv') as  file:
    next(file)
    for i in file:
        name,marks = i.strip().split(',')
        if float(marks) > 75:
            print(name)
