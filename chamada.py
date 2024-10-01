# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

presentes = []

while True:
    nomes = input("digite o nomes dos alunos presentes (digite 1 para encerrar a lista): ")
    if nomes == "1":
        break
    presentes.append(nomes)

print(f"alunos presentes: {len(presentes)}")
print(f"lista de alunos presentes: {presentes}")

print("revistar lista de chamadas" if len(presentes) < 5 else "alunos nescessarios")
