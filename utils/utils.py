import csv # bibiloteca que sabe ler e escrever arquivo csv

def ler_csv(arquivo_csv):
    dados_csv = []                                          # cria lista em branco
    try:                                                    # try / except tratamento de erro
        with open(arquivo_csv, newline='') as massa:        # com o arquivo --> informa o nome e o apelido massa
                                                            # newline seria o caractere de final de linha
            tabela = csv.reader(massa, delimiter=',')       # com os dados do arquivo, menos o cabeçalho
                                                            # informando que o separador é a virgula
            next(tabela)                                    # serve para pular a linha do cabeçalho
            for linha in tabela:                            # para cada linha na tabela
                dados_csv.append(linha)                     # guardando os dados separados para uso
        return  dados_csv                                   # devolver os dados para serem usados no teste
    except  FileNotFoundError:                              # tratamento de erro para arquivo não encontrado
        print(f'Arquivo não encontrado: {arquivo_csv}')     # mensagem de erro de arquivo não encontrado
    except  Exception as fail:                              # qualquer erro não previsto
        print(f'Falha imprevista: {fail}')                  # mensagem de erro que voltará do sistema