% rebase('osnovna_stran')


<h1 class="title">
	Rezultati iskanja članov:
</h1>

(Ime, priimek, datum rojstva)
<ol>
	%for id, ime,priimek,datumRojstva in clani:
		<li> 
			<a href = "/clani/{{id}}/">
				{{ime}}, {{priimek}}, {{datumRojstva}}
			</a>
		</li>
	%end
</ol>



<a href = '/dodaj-clana/'>
	Dodaj člana
</a>

