import modeli


def izberi_moznost(moznosti):
    """
    Funkcija, ki izpiše seznam možnosti in vrne indeks izbrane možnosti.
    Če na voljo ni nobene možnosti, izpiše opozorilo in vrne None.
    Če je na voljo samo ena možnost, vrne 0.
    >>> izberi_moznost(['jabolko', 'hruška', 'stol'])
    1) jabolko
    2) hruška
    3) stol
    Vnesite izbiro > 2
    1
    >>> izberi_moznost([])
    >>> izberi_moznost(['jabolko'])
    0
    """

    if len(moznosti) == 0:
        return
    elif len(moznosti) == 1:
        return 0
    else:
        for i, moznost in enumerate(moznosti, 1):
            print('{}) {}'.format(i, moznost))

        st_moznosti = len(moznosti)
        while True:
            izbira = input('Vnesite izbiro > ')
            if not izbira.isdigit():
                print('NAPAKA: vnesti morate število')
            else:
                n = int(izbira)
                if 1 <= n <= st_moznosti:
                    return n - 1
                else:
                    print('NAPAKA: vnesti morate število med 1 in {}!'.format(st_moznosti))



def izberi_clana():
    niz = input('Vnesite ime osebe > ')
    idji_clanov = modeli.poisci_clana(niz)
    moznosti = [
        ime for _, ime ,_, _, in modeli.podatki_clanov(idji_clanov)
    ]
    izbira = izberi_moznost(moznosti)
    return None if izbira is None else idji_clanov[izbira]



def prikazi_podatke_clana():
    id_clana = izberi_clana()
    if id_clana is None:
        print('Nobena oseba ne ustreza iskalnemu nizu. Poskusi znova.')
    else:
        if len(modeli.poisci_intervencije_in_vaje_clana(id_clana))==0:
            ime, priimek, datumRojstva, clanOd, zadnjiZdravniski = modeli.podatki_clana(id_clana)
            print(ime + ' '+ priimek + ', '+ datumRojstva + ', ' + clanOd + ', ' + zadnjiZdravniski)
        else:
            ime, priimek, datumRojstva, clanOd, zadnjiZdravniski, aktivnosti = modeli.podatki_clana(id_clana)
            print(ime + ' '+ priimek + ', '+ datumRojstva + ', ' + clanOd + ', ' + zadnjiZdravniski)
            for i in aktivnosti:
                print(i)


def izberi_vajo():
    niz = input('Vnesite kraj in datum vaje >')
    id_vaje = modeli.poisci_vajo(niz)
    return id_vaje
        
def izberi_intervencijo():
    niz = input('Vnesite kraj in datum intervencije >')
    id_intervencije = modeli.poisci_intervencijo(niz)
    return id_intervencije

def prikazi_podatke_intervencije():
    id_intervencije = izberi_intervencijo()
    if id_intervencije is None:
        print('Ta dan ni bilo intervencije')
    else:
        intervencija = model.podatki_intervencije(id_intervencije)
        for i in intervencija:
            print(i)
            
def prikazi_podatke_vaje():
    id_vaje = izberi_vajo()
    if id_vaje is None:
        print('Ta dan ni bilo vaje')
    else:
        vaja = model.podatki_vaje(id_vaje)
        for i in vaja:
            print(i)

def prikazi_podatke_intervencije():
    return None
def prikazi_podatke_vaje():
    return None
def prikazi_podatke_ida():
    return None
def prikazi_podatke_vozila():
    return None



def dodaj_clana():
    ime = input('Vnesite ime novega člana > ')
    priimek = input('Vnesite priimek novega člana > ')
    datumRojstva = input('Vnesite datum rojstva novega člana > ')
    clanOd = input('Vnesite datum včlanitve. > ')
    zadnjiZdravniski = input('Vnesite datum zadnjega zdravniškega pregleda. > ')
    modeli.dodajClana(ime, priimek, datumRojstva, clanOd, zadnjiZdravniski)
    
def dodaj_intervencijo():
    zacetek = input('Vnesite datum začetka intervencije > ')
    zacetekUra = input('Vnesite uro začetka intervencije > ')
    konec = input('Vnesite datum zaključka intervencije > ')
    konecUra = input('Vnesite uro zaključka intervencije > ')
    kraj = input('Vnesite kraj intervencije > ')
    kilometri = input('Vnesite prevožene kilometre na intervenciji > ')
    opis = input('Vnesite opis intervencije > ')
    opomba = input('Vnesite opombo > ')

    modeli.dodajIntervencijo(zacetek, zacetekUra, konec, konecUra, kraj, kilometri, opis, opomba)

def dodaj_vajo():
    zacetek = input('Vnesite datum začetka vaje > ')
    zacetekUra = input('Vnesite uro začetka vaje > ')
    konec = input('Vnesite datum zaključka vaje > ')
    konecUra = input('Vnesite uro zaključka vaje > ')
    kraj = input('Vnesite kraj vaje > ')
    kilometri = input('Vnesite prevožene kilometre na vaji > ')
    opis = input('Vnesite opis vaje > ')
    opomba = input('Vnesite opombo > ')
    modeli.dodajVajo(zacetek, zacetekUra, konec, konecUra, kraj, kilometri, opis, opomba)
    
def naredi_porocilo():
    return None

def pokazi_moznosti():
    print(50 * '-')
    izbira = izberi_moznost([
        'Prikaži podatke o članih',
        'Prikaži podatke o intervencijah', 
        'Prikaži podatke o vajah',
        'Prikaži podatke o uporabi ida',
        'Prikaži podatke o uporabi vozil',
        'Dodaj nove člane',
        'Dodaj intervencije',
        'Dodaj vaje',
        'Naredi poročilo preteklega leta',
        'Izhod'
        
    ])
    if izbira == 0:
        prikazi_podatke_clana()
    elif izbira == 1:
        prikazi_podatke_intervencije()
    elif izbira == 2:
        prikazi_podatke_vaje()
    elif izbira == 3:
        prikazi_podatke_ida()
    elif izbira == 4:
        prikazi_podatke_vozila()
    elif izbira == 5:
        dodaj_clana()
    elif izbira == 6:
        dodaj_intervencijo()
    elif izbira == 7:
        dodaj_vajo()
    elif izbira == 8:
        naredi_porocilo()
    else:
        print('Nasvidenje!')
        exit()

def main():
    print('Pozdravljeni v bazi PGD Hrušica!')
    while True:
        pokazi_moznosti()

main()

