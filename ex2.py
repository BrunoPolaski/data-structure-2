sum = 0
avg = 0
numbers = []

number = int(input("Enter a number: "))
while number >= 0:
  numbers.append(number)
  sum += number
  avg += 1
  number = int(input("Enter a number: "))

print("Sum:", sum)
print("Average:", sum / len(numbers))