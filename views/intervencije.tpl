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
    <li><a class="is-active" href = "/intervencije">Vse intervencije</a></li>
    <li><a href = "/dodaj-intervencijo/">Dodaj intervencijo</a></li>
  </ul>
  <p class="menu-label">
    Vaje
  </p>
  <ul class="menu-list">
    <li><a href = "/vaje">Vse vaje</a></li>
    <li><a href = "/dodaj-vajo/">Dodaj vajo</a></li>
  </ul>
  <p class="menu-label">
    Vozila
  </p>
  <ul class="menu-list">
    <li><a>Podatki o vozilih</a></li>
    <li><a>Dodaj vozilo</a></li>
    <li><a>Odstrani vozilo</a></li>
  </ul>
  <p class="menu-label">
    Uporaba IDA
  </p>
  <ul class="menu-list">
    <li><a>Podatki o uporabi IDA</a></li>
  </ul>
  <p class="menu-label">
    Tečaji
  </p>
  <ul class="menu-list">
    <li><a>Vsi tečaji</a></li>
    <li><a>Dodaj tečaj</a></li>
  </ul>
  <p class="menu-label">
    Drugo
  </p>
  <ul class="menu-list">
    <li><a>Letno poročilo</a></li>
    <li><a>Uporabniki baze</a></li>
  </ul>
</aside>
</div>
<div class ="column">
	


<h2 class ="title is-2">Intervencije PGD Hrušica</h2>

<h3 class ="title is-3">Pretekle intervencije</h3>

( Začetek, Začetek ura, Konec, Konec ura, Kraj )

<ol>
	%for zacetek, zacetekUra, konec, konecUra, kraj in interv:
		<li> 
			<a href = "/intervencije/{{id}}/">
				{{zacetek}}, {{zacetekUra}}, {{konec}}, {{konecUra}}, {{kraj}}
			</a>
		</li>
	%end

</ol>





<!--Make sure the form has the autocomplete function switched off:-->
<form autocomplete="off" action="/action_page.php">
  <div class="autocomplete" style="width:300px;">
    <input id="myInput" type="text" name="myCountry" placeholder="Kraj intervencije">
  </div>
  <label for="start">Datum intervencije:</label>

	<input type="date" id="start" name="trip-start"
       value=""
       min="" max="">
	<input type="submit" value="Poišči">
</form>

<h3 class ="title is-3">Dodaj intervencijo</h3>

 </div>
</div>




