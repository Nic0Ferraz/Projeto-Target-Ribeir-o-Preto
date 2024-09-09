def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def contar_letra_a(s):
    return s.lower().count('a')

def soma_while(indice):
    soma = 0
    k = 1
    while k < indice:
        k += 1
        soma += k
    return soma

def completar_padrao():
    padroes = {
        "a": [1, 3, 5, 7, 9],
        "b": [2, 4, 8, 16, 32, 64, 128],
        "c": [0, 1, 4, 9, 16, 25, 36, 49],
        "d": [4, 16, 36, 64, 100],
        "e": [1, 1, 2, 3, 5, 8, 13],
        "f": [2, 10, 12, 16, 17, 18, 19, 20]
    }
    return padroes

def main():
    
    numero = int(input("Digite um número para verificar na sequência de Fibonacci: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
   
    string = input("Digite uma string para contar a letra 'a': ")
    quantidade = contar_letra_a(string)
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
    
   
    indice = 12
    resultado_soma = soma_while(indice)
    print(f"Resultado da soma no código while: {resultado_soma}")
    
    
    padroes = completar_padrao()
    print("Próximos elementos dos padrões:")
    print(f"a) {padroes['a']}")
    print(f"b) {padroes['b']}")
    print(f"c) {padroes['c']}")
    print(f"d) {padroes['d']}")
    print(f"e) {padroes['e']}")
    print(f"f) {padroes['f']}")
    
    
    print("Solução para o enigma dos interruptores e lâmpadas:")
    print("1. Ligue o primeiro interruptor e deixe-o ligado por 10 minutos, depois desligue-o.")
    print("2. Ligue o segundo interruptor e vá até as salas das lâmpadas.")
    print("   - A lâmpada acesa é controlada pelo segundo interruptor.")
    print("   - A lâmpada desligada, mas quente, é controlada pelo primeiro interruptor.")
    print("   - A lâmpada desligada e fria é controlada pelo terceiro interruptor.")

if __name__ == "__main__":
    main()