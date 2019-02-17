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
	<li><a href = "/dodaj-intervencijo/">Dodaj intervencijo</a></li>
  </ul>
  <p class="menu-label">
    Vaje
  </p>
  <ul class="menu-list">
    <li><a href = "/vaje">Vse vaje</a></li>
    <li><a class="is-active" href = "/dodaj-vajo/">Dodaj vajo</a></li>
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
	
<h1 class ="title"> Dodaj vajo: </h1>

<form method="post">

zacetek: <input type="text" name="zacetek" value="{{zacetek}}" /><br />

zacetekUra: <input type="text" name="zacetekUra" value="{{zacetekUra}}" /><br />

konec: <input type="text" name="konec" value="{{konec}}" /><br />

konecUra: <input type="text" name="konecUra" value="{{konecUra}}" /><br />

opomba: <input type="text" name="opomba" value="{{opomba}}" /><br />

opis: <input type="text" name="opis" value="{{opis}}" /><br />

kraj: <input type="text" name="kraj" value="{{kraj}}" /><br />

kilometri: <input type="text" name="kilometri" value="{{kilometri}}" /><br />


<input type = "submit" value = "Dodaj vajo">
</form>


 </div>
</div>