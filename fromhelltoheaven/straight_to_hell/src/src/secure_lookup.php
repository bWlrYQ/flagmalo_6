<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=devide-width, initial-scale=1">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script src="js/bootstrap.bundle.min.js"></script>
		<title>Secure Lookup</title>
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
			$isBot = false;
			if($_SERVER['HTTP_USER_AGENT']=="wh4t_a_cuT3_b0T_R1gHt"){$isBot=true;echo(urldecode($_GET['user']));}else{session_start();}
			if(!$isBot){
                if($_SERVER['REQUEST_METHOD']=='GET'){
                    if($_SESSION['isMod']==true){
                        $user="";
                        echo'<div class="container text-center">
                            <h4>User Lookup</h4>
                            <p>Type in the username of a user to get every information concerning him</p>
                        </div>
                        <div class="container w-25">
                            <form class="form-inline" action="secure_lookup.php" method="GET">
                                <div class="form-group mx-sm-3 mb-2">
                                    <input type="text" class="form-control" id="user" placeholder="username" name="user">
                                </div>
                                <div class="form-group d-grid mx-auto">
                                    <button type="submit" class="btn button-flag-malo text-center text-white">Search</button>
                                </div>
                            </form>
                        </div><br>';
                        $found = false;
                        if(isset($_GET['user'])){
                            $user = $_GET['user'];
                            $jsonDB = json_decode(file_get_contents("files/61a428341f70fe7dd67f955fb43b3202/db.json"),true);
                            $pseudo;$mail;$isMod;$isAdmin;$password;      
                            foreach($jsonDB as $key => $name){
                                if($name['username'] == $user){ 
                                    $found = true;           
                                    $pseudo=$name['username'];
                                    $mail=$name['mail'];
                                    $isMod=$name['isMod'];
                                    if($isMod){$isMod="<span class='text-success'>Yes<span>";}else{$isMod="<span class='text-danger'>No<span>";}
                                    $isAdmin=$name['isAdmin'];
                                    if($isAdmin){$isAdmin="<span class='text-success'>Yes<span>";}else{$isAdmin="<span class='text-danger'>No<span>";}
                                    $note=$name['note']; 
                                    $pass=$name['password'];
                                }
                            }
                        }
                        if($found){
                            echo'<div class="d-flex justify-content-center">
                            <div class="card text-center text-dark" style="width: 18rem;">
                                <img src="img/avatar.png" class="card-img-top" alt="...">
                                    <div class="card-body">
                                        <h5 class="card-title">'.$pseudo.'</h5>
                                        <p class="card-text">Note: '.$note.'</p>
                                    </div>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">Mail: '.$mail.'</li>
                                    <li class="list-group-item">Moderator: '.$isMod.'</li>
                                    <li class="list-group-item">Administrator: '.$isAdmin.'</li>
                                    <li class="list-group-item">Password (hash): '.$pass.'</li>
                                </ul>
                            </div>
                        </div>';
                        }else if(!$found && isset($_GET['user'])){
                            echo('<h4 class="text-center">'.$user.' not found</h4>');
                        }

                        echo'<div class="container text-light text-center w-50">
                            <hr>
                            <h4>Bug Report</h4>
                            <p>If you find a bug, just submit the full link here so that admins can review it (mod job, you know)</p>
                            <div class="container w-50">
                                <form class="form-inline" action="bug_reports.php" method="POST">
                                    <div class="form-group mx-sm-3 mb-2">
                                        <input type="text" class="form-control" id="link" placeholder="link" name="link">
                                    </div>
                                    <div class="form-group d-grid mx-auto">
                                        <button type="submit" class="btn button-flag-malo text-center text-white">Report</button>
                                    </div>
                                </form>
                            </div><br>
                        </div>';
                    }else{
                        echo'<div class="text-center container alert-danger" role="alert">
                            You must be logged in and be a moderator to access this page.
                        </div>
                        <script>window.onload = function(){setTimeout(() => {location.replace("login.php");}, 3000);}</script>';
                    }
                }else if($_SERVER['REQUEST_METHOD']=='POST'){

                }else{
                    http_response_code(403);
                    die('Forbidden HTTP Method');
                }
			}?>
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
                ?>
			</div>
		</footer>
	</body>
</html>
