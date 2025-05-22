a = int(input("Enter the start number: "))
b = int(input("Enter the end number: "))

def prime(x, y):
    for i in range(x, y + 1):
        if i > 1:  # primes are greater than 1
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                print(i, end=' ')

print("Prime numbers between", a, "and", b, "are:")
prime(a, b)
