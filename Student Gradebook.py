gradebook = {
    'Anusha': 560,
    'Bindu': 516,
    'Raksha': 506,
    'Umang': 496
}

name = input("Enter student name to get marks: ")

marks = gradebook.get(name)

if marks is not None:
    print(f"Marks of {name}: {marks}")
else:
    print(f"{name} not found in the gradebook.")
