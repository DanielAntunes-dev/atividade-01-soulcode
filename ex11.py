nomes = []
notas = []

for x in range(5):
    
  nome = input(f"Digite o nome do aluno {x+1}: ")
  nota = float(input(f"Digite a nota do aluno(0-100) {x+1}: "))
  
  nomes.append(nome)
  notas.append(nota)
  
for a in range(5):
  if notas[a] <= 100 and notas[a] >= 60:
    print(f"O aluno {nomes[a]} tirou nota {notas[a]}, com isso está aprovado!")
  elif notas[a] >= 0 and notas[a] < 60:
    print(f"O aluno {nomes[a]} tirou nota {notas[a]}, com isso está reprovado!")
  else:
   print(f"Aluno {nomes[a]}, Nota inválida!")

