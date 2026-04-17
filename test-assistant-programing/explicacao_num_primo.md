## Explicação linha a linha de `num_primo.py`

### Função `is_prime(value)`

1. `import math`
   - Importa o módulo `math` para usar funções matemáticas confiáveis.
   - Aqui ele é usado para calcular a raiz quadrada inteira com `math.isqrt`.

2. `def is_prime(value: int) -> bool:`
   - Define a função `is_prime` que recebe `value` como inteiro.
   - O `-> bool` indica que a função devolve `True` ou `False`.

3. `    """Retorna True se value for um numero primo, caso contrario False."""`
   - Documenta o propósito da função e o tipo de retorno esperado.

4. `    if not isinstance(value, int):`
   - Verifica se o argumento é realmente um número inteiro.
   - Essa validação evita processar valores como `3.5`, `"texto"` ou `None`.

5. `        return False`
   - Retorna `False` imediatamente para entradas não inteiras.
   - Um primo deve ser um inteiro positivo maior que 1.

6. `    if value <= 1:`
   - Verifica valores que não são primos por definição matemática.
   - Isso inclui negativos, zero e 1.

7. `        return False`
   - Retorna `False` para qualquer `value` menor ou igual a 1.

8. `    if value <= 3:`
   - Lida com os casos pequenos `2` e `3`.
   - Eles são primos e não precisam de mais cálculos.

9. `        return True`
   - Retorna `True` para `2` e `3`.

10. `    if value % 2 == 0:`
    - Verifica se `value` é par.
    - Qualquer primo maior que 2 é ímpar.

11. `        return False`
    - Retorna `False` se o número for par e maior que 2.

12. `    max_divisor = math.isqrt(value)`
    - Calcula a raiz quadrada inteira de `value`.
    - Não é necessário testar divisores acima dessa raiz.

13. `    for divisor in range(3, max_divisor + 1, 2):`
    - Percorre apenas divisores ímpares começando em 3.
    - Pula números pares porque eles já foram eliminados.

14. `        if value % divisor == 0:`
    - Verifica se `divisor` divide `value` sem resto.
    - Se sim, `value` não é primo.

15. `            return False`
    - Retorna `False` ao encontrar o primeiro divisor.
    - O loop termina cedo, evitando trabalho extra.

16. `    return True`
    - Se nenhum divisor for encontrado até a raiz quadrada, `value` é primo.

---

### Função `run_test_suite()`

17. `def run_test_suite() -> bool:`
    - Define uma função separada para executar os testes.
    - Isso melhora a organização e permite reutilizar a lógica de teste.

18. `    test_cases = [`
    - Lista de casos com valores e resultados esperados.
    - Permite validar diferentes situações: negativos, limites e números primos.

19. `    all_passed = True`
    - Inicializa o controle de sucesso dos testes.
    - Permanece `True` até encontrar uma falha.

20. `    for value, expected in test_cases:`
    - Percorre cada caso de teste.
    - Desempacota `value` e o resultado esperado.

21. `        result = is_prime(value)`
    - Chama `is_prime` para cada valor de teste.

22. `        print(f"{value}: {result} (esperado: {expected})")`
    - Mostra o resultado de cada caso.
    - Ajuda a identificar quais valores falharam.

23. `        if result != expected:`
    - Compara o resultado real com o esperado.

24. `            all_passed = False`
    - Marca como falha se qualquer caso não corresponder.

25. `    return all_passed`
    - Retorna o estado geral dos testes.
    - `True` se todos passaram, caso contrário `False`.

---

### Função `prompt_integer()`

26. `def prompt_integer() -> int | None:`
    - Define uma função que lê o número digitado pelo usuário.
    - Retorna um inteiro ou `None` se a entrada for inválida.

27. `    raw_value = input("Digite um número inteiro: ").strip()`
    - Solicita ao usuário um valor pelo console.
    - Remove espaços antes e depois da string.

28. `    try:`
    - Inicia o bloco de tratamento de erro para conversão.

29. `        return int(raw_value)`
    - Tenta converter a entrada para inteiro.

30. `    except ValueError:`
    - Captura qualquer entrada que não seja um inteiro válido.

31. `        return None`
    - Retorna `None` para sinalizar entrada inválida.

---

### Função `main()`

32. `def main() -> None:`
    - Define o ponto principal de execução do script.
    - Mantém a estrutura do programa mais clara.

33. `    value = prompt_integer()`
    - Solicita o número ao usuário chamando `prompt_integer()`.

34. `    if value is None:`
    - Verifica se a conversão falhou.

35. `        print("Entrada inválida. Digite um número inteiro.")`
    - Informa ao usuário que a entrada não foi reconhecida como inteiro.

36. `        return`
    - Encerra a função principal sem continuar.

37. `    if is_prime(value):`
    - Verifica se o número digitado é primo.

38. `        print(f"Numero : {value} é primo")`
    - Exibe o resultado quando o número é primo.

39. `    else:`
    - Caso o número não seja primo.

40. `        print(f"Numero : {value} nao é primo")`
    - Exibe o resultado quando o número não é primo.

---

### Bloco principal

41. `if __name__ == "__main__":`
    - Evita executar o código principal quando o módulo for importado.

42. `    main()`
    - Chama a função principal somente quando o arquivo é executado diretamente.

---

## Observações de clean code

- A função `is_prime` agora tem tipos explícitos e um nome mais descritivo para o parâmetro.
- O cálculo da raiz quadrada usa `math.isqrt`, que é mais preciso e eficiente.
- O comportamento de teste foi separado em `run_test_suite` e `main`.
- O código agora segue o princípio de responsabilidade única: cada função faz apenas uma tarefa.
