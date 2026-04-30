lista_alunos = []

# Registra um aluno com seu nome e duas notas.
# A média é calculada e o status inicial fica indefinido até a avaliação.
def cadastrar_aluno(nome, nota1, nota2):
    media = (nota1 + nota2) / 2

    aluno = {
        "nome": nome,
        "media": media,
        "status": "Indefinido"
    }

    lista_alunos.append(aluno)
    print("Aluno " + nome + " cadastrado com sucesso!")

# Percorre cada aluno para determinar se está aprovado ou reprovado.
# A decisão depende exclusivamente da média em relação ao valor de corte 7.
def verificar_aprovacao(lista):
    for aluno in lista:
        if aluno["media"] >= 7:
            aluno["status"] = "Aprovado"
        else:
            aluno["status"] = "Reprovado"

        # Mostra o resultado imediatamente após definir o status.
        print(f"O aluno {aluno['nome']} está {aluno['status']}")

print("--- Sistema de Notas ---")
cadastrar_aluno("João", 8, 7.5)
cadastrar_aluno("Maria", 9.0, 8.5)

verificar_aprovacao(lista_alunos)
print("Total de alunos processados: " + str(len(lista_alunos)))