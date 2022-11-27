<!DOCTYPE html>
<html lang="en">
        <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=devide-width, initial-scale=1">
                <link href="css/bootstrap.min.css" rel="stylesheet">
                <script src="js/bootstrap.bundle.min.js"></script>
                <title>Admin Panel</title>
                <link rel="icon" type="image/x-icon" href="img/logo.png">
                <style>.button-flag-malo{background-color: #8c56ac;}</style>
        </head>
        <body class="bg-dark text-light">
                <main>
                        <div class="container">
                                <a href="index.php"><img src="img/logo.png" alt="logo" class="mw-50 mx-auto d-block img-fluid mt-2"></a>
                                <h2 class="text-center mt-2">Admin Panel</h2>
                        </div>
                        <div class="container mw-75">
                                <hr>
                        </div>
                        <?php
                        session_start();
                        if($_SERVER['REQUEST_METHOD']=='GET'){
                                if(isset($_COOKIE['ADMIN_COOKIE'])){
                                        if($_COOKIE['ADMIN_COOKIE']="e09c4bc5382d1e56f45c72208caae1a9"){
                                                echo '<div class="alert alert-success text-center container w-75" role="alert">Aaaaah you owned my admin panel... You will not go further but yet take this Flag #4: FMCTF{XSS_rUl3s_tH3_W0rld!!}</div>';
                                                echo '<div class="container">
                                                        <h4 class="text-center">Database Querier</h4>
                                                        <p class="text-center">As long as the 2nd field is set to \'disabled\' WHERE parameter will not be taken into account, only the SELECT field will.</p><br>

                                                        <form>
                                                                <div class="row g-0">
                                                                        <h5 class="col-sm text-center">SELECT</h5>
                                                                        <select class="col-sm" name="what" id="select-field">
                                                                                <option value="*">*</option>
                                                                                <option value="name">name</option>
                                                                                <option value="category">category</option>
                                                                                <option value="flag">flag</option>
                                                                        </select>
                                                                        <h5 class="col-sm-3 text-center">FROM challenges WHERE</h5>
                                                                        <select class="col-sm" name="where-param" id="select-field">
                                                                                <option value="disabled">disabled</option>
                                                                                <option value="*">*</option>
                                                                                <option value="name">name</option>
                                                                                <option value="category">category</option>
                                                                                <option value="flag">flag</option>
                                                                        </select>
                                                                        <h5 class=" text-center col-sm">=</h5>
                                                                        <input type="text" id="where-equals" name="where-equals" class="col-sm" value="">
                                                                        <button type="submit" class="btn button-flag-malo text-center text-white col-sm">Query</button>
                                                                </div>
                                                        </form>
                                                </div><br>';
                                                $mustQuery = false;
                                                $query;
                                                if(isset($_GET['what'])){
                                                        if((!isset($_GET['where-param'])) && (!isset($_GET['where-equals']))){
                                                                $param = addslashes($_GET['what']);
                                                                $query = "SELECT $param FROM challenges;";
                                                                echo("<p class='text-center'>Queried: ".$query."</p>");
                                                                $mustQuery = true;
                                                        }else if(isset($_GET['where-param']) && isset($_GET['where-equals'])){
                                                                if($_GET['where-param'] == "disabled"){
                                                                        $param = addslashes($_GET['what']);
                                                                        $query = "SELECT $param FROM challenges;";
                                                                        echo("<p class='text-center'>Queried: ".$query."</p>");
                                                                        $mustQuery = true;
                                                                }else{
                                                                        $param1 = addslashes($_GET['what']);
                                                                        $param2 = addslashes($_GET['where-param']);
                                                                        $param3 = addslashes($_GET['where-equals']);
                                                                        $query = "SELECT $param1 from challenges WHERE $param2 = '$param3'";
                                                                        echo("<p class='text-center'>Queried: ".$query."</p>");
                                                                        $mustQuery = true;
                                                                }
                                                        }else{
                                                                echo('<p class="text-center">Incorrect Query, please try again and specify correct parameters...');
                                                        }
                                                }
                                                if($mustQuery){
                                                        require_once('function_database.php');
                                                        $db = connectDB();
                                                        try{
                                                                $result = $db->query($query);
                                                                $results = $result->fetch_all(MYSQLI_ASSOC);
                                                                echo('<p class="text-center">Result:</p><br>');
                                                                echo'<div class="container w-75"><table class="table-striped table table-primary">';
                                                                $theadDone = false;
                                                                $startThead = "<thead><tr>";
                                                                $endThead = "</tr></thead>";
                                                                $startTbody = "<tbody>";
                                                                $endTbody = "</tbody>";
                                                                foreach($results as $row){
                                                                        if(!$theadDone){
                                                                                for($i=0;$i<count(array_keys($row));$i++){
                                                                                        $startThead=$startThead."<th scope='col'>".array_keys($row)[$i]."</th>";
                                                                                }
                                                                                $theadDone=true;
                                                                        }
                                                                        for($i=0;$i<count($row);$i++){
                                                                                if($i==0){
                                                                                        $startTbody=$startTbody."<tr><th scope='row'>".$row[array_keys($row)[$i]];
                                                                                }else if($i==count($row)-1){
                                                                                        $startTbody=$startTbody."<td>".$row[array_keys($row)[$i]]."</td></tr>";
                                                                                }else{
                                                                                        $startTbody=$startTbody."<td>".$row[array_keys($row)[$i]]."</td>";
                                                                                }
                                                                        }
                                                                }
                                                                echo $startThead;
                                                                echo $endThead;
                                                                echo $startTbody;
                                                                echo $endTbody;
                                                                echo'</table></div>';
                                                        }catch(Exception $e){
                                                                echo("<p class='text-center'>Query Failed $e, please try again</p>");
                                                        }
                                                }
                                        }else{
                                                http_response_code(403);
                                                die('Stop trying to fake, you\'re not admin');
                                        }
                                }else{
                                        http_response_code(403);
                                        die('You\'re not admin');
                                }
                        }else{
                                http_response_code(403);
                                die('Forbidden HTTP method');
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
                                echo('<br>');
                ?>
                        </div>
                </footer>
        </body>
</html>