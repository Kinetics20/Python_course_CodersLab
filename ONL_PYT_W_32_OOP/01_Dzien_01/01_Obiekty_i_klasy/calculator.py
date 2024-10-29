class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f'Added {num1} and {num2} got {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f'Multiplied {num1} and {num2} got {result}')
        return result

    def print_operations(self):
        for i, entry in enumerate(self.history):
            print(f'{i}. {entry}')


calc1 = Calculator()
calc2 = Calculator()
calc3 = Calculator()

print(calc1.add(1, 2))
print(calc1.multiply(3, 7))
print(calc1.add(11, 17))
print(calc2.add(4, 6))
print(calc2.multiply(40, 20))
print(calc2.add(8, 8))
print(calc3.add(9, 6))
print(calc3.multiply(12, 18))
print(calc3.add(6, 6))
print(calc1.multiply(19, 23))

print('Historia kalkulatora 1:')
calc1.print_operations()
print()
print('Historia kalkulatora 2:')
calc2.print_operations()
print()
print('Historia kalkulatora 3:')
calc3.print_operations()