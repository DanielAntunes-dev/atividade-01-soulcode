
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua alwtura: "))


while True:
  email = input("Digte seu email: ")
  if '@' in email:
    break
  else:
    print("Email inválido!")


imc = peso / (altura * altura)

cliente = {
  "Nome": nome,
  "Idade": idade,
  "Peso": peso,
  "Altura": altura,
  "E-mail": email,
  "IMC": round(imc, 2)
}

for chave, valor in cliente.items():
  print(f"{chave}: {valor}")