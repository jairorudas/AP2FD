import numpy

dict1 = {}

def createEsparsa(matriz, i = 0, x = 0):
    esparsa = {}
    while ( len(matriz) > i ):

        for n in matriz[i]:
            if ( n != 0 ):
                esparsa.update(dict({(i, x): n}))
            x += 1
        x = 0
        i += 1

    return esparsa


def createMatriz(dimensoes, i=0, tipomatriz=None):
    matriz  = []
    entrada = []

    while(int(dimensoes[0]) > i):
        entrada = input('insere a {0} linha da matriz => '.format(tipomatriz))

        if(entrada.rindex(' ') == len(entrada) -1 ):
            entrada.split().pop()
            entrada = entrada.split()
            print(entrada)
        else:
            entrada = entrada.split()


        matriz.append(([int(n) for n in entrada])[:int(dimensoes[1])])
        i += 1

    return matriz

def apagaEspaco(param):

    if(str(param).rindex(' ') == len(param) - 1 ):
        param.pop()
        return param
    else:
        return param

def mult_matrix(matrixA, matrixB):

    return numpy.dot(matrixA, matrixB)



def main():
    dimensaoPrimeiraMatriz = input('Digite a dimensao da primeira matriz por favor: ').split()
    dimensaoSegundaMatriz = input('Digite a dimensao da segunda matriz por favor: ').split()


    if(dimensaoPrimeiraMatriz[1] == dimensaoSegundaMatriz[0]):

        matriz1 = createMatriz(dimensaoPrimeiraMatriz, 0, 'Primeira')

        matriz2 = createMatriz(dimensaoSegundaMatriz, 0, 'Segunda')

        esparsa1 = createEsparsa(matriz1)
        print(esparsa1, 'Matriz Esparsa A')

        esparsa2 = createEsparsa(matriz2)
        print(esparsa2, 'Matriz Esparsa B')

        matriz_resultante = mult_matrix(matriz1, matriz2)

        matriz_resultante = createEsparsa(matriz_resultante)
        print(matriz_resultante, 'Matriz Esparsa R')

    else:
        print('nao e possivel fazer a operaçao')

if __name__ == '__main__':
    main()