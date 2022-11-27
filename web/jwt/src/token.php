<!DOCTYPE html>
<html lang="fr" dir="ltr">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ma Chocolaterie - Connection</title>
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  <!-- JavaScript Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
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
            <a class="nav-link active" href="token.php">Connection</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="shop.php">Boutique</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <br>
  <?php if(!isset($_COOKIE['JWT_TOKEN'])){?>
  <form method="post" action="token.php">
    <div class="mb-3">
      <label for="email" class="form-label">Adresse Email</label>
      <input type="email" class="form-control" name="email" id="email" aria-describedby="emailHelp">
      <div id="emailHelp" class="form-text">Vos informations seront uniquement utilisé pour vous envoyez un mail de contacte.</div>
    </div>
    <button type="submit" name="log" id="log" class="btn btn-primary">Submit</button>
  </form>
  <?php
  }else{
    echo '<h1>Vous êtes déjà connecté</h1>
    <form method="post" action="token.php">
    <label for="deco" class="form-label">Voulez-vous vous déconnectez ?</label>
    <button type="submit" name="del" class="btn btn-primary">Déconnection</button>
    </form>';
  }
  require_once('vendor/autoload.php');

  use Firebase\JWT\JWT;
  use Firebase\JWT\Key;

  function refresh(){
    unset($_COOKIE['JWT_TOKEN']);
    setcookie("JWT_TOKEN", "", time() - 3600);
    header('Location: token.php');
  }
  function generate()
  {
    $droit = 'visiteur';
    if(htmlspecialchars($_POST['email'])=="4dm1n@ch0c0l4t.com"){
      $droit = 'membre';
    }
    $key = 'choco';
    $payload = [
      'ip' => $_SERVER["REMOTE_ADDR"],
      'droit' => $droit,
      'mail' => htmlspecialchars($_POST['email'])
    ];

    $jwt = base64_encode(JWT::encode($payload, $key, 'HS512'));
    setcookie(
      'JWT_TOKEN',
      $jwt,
      [
        'expires' => time() + 365 * 24 * 3600,
        'secure' => true,
        'httponly' => false,
      ]
    );
    header('Location: index.php');
  }
  if (isset($_POST['log'])) {
    generate();
  } elseif (isset($_POST['del'])) {
    refresh();
  }
  ?>
</body>
</html>