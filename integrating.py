import math


def rect(fun: callable, n: int, p: float, q: float) -> float:
    """
    :param fun: funkcja do calkowania
    :param n: liczba prostokątów
    :param p: lewa granica
    :param q: prawa granica
    :return: pole powierzchni pod funkcja miedzy granicami p, q oraz osia 0x
    """

    # długość boku prostokąta w każdej iteracji
    shift = (q - p) / n

    # wynik całki, suma pól prostokątów
    suma = 0

    for x in range(n):
        # wartość funkcji w punkcie x
        y = fun(p + (x * shift))
        #  pomijamy jeśli poniżej 0x
        if y < 0:
            continue

        suma += y * shift

    return suma


def trapeze(fun: callable, n: int, p: float, q: float) -> float:
    """
    :param fun: funkcja do calkowania
    :param n: liczba trapezów
    :param p: lewa granica
    :param q: prawa granica
    :return: pole powierzchni pod funkcja miedzy granicami p, q oraz osia 0x
    """

    # podstawa trapezu
    shift = (q - p) / n

    # wynik całki, suma pól trapezów
    suma = 0

    for x in range(n):
        # wartość funkcji w punkcie x
        y = fun(p + (x * shift))

        # wartość funkcji w punkcie x + 1
        y2 = fun(p + ((x + 1) * shift))

        #  pomijamy jeśli poniżej 0x
        if y < 0 or y2 < 0:
            continue
        # prostokąt w trapezie
        suma += y * shift
        # wysokosc trojkata w trapezie
        h = abs(y2 - y)

        # pole trojkata w trapezie
        suma += .5 * shift * h

    return suma


# funkcje z zadania
a = lambda x: x ** 2 - x - 3

b = lambda x: -x ** 3 - x ** 2 + 1

c = lambda x: math.cos(x) + 1

d = lambda x: (3 * x) ** (1 / 2) - 1
