% rebase('osnovna_stran')

<div class = "columns">
<div class = "column is-one-fifth">
<aside class="menu">
  <p class="menu-label">
    Člani
  </p>
  <ul class="menu-list">
    <li><a class="is-active" href= "/clani">Vsi člani</a></li>
	<li><a href = /dodaj-clana/>Dodaj člana</a></li>
  </ul>
  <p class="menu-label">
    Intervencije
  </p>
  <ul class="menu-list">
    <li><a href = "/intervencije">Vse intervencije</a></li>
    <li><a>Dodaj intervencijo</a></li>
  </ul>
  <p class="menu-label">
    Vaje
  </p>
  <ul class="menu-list">
    <li><a>Vse vaje</a></li>
    <li><a>Dodaj vajo</a></li>
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
	<h1 class="title">
	Podatki člana:
</h1>

<h2 class="subtitle">
	{{ime}} {{priimek}}
</h2>

<h3 class="subtitle">
	Aktivnosti:
</h3>
%if len(aktivnosti)==0:
	/
%end

<ol>
	%for i in aktivnosti:
		<li> 
			<a href = "">
				{{i}}
			</a>
		</li>
	%end
</ol>

<a href = '/dodaj-clana/'>
	Dodaj člana
</a>
 </div>
</div>





