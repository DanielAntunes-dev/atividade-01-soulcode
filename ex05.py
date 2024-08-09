# 5.1
email = input("Digite seu email: ")

if email.find('@') != -1:
  print("Email válido")
else:
  print("Email inválido")
  
# 5.2

frase = input("Digite uma frase: ")
print(f"Frase que o úsuario escreveu: {frase}")
print(frase.upper())
print(frase.lower())
print(frase.title())
print("A frase começa com 'A': ", frase.startswith('A'))



