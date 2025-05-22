import ast

def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

user_input = input("Enter a nested list (e.g., [1, [2, 3], [4, [5, 6]]]): ")

try:
    nested_list = ast.literal_eval(user_input)
    if isinstance(nested_list, list):
        flat = flatten_list(nested_list)
        print("Flattened list:", flat)
    else:
        print("Please enter a valid list.")
except Exception as e:
    print("Invalid input.")
