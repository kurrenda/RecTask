from decimal import Decimal


def zad1(self):
    first = "79-900"
    second = "80-155"


    firstSplit = first.split("-")
    firstResult = int((str(firstSplit[0]) + str(firstSplit[1])))
    secondSplit = second.split("-")
    secondResult = int((str(secondSplit[0]) + str(secondSplit[1])))

    for x in range(firstResult, secondResult):
        res = str(x)
        print(res[0]+res[1]+"-"+res[2]+ res[3]+res[4])

def zad2(self , n):

    tab = [1,2,3,4,5,6,7,8,9,10]

    tab2 = [2,3,7,4,9,10]
    tab2.remove(n)

    set1 = set(tab)
    set2 = set(tab2)

    add = list(sorted(set1 - set2))
    print(add)

def zad3(self):

    lista = []
    first = Decimal(2)
    resRange = int((5.5 - 2)*2)
    for x in range(resRange+1):
        lista.append(first)
        first = first+Decimal(0.5)

    print(lista)









