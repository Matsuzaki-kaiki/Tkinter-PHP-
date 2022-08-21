<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">

    <title></title>
</head>
<body>
<p>ようこそ <?php echo $user_name; ?> さん</p>

<?php
    $count = $start;
    foreach($result as $row) {
    $count += 1;
    echo'<p>';
    echo $count;
    echo ',  ';
    echo $row["name_"];
    echo ',  \\';
    echo $row["price"];
    echo '</p>';

    echo '<form action = "update.php" mechod="get">';
    echo '    <input type="hidden" name="user_name" value="<?php echo $user_name; ?>">';
    echo '    <input type="hidden" name="user_id" value="<?php echo $user_ID; ?>">';
    echo '    <input type="submit" name="submitBtn" value="更新">';
    echo '</form>';
    }
?>


<form action = "register.php" mechod="get">
    <input type="hidden" name="user_id" value="<?php echo $user_ID; ?>">
    <input type="hidden" name="start" value="0">
    <input type="hidden" name="size" value="5">
    <input type="submit" name="submitBtn" value="新規">
</form>


 <form action = "select.php" mechod="get">
    <input type="hidden" name="user_id" value="<?php echo $user_ID; ?>">
    <input type="hidden" name="start" value="  
<?php
     $next = $start - 5;
     if ($next < 0) {
         $next = 0;
     }
     echo $next;
?>
     ">
     <input type="hidden" name="size" value="<?php echo $size; ?>">
     <input type="submit" name="submitBtn" value="前へ">
 </form>

 <form action="select.php" method="get">
    <input type="hidden" name="user_id" value="<?php echo $user_ID;?>">
    <input type="hidden" name="size" value="<?php echo $size; ?>">
    <input type="hidden" name="start" value="
<?php
     $next = $start + 5;
     echo $next;
?>    
    ">
    <input type="submit" name="submitBtn" value="次へ">
 </form>


</p>
</body>
</html>