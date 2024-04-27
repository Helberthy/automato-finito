def load_automata(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linha = arquivo.readlines()

        if len(linha) < 5:
            raise Exception("Formato de arquivo incorreto")

        alfabeto = linha[0].split()
        estados = linha[1].split()
        estados_finais = linha[2].split()
        estado_inicial = linha[3].strip()

        transicoes = {}
        for linha in linha[4:]:
            parte = linha.split()
            if len(parte) != 3:
                raise Exception("Formato de transição incorreto")
            transicoes[(parte[0], parte[1])] = parte[2]

        return alfabeto, estados, transicoes, estado_inicial, estados_finais

def process(automato, palavras):
    alfabeto, estados, transicoes, estado_inicial, estados_finais = automato
    resultados = {}

    for palavra in palavras:
        resultado = ''
        estado_atual = estado_inicial

        if any(simbolo not in alfabeto for simbolo in palavra):
            resultados[palavra] = 'INVÁLIDA'
            continue

        for simbolo in palavra:
            if (estado_atual, simbolo) in transicoes:
                estado_atual = transicoes[(estado_atual, simbolo)]
            else:
                estado_atual = None
                break

        if estado_atual in estados_finais:
            resultado = 'ACEITA'
        else:
            resultado = 'REJEITA'

        resultados[palavra] = resultado

    return resultados

if __name__ == "__main__":
    # Carrega o autômato do arquivo
    automato = load_automata('automato.txt')

    # Define as palavras para testar
    palavras = ['ab', 'aaab', 'bbb', 'baab']

    # Processa as palavras usando o autômato
    resultados = process(automato, palavras)

    # Exibe os resultados
    for palavra, resultado in resultados.items():
        print(f'A palavra "{palavra}" foi {resultado} pelo autômato.')
