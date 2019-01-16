<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
  
  
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="https://bulma.io">
      <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
    </a>

    <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item" href= "/izbira">
        Domov
      </a>

      <a class="navbar-item">
        Dokumentacija
      </a>

      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          Več
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            O aplikaciji
          </a>
          <a class="navbar-item">
            Jobs
          </a>
          <a class="navbar-item">
            Contact
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Report an issue
          </a>
        </div>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
		  <a href= "/odjava/" class="button is-light">Odjava</a>
        </div>
      </div>
    </div>
  </div>
</nav>  
  

<div class = "columns" style= "margin-left:10px; margin-top: 50px">
<div class = "column is-one-fifth">
<aside class="menu">
  <p class="menu-label">
    Člani
  </p>
  <ul class="menu-list">
    <li><a class="is-active">Vsi člani</a></li>
	<li><a>Dodaj člana</a></li>
  </ul>
  <p class="menu-label">
    Intervencije
  </p>
  <ul class="menu-list">
    <li><a>Vse intervencije</a></li>
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

<section class="section">
    <div class="container">
	{{ !base }}
      
    </div>
  </section>

</div>
</div>
  
  <footer class="footer">
	<div class= "contant has-text-centered">
		<p>
			&copy; 2019 Lea Pečnik & Alenka Kejžar
		</p>
	</div>
	</footer>
  </body>
</html>