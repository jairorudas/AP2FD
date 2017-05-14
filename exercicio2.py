nextPoint = 0
somaNumeros = 0
numeroMaior = 0
contador = 0

def verificaLinha(k, linha):
    global contador
    global numeroMaior
    global somaNumeros

    tamanho = linha.replace('\n', '')
    tamanho = tamanho.split(' ')

    if(len(tamanho) > 1):
        for i in tamanho:
            contador += 1
            somaNumeros += float(i)

            if float(i) > numeroMaior:
                numeroMaior = float(i)
    else:
        return 0


def verificaNumeroMaior(i=None, data=None):

    global numeroMaior

    data = float(data)

    if (i == 0):
        numeroMaior = data

    elif (data > numeroMaior):
        numeroMaior = data


def lerLinhas(i=0, nomearquivo=None):

    global nextPoint
    global somaNumeros
    global numeroMaior
    global contador



    with open(nomearquivo, 'r') as binary_file:
        binary_file.seek(i)
        data = binary_file.readline()

        if(data == ''):
            imprimeResposta()
            exit()
        else:
            retornoDaverificacao = verificaLinha(i, data)


        if(retornoDaverificacao == 0):
            data = float(data)
            contador += 1
            somaNumeros += float(data[:-1])


            if(data.find('\n') != -1):

                verificaNumeroMaior(i, data)

                nextPoint += len(data)
                lerLinhas(nextPoint, nomearquivo)

            else:
                verificaNumeroMaior(i, data)
        else:
            nextPoint += len(data)
            lerLinhas(nextPoint, nomearquivo)


        imprimeResposta()


def imprimeResposta():
    print('Numero Maior', numeroMaior)
    print('A media dos numeros e', somaNumeros / contador)


def main():
    nomeArquivo = input('insira o nome do arquivo => ')
    lerLinhas(0, nomeArquivo)

if __name__ == '__main__':
    main()


