pesquisa = {}
satisfeitos = []
insatisfeitos = []

for x in range(2):
  nome = input(f"Digite o nome do participante {x+1}: ")
  
  while True:
    opiniao = input("Deixe sua opinião sobre o produto (satisfeito/insatisfeito)").strip().lower()
    if opiniao in ["satisfeito", "insatisfeito"]:
      break
    else:
      print("Opinião inválida, digite 'satisfeito' ou 'insatisfeito', Obrigado!")
  
  pesquisa[nome] = opiniao
  
  if opiniao == "satisfeito":
    satisfeitos.append(nome)
  else:
    insatisfeitos.append(nome)
    
totalSatisfeitos = len(satisfeitos)
totalInsatisfeitos = len(insatisfeitos)

print(pesquisa)
print(f"Total de participantes satisfeitos: {totalSatisfeitos}:  {" ,".join(satisfeitos)}")
print(f"Total de participantes satisfeitos: {totalInsatisfeitos}:  {" ,".join(insatisfeitos)}")