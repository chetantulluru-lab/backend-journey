# Count digits in a number
num = int(input("Enter a number: "))
count = 0
for digit in str(num):
    count += 1
print("Number of digits =", count)
