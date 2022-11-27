<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=devide-width, initial-scale=1">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script src="js/bootstrap.bundle.min.js"></script>
		<title>Home</title>
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
					echo '<div class="container w-75">
						<div class="alert button-flag-malo text-center" role="alert">
							Welcome, registrations are currently <strong>closed</strong> you may come back later.
						</div>
					</div>';
					echo '<div class="container w-25">
						<form action="index.php" method="POST">
							<div class="form-group">
								<label for="user">Username</label>
								<input type="text" class="form-control" id="user" placeholder="username" name="user">
							</div>
							<div class="form-group">
								<label for="mail">Mail</label>
								<input type="email" class="form-control" id="mail" placeholder="e-mail" name="mail">
							</div>
							<div class="form-groupe">
								<label for="pass">Password</label>
								<input type="password" class="form-control" id="pass" placeholder="password" name="pass">
							</div>
							<div class="form-group">
								<input id="registration" name="createAcc" type="hidden" value="off">
							</div>
							<br>
							<div class="form-group d-grid mx-auto">
								<button type="submit" class="btn button-flag-malo text-center text-white" disabled>Register</button>
							</div>
						</form>
						<p class="text-center mt-1">Or login by clicking <a href="login.php">here</a></p>																																																							<!-- Flag #1: FMCTF{1nsp3ct1ng_C0d3_1s_4lways_Th3_1st_StEp} -->
					</div><br>';
				}
			}else if($_SERVER['REQUEST_METHOD']=='POST'){
				$user = filter_var($_POST['user'], FILTER_SANITIZE_SPECIAL_CHARS);
				$pass = filter_var($_POST['pass'], FILTER_SANITIZE_SPECIAL_CHARS);
				$mail = filter_var($_POST['mail'],FILTER_SANITIZE_EMAIL);
				$createAcc = filter_var($_POST['createAcc'], FILTER_SANITIZE_SPECIAL_CHARS);
				$userExists = false;
				if($createAcc=="on"){
					$jsonDB = json_decode(file_get_contents("files/61a428341f70fe7dd67f955fb43b3202/db.json"),true);
					if(strlen($user)>2){
						if(strlen($mail)>2){
							if(strlen($pass)>2){
								foreach($jsonDB as $key => $name){
									if($name['username'] == $user){
										$userExists = true;
										echo'<div class="text-center container" role="alert">
											The username you entered is already taken, please chose another one.
									  	</div>
										<script>window.onload = function(){setTimeout(() => {location.replace("index.php");}, 3000);}</script>';
										break;
									}
								}
								if(!$userExists){
									$allIds = array();
									$possibleId = rand(0,5000);
									foreach($jsonDB as $key => $name){
										array_push($allIds,$name['id']);
									}
									if(in_array($possibleId, $allIds)){
										while(in_array($possibleId)){
											$possibleId = rand(0,5000);
										}
									}
									array_push($jsonDB, array(
										"username" => $user,
										"mail" => $mail,
										"id" => $possibleId,
										"password" => md5($pass),
										"isMod" => false,
										"isAdmin" => false,
										"note" => "Flag #2 : FMCTF{D0nt_Base_S3cur1ty_0n_Us3r_C0ntrolled_Par@m3ters}"
									));
									file_put_contents("files/61a428341f70fe7dd67f955fb43b3202/db.json", json_encode($jsonDB));
									$_SESSION['username']=$user;$_SESSION['id']=$possibleId;$_SESSION['isMod']=false;$_SESSION['isAdmin']=false;
									echo'<div class="text-center container alert-success" role="alert">
										Your registration is complete, you can now log in.
				  					</div>
									<script>window.onload = function(){setTimeout(() => {location.replace("profile.php");}, 3000);}</script>';
								}
							}else{
								echo'<div class="text-center container alert-danger" role="alert">
									Your password is too short, please chose a longer one.
				  				</div>
								<script>window.onload = function(){setTimeout(() => {location.replace("index.php");}, 3000);}</script>';
							}
						}else{
							echo'<div class="text-center container alert-danger" role="alert">
								Your e-mail is too short, please chose a longer one.
				  			</div>
							<script>window.onload = function(){setTimeout(() => {location.replace("index.php");}, 3000);}</script>';
						}
					}else{
						echo'<div class="text-center container container alert-danger" role="alert">
							Your username is too short, please chose a longer one.
				  		</div>
						<script>window.onload = function(){setTimeout(() => {location.replace("index.php");}, 3000);}</script>';
					}
				}else{
					echo'<div class="text-center container alert-danger" role="alert">
						Are you really trying to bypass my security ? Lol...
						</div>
					<script>window.onload = function(){setTimeout(() => {location.replace("index.php");}, 3000);}</script>';
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
               echo '<br>';
	       ?>
			</div>
		</footer>
	</body>
</html>
