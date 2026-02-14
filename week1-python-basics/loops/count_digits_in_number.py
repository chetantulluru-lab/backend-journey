# count_digits_in_number.py

n = int(input("Enter a number: "))
count = 0

for digit in str(n):   # convert number to string and loop through each character
    count += 1

print("Number of digits:", count)
