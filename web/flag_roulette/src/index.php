<?php session_start(); 
if(!isset($_SESSION['balance'])){
  $_SESSION['balance']=0;
}
?>
<html>
  <head>
    <title>Roulette</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="static/bootstrap.min.css" rel="stylesheet" media="screen">
    <script src="static/bootstrap.bundle.min.js"></script>
    <script src="static/roulette.js" defer></script>
  </head>
  <body class="bg-dark text-light">
    <div class="container">
      <a href="/"><img src="static/logo.png" alt="logo" class="mw-50 mx-auto d-block img-fluid mt-2"></a>
      <h2 class="text-center">Flag Roulette</h2>
      <hr>
    </div>
    <div class="container w-25 text-center">
      <h5 id="balance">Balance: <?php echo $_SESSION['balance']; ?>$</h5>
      <div class="d-flex justfiy-content-center">
        <canvas id="canvas" width="500" height="500"></canvas>
      </div>
      <input type="button" value="spin" id='spin' />
    </div>
  </body>
  <footer>
    <br>
    <div class="container text-center">
        <p class="text-secondary text-center">Made with ❤️ by Matthieu</p>
    </div>
  </footer>
</html>

<?php
if($_SERVER['REQUEST_METHOD']=="POST"){
  $toBalance = $_POST['balance'];
  if($toBalance=="reset"){
    $_SESSION['balance']=0;
  }elseif($toBalance=="🚩 Flag"){
    flag();
  }else{
    $_SESSION['balance']+=(int)str_replace("$","",$toBalance);
    $balance=$_SESSION['balance'];
    echo("<script>document.getElementById('balance').innerHTML='Balance: $balance$'</script>");
    if($_SESSION['balance']>99999999999999999){
      flag();
    }
  }
}

function flag(){
  echo("<script>alert('Well done, flag is FMCTF{I_HatE_Ch3@teRz}')</script>");
}
?>