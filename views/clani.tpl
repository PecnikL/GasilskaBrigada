Trenutno je v bazi {{ st_clanov }} čalonov: 



<ol>
	%for id, ime, priimek, datumRojstva, clanOd, zadnjiZdravniski in clani:
		<li> 
			<a href = "/clan/{{id}}/">
				{{ime}} {{priimek}}, {{datumRojstva}}, {{clanOd}}, {{zadnjiZdravniski}} 
			</a>
		</li>
	%end

</ol>