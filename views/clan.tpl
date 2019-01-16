% rebase('osnovna_stran')


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

