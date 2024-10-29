# write the function from exercise 1 here

# the lines below will test your function:

def square(num):
    return num ** num


print("2 squared is:", square(2))  # should be 4
print("16^2=", square(16))  # should be 256
print("256 to the 2nd power =", square(256))  # should be 65536


def square_print(num):
    print(num ** 2)
    return num ** 2


square_print(42)

a = square(10) + 10
b = square_print(10) + 10
