from bottle import get,post, run, template
import modeli
import bottle
import hashlib

SKRIVNOST = 'skriv'

def prijavljen_uporabnik():
    return bottle.request.get_cookie('prijavljen', secret=SKRIVNOST) == 'da'


@get('/')
def zacetna_stran():
    if prijavljen_uporabnik():
        bottle.redirect('/izbira')
    return template(
        'zacetna_stran'
    )


@get('/izbira')
def izbira():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    
    return template(
        'izbira'
    )

@get('/clani')
@get('/clani/<id1>/')
def clani(id1=None):
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    
    if id1 == None:
        clani = modeli.vsi_clani()
        return template(
            'clani',
            st_clanov = modeli.stevilo_clanov(),
            clani = clani
        )
    else:
        ime,priimek,datumRojstva,clanOd, zadnjiZdravniski, aktivnosti = modeli.podatki_clana(int(id1))
        vse_aktivnosti = modeli.podatki_intervencij(aktivnosti)
        return template(
            'clan',
            ime = ime,
            priimek = priimek,
            datumRojstva = datumRojstva,
            clanOd = clanOd,
            zadnjiZdravniski = zadnjiZdravniski,
            vse_aktivnosti = vse_aktivnosti
            )

@get('/iskanje-clanov/')
def iskanje_clanov():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    niz = bottle.request.query.ime_priimek
    clani_id = modeli.poisci_clana(niz)
    clani = modeli.podatki_clanov(clani_id)
    return template(
        'rezultati_iskanja_clanov',
        clani = clani
        )   
    

@get('/dodaj-clana/')
def dodaj_clana():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    return template(
        'dodaj_clana',
        ime = "",
        priimek = "",
        datumRojstva = "",
        clanOd = "",
        zadnjiZdravniski=""
        )
@post('/dodaj-clana/')
def dodajanje_clana():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    ime = bottle.request.forms.ime
    priimek = bottle.request.forms.priimek
    datumRojstva = bottle.request.forms.datumRojstva
    clanOd = bottle.request.forms.clanOd
    zadnjiZdravniski = bottle.request.forms.zadnjiZdravniski
    id1 = None
    try:
        id1 = modeli.dodajClana(ime, priimek, datumRojstva, clanOd, zadnjiZdravniski)
    except:
        return template('dodaj_clana',
                        ime = bottle.request.forms.ime,
                        priimek = bottle.request.forms.priimek,
                        datumRojstva = bottle.request.forms.datumRojstva,
                        clanOd = bottle.request.forms.clanOd,
                        zadnjiZdravniski = bottle.request.forms.zadnjiZdravniski)
    bottle.redirect('/clani/'+str(id1) + '/')
    
@get('/intervencije')
@get('/intervencije/<id1>/')
def intervencije(id1 = None):
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    kraji = modeli.vsi_kraji_intervencij()
    interv = modeli.vse_intervencije()
    if id1 == None:
        return template(
            'intervencije',
            kraji = kraji,
            interv = interv
        )
    else:

        id2, vrsta, zacetek, zacetekUra, konec, konecUra, opomba, opis, kraj, kilometri = modeli.podatki_intervencije(int(id1))
        
        return template(
            'intervencija',
            id2 = id2,
            vrsta = vrsta,
            zacetek = zacetek,
            zacetekUra = zacetekUra,
            konec = konec,
            konecUra = konecUra,
            opomba = opomba,
            opis = opis,
            kraj = kraj,
            kilometri= kilometri
        )
@get('/dodaj-intervencijo/')
def dodaj_intervencijo():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    return template(
        'dodaj_intervencijo',
        zacetek = "",
        zacetekUra = "",
        konec = "",
        konecUra = "",
        opomba = "",
        opis = "",
        kraj = "",
        kilometri = ""
        )
@post('/dodaj-intervencijo/')
def dodajanje_intervencije():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    id1 = None
    try:
        id1 = modeli.dodajIntervencijo(
                               zacetek = bottle.request.forms.zacetek,
                               zacetekUra = bottle.request.forms.zacetekUra,
                               konec = bottle.request.forms.konec,
                               konecUra = bottle.request.forms.konecUra,
                               opomba = bottle.request.forms.opomba,
                               opis = bottle.request.forms.opis,
                               kraj = bottle.request.forms.kraj,
                               kilometri = bottle.request.forms.kilometri)
    except:
        return template('dodaj_intervencijo',
                               vrsta = 'intervencija',
                               zacetek = bottle.request.forms.zacetek,
                               zacetekUra = bottle.request.forms.zacetekUra,
                               konec = bottle.request.forms.konec,
                               konecUra = bottle.request.forms.konecUra,
                               opomba = bottle.request.forms.opomba,
                               opis = bottle.request.forms.opis,
                               kraj = bottle.request.forms.kraj,
                               kilometri = bottle.request.forms.kilometri)

    bottle.redirect('/intervencije/'+str(id1)+'/')

@get('/vaje')
@get('/vaje/<id1>/')
def vaje(id1 = None):
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    kraji = modeli.vsi_kraji_vaj()
    vaje = modeli.vse_vaje()
    if id1 == None:
        return template(
            'vaje',
            kraji = kraji,
            vaje = vaje
        )
    else:
        id2, vrsta, zacetek, zacetekUra, konec, konecUra, opomba, opis, kraj, kilometri = modeli.podatki_vaje(int(id1))
        
        return template(
            'vaja',
            id2 = id2,
            vrsta = vrsta,
            zacetek = zacetek,
            zacetekUra = zacetekUra,
            konec = konec,
            konecUra = konecUra,
            opomba = opomba,
            opis = opis,
            kraj = kraj,
            kilometri= kilometri
        )

@get('/dodaj-vajo/')
def dodaj_vajo():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    return template(
        'dodaj_vajo',
        zacetek = "",
        zacetekUra = "",
        konec = "",
        konecUra = "",
        opomba = "",
        opis = "",
        kraj = "",
        kilometri = ""
        )
@post('/dodaj-vajo/')
def dodajanje_vaje():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    id1 = None
    try:
        id1 = modeli.dodajVajo(
                               zacetek = bottle.request.forms.zacetek,
                               zacetekUra = bottle.request.forms.zacetekUra,
                               konec = bottle.request.forms.konec,
                               konecUra = bottle.request.forms.konecUra,
                               opomba = bottle.request.forms.opomba,
                               opis = bottle.request.forms.opis,
                               kraj = bottle.request.forms.kraj,
                               kilometri = bottle.request.forms.kilometri)
    except:
        return template('dodaj_vajo',
                               zacetek = bottle.request.forms.zacetek,
                               zacetekUra = bottle.request.forms.zacetekUra,
                               konec = bottle.request.forms.konec,
                               konecUra = bottle.request.forms.konecUra,
                               opomba = bottle.request.forms.opomba,
                               opis = bottle.request.forms.opis,
                               kraj = bottle.request.forms.kraj,
                               kilometri = bottle.request.forms.kilometri)
    if id1 == None:
        bottle.redirect('/vaje')
    else:
        bottle.redirect('/vaje/'+str(id1)+'/')



@get('/vozila')
@get('/vozila/<id1>/')
def vozila(id1 = None):
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    stevilo_vozil = modeli.stevilo_vozil()
    vozila = modeli.vsa_vozila()
    if id1 == None:
        return template(
            'vozila',
            stevilo_vozil = stevilo_vozil,
            vozila = vozila
        )
@get('/dodaj-vozilo/')
def dodaj_vozilo():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    return template(
        'dodaj_vozilo',
        vrstaVozila = "",
        prevozeniKm = "",
        zadnjiTehnicni = ""
        )
@post('/dodaj-vozilo/')
def dodaj_vozilo():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    id1 = None
    vrstaVozila = bottle.request.forms.vrstaVozila
    prevozeniKm = bottle.request.forms.prevozeniKm
    zadnjiTehnicni = bottle.request.forms.zadnjiTehnicni
    try:
        id1 = modeli.dodajVozilo(vrstaVozila, prevozeniKm, zadnjiTehnicni)
    except:
        return template('dodaj_vozilo',
                            vrstaVozila = bottle.request.forms.vrstaVozila,
                            prevozeniKm = bottle.request.forms.prevozeniKm,
                            zadnjiTehnicni = bottle.request.forms.zadnjiTehnicni
                            )

    bottle.redirect('/vozila')
                    
@get('/ida')
def ida(id1 = None):
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    clani = modeli.vsi_clani()
    
    seznam_uporab_ida_vseh_clanov = []
    for i in clani:
        sez = []
        sez.append(i[0])
        sez.append(modeli.stevilo_uporab_ida_clana(i[0]))
        uporabe = modeli.poisci_uporabo_ida(i[0])
        sez1 = []
        for j in uporabe:
            sez1.append(j)
        sez.append(sez1)
        seznam_uporab_ida_vseh_clanov.append(sez)
    
    
    return template(
        'ida',
        seznam_uporab_ida_vseh_clanov = seznam_uporab_ida_vseh_clanov
        )


@get('/dodaj-uporabo-ida/')
def dodaj_uporabo_ida():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    intervencije = modeli.vse_intervencije()
    clani = modeli.vsi_clani()
    return template(
        'dodaj_uporabo_ida',
        intervencije = intervencije,
        clani = clani,
        intervencija = "",
        clan = ""
        )
@post('/dodaj-uporabo-ida/')
def dodaj_uporabo_ida():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    clani = modeli.vsi_clani()

    
    idd = bottle.request.forms.clan
    inte = bottle.request.forms.intervencija
    try:
        modeli.dodajUporaboIda(int(idd),int(inte))
    except: 
        return template('dodaj_uporabo_ida',
                        intervencije = modeli.vse_intervencije(),
                        clani = modeli.vsi_clani(),
                        intervencija = "",
                        clan = ""
                             )
    bottle.redirect('/ida')
                    


@get('/tecaji')
def tecaji():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    stevilo_tecajev = modeli.stevilo_tecajev()
    tecaji = modeli.vsi_tecaji()
    
    return template(
        'tecaji',
        stevilo_tecajev = stevilo_tecajev,
        tecaji = tecaji
    )
@get('/dodaj-tecaj/')
def dodaj_tecaj():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    return template(
        'dodaj_tecaj',
        naziv = ""
        )
@post('/dodaj-tecaj/')
def dodaj_vozilo():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    naziv = bottle.request.forms.naziv
    try:
        modeli.dodajTecaj(naziv)
    except:
        return template('dodaj_tecaj',
                            naziv = naziv
                            )

    bottle.redirect('/tecaji')

@get('/letno-porocilo')
def letno_porocilo():
    if not prijavljen_uporabnik():
        raise bottle.HTTPError(401)
    
    return template(
        'letno_porocilo'
    )

@get('/static/<filename>')
def staticna_datoteka(filename):
    return bottle.static_file(filename, root='static')
    

@get('/prijava')
def prijava():
    return template(
            'prijava',
            geslo = "",
            uporabnik = "",
        )
@post('/prijava')
def prijava():
    nazaj = bottle.request.POST.get('Nazaj')
    if nazaj is not None:
        bottle.redirect('/')
    
    prijavljen = modeli.uporabnik_baze(bottle.request.forms.geslo,
                                     bottle.request.forms.uporabnik)
    if prijavljen:
        bottle.response.set_cookie(
            'prijavljen', 'da', secret=SKRIVNOST, path='/')
        bottle.redirect('/izbira' )
    else:
        raise bottle.HTTPError(403, "Napačno geslo ali uporabniško ime!")

@get('/odjava/')
def odjava():
    bottle.response.set_cookie('prijavljen', '', path='/')
    bottle.redirect('/')    

@get('/registracija')
def registracija():
    return template(
            'registracija',
            ime = "",
            priimek = "",
            datumRojstva= "",
            naslov = "",
            email = "",
            uporabniskoIme= "",
            geslo = "",
            sporocilo = "",
            vrednost = ""
        )
@post('/registracija')
def registracija():
    nazaj = bottle.request.POST.get('Nazaj')
    if nazaj is not None:
        bottle.redirect('/')
    geslo = bottle.request.forms.geslo
    uporabniskoIme = bottle.request.forms.uporabniskoIme
        
    if not modeli.uporabnik_baze(geslo, uporabniskoIme):
        if modeli.uporabljeno_uporabniskoIme(uporabniskoIme):
            modeli.dodaj_uporabnika_baze(geslo,uporabniskoIme)
        else:
            raise bottle.HTTPError(403, "Uporabnik s tem uporabniškim imenom že obstaja!")

    else:
        raise bottle.HTTPError(403, "Uporabnik s tem uporabniškim imenom že obstaja!")
    bottle.redirect('/prijava')
    


run(debug= True)
