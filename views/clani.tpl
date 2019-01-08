% rebase('osnovna_stran')

<h1 class ="title"> Trenutno je v bazi {{ st_clanov }} članov: </h1>

( Ime Priimek, datum rojstva, član od, zadnji zdravniški )

<ol>
	%for id, ime, priimek, datumRojstva, clanOd, zadnjiZdravniski in clani:
		<li> 
			<a href = "/clani/{{id}}/">
				{{ime}} {{priimek}}, {{datumRojstva}}, {{clanOd}}, {{zadnjiZdravniski}} 
			</a>
		</li>
	%end

</ol>