# 7.1

cliente = ("Daniel", 37, 110, 1.90,)
nome, idade, peso, altura = cliente

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}kg")
print(f"Altura: {altura:.2f}m")


# 7.2

email = "daniel@email.com"

addEmailCliente = cliente + (email,)
n, i, p, a, e = addEmailCliente

print('_______________________________')
print(f"Nome: {n}")
print(f"Idade: {i}")
print(f"Peso: {p}kg")
print(f"Altura: {a:.2f}m")
print(f"Email: {e}")




