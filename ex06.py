# 6.1

amigos = ["Daniel", "Gabriel", "Caio", "Natalia", "Luciana"]
print(amigos[2])

# 6.2

amigos.append("Adriano")
print(f"Adionando mais um amigo, {amigos}")
amigos.pop(0)
print(f"Removendo o primeiro amigo, {amigos}")

# 6.3

idades = [ 40, 50, 15, 13, 12]
maisVelho = max(idades)
maisNovo = min(idades)
total = sum(idades)

print(f"O mais velho tem {maisVelho} anos")
print(f"O mais novo tem {maisNovo} anos")
print(f"A soma de todas as idade é {total} anos")