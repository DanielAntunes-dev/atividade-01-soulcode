# 8.1
cliente = {
  "nome":"Daniel",
  "idade": 37,
  "peso": 110,
  "altura":1.88
}

print(cliente["nome"])

#8.2
cliente["email"] = "daniel@email.com"
print(cliente)

# 8.3
cliente.pop("peso")
print(f"Sem a chave peso {cliente}")

if "endereço" in cliente:
  print("A chave 'endereço' existe no dicionário")
else:
  print("A chave 'endereço' NÃO existe no dicionário'")

