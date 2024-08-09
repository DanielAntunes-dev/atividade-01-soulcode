# 3.1

nome = input("Digite seu nome: ")
print(f"Bem vindo as curso de python, {nome}")

# 3.2
idade = int(input("Digite sua idade: "))
peso = float(input("Digite sua peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/ (altura*altura)

print(f"{nome}, seu índice de massa corporal é {imc:.2f}")