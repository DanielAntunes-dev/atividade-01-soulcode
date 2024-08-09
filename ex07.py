# 7.1

tuplaCliente = ("Daniel", 37, 110, 1.90,)
nome, idade, peso, altura = tuplaCliente

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}kg")
print(f"Altura: {altura:.2f}m")


# 7.2

email = "daniel@email.com"

novaTuplaCliente = tuplaCliente + (email,)
n, i, p, a, e = novaTuplaCliente

print('_______________________________')
print(f"Nome: {n}")
print(f"Idade: {i}")
print(f"Peso: {p}kg")
print(f"Altura: {a:.2f}m")
print(f"Email: {e}")




