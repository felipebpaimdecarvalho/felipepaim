def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_procurada, nova_palavra):
    return [nova_palavra if palavra == palavra_procurada else palavra for palavra in lista]

def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplos de uso:
if __name__ == "__main__":
    # Questão 1
    lista_numeros = [1, 2, 3, 4]
    soma, media = calcular_soma_e_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    # Questão 2
    lista_palavras = ["paim", "flamengo", "vasco"]
    palavra_procurada = "paim"
    nova_palavra = "botafogo"
    lista_alterada = substituir_palavra(lista_palavras, palavra_procurada, nova_palavra)
    print("Lista alterada:", lista_alterada)

    # Questão 3
    num_linhas = 4
    gerar_triangulo(num_linhas)
