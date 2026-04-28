lista_alunos = []

def cadastrar_aluno(nome, nota1, nota2)
    media = (nota1 + nota2) / 2
    
    aluno = {
        "nome": nome,
        "media": media
        "status": "Indefinido"
    }
    
    lista_alunos.append(aluno)
    print("Aluno " + nome + " cadastrado com sucesso!)

def verificar_aprovacao(lista):
    for aluno in lista:
        if aluno['media'] >= 7
        aluno['status'] = "Aprovado"
    else:
        aluno['status'] = "Reprovado"
        
        print(f"O aluno {aluno['nome']} está {aluno['Status']}")

print("--- Sistema de Notas ---")
cadastrar_aluno("João", "8", 7.5)
cadastrar_aluno(Maria, 9.0, 8.5)

verificar_aprovacao(lista_alunos)
print("Total de alunos processados: " + len(lista_alunos))