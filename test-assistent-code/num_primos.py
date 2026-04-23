import math


def is_prime(n: int) -> bool:
    """Retorna True se n for um número primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    return not _has_odd_divisor(n)


def _has_odd_divisor(n: int) -> bool:
    """Retorna True se n tiver algum divisor ímpar entre 3 e sqrt(n)."""
    limit = math.isqrt(n)
    return any(n % divisor == 0 for divisor in range(3, limit + 1, 2))


def format_prime_result(n: int) -> str:
    """Retorna uma string com o resultado da verificação de primo."""
    status = "primo" if is_prime(n) else "não primo"
    return f"{n}: {status}"


def main() -> None:
    """Executa a verificação de números de exemplo."""
    sample_numbers = [1, 2, 3, 4, 17, 18, 19, 20, 97, 100]
    for number in sample_numbers:
        print(format_prime_result(number))


if __name__ == "__main__":
    main()
