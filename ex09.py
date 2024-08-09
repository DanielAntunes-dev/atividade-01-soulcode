# 9.1

idade = int(input("Digite sua idade: "))

if(idade < 18):
    print("Menor de idade")
elif (idade >= 18 and idade < 65):
    print('Adulto')
elif(idade >= 65 and idade <= 130):
    print("Idoso")
else:
    print("Idade inválida!")
    

# 9.2

nota = int(input("Digite uma nota: ")) 

if (nota <= 100 and nota >= 60):
  print("Aprovado!")
elif (nota >= 0 and nota < 60):
  print("Reprovado!")
else:
  print("Nota inválida!")
  

# 9.3

cidades = ["RJ", "ES", "SP", "MG", "AM"]

for x in cidades:
  print(f"Cidade do: {x}")
  
# 9.4

numeros = list(range(1, 11))
print(numeros)

for x in numeros:
  quadrado = x ** 2
  print(f"Quadrado de {x} é {quadrado}")