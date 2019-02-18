% rebase('osnovna_stran')

% rebase('osnovna_stran')


<div class = "columns">
<div class = "column is-one-fifth">
<aside class="menu">
  <p class="menu-label">
    Člani
  </p>
  <ul class="menu-list">
    <li><a href= "/clani">Vsi člani</a></li>
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
    <li><a class="is-active" href = "/vaje" >Vse vaje</a></li>
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
	


<h2 class ="title is-2">Vaje PGD Hrušica</h2>

<h3 class ="title is-3">Pretekle vaje</h3>

( Začetek, Začetek ura, Konec, Konec ura, Kraj )

<ol>
	%for id, zacetek, zacetekUra, konec, konecUra, kraj in vaje:
		<li> 
			<a href = "/vaje/{{id}}/">
				{{zacetek}}, {{zacetekUra}}, {{konec}}, {{konecUra}}, {{kraj}}
			</a>
		</li>
	%end

</ol>



<br>

<label for="start">Datum vaje:</label>
<input type="date" id="start" name="trip-start"
       value=""
       min="" max="">
<input type="submit" value="Poišči">


<br>
<br>
<a href = '/dodaj-vajo/'>
	Dodaj vajo
</a>

 </div>
</div>





