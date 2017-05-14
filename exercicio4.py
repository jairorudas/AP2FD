import operator

total = []
ocorrencia = {}
file = []
enumarable = []

file = open('tuituii.txt', 'r')
total = file.readlines()
total = [strig.replace('\n', '') for strig in total]
enumarable = list(set(total))

for palavra in enumarable:
    ocorrencia[palavra] = total.count(palavra)

maior = sorted(ocorrencia.items(), key=operator.itemgetter(1), reverse=True)

if maior[0][1] == maior[1][1]:
    print(maior[0][0])
    print(maior[1][0])
else:
    print(maior[0][0])



#for line in file:
#   print(file.read())
file.close()
