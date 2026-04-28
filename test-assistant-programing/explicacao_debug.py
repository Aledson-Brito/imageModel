# EXPLICAÇÃO DOS ERROS ENCONTRADOS NO ARQUIVO debug.py

"""
Este arquivo documenta todos os erros sintáticos e lógicos encontrados
no arquivo debug.py e suas correções.
"""

# ============================================================================
# ERRO 1 - LINHA 1: Falta dois-pontos (:) após a definição da função
# ============================================================================
# ❌ ERRADO:
# def cadastrar_aluno(nome, nota1, nota2)

# ✅ CORRETO:
# def cadastrar_aluno(nome, nota1, nota2):
# Explicação: Toda definição de função em Python precisa terminar com ":"

# ============================================================================
# ERRO 2 - LINHA 7: Falta vírgula após "media": media
# ============================================================================
# ❌ ERRADO:
# aluno = {
#     "nome": nome,
#     "media": media
#     "status": "Indefinido"
# }

# ✅ CORRETO:
# aluno = {
#     "nome": nome,
#     "media": media,    # <- vírgula adicionada
#     "status": "Indefinido"
# }
# Explicação: Pares chave-valor em dicionários devem ser separados por vírgula

# ============================================================================
# ERRO 3 - LINHA 12: Falta aspas de fechamento na string
# ============================================================================
# ❌ ERRADO:
# print("Aluno " + nome + " cadastrado com sucesso!)

# ✅ CORRETO:
# print("Aluno " + nome + " cadastrado com sucesso!")
# Explicação: Todas as strings devem ter aspas de abertura E fechamento

# ============================================================================
# ERRO 4 - LINHA 15: Falta dois-pontos (:) após a condição if
# ============================================================================
# ❌ ERRADO:
# if aluno['media'] >= 7

# ✅ CORRETO:
# if aluno['media'] >= 7:
# Explicação: Estruturas de controle (if, else, for, etc) precisam de ":" no final

# ============================================================================
# ERRO 5 e 6 - LINHA 16-17: Indentação incorreta com else mal posicionado
# ============================================================================
# ❌ ERRADO:
# if aluno['media'] >= 7
#     aluno['status'] = "Aprovado"
# else:
#     aluno['status'] = "Reprovado"

# ✅ CORRETO:
# if aluno['media'] >= 7:
#     aluno['status'] = "Aprovado"
# else:
#     aluno['status'] = "Reprovado"
# Explicação: O else está fora do loop. Deveria estar dentro do loop for
# A estrutura correta seria:
# for aluno in lista:
#     if aluno['media'] >= 7:
#         aluno['status'] = "Aprovado"
#     else:
#         aluno['status'] = "Reprovado"

# ============================================================================
# ERRO 7 - LINHA 20: Chave incorreta no dicionário (case-sensitive)
# ============================================================================
# ❌ ERRADO:
# print(f"O aluno {aluno['Status']}")

# ✅ CORRETO:
# print(f"O aluno {aluno['nome']} está {aluno['status']}")
# Explicação: Python diferencia maiúsculas de minúsculas. A chave é 'status'
# (minúscula), não 'Status' (maiúscula). Isso causa KeyError.

# ============================================================================
# ERRO 8 - LINHA 24: Nota como string em vez de número
# ============================================================================
# ❌ ERRADO:
# cadastrar_aluno("João", "8", 7.5)

# ✅ CORRETO:
# cadastrar_aluno("João", 8, 7.5)
# Explicação: Notas devem ser números (int ou float), não strings.
# Strings não podem ser usadas em operações matemáticas como divisão.

# ============================================================================
# ERRO 9 - LINHA 25: Nome sem aspas (não é uma string)
# ============================================================================
# ❌ ERRADO:
# cadastrar_aluno(Maria, 9.0, 8.5)

# ✅ CORRETO:
# cadastrar_aluno("Maria", 9.0, 8.5)
# Explicação: "Maria" deve ser uma string (entre aspas). Sem aspas, Python
# tenta buscar uma variável chamada Maria, que não existe.

# ============================================================================
# ERRO 10 - LINHA 27: Concatenação de string com inteiro
# ============================================================================
# ❌ ERRADO:
# print("Total de alunos processados: " + len(lista_alunos))

# ✅ CORRETO (opção 1 - conversão):
# print("Total de alunos processados: " + str(len(lista_alunos)))

# ✅ CORRETO (opção 2 - f-string):
# print(f"Total de alunos processados: {len(lista_alunos)}")

# ✅ CORRETO (opção 3 - vírgula):
# print("Total de alunos processados:", len(lista_alunos))
# Explicação: Não é possível concatenar strings com números usando +.
# É necessário converter para string ou usar f-strings/vírgulas.

# ============================================================================
# RESUMO DOS ERROS:
# ============================================================================
# 1. Falta de dois-pontos em definições de função e estruturas
# 2. Falta de vírgulas em dicionários
# 3. Falta de aspas de fechamento em strings
# 4. Case-sensitive: 'status' ≠ 'Status'
# 5. Tipos de dados incorretos (strings vs números)
# 6. Variáveis indefinidas (nomes sem aspas)
# 7. Operações com tipos incompatíveis (string + int)
# 8. Problemas de indentação e estrutura lógica
