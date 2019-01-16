% rebase('osnovna_stran_zacetek')


<h1 class ="title">Prijava v bazo PGD Hrušica.</h1>

<form action="prijava" method = "post">

<div class="field">
  <label class="label">Uporabniško ime</label>
  <div class="control has-icons-left has-icons-right">
    <input class="input" type="text" placeholder="Text input" name = "uporabnik" value="{{uporabnik}}">
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


<div class="field is-grouped">
  <div class="control">
    <button class="button is-link" type = "submit" value="Prijavi se">Prijava</button>
  </div>
  <div class="control">
    <button class="button is-text" type = "submit" name = "Nazaj" value="Nazaj">Prekliči</button>
  </div>
</div>

</form>
