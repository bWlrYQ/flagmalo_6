<?php
echo'<table class="table-striped table boutton-flag-malo">
    <thead>
        <tr>';
            for($i=0;$i<count($row);i++){
                echo("<th scope='col'> Column".$row[i]."</th>");
            }
        echo'</tr>
    </thead>
    <tbody>';
            for($i=0;$i<count($row);i++){
                echo'<tr>';
                for($q=0;$q<count($row);q++){
                    echo'<th scope="row">'.$row[i].'</th>';
                }
                echo'</tr>';
            }
    echo'</tbody>
</table>';
?>