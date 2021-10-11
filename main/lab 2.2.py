def get_base_2(n):
    '''
    Transforma un numar din baza 10 in baza 2
    :param n: numar intreg
    :return: numar intreg
    '''
    x = 0
    p = 1
    while n > 0:
        x = x + p * (n % 2)
        n = n//2
        p = p * 10
    print(x)

def test_get_base_2():
    assert get_base_2(116) == 1110100
    assert get_base_2(50) == 110010
    assert get_base_2(2) == 10


def printMeniu():
    print("1.Transformarea unui numar din baza 10 in baza 2")
    print("2.Iesire")


if __name__ == '__main__':
    while True:
        printMeniu()
        x = input("Dati optiunea ")
        if x == "1":
            t = int(input("Dati valoarea "))
            print(get_base_2(t))
        elif x == "2":
            break
        else: print("Eroare. Ati dat o valoare gresita")