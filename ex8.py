# 8. Escreva um programa que solicita ao usuário um número e verifica se ele  é um número perfeito. Um número perfeito é aquele cuja soma de seus  divisores (excluindo ele mesmo) é igual ao próprio número. Exemplo: 28  é um número perfeito (1 + 2 + 4 + 7 + 14 = 28).

number = int(input("Enter a number: "))
sum = 0
for i in range(1, number):
    if number % i == 0:
        sum += i
if sum == number:
    print("It's a perfect number")
else:
    print("It's not a perfect number")