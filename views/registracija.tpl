% rebase('osnovna_stran_zacetek')


<h1 class ="title">Registracija</h1>

<form action="registracija" method = "post">
<div class="field">
  <label class="label">Ime</label>
  <div class="control">
    <input class="input" type="text" placeholder="Text input" name = "ime" value="{{ime}}">
  </div>
</div>

<div class="field">
  <label class="label">Priimek</label>
  <div class="control">
    <input class="input" type="text" placeholder="Text input" name = "priimek" value="{{priimek}}">

  </div>
</div>

<div class="field">
  <label class="label">Datum rojstva</label>
  <div class="control">
    <input class="input" type="text" placeholder="Text input" name = "datumRojstva" value="{{datumRojstva}}">

  </div>
</div>

<div class="field">
  <label class="label">Naslov</label>
  <div class="control">
    <input class="input" type="text" placeholder="Text input" name = "naslov" value="{{naslov}}">
	

  </div>
</div>

<div class="field">
  <label class="label">Email</label>
  <div class="control has-icons-left has-icons-right">
    <input class="input" type="email" placeholder="Vnesite vaš email" name ="email" value="{{email}}">

    <span class="icon is-small is-left">
      <i class="fas fa-envelope"></i>
    </span>
    <span class="icon is-small is-right">
      <i class="fas fa-exclamation-triangle"></i>
    </span>
  </div>
</div>

<div class="field">
  <label class="label">Uporabniško ime</label>
  <div class="control has-icons-left has-icons-right">
    <input class="input" type="text" placeholder="Text input" name = "uporabniskoIme" value="{{uporabniskoIme}}">
    <span class="icon is-small is-left">
      <i class="fas fa-user"></i>
    </span>
    <span class="icon is-small is-right">
      <i class="fas fa-check"></i>
    </span>
  </div>
</div>

<div class="field">
  <label class="label">Geslo</label>
  <p class="control has-icons-left">
	<input class="input" type="password" placeholder="Geslo" name = "geslo" value ="{{geslo}}" id="pwd">
    <span class="icon is-small is-left">
      <i class="fas fa-lock"></i>
    </span>
  </p>
</div>

<div class="field">
  <label class="label">Sporočilo</label>
  <div class="control">
    <textarea class="textarea" placeholder="" name = "sporocilo" value="{{sporocilo}}"></textarea>
  </div>
</div>

<div class="field">
  <div class="control">
    <label class="checkbox">
      <input type="checkbox">
      Strinjam se z <a href="#">danimi pogoji</a>
    </label>
  </div>
</div>



<div class="field is-grouped">
  <div class="control">
    <button class="button is-link" type = "submit" value="Registriraj se">Registriraj se</button>
  </div>
  <div class="control">
    <button class="button is-text" type = "submit" name = "Nazaj" value="Nazaj">Prekliči</button>
  </div>
</div>
</form>