% rebase('osnovna_stran')


<div class = "columns">
<div class = "column is-four-fifth">
<h1 class ="title"> Trenutno je v bazi {{ st_clanov }} članov: </h1>

<form action="iskanje-clanov/" method ="get" _lpchecked="1">
	<input type="text" name="ime_priimek" value="">
	<input type="submit" value="išči">
</form>

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


<a href = '/dodaj-clana/'>
	Dodaj člana
</a>


</div>
</div>