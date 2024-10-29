#!/user/bin/python3

numbers = []
n = int(input("Enter n: "))

for k in range(n):
    num = int(input("Enter a number : "))
    numbers.append(num)
new_list = []
for element in numbers:
    new_list.append(str(element))
# print("Entered numbers: {}".format(" ".join(new_list)))
print(f"Entered numbers: {' '.join(new_list)}")
# print(f"Entered numbers: {numbers}")
sum_1 = sum(numbers)
print(f"Sum: {sum_1},")
average_1 = float(sum_1 / len(numbers))
print(f"average: {average_1}")

if sum_1 > average_1:
    print("The sum is greater!")
if sum_1 < average_1:
    print("The average is greater!")
