<!DOCTYPE html>
<html lang="fr" dir="ltr">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ma Chocolaterie - Boutique</title>
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>

<body>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="index.php">Ma Chocolaterie</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" aria-current="page" href="index.php">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="token.php">Connection</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="shop.php">Boutique</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <?php
  require_once('vendor/autoload.php');

  use Firebase\JWT\JWT;
  use Firebase\JWT\Key;

  function decode(){
    $key = 'choco';
    $jwt = base64_decode($_COOKIE['JWT_TOKEN']);
    $decoded['droit'] = 'visiteur';
    try{
      if (isset($jwt) && !empty($jwt) && preg_match('/^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)/', $jwt)) {
        $decoded = json_decode(json_encode(JWT::decode($jwt, new Key($key, 'HS512'))), true);
        if($decoded['droit']=='membre'){
          return true;
        }
      }
    }catch(Exception $e){
      return false;
    }
  }
 if(isset($_COOKIE['JWT_TOKEN'])){
  if (decode()) {
    echo '<h1>FMCTF{JWT_IS_TO_E4SY}</h1><div class="container">
    <br>
    <div class="row">
      <div class="col-sm-3">
        <div class="card">
          <img src="src/berettaM9.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Beretta M9 9mm Parabellum</h5>
            <p class="card-text">Prix : 200€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
      <div class="col-sm-3">
        <div class="card">
          <img src="src/colt1911.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">SIG SAUER 1911 22Lr</h5>
            <p class="card-text">Prix : 350€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
      <div class="col-sm-3">
        <div class="card">
          <img src="src/smith&wessonMagnum.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Smith & Wesson 629 .44 Magnum</h5>
            <p class="card-text">Prix : 1859.95€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
      <div class="col-sm-3">
        <div class="card">
          <img src="src/desertEagle.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Desert Eagle L5 cal.44 Magnum</h5>
            <p class="card-text">Prix : 3569.95€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
    </div>
    <br>
  </div>';
  } else {
    echo '<div class="container">
    <br>
    <div class="row">
      <div class="col-sm-3">
        <div class="card">
          <img src="src/choco1.webp" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Barre de chocolat Noir et Chocolat au Lait au Nougat</h5>
            <p class="card-text">Prix : 2€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
      <div class="col-sm-3">
        <div class="card">
          <img src="src/choco2.webp" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Barre de chocolat au Lait et Praliné Noisettes Entières</h5>
            <p class="card-text">Prix : 2€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
      <div class="col-sm-3">
        <div class="card">
          <img src="src/choco3.webp" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Barre Écorce Chocolat Noir, Cranberries et Muesli</h5>
            <p class="card-text">Prix : 2€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
      <div class="col-sm-3">
        <div class="card">
          <img src="src/choco4.webp" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Barre Écorce Chocolat au Lait et Noisettes</h5>
            <p class="card-text">Prix : 2€</p>
            <a href="#" class="btn btn-success disabled">Acheter</a>
          </div>
        </div>
      </div>
    </div>
    <br>
  </div>';
  }}else{
    echo "<h1>Vous devez être connecté pour voir ici</h1>";
  };
  ?>
  <!-- JavaScript Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
</body>

</html>