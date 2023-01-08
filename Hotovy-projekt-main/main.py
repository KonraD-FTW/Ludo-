import random


def tlac_sachovnicu(n, hrac_A, hrac_B,save_A,save_B,domcek_A,domcek_B):
    """
    Tato funkcia ma za ulohu vytlacit n*n rozmernu sachovnicu
    pre dvoch hracov A a B pricom rozlisujeme odlisne pozicie, pretoze ak sa prva suradnica sachovnice rovna
    startovacej pozicii hraca A alebo B, printujeme daneho hraca a dalej uz len podla pozicii hraciu drahu
    alebo stred sachovnice alebo domceky hracov. Pricom n je rozmer sachovnice.
    """

    for riadok in range(n):
        for stlpec in range(n):
            if (riadok == hrac_A[0] and stlpec == hrac_A[1]) or (riadok == hrac_B[0] and stlpec == hrac_B[1]):
                if riadok == hrac_B[0] and stlpec == hrac_B[1]:
                    print("B", end=" ")
                if riadok == hrac_A[0] and stlpec == hrac_A[1]:
                    print("A", end=" ")
            elif je_stred(stlpec, riadok, n):
                print("X", end=" ")
            elif je_cesta(stlpec, riadok, n) or je_cesta(riadok, stlpec, n):
                print("*", end=" ")
            elif kontrola_domcekov(save_A,domcek_A,riadok,stlpec):
                print("A",end=" ")
            elif kontrola_domcekov(save_B,domcek_B,riadok,stlpec):
                print("B",end=" ")
            elif je_domcek(stlpec, riadok, n):
                print("D", end=" ")
            else:
                print(" ", end=" ")
        print()

    print()
def kontrola_domcekov(save,domcek,riadok,stlpec):
    for index,i in enumerate(save):
        if domcek[index] == True and i[0] == riadok and i[1] == stlpec:
           return True
    return False



def je_cesta(x, y, n):
    """
    Pomocou tejto funkcie zistujeme ci dana pozicia je cesta alebo nie
    """
    return ((((n // 2) - 1) == x or ((n // 2) + 1) == x) and (y != n // 2)) or (
            (n // 2) == x and (y == 0 or y == n - 1))


def je_stred(x, y, n):
    """
    Tato funkcia hlada konkretne stred n*n rozmernej sachovnice
    """
    return x == n // 2 and y == n // 2


def je_domcek(x, y, n):
    """
    Pomocou tejto funkcie hladame konkretne pozicie domcekov na hracej ploche
    """
    return x == n // 2 or y == n // 2


def clovece_nehnevaj_sa(n, cesta_hraca_A, domcek_hraca_A,cesta_hraca_B,domcek_hraca_B,pocet_panak_A,pocet_panak_B):
    pozicia_hraca_A = 0
    pozicia_hraca_B = 0
    domcek_A = []
    domcek_B = []
    for i in range(pocet_panak_A):
        domcek_A.append(False)
    for i in range(pocet_panak_B):
        domcek_B.append(False)
    #domcek_A[1] = True
    while True:
        hodene_cislo = hod_kockou()
        print("Hod hraca A",hodene_cislo)
        if (pozicia_hraca_A + hodene_cislo) >= (len(cesta_hraca_A) + len(domcek_hraca_A)):
            pozicia_hraca_A += 0

        elif (pozicia_hraca_A + hodene_cislo) >= len(cesta_hraca_A):
            pozicia_v_domceku_A = (pozicia_hraca_A + hodene_cislo) - (len(cesta_hraca_A))
            if domcek_A[pozicia_v_domceku_A] == False:
                domcek_A[pozicia_v_domceku_A] = True
                pocet_panak_A -= 1
                if pocet_panak_A != 0:
                    pozicia_hraca_A = 0
                    print('lol')
                else:
                    print('Vyhral hrac A')
                    tlac_sachovnicu(n, domcek_hraca_A[pozicia_v_domceku_A], cesta_hraca_B[pozicia_hraca_B], save_A,
                                    save_B,
                                    domcek_A, domcek_B)
                    exit()
            else:
                pozicia_hraca_A += 0

            tlac_sachovnicu(n, domcek_hraca_A[pozicia_v_domceku_A], cesta_hraca_B[pozicia_hraca_B],save_A,save_B,
                            domcek_A,domcek_B)
        else:
            pozicia_hraca_A += hodene_cislo
        hodene_cislo = hod_kockou()
        print("Hod hraca B",hodene_cislo)
        if (pozicia_hraca_B + hodene_cislo) >= (len(cesta_hraca_B) + len(domcek_hraca_B)):
            pozicia_hraca_B += 0
        elif (pozicia_hraca_B + hodene_cislo) >= len(cesta_hraca_B):
            pozicia_v_domceku_B = (pozicia_hraca_B + hodene_cislo) - (len(cesta_hraca_B))
            if domcek_B[pozicia_v_domceku_B] == False:
                domcek_B[pozicia_v_domceku_B] = True
                pocet_panak_B -= 1
                if pocet_panak_B != 0:
                    pozicia_hraca_B = 0
                    print('lol')
                else:
                    print('Vyhral hrac B')
                    tlac_sachovnicu(n, cesta_hraca_A[pozicia_hraca_A], domcek_hraca_B[pozicia_v_domceku_B], save_A,
                                    save_B,
                                    domcek_A, domcek_B)
                    exit()
            else:
                pozicia_hraca_B += 0
            tlac_sachovnicu(n,cesta_hraca_A[pozicia_hraca_A], domcek_hraca_B[pozicia_v_domceku_B],save_A,save_B,
                            domcek_A,domcek_B)
        else:
            pozicia_hraca_B += hodene_cislo

        tlac_sachovnicu(n, cesta_hraca_A[pozicia_hraca_A], cesta_hraca_B[pozicia_hraca_B],save_A,save_B,
                            domcek_A,domcek_B )


def hod_kockou():
    """
    Generuje sa cislo od 1 po 6 ako hod hracej kocky
    """
    return random.randint(1, 6)


def create_board():
    """
    Tato funkcia vyratava suradnice n*n hracej plochy pre hraca A a hraca B
    """
    tmp_board = []
    tmp_board.append((0, stred_dosky + 1))

    for i in range(pocet_panacikov):
        tmp_board.append((1 + i, stred_dosky + 1))

    for i in range(pocet_panacikov - 1):
        tmp_board.append((stred_dosky - 1, stred_dosky + 2 + i))

    for i in range(3):
        tmp_board.append((stred_dosky - 1 + i, velkost_sachovnice - 1))

    for i in range(pocet_panacikov):
        tmp_board.append((stred_dosky + 1, velkost_sachovnice - 2 - i))

    for i in range(pocet_panacikov - 1):
        tmp_board.append((stred_dosky + 2 + i, stred_dosky + 1))

    for i in range(3):
        tmp_board.append((velkost_sachovnice - 1, stred_dosky + 1 - i))

    for i in range(pocet_panacikov):
        tmp_board.append((velkost_sachovnice - 2 - i, stred_dosky - 1))

    for i in range(pocet_panacikov - 1):
        tmp_board.append((stred_dosky + 1, stred_dosky - 2 - i))

    for i in range(3):
        tmp_board.append((stred_dosky + 1 - i, 0))

    for i in range(pocet_panacikov):
        tmp_board.append((stred_dosky - 1, 1 + i))

    for i in range(pocet_panacikov - 1):
        tmp_board.append((stred_dosky - 2 - i, stred_dosky - 1))

    for i in range(2):
        tmp_board.append((0, stred_dosky - 1 + i))

    return tmp_board


def suradnice_domcekov(tym):
    """
    Tato funkcia ma za ulohu zistit suradnice n*n rozmernej sachovnice pre domceky hracov A a B
    """
    tmp_save = []

    if tym == 'A':
        for i in range(pocet_panacikov):
            tmp_save.append((1+i, stred_dosky))

    elif tym == 'B':
        for i in range(pocet_panacikov):
            tmp_save.append((velkost_sachovnice-2-i, stred_dosky))

    return tmp_save


if __name__ == '__main__':

    velkost_sachovnice = int(input("Zadaj velkost sachovnice: "))

    if velkost_sachovnice % 2 != 1:
        velkost_sachovnice += 1

    stred_dosky = int(velkost_sachovnice / 2)
    pocet_panacikov = int((velkost_sachovnice - 3) / 2)
    pocet_panak_A = pocet_panacikov
    pocet_panak_B = pocet_panacikov
    board_A = create_board()
    board_B = board_A[int(len(board_A)/2):] + board_A[:int(len(board_A)/2)]
    save_A = suradnice_domcekov('A')
    save_B = suradnice_domcekov('B')
    clovece_nehnevaj_sa(velkost_sachovnice, board_A, save_A,board_B,save_B,pocet_panak_A,pocet_panak_B)

    print()
