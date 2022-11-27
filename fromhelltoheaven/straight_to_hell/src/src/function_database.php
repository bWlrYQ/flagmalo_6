<?php
function connectDB(){
    $db = new MySQLi("10.5.0.3", "root", "l4RavYAn2zh0uJq9gCfbOHS4m", "StraightToHell");
    return $db;
}
?>