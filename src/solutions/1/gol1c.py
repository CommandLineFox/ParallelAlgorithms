from threading import Barrier, Thread


class Celija:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.susedi = 0
        self.procitani = 0
        self.iteracija = 0

    def __str__(self):
        return f"{self.value}"


def upis_matrice(n, m):
    mat = []
    for i in range(n):
        cur = []
        for j in range(m):
            c = Celija(i, j, int(input()))
            cur.append(c)
        mat.append(cur)
    return mat


def ispis_matrice(mat, m, n):
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()


def proveri_polje(mat, i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    c = mat[i][j]
    if c.value == 1:
        return 1
    return 0


def vrati_broj_suseda(mat, i, j, n, m):
    broj_suseda = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if (k != i or l != j) and proveri_polje(mat, k, l, n, m) == 1:
                broj_suseda += 1
    return broj_suseda


def slucaj(mat, i, j, n, m, barriers):

    c = mat[i][j]
    broj_suseda = vrati_broj_suseda(mat, i, j, n, m)

    barriers.wait()

    if (broj_suseda < 2 or broj_suseda > 3):
        c.value = 0
    elif (broj_suseda == 3):
        c.value = 1


def IgraZivota(mat, n, m):

    threads = []

    barriers = Barrier(n*m)
    for i in range(n):
        for j in range(m):
            t = Thread(target=slucaj, args=[mat, i, j, n, m, barriers])
            t.start()
            threads.append(t)

    for tr in threads:
        tr.join()


def DodajSusede(mat, n, m):
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or (i == n-1 and j == 0) or (i == 0 and j == m-1) or (i == n-1 and j == 0):
                mat[i][j].susedi = 3
            elif i == 0 or j == 0 or i == n-1 or j == m-1:
                mat[i][j].susedi = 5
            else:
                mat[i][j].susedi = 8


def main():
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    mat = upis_matrice(n, m)
    DodajSusede(mat, n, m)

    ispis_matrice(mat, n, m)
    IgraZivota(mat, n, m)
    ispis_matrice(mat, n, m)


main()