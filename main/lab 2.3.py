def is_palindrome(n) -> bool:
    '''
    Determinam daca un numar este palindrom sau nu
    :param n: numar intreg
    :return: true sau false
    '''
    aux = n
    t = 0
    while aux > 0:
        t = t * 10 + aux % 10
        aux = aux//10
    if t == n:
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(123) is False
    assert is_palindrome(121) is True

def printMeniu():
    print("1.Verifica daca un numar este palindrom")
    print("2.Iesire")


if __name__ == '__main__':
    while True:
        printMeniu()
        x = input("Dati optiunea ")
        if x == "1":
            t = int(input("Dati valoarea "))
            if is_palindrome(t) is True:
                print("Numarul dat este palindrom")
            else:
                print("Numarul dat nu este palindrom")
        elif x == "2":
            break
        else: print("Eroare. Ati dat o valoare gresita")