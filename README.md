# Projeto Site e Scripts Python

Este projeto contém uma página web estática e um conjunto de scripts Python didáticos para validação de números primos, refatoração de estatísticas e correção de um sistema simples de notas.

## Estrutura do Projeto

- `index.html` - Página principal do site com interface estática em HTML/CSS e Bootstrap.
- `test-assistant-programing/` - Pasta com exemplos de scripts Python e explicações.
  - `debug.py` - Script para cadastro de alunos, cálculo de média e verificação de aprovação.
  - `num_primo.py` - Verificação de números primos com entrada do usuário e suíte de testes.
  - `refatoracao.py` - Cálculo de estatísticas (soma, média, maior e menor) a partir de uma lista de valores.
  - `explicacao_debug.py` - Documento explicando erros e correções do arquivo `debug.py`.
  - `explicacao_num_primo.md` - Documento explicando a lógica linha a linha do arquivo `num_primo.py`.
  - `explicacao_refatoracao.md` - (se presente) documento explicando o raciocínio do arquivo `refatoracao.py`.

## Visão Geral dos Componentes

### `index.html`

A página web é um protótipo visual com estilo moderno usando Bootstrap e CSS personalizado. Ela contém:
- layout responsivo
- seção para exibição de vídeo/câmera
- botões e elementos de status
- área de previsões estilizada

### `test-assistant-programing/debug.py`

Funcionalidade:
- cadastramento de alunos em uma lista global
- cálculo da média entre duas notas
- verificação do status `Aprovado` ou `Reprovado` com base na média
- exibição do resultado no console

Observação: o arquivo também foi corrigido com comentários explicativos de lógica e estrutura.

### `test-assistant-programing/num_primo.py`

Funcionalidade:
- verifica se um número inteiro é primo
- rejeita entradas não inteiras
- usa otimização com `math.isqrt` para testar divisores até a raiz quadrada
- inclui uma suíte de testes automatizada para validar casos comuns
- lê valor do usuário a partir do console

### `test-assistant-programing/refatoracao.py`

Funcionalidade:
- calcula estatísticas básicas a partir de uma lista de números:
  - total
  - média
  - maior valor
  - menor valor
- demonstra bom uso de tipos e funções modulares

## Requisitos

- Python 3.10 ou superior

> O uso da sintaxe `int | None` em `num_primo.py` requer Python 3.10+.

## Como Executar

### Executar o site

Abra o arquivo `index.html` em um navegador ou hospede-o em um servidor local.

### Executar os scripts Python

No terminal, navegue até a pasta do projeto e execute:

```bash
python test-assistant-programing/debug.py
python test-assistant-programing/num_primo.py
python test-assistant-programing/refatoracao.py
```

### Executar os testes de `num_primo.py`

O script `num_primo.py` já contém uma função de suíte de testes interna (`run_test_suite`). Para executar essa suíte manualmente, você pode importar e chamar a função a partir de outro script ou adaptá-lo conforme necessário.

## Melhoria e Extensões Possíveis

- integrar lógica de avaliação de notas com interface web
- criar testes automatizados usando `unittest` ou `pytest`
- adicionar validação de entrada mais robusta no `debug.py`
- separar dados e lógica em módulos distintos para maior organização

## Observações

Este projeto funciona como uma base de aprendizado para:
- programação Python básica e tratamento de fluxo
- manipulação de listas e dicionários
- detecção e correção de erros comuns
- implementação de validações simples e testes manuais

---

Se desejar, posso também gerar uma versão estendida deste README com passos de instalação e exemplos de uso detalhados para cada script.