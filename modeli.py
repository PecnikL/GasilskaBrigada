import baza
import sqlite3

conn = sqlite3.connect('GasilskaBrigada.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute("PRAGMA foreign_keys = ON")

import time

def stevilo_clanov():
    poizvedba = """
        SELECT COUNT(*)
        FROM clan
    """
    (st_clanov,) = conn.execute(poizvedba).fetchone()
    return st_clanov


def stevilo_vozil():
    poizvedba = """
        SELECT COUNT(*)
        FROM vozilo
    """
    (st_vozil,) = conn.execute(poizvedba).fetchone()
    return st_vozil

def stevilo_tecajev():
    poizvedba = """
        SELECT COUNT(*)
        FROM tecaji
    """
    (st_tecajev,) = conn.execute(poizvedba).fetchone()
    return st_tecajev




def poisci_intervencije_in_vaje_clana(id_clana):
    """
    Funkcija, ki poišče vse intervencije in vaje, ki se jih je udeležil član.
    """
    poizvedba = """
        SELECT intervencija
        FROM sodeluje
        WHERE clan = ?
    """
    return [id_intervencija for (id_intervencija,) in conn.execute(poizvedba, id_clana)]




def poisci_intervenicje_clana(id_clana):
    """
    Funkcija, ki poišče vse intervencije, ki se jih je udeležil član
    """
    poizvedba = """
        SELECT intervencija
        FROM sodeluje
        WHERE clan = ? and (SELECT vrsta FROM intervencija WHERE id = x)= ?
    """
    return [id_intervencija for (id_intervencija,) in conn.execute(poizvedba, (id_clana, 'intervencija'))]



def poisci_vaje_clana(id_clana):
    """
    Funkcija, ki poišče vse vaje, ki se jih je udeležil član
    """
    poizvedba = """
        SELECT intervencija
        FROM sodeluje
        WHERE clan = ? and (SELECT vrsta FROM intervencija WHERE id = x)= ?
    """
    return [id_vaja for (id_vaja,) in conn.execute(poizvedba, (id_clana, 'vaja'))]




def poisci_sodelujoce_v_interveniji(id_intervencija):
    """
    Funkcija poišče vse sodelujoče člane v določeni intervenciji.
    """
    poizvedba = """
        SELECT clan
        FROM sodeluje
        WHERE intervencija = ?
    """
    return [id_clana for (id_clana,) in conn.execute(poizvedba,[id_intervencija])]




def id_clana(oseba, ustvari_ce_ne_obstaja=False):
    """
    Vrne ID podane osebe. Če oseba ne obstaja, jo doda v bazo
    """
    ime = oseba.split()[0]
    priimek = oseba.split()[1]
    vrstica = conn.execute("SELECT id FROM clan WHERE ime =?, priimek=?",[ime,priimek]).fetchone()
    if vrstica is not None:
        return vrstica[0]
    elif ustvari_ce_ne_obstaja:
        return conn.execute("INSERT INTO clan (ime,priimek) VALUES (?,?)", [ime,priimek]).lastrowid
    else:
        return None 




def dodajClana(ime, priimek, datumRojstva, clanOd, zadnjiZdravniski):
    """
    V bazo doda novega člana.
    """
    return conn.execute("INSERT INTO clan (ime,priimek, datumRojstva, clanOd, zadnjiZdravniski) VALUES (?,?,?,?,?)", [ime,priimek, datumRojstva, clanOd, zadnjiZdravniski]).lastrowid
    




def dodajIntervencijo(zacetek,zacetekUra, konec, konecUra, kraj, kilometri, opis, opomba):
    poizvedba = """
        INSERT INTO intervencija
        (vrsta, zacetek, zacetekUra, konec, konecUra, opomba, opis, kraj, kilometri)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    with conn:
        conn.execute(poizvedba ,['intervencija', zacetek, zacetekUra, konec, konecUra, opomba, opis, kraj, kilometri])





def dodajVajo(zacetek,zacetekUra, konec, konecUra, kraj, kilometri, opis, opomba):
    poizvedba = """
        INSERT INTO intervencija
        (vrsta, zacetek, zacetekUra, konec, konecUra, opomba, opis, kraj, kilometri)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    with conn:
        conn.execute(poizvedba ,['vaja', zacetek, zacetekUra, konec, konecUra, opomba, opis, kraj, kilometri])




def dodajVozilo(vrstaVozila, prevozeniKm, zadnjiTehnicni):
    poizvedba = """
        INSERT INTO vozilo
        (vrstaVozila, prevozeniKm, zadnjiTehnicni)
        VALUES (?, ?, ?)
    """
    with conn:
        conn.execute(poizvedba ,[vrstaVozila, prevozeniKm, zadnjiTehnicni])




def dodajIda(clanId, intervencijaId):
    """
    Funkcija, ki v tabelo shrani podatke o uporabi ida.
    """
    poizvedba = """
        INSERT INTO ida
        (clan, intervencija)
        VALUES (?, ?)
    """
    with conn:
        conn.execute(poizvedba ,[clanId, intervencijaId])


        

def dodajTecaj(ime):
    poizvedba = """
        INSERT INTO tecaji
        (naziv)
        VALUES (?)
    """
    with conn:
        conn.execute(poizvedba ,[ime])


        

def dodajSodeluje(clanId, intervencijaId):
    poizvedba = """
        INSERT INTO sodeluje
        (clan, intervencija)
        VALUES (?, ?)
    """
    with conn:
        conn.execute(poizvedba ,[clanId, intervencijaId])


        
        
def dodajSeUporabi(voziloId, intervencijaId, skupajPrevozeno):
    """
    Funkcija, ki v tabelo seUporabi zabeleži uporabo vozila.
    """
    poizvedba = """
        INSERT INTO seUporabi
        (vozilo, intervencija, skupajPrevozeno)
        VALUES (?, ?, ?)
    """
    with conn:
        conn.execute(poizvedba ,[voziloId, intervencijaId, skupajPrevozeno])




def spremeni_datum_zdravniškega_pregleda(id_clan, datum = None):
    """
        Funkcija, ki spremeni datum zadnjega zdravniškega pregleda.
        Če je podan ga spremeni na danega, sicer na trenutnega.
    """
    if datum == None:
        poizvedba = """
            SELECT * REPLACE zadnjiZdravniski WITH current date
            FROM TABLE clan
            WHERE id = ?
        """
        conn.execute(poizvedba, [id_clan])
    else:
        poizvedba = """
            SELECT * REPLACE zadnjiZdravniski WITH ?
            FROM TABLE clan
            WHERE id = ?
        """
        conn.execute(poizvedba, [datum, id_clan])
    return None

