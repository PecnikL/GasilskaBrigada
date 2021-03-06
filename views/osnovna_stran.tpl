<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Baza PGD Hrušica</title>
	<link rel="shortcut icon" href="/static/icon.ico">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
  
  
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <img src="/static/logo.png"  height="112">
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
  



<section class="section">
    <div class="container">
	{{ !base }}
      
    </div>
  </section>

  
  <footer class="footer">
	<div class= "contant has-text-centered">
		<p>
			&copy; 2019 Lea Pečnik & Alenka Kejžar
		</p>
	</div>
	</footer>
  </body>
</html>