% rebase('osnovna_stran')

<h1 class ="title"> Trenutno je v bazi {{ st_clanov }} čalonov: </h1>



<ol>
	%for id, ime, priimek, datumRojstva, clanOd, zadnjiZdravniski in clani:
		<li> 
			<a href = "/clani/{{id}}/">
				{{ime}} {{priimek}}, {{datumRojstva}}, {{clanOd}}, {{zadnjiZdravniski}} 
			</a>
		</li>
	%end

</ol>