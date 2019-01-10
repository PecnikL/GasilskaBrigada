from bottle import get, run, template
import modeli

@get('/')
def glavna_stran():
    
    return template(
        'glavna_stran',
    )

@get('/clani')
@get('/clani/<id1>/')
def clani(id1=None):
    if id1 == None:
        clani = modeli.vsi_clani()
        return template(
            'clani',
            st_clanov = modeli.stevilo_clanov(),
            clani = clani
        )
    else:
        if len(modeli.podatki_clana(int(id1))) == 5:
            ime,priimek,datumRojstva,clanOd, zadnjiZdravniski = modeli.podatki_clana(int(id1))
            return template(
                'clan',
                ime = ime,
                priimek = priimek,
                datumRojstva = datumRojstva,
                clanOd = clanOd,
                zadnjiZdravniski = zadnjiZdravniski
            )
        elif len(modeli.podatki_clana(int(id1))) == 6:
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
     
@get('/intervencije')
@get('/intervencije/<id1>/')
def intervencije(id1 = None):
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


@get('/prijava')
def prijava():
    return template(
            'prijava',
            geslo = None,
            uporabnik = None,
        )


@get('/registracija')
def registracija():
    return template(
            'registracija',
        )


run(debug= True)
