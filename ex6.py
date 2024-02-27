vogals = ['a', 'e', 'i', 'o', 'u']

vogalsCount = 0

word = input("Enter a word: ")
for i in range(len(word)):
    if word[i] in vogals:
        vogalsCount += 1

print("Number of vogals:", vogalsCount)