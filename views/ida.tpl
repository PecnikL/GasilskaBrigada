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
    <li><a class="is-active" href = "/ida">Podatki o uporabi IDA</a></li>
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
	


<h2 class ="title is-2">Podatki o uporabi IDA</h2>

<table style="width:70%">
<thead>
<tr>
<th> Id-člana </th>
<th> Število uporab </th>
<th> Intervencije na katerih je bil uporabljen </th>
</tr>
</thead>
<tbody>


	
	%for i in seznam_uporab_ida_vseh_clanov:
		<tr> 
		%for j in range(len(i)):
				%if j == 0:
					<td><a href= "/clani/{{i[0]}}/">{{i[0]}}</a> </td>
				%end
				%if j==1:
					<td>{{i[1]}}</td>
				%end
				%if j==2:
				<td>
				[
					%for k in range(len(i[2])):
						<a href= "/intervencije/{{i[2][k][0]}}/">{{i[2][k][0]}}</a>
						%if k!= len(i[2])-1:
							,
							
						%end
					%end
				]
				<td>
				%end
		
		%end
		</tr>
	%end	


</tbody>
</table>




<br>
<br>
<a href = '/dodaj-uporabo-ida/'>
	Dodaj uporabo IDA
</a>

 </div>
</div>