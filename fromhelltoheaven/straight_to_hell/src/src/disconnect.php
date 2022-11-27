<?php
session_start();
?>
<?php
session_unset();
session_destroy();
if(isset($_COOKIE['ADMIN_COOKIE'])){
	setcookie('ADMIN_COOKIE', null, time()-3600);
}
header('Location: login.php?disconnect=yes');
exit;
?>
