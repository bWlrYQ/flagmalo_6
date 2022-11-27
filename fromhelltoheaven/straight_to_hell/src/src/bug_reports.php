<?php
session_start();
if($_SERVER['REQUEST_METHOD']=='POST'){
	if($_SESSION['isMod']==true || $_SESSION['isAdmin']==true){
		$url = $_POST['link'];
		if(!strlen($url)==0){
			$randInt = rand(100,5000);
			$fileName = "payload".$randInt;
			$url = str_replace("\n","",$url);
			file_put_contents('files/fa6543d2f5258fa531c07f7030a46756/'.$fileName,$url);
			print_r("Report: ".htmlspecialchars($url)." has been submited, please wait will we review it.");
		}else{
			echo("Report URL can't be empty...");
		}
	}else{
		http_response_code(403);
		die('Forbidden, you\'re not moderator');
	}
}else{
	http_response_code(403);
	die('Forbidden');
}
