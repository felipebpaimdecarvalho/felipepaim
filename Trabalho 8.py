def imprimir_info(nome, idade, cidade):
    print("Nome:", nome, sep=" ", end=", ")
    print("Idade:", idade, sep=" ", end=", ")
    print("Cidade:", cidade, sep=" ", end=".")

# Exemplo de uso da função
imprimir_info("João", 25, "São Paulo")



def calcular():
    # Solicitar dois números e a operação ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Calcular o resultado com base na operação especificada
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:  # Verificar se o segundo número não é zero para evitar divisão por zero
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return  # Encerrar a função se a divisão por zero for detectada
    else:
        print("Operação inválida!")
        return  # Encerrar a função se a operação não for reconhecida

    # Imprimir o resultado
    print("Resultado:", resultado)

# Exemplo de uso da função
calcular()

def criar_lista_compras():
    # Solicitar ao usuário que digite os itens da lista de compras
    entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Dividir a entrada em itens individuais usando a vírgula como separador
    itens = entrada.split(',')

    # Imprimir os itens da lista em linhas separadas usando um laço
    print("Lista de Compras:")
    for item in itens:
        print(item.strip())  # strip() remove espaços em branco extras antes e depois de cada item

# Exemplo de uso da função
criar_lista_compras()

def celsius_para_fahrenheit():
    # Solicitar ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converter a temperatura de Celsius para Fahrenheit usando a fórmula fornecida
    fahrenheit = (celsius * 9/5) + 32

    # Imprimir o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit)

def celsius_para_fahrenheit():
    # Solicitar ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converter a temperatura de Celsius para Fahrenheit usando a fórmula fornecida
    fahrenheit = (celsius * 9/5) + 32

    # Imprimir o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso da função
celsius_para_fahrenheit()

def solicitar_nomes():
    nomes = []  # Inicializa uma lista vazia para armazenar os nomes

    while True:  # Loop infinito
        nome = input("Digite um nome ou 'sair' para terminar: ")
        if nome.lower() == 'sair':
            break  # Sai do loop se o usuário digitar 'sair'
        nomes.append(nome)  # Adiciona o nome à lista de nomes

    # Imprime todos os nomes digitados, um por linha
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Exemplo de uso da função
solicitar_nomes()
