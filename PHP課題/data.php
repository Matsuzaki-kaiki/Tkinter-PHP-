<DOCTYPE html>
<html>
  
<head>
<meta charset="utf-8">
  <title></title>
</head>
</div>
<div align="center" class="body">
<body>
  <?php
      $user_ID = $_GET["user_id"];
  ?>

  <form action="data.php" method="get">

    <p>
    <label for="price">金額</label>
    <input type="int" name="price" placeholder="price"/>
    </p>

    <p>
    <label for="name_">商品名</label>
    <input type="text" name="name_"  placeholder="name_"/>
    </p>

    <input type="hidden" name="user_id" value="<?php echo $user_ID; ?>">
    <input type="hidden" name="start", value="0">
    <input type="hidden" name="size", value="5">
    <input type="submit" name="sunmitBtn", value="登録する">

   </form>
  </body>
 </div>
 </html>