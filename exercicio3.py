import operator

agenda = {}
entrada = ''


def filtrar(ind=0):
    global agenda
    resultadoNomes = sorted(agenda.items(), key=operator.itemgetter(ind))
    return resultadoNomes

def imprime():
    porNomes = filtrar()
    porNumeros = filtrar(1)

    print(' ')
    print('========= POR NOMES =============')
    for nomes in porNomes:
        print(nomes[0], ': ', nomes[1])

    print(' ')
    print('========= POR NUMEROS ===========')
    for numeros in porNumeros:
        print(numeros[0], ': ', numeros[1])

    exit()



def main():
    global entrada

    entrada = input('Digite a lista de contatos separado o nome do numero por espaço => ')
    entrada = entrada.lower()

    while entrada != 'acabou':
        entrada = entrada.split()
        agenda[entrada[0]] = entrada[1]
        main()

    imprime()


if __name__ == '__main__':
    main()