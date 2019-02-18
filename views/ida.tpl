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




( Id-člana, Število uporab, (intervencije na katerih je bil uporabljen) )

<ol>
	%for i in seznam_uporab_ida_vseh_clanov:
		<li> 
		%for j in range(len(i)):
				%if j == 0:
					<a href= "/clani/{{i[0]}}/">{{i[0]}}</a>,
				%end
				%if j==1:
					{{i[1]}},
				%end
				%if j==2:
				[
					%for k in range(len(i[2])):
						<a href= "/intervencije/{{i[2][k][0]}}/">{{i[2][k][0]}}</a>
						%if k!= len(i[2])-1:
							,
							
						%end
					%end
				]
				%end
		
		%end
		<br>
		</li>
	%end	
</ol>



<br>
<br>
<a href = '/dodaj-uporabo-ida/'>
	Dodaj uporabo IDA
</a>

 </div>
</div>