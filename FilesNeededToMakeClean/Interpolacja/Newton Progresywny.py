tx = [-4,-2,0,2,4]
ty = [876,50,0,102,1268]
x1 = 1


#tx = [1, 2, 3, 4]
#ty = [3, 7, 8, 15]
#x1 = 1


def silnia(i):
    if i >1:
        w= 1
        w = i*silnia(i-1)
        return w
    elif i in (0,1):
        return 1
    w = 1
    for j in range(i):
        w *= j
    return w


def potega(a, n):
    potega = 1
    tmp = n
    while tmp > 0:
        potega *= a
        tmp = tmp - 1
    return potega


def Newton_Progresywna(tx, ty, x1):
    H = tx[1] - tx[0]
    pom = 0
    wynik = 0.0
    omega = 1

    n2 = len(tx)
    n = int(n2)

    rzad = [[0 for x in range(n)] for y in range(n)]

    ty_length = len(ty)
    for i in range(0, ty_length):
        rzad[i][0] = ty[i]

    for i in range(n):
        try:
            for j in range(n-1):
                rzad[j][i + 1] = ((rzad[j + 1][i] - rzad[j][i]))

                print("Różnica progresowa: ", i + 1, "Element nr: ", j + 1, "Wartość: ", rzad[j][i + 1])


        except ValueError:
            print("Error")
        pom = pom + pom
        print(" ")
        wynik = wynik + ((rzad[0][i] * omega) / (potega(H, i) * silnia(i)))
        omega = omega * (x1 - tx[i])
    return wynik


Wynik_Ostateczny = Newton_Progresywna(tx, ty, x1)
print(Wynik_Ostateczny)


#Dziala dobrze
#print(silnia(3))