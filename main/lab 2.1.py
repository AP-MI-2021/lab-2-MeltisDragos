def NumarPrim(a):
    '''
    Determina daca un numar este prim sau nu
    :param a: numar intreg
    :return: true sau false
    '''
    if a < 2:
        return False
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    '''
    Functia determina cel mai mare numar prim mai care decat n
    :param n: numar intreg
    :return: numar intreg
    '''
    for i in range(n - 1, 1, -1):
        if NumarPrim(i):
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(11) == 7
    assert get_largest_prime_below(7) == 5


def printMeniu():
    print("1.Cel mai mare numar prim mai mic decat un numar dat")
    print("2.Iesire")


if __name__ == '__main__':
    while True:
        printMeniu()
        x = input("Dati optiunea ")
        if x == "1":
            t = int(input("Dati valoarea "))
            print(get_largest_prime_below(t))
        elif x == "2":
            break
        else: print("Eroare. Ati dat o valoare gresita")

