<?php session_start()?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=devide-width, initial-scale=1">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script src="js/bootstrap.bundle.min.js"></script>
		<title>Profile</title>
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
                <?php
                if($_SESSION['isMod'] == true && $_GET['id']==13){
                    echo'<div class="container text-center">
                            <h4><a href="secure_lookup.php" class="link-light text-decoration-none">Secure Lookup</a></h4>
                    </div>
                <hr>
                <div class="alert alert-success text-center" role="alert">
                    Well done ! Flag #3: FMCTF{1D0R_r3@lly_1s_D4ngEr0uS_N0?}
                </div>';
                }
                ?>
			</div>
			<?php
            if(!isset($_SESSION['isMod'])){
                header('Location: login.php');
            }else{
                if($_SERVER['REQUEST_METHOD']=='GET'){
                    if(!isset($_GET['id'])){
                        if(isset($_SESSION['id'])){
                            header('Location: profile.php?id='.$_SESSION['id']);
                        }else{
                            header('Location: index.php');
                        }
                    }else if(isset($_GET['id'])){
                        $jsonDB = json_decode(file_get_contents("files/61a428341f70fe7dd67f955fb43b3202/db.json"),true);
                        $id = $_GET['id'];
                        $lookup = true;
                        $allId = array();
                        $pseudo;$mail;$isMod;$isAdmin;
                        try {
                            $id = intval($id);
                        }catch(Exception $e) {
                            $lookup=false;
                        }
                        if($lookup){
                            foreach($jsonDB as $key => $name){
                                array_push($allId,$name['id']);
                            }
                            if(in_array($id,$allId)){
                                foreach($jsonDB as $key => $name){
                                    if($name['id'] == $id){
                                        $pseudo=$name['username'];
                                        $mail=$name['mail'];
                                        $isMod=$name['isMod'];
                                        if($isMod){$isMod="<span class='text-success'>Yes<span>";}else{$isMod="<span class='text-danger'>No<span>";}
                                        $isAdmin=$name['isAdmin'];
                                        if($isAdmin){$isAdmin="<span class='text-success'>Yes<span>";}else{$isAdmin="<span class='text-danger'>No<span>";}
                                        $note=$name['note'];
                                    }
                                }
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
                                            </ul>
                                        </div>
                                    </div>';
                            }else{
                                echo'<div class="text-center container">
                                    404 Not Found
                                  </div>
                                <script>window.onload = function(){setTimeout(() => {location.replace("profile.php?id='.$_SESSION['id'].'");}, 3000);}</script>';
                                http_response_code(404);        
                            }
                        }else{
                            echo'<div class="text-center container">
                                404 Not Found
                              </div>
                            <script>window.onload = function(){setTimeout(() => {location.replace("profile.php?id='.$_SESSION['id'].'");}, 3000);}</script>';
                            http_response_code(404);
                        }
                    }else{
                        header('Location: index.php');
                    }
                }else{
                    http_response_code(403);
                    die('Forbidden HTTP Method');
                }
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
