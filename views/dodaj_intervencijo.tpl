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
	<li><a class="is-active" href = /dodaj-intervencijo/>Dodaj intervencijo</a></li>
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
	
<h1 class ="title"> Dodaj intervencijo: </h1>

<form method="post">

Začetek: <input type="text" name="zacetek" value="{{zacetek}}" /><br />

Začetek ura: <input type="text" name="zacetekUra" value="{{zacetekUra}}" /><br />

Konec: <input type="text" name="konec" value="{{konec}}" /><br />

Konec ura: <input type="text" name="konecUra" value="{{konecUra}}" /><br />

Opomba: <input type="text" name="opomba" value="{{opomba}}" /><br />

Opis: <input type="text" name="opis" value="{{opis}}" /><br />

Kraj: <input type="text" name="kraj" value="{{kraj}}" /><br />

Kilometri: <input type="text" name="kilometri" value="{{kilometri}}" /><br />


<input type = "submit" value = "Dodaj intervencijo">
</form>


 </div>
</div>
