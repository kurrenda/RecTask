from decimal import Decimal


def zad1():
    first = "79-900"
    second = "80-155"


    firstSplit = first.split("-")
    firstResult = int((str(firstSplit[0]) + str(firstSplit[1])))
    secondSplit = second.split("-")
    secondResult = int((str(secondSplit[0]) + str(secondSplit[1])))

    for x in range(firstResult+1, secondResult):
        res = str(x)
        print(res[0]+res[1]+"-"+res[2]+ res[3]+res[4])

def zad2(tab2,n):

    tab = []

    for i in range(1,n+1):
        tab.append(i)

    print("Brakujące elementy tablicy:",set(tab).difference(set(tab2)))



def zad3():

    lista = []
    first = Decimal(2)
    resRange = int((5.5 - 2)*2)
    for x in range(resRange+1):
        lista.append(first)
        first = first+Decimal(0.5)

    print(lista)




