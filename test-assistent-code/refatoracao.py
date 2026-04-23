def calculate_statistics(numbers):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numbers (list): Lista de números inteiros ou flutuantes.

    Returns:
        tuple: (total, average, maximum, minimum)
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


def main():
    """Executa o cálculo de estatísticas para uma lista de exemplo."""
    sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    total, average, maximum, minimum = calculate_statistics(sample_numbers)

    print("Total:", total)
    print("Média:", average)
    print("Maior:", maximum)
    print("Menor:", minimum)


if __name__ == "__main__":
    main()
