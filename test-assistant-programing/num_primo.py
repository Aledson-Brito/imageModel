import math


def is_prime(value: int) -> bool:
    """Verifica se um número inteiro é primo.

    Args:
        value (int): Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, caso contrário False.
    """
    if not isinstance(value, int):
        return False

    if value <= 1:
        return False

    if value <= 3:
        return True

    if value % 2 == 0:
        return False

    max_divisor = math.isqrt(value)
    for divisor in range(3, max_divisor + 1, 2):
        if value % divisor == 0:
            return False

    return True


def run_test_suite() -> bool:
    test_cases = [
        (-5, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (13, True),
        (25, False),
        (97, True),
        (100, False),
    ]

    all_passed = True
    for value, expected in test_cases:
        result = is_prime(value)
        print(f"{value}: {result} (esperado: {expected})")
        if result != expected:
            all_passed = False

    return all_passed


def prompt_integer() -> int | None:
    raw_value = input("Digite um número inteiro: ").strip()
    try:
        return int(raw_value)
    except ValueError:
        return None


def main() -> None:
    value = prompt_integer()
    if value is None:
        print("Entrada inválida. Digite um número inteiro.")
        return

    if is_prime(value):
        print(f"Numero : {value} é primo")
    else:
        print(f"Numero : {value} nao é primo")


if __name__ == "__main__":
    main()
