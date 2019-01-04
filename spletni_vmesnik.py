from bottle import get, run, template
import modeli

@get('/')
def glavna_stran():
    
    return template(
        'glavna_stran',
    )
@get('/clani')
def clani():
    clani = modeli.vsi_clani()
    return template(
        'clani',
        st_clanov = modeli.stevilo_clanov(),
        clani = clani
    )
@get('/clan/<id1>/')
def clan(id1):
    ime,priimek,datumRojstva,clanOd, zadnjiZdravniski = modeli.podatki_clana(int(id1))
    return template(
        'clan',
         podatki_clana = ime
    )
     
run(debug= True)
