# Função que verifica se um número é primo.
# Um número primo é aquele que só pode ser dividido por 1 e por ele mesmo.
def e_primo(num):
    # Se o número for menor que 2, ele não pode ser primo.
    if num < 2:
        return False
    # Percorre de 2 até a raiz quadrada do número (inclusive) para procurar divisores.
    # Essa otimização diminui o número de iterações necessárias.
    for i in range(2, int(num**0.5) + 1):
        # Se o número for divisível por 'i', então ele não é primo.
        if num % i == 0:
            return False
    # Se não encontrar nenhum divisor, o número é primo.
    return True

# Solicita ao usuário para digitar um número inteiro.
numero = int(input("Digite um número: "))

# Verifica se o número digitado é primo utilizando a função 'e_primo'
# e imprime a mensagem correspondente.
if e_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
