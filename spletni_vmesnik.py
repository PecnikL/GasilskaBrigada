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
        return template(
            'clan',
            ime = ime,
            priimek = priimek,
            datumRojstva = datumRojstva,
            clanOd = clanOd,
            zadnjiZdravniski = zadnjiZdravniski,
            aktivnosti = aktivnosti
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
    try:
        id = modeli.dodajClana(ime = bottle.request.forms.ime,
                               priimek = bottle.request.forms.priimek,
                               datumRojstva = bottle.request.forms.datumRojstva,
                               clanOd = bottle.request.forms.clanOd,
                               zadnjiZdravniski = bottle.request.forms.zadnjiZdravniski)
    except:
        return template('dodaj_clana',
                        ime = bottle.request.forms.ime,
                        priimek = bottle.request.forms.priimek,
                        datumRojstva = bottle.request.forms.datumRojstva,
                        clanOd = bottle.request.forms.clanOd,
                        zadnjiZdravniski = bottle.request.forms.zadnjiZdravniski)

    bottle.redirect('/clani')

    
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
        return template(
            'intervencija'
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
    try:
        id = modeli.dodajIntervencijo(vrsta = 'intervencija',
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

    bottle.redirect('/intervencije')

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
        return template(
            'vaja'
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
    try:
        id = modeli.dodajVajo(
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

    bottle.redirect('/vaje')


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
