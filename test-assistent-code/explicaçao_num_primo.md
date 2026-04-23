# Explicação Técnica do Código Python de Verificação de Número Primo

Este arquivo descreve o funcionamento do código presente em 
um_primos.py, que verifica se um número inteiro é primo.

## 1. Objetivo da função
A função is_prime(n: int) -> bool determina se o número 
 é primo. Ela retorna True quando 
 é primo e False caso contrário.

## 2. Melhorias de estilo clean code
O código foi refatorado para manter a lógica separada da apresentação e para melhorar a legibilidade:
- uso de main() para a execução principal do script;
- uso de ormat_prime_result() para isolar a formatação da saída;
- criação da função _has_odd_divisor() para encapsular a verificação de divisores;
- variáveis e funções com nomes descritivos;
- docstrings claras para cada função.

## 3. Fluxo de verificação
A função is_prime segue uma sequência de verificações simples:

### Passo 1: Número menor ou igual a 1
Números menores ou iguais a 1 não são primos. A função retorna False imediatamente.

### Passo 2: Números 2 e 3
Os valores 2 e 3 são primos. A função retorna True diretamente.

### Passo 3: Números pares
Se 
 for par (
 % 2 == 0), então 
 não é primo, exceto o 2, que já foi tratado.

### Passo 4: Raiz quadrada
A função calcula limit = math.isqrt(n) para testar divisores apenas até a raiz quadrada do número.
Isso reduz o número de verificações.

### Passo 5: Teste de divisores ímpares
A função _has_odd_divisor(n) verifica se existe um divisor ímpar entre 3 e limit.
Se algum divisor divide 
, a função is_prime retorna False.

### Passo 6: Conclusão
Se nenhum divisor for encontrado até limit, a função retorna True, indicando que 
 é primo.

## 4. Estrutura do script
O script agora separa a lógica de primalidade da apresentação:

`python
if __name__ == "__main__":
    main()
`

A função main() contém a lista de números de exemplo e imprime os resultados usando ormat_prime_result().

## 5. Benefícios da refatoração
- melhor organização do fluxo de execução;
- funções menores e com responsabilidade única;
- código mais fácil de manter;
- separação entre cálculo e formatação de saída.
