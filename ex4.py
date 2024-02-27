import random

numbers = []

results = []
for i in range(20):
  results.append(random.randint(1, 6))

for i in range(len(results)):
  if results[i] == 1:
    results[0] += 1
  elif results[i] == 2:
    results[1] += 1
  elif results[i] == 3:
    results[2] += 1
  elif results[i] == 4:
    results[3] += 1
  elif results[i] == 5:
    results[4] += 1
  elif results[i] == 6:
    results[5] += 1

print("1:", results[0])
print("2:", results[1])
print("3:", results[2])
print("4:", results[3])
print("5:", results[4])
print("6:", results[5])
    