expenses = {}

def add_expense(day, amount):
    if day in expenses:
        expenses[day] += amount
    else:
        expenses[day] = amount

while True:
    day = input("Enter the day of the week ('done' to finish): ").capitalize()
    if day.lower() == 'done':
        break
    try:
        amount = float(input(f"Enter the amount spent on {day}: "))
        add_expense(day, amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")

def weekly_summary():
    print("\nWeekly Summary:")
    for day, total in expenses.items():
        print(f"{day}: ${total:.2f}")

weekly_summary()
