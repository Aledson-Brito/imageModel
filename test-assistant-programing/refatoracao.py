from typing import Iterable, Tuple


def calculate_statistics(numbers: Iterable[float]) -> Tuple[float, float, float, float]:
    """Return the total, average, maximum, and minimum values of the given numbers."""
    values = list(numbers)
    if not values:
        raise ValueError("The list of numbers must not be empty.")

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)
    return total, average, maximum, minimum


def main() -> None:
    sample_values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(sample_values)

    print("total:", total)
    print("media:", average)
    print("maior:", maximum)
    print("menor:", minimum)


if __name__ == "__main__":
    main()