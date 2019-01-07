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
        ime,priimek,datumRojstva,clanOd, zadnjiZdravniski = modeli.podatki_clana(int(id1))
        return template(
            'clan',
             podatki_clana = ime
        )
     


@get('/prijava')
def prijava():
    return template(
            'prijava',
        )

run(debug= True)
