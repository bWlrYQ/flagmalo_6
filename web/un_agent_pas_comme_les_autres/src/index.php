<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Un agent pas comme les autres</title>
</head>
<body>
	<?php
	if (str_contains($_SERVER['HTTP_USER_AGENT'], "Nokia 3310") && str_contains($_SERVER['HTTP_USER_AGENT'], "Chrome/60.0.3110.70")) {
		$flag = fopen("flag.txt", "r");
		echo "<h3>Flag : ". fread($flag, 1000) ."</h3>";
		fclose($flag);
	} else {
		echo "<h3>Accès interdit : vous n'êtes toujours pas revenu dans le passé &#128549 !</h3>";
	}
	?>
</body>
</html>