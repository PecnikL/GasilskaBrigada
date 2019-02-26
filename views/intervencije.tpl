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
	


<h2 class ="title is-2">Intervencije PGD Hrušica</h2>

<h3 class ="title is-3">Pretekle intervencije</h3>
<table style="width:100%">
<thead>
<tr>
<th> Začetek </th>
<th> Začetek ura </th>
<th> Konec </th>
<th> Konec ura </th>
<th> Kraj </th>
</tr>
</thead>
<tbody>

	%for id, zacetek, zacetekUra, konec, konecUra, kraj in interv:
		<tr> 
				<td> <a href = "/intervencije/{{id}}/" > {{zacetek}} </a> </td>
				<td> <a href = "/intervencije/{{id}}/" > {{zacetekUra}} </a> </td>
				<td> <a href = "/intervencije/{{id}}/" > {{konec}} </a> </td> 
				<td> <a href = "/intervencije/{{id}}/" > {{konecUra}} </a> </td> 
				<td> <a href = "/intervencije/{{id}}/" > {{kraj}} </a> </td>
		</tr>
	%end


</tbody>
</table>



<br>

<label for="start">Datum intervencije:</label>
<input type="date" id="start" name="trip-start"
       value=""
       min="" max="">
<input type="submit" value="Poišči">


<br>
<br>
<a href = '/dodaj-intervencijo/'>
	Dodaj Intervencijo
</a>

 </div>
</div>




