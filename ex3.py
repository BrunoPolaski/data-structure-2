itemValue = float(input("Enter the necessary value: "))
currentValue = 0

while currentValue < itemValue:
    currentValue += float(input("Input the amount you want to spend: "))
    if currentValue < itemValue:
    	print("Necessary value to buy item:", itemValue - currentValue)

print("You have enough money to buy the item.")

if currentValue > itemValue:
	print("The amount is bigger than the item value. The change is: ", currentValue - itemValue)