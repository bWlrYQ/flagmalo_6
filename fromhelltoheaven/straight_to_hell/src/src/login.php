<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=devide-width, initial-scale=1">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script src="js/bootstrap.bundle.min.js"></script>
		<title>Login</title>
		<link rel="icon" type="image/x-icon" href="img/logo.png">
		<style>.button-flag-malo{background-color: #8c56ac;}</style>
	</head>
	<body class="bg-dark text-light">
		<main>
			<div class="container">
				<a href="index.php"><img src="img/logo.png" alt="logo" class="mw-50 mx-auto d-block img-fluid mt-2"></a>
				<h2 class="text-center mt-2">FlagMalo</h2>
			</div>
			<div class="container mw-75">
				<hr>
			</div>
			<?php
			session_start();
			if($_SERVER['REQUEST_METHOD']=='GET'){
				if(isset($_SESSION['isMod'])){
					header('Location: profile.php');
				}else{
					echo '<div class="container w-25">
						<form action="login.php" method="POST">
							<div class="form-group">
								<label for="user">Username</label>
								<input type="text" class="form-control" id="user" placeholder="username" name="user">
							</div>
							<div class="form-groupe">
								<label for="pass">Password</label>
								<input type="password" class="form-control" id="pass" placeholder="password" name="pass">
							</div>
							<br>
							<div class="form-group d-grid mx-auto">
								<button type="submit" class="btn button-flag-malo text-center text-white">Login</button>
							</div>
						</form>
						<p class="text-center mt-1">Or register by clicking <a href="index.php">here</a></p>
					</div><br>';
				}
			}else if($_SERVER['REQUEST_METHOD']=='POST'){
				$user = filter_var($_POST['user'], FILTER_SANITIZE_SPECIAL_CHARS);
				$pass = filter_var($_POST['pass'], FILTER_SANITIZE_SPECIAL_CHARS);
                $jsonDB = json_decode(file_get_contents("files/61a428341f70fe7dd67f955fb43b3202/db.json"),true);
                $loggedIn = false;
                foreach($jsonDB as $key => $name){
                    if($name['username']==$user && $name['password']==md5($pass)){
                        $loggedIn=true;
                        $_SESSION['username']=$name['username'];
                        $_SESSION['id']=$name['id'];
                        $_SESSION['isMod']=$name['isMod'];
                        $_SESSION['isAdmin']=$name['isAdmin'];
                        break;
                    }
                }
                if($loggedIn){
                    echo'<div class="text-center container alert-success" role="alert">
                        Login successfull, please wait while you\'re being redirected.
                    </div>
                    <script>window.onload = function(){setTimeout(() => {location.replace("profile.php");}, 3000);}</script>';
                }else{
                    echo'<div class="text-center container alert-danger" role="alert">
					    Your password or username is incorrect, please try again.
				  	</div>
					<script>window.onload = function(){setTimeout(() => {location.replace("login.php");}, 3000);}</script>';
                }
			}else{
				http_response_code(403);
				die('Forbidden HTTP Method');
			}
			?>
		</main>
		<footer>
			<br>
			<div class="container text-center">
				<p class="text-secondary text-center">Made with ❤️ by bWlrYQ & Maxence</p>
                <?php
                if($_SESSION['id']){
                    echo'<br><a href="disconnect.php" class="text-secondary">Disconnect</a>';
                }
		if(isset($_COOKIE['ADMIN_COOKIE'])){if($_COOKIE['ADMIN_COOKIE']="e09c4bc5382d1e56f45c72208caae1a9"){echo ' | <a href="admin_panel.php" class="text-secondary">Admin Panel</a>';}}
		echo('<br>');
                ?>
			</div>
		</footer>
	</body>
</html>
