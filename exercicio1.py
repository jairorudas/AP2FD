from funcoes import funcoesAula8 as fn
from funcoes import customfunctions as fun

#Ecercicio 1
def maior(lista):
    isList = fn.ehLista(lista)

    if isList and len(lista) > 0:
        print(max(lista))
    else:
        print(0)


#Excercicio 2
def mediaPositivos(lista):

    arrayPositives = list(filter(fun.onlyPositives, lista))

    if not lista or len(arrayPositives) == 0:
        print(0)
    else:
        print(sum(arrayPositives) / len(arrayPositives))


#Execercicio 3
#def emagrece(matrix):



def main():
    maior([1, 2, 3, 4, 23, 43, 100])
    mediaPositivos([-1, 3, 4, -5, -3, 10])




if __name__ == '__main__':
    main()