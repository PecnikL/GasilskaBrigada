% rebase('osnovna_stran')

<div class = "columns">
<div class = "column is-one-fifth">
<aside class="menu">
  <p class="menu-label">
    Člani
  </p>
  <ul class="menu-list">
    <li><a class="is-active" href= "/clani">Vsi člani</a></li>
	<li><a href = "/dodaj-clana/">Dodaj člana</a></li>
  </ul>
  <p class="menu-label">
    Intervencije
  </p>
  <ul class="menu-list">
    <li><a href = "/intervencije">Vse intervencije</a></li>
	<li><a href = /dodaj-intervencijo/>Dodaj intervencijo</a></li>
  </ul>
  <p class="menu-label">
    Vaje
  </p>
  <ul class="menu-list">
    <li><a href = "/vaje" >Vse vaje</a></li>
    <li><a href = "/dodaj-vajo/">Dodaj vajo</a></li>
  </ul>
  <p class="menu-label">
    Vozila
  </p>
  <ul class="menu-list">
    <li><a href="/vozila">Podatki o vozilih</a></li>
    <li><a href="/dodaj-vozilo/">Dodaj vozilo</a></li>
  </ul>
  <p class="menu-label">
    Uporaba IDA
  </p>
   <ul class="menu-list">
    <li><a href = "/ida">Podatki o uporabi IDA</a></li>
	<li><a  href = "/dodaj-uporabo-ida/">Doda uporabo IDA</a></li>
  </ul>
  <p class="menu-label">
    Tečaji
  </p>
  <ul class="menu-list">
    <li><a href="/tecaji">Vsi tečaji</a></li>
    <li><a  href = "/dodaj-tecaj/">Dodaj tečaj</a></li>
  </ul>
  <p class="menu-label">
    Drugo
  </p>
  <ul class="menu-list">
    <li><a href = "/letno-porocilo">Letno poročilo</a></li>
  </ul>
</aside>
</div>
<div class ="column">
<h1 class="title">
	Podatki člana:
</h1>
<br>
<h2 class="subtitle">
	{{ime}} {{priimek}}
</h2>

Datum rojstva: {{datumRojstva}}<br>
Član od: {{clanOd}}<br>
Zadnji zdravniški pregled je bil opravljen dne: {{zadnjiZdravniski}}<br>
<br>


<h3 class="subtitle">
	Aktivnosti:
</h3>
%if len(vse_aktivnosti)==0:
	/ 
	<br>
	<br>


%else:
<ol>
(Začetek datum, Konec datum, kraj)
%for id, zacetek,konec, opis, kraj in vse_aktivnosti:
	<li> 
		<a href = "">
			{{zacetek}}, {{konec}} , {{kraj}}
		</a>
	</li>
</ol>
<br>
%end
%end

Nazaj na: <br>
<a href = '/clani'>
	Vsi člani
</a>
<br>
<a href = '/dodaj-clana/'>
	Dodaj člana
</a>
%end

<ol>
</div>
</div>





