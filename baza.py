import csv

def pobrisi_tabele(conn):
    """Pobriši tabele iz baze."""
    conn.execute("DROP TABLE IF EXISTS clan;")
    conn.execute("DROP TABLE IF EXISTS intervencija;")
    conn.execute("DROP TABLE IF EXISTS vozilo;")
    conn.execute("DROP TABLE IF EXISTS seUporabi;")
    conn.execute("DROP TABLE IF EXISTS sodeluje;")
    conn.execute("DROP TABLE IF EXISTS ida;")
    conn.execute("DROP TABLE IF EXISTS tecaji;")

def ustvari_tabele(conn):
    """Ustvari tabele v bazi."""
    conn.execute("""
                 CREATE TABLE clan(
                     id    INTEGER PRIMARY KEY AUTOINCREMENT,
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
                    id IINTEGER PRIMARY KEY AUTOINCREMENT,
                    naziv TEXT
                    );
                """)


def uvozi_clane(conn):
    """Uvozi podatke o članih."""
    conn.execute("DELETE FROM clan;")
    with open('podatki/clan.csv') as datoteka:
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
    with open('podatki/vozilo.csv') as datoteka:
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
    with open('podatki/intervencija.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO intervencija VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_itecaji(conn):
    """Uvozi podatke o tecajih."""
    conn.execute("DELETE FROM tecaji;")
    with open('podatki/tecaji.csv') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO tecaji VALUES ({})
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
    vozi_tecaji(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    """Ustvari bazo, če ta še ne obstaja."""
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
            ustvari_bazo(conn)
                    
