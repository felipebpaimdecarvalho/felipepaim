def gravar_nome_em_arquivo():
    nome = input("Por favor, informe seu nome: ")  # Solicita o nome do usuário

    # Abre o arquivo no modo de escrita ('w'), se não existir será criado
    with open('nome.txt', 'w') as arquivo:
        arquivo.write(nome)  # Escreve o nome no arquivo

    print("Nome gravado com sucesso no arquivo 'nome.txt'.")

# Exemplo de uso da função
gravar_nome_em_arquivo()


def imprimir_conteudo_arquivo():
    nome_arquivo = input("Por favor, informe o nome do arquivo de texto: ")  # Solicita o nome do arquivo

    # Abre o arquivo no modo de leitura ('r')
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo

    # Imprime o conteúdo do arquivo
    print("Conteúdo do arquivo:")
    print(conteudo)

# Exemplo de uso da função
imprimir_conteudo_arquivo()


def copiar_arquivo():
    nome_arquivo_origem = input("Por favor, informe o nome do arquivo de origem: ")  # Solicita o nome do arquivo de origem
    nome_arquivo_destino = input("Por favor, informe o nome do arquivo de destino: ")  # Solicita o nome do arquivo de destino

    # Abre o arquivo de origem no modo de leitura ('r')
    with open(nome_arquivo_origem, 'r') as arquivo_origem:
        conteudo = arquivo_origem.read()  # Lê todo o conteúdo do arquivo de origem

    # Abre o arquivo de destino no modo de escrita ('w')
    with open(nome_arquivo_destino, 'w') as arquivo_destino:
        arquivo_destino.write(conteudo)  # Escreve o conteúdo lido do arquivo de origem no arquivo de destino

    print("Conteúdo do arquivo copiado com sucesso para o arquivo de destino:", nome_arquivo_destino)

# Exemplo de uso da função
copiar_arquivo()


def encontrar_nome_por_numero():
    numero = input("Digite um número para encontrar o nome correspondente: ")  # Solicita um número ao usuário

    try:
        with open('exemplo.txt', 'r') as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo

            encontrado = False
            for i in range(0, len(linhas), 2):  # Itera sobre as linhas do arquivo de dois em dois
                if linhas[i].strip() == numero:  # Compara o número com a linha atual (removendo espaços em branco extras)
                    print("Nome correspondente ao número", numero + ":", linhas[i+1].strip())  # Imprime o nome correspondente
                    encontrado = True
                    break  # Sai do loop se o número for encontrado

            if not encontrado:
                print("Número não encontrado no arquivo.")

    except FileNotFoundError:
        print("Arquivo de exemplo não encontrado.")

# Exemplo de uso da função
encontrar_nome_por_numero()
