<?php
set_include_path('/proc');
if($_SERVER['REQUEST_METHOD'] == 'GET'){
    if(!isset($_GET['view'])){
        include("top.html");
        include("home.html");
        include("bottom.html");
    }else{
        include("top.html");
        $req = urldecode($_GET['view']);
        if(strlen($req)>0){
            if(is_readable($req)){
                if(preg_match("/(etc)|(var)|(mnt)|(dev)|(self\/fd)|(php)|(filter)/m",$req)){
                    echo("<p class='text-center'>Hey, don't try to hack our website 😡.</p>");
		    include("bottom.html");
                    http_response_code(403);
                    die();
                }else{
                    include($req);
                }
            }else{
                echo("<p class='text-center'>404 Not Found</p>");
		include("bottom.html");
                http_response_code(404);
                die();
            }
        }else{
            include("home.html");
        }
        include("bottom.html");
    }
}else{
    http_response_code(403);
    die('Forbidden');
}
?>
