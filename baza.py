import csv
import codecs


def pobrisi_tabele(conn):
    """Pobriši tabele iz baze."""
    conn.execute("DROP TABLE IF EXISTS clan;")
    conn.execute("DROP TABLE IF EXISTS intervencija;")
    conn.execute("DROP TABLE IF EXISTS vozilo;")
    conn.execute("DROP TABLE IF EXISTS seUporabi;")
    conn.execute("DROP TABLE IF EXISTS sodeluje;")
    conn.execute("DROP TABLE IF EXISTS ida;")
    conn.execute("DROP TABLE IF EXISTS tecaji;")
    conn.execute("DROP TABLE IF EXISTS uporabnik_baze;")
    conn.execute("DROP TABLE IF EXISTS sodeluje;")

def ustvari_tabele(conn):
    """Ustvari tabele v bazi."""
    conn.execute("""
                 CREATE TABLE clan(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     ime   TEXT,
                     priimek TEXT,
                     datumRojstva TEXT,
                     clanOd TEXT,
                     zadnjiZdravniski TEXT
                     );
                 """)
    conn.execute("""
                CREATE TABLE vozilo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vrstaVozlia TEXT,
                    prevozeniKm INTEGER,
                    zadnjiTehnicni TEXT
                    );
                """)
    conn.execute("""
                CREATE TABLE intervencija (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vrsta TEXT,
                    zacetek TEXT,
                    zacetekUra TEXT,
                    konec TEXT,
                    konecUra TEXT,
                    opomba TEXT,
                    opis TEXT,
                    kraj TEXT,
                    kilometri INTEGER
                    );
                  """)
    conn.execute("""
                CREATE TABLE  seUporabi (
                    vozilo INTEGER REFERENCES vozilo(id),
                    intervencija INTEGER REFERENCES intervencija(id),
                    skupajPrevozeno INTEGER
                    );
                """)
    conn.execute("""
                CREATE TABLE sodeluje (
                    clan INTEGER REFERENCES clan(id),
                    intervencija INTEGER REFERENCES intervencija(id)
                    );
                  """)
    conn.execute("""
                CREATE TABLE ida (
                    clan INTEGER REFERENCES clan(id),
                    intervencija INTEGER REFERENCES intervencija(id)
                    );
                """)
    conn.execute("""
                CREATE TABLE tecaji (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    naziv TEXT
                    );
                """)
    conn.execute("""
                CREATE TABLE uporabnik_baze (
                    uporabnik TEXT PRIMARY KEY,
                    geslo TEXT,
                    sol TEXT
                    );
                """)

def uvozi_clane(conn):
    """Uvozi podatke o članih."""
    conn.execute("DELETE FROM clan;")
    with codecs.open('podatki/clan.csv', 'r', 'utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO clan VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_vozila(conn):
    """Uvozi podatke o vozilih."""
    conn.execute("DELETE FROM vozilo;")
    with codecs.open('podatki/vozilo.csv', 'r', 'utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO vozilo VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)
            
def uvozi_intervencije(conn):
    """Uvozi podatke o intervencijah."""
    conn.execute("DELETE FROM intervencija;")
    with codecs.open('podatki/intervencija.csv', 'r', 'utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO intervencija VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_tecaji(conn):
    """Uvozi podatke o tecajih."""
    conn.execute("DELETE FROM tecaji;")
    with codecs.open('podatki/tecaji.csv', 'r', 'utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO tecaji VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_uporabnike_baze(conn):
    """Uvozi uporabnike baze"""
    conn.execute("DELETE FROM uporabnik_baze;")
    with codecs.open('podatki/uporabnik_baze.csv', 'r', 'utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO uporabnik_baze VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_sodeluje(conn):
    """Uvozi podatke v tabelo sodeluje"""
    conn.execute("DELETE FROM sodeluje;")
    with codecs.open('podatki/sodeluje.csv', 'r', 'utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO sodeluje VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def ustvari_bazo(conn):
    """Opravi celoten postopek postavitve baze."""
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    uvozi_clane(conn)
    uvozi_vozila(conn)
    uvozi_intervencije(conn)
    uvozi_tecaji(conn)
    uvozi_uporabnike_baze(conn)
    uvozi_sodeluje(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    """Ustvari bazo, če ta še ne obstaja."""
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
            ustvari_bazo(conn)
                    
