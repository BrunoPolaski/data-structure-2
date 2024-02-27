number = int(input("Enter a number: "))
inputCount = 0
total = 0
while total <= 100:
    total += number
    inputCount += 1
    number = int(input("Enter a number: "))

print("Quantidade de números colocados:", inputCount)