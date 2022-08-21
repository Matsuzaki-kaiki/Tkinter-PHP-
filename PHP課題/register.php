<?php
    $price = $_GET["price"];
    $name_ = $_GET["name_"];
    $user_ID = $_GET["user_id"];
    $size = $_GET["size"];
    $start = $_GET["start"];
    
    try{
        // データベースに接続
        $pdo = new PDO(
            // ホスト名、データベース名
            'mysql:host=localhost;dbname=order;',
            // ユーザー名
            'root',
            // パスワード
            '',
            // レコード列名をキーとして取得させる
            [ PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC ]
        );
 
        // SQLクエリ作成（よくない例）
        // $query = "SELECT * FROM user WHERE user_id = \'' . $user_id . '\' AND password = \ '' . $password .'\\ ;
        $query = 'INSERT INTO products (name_, price) VALUES (:name_data, :price_data)';
        // SQL文をリセット
        //$stmt = $pdo->prepare('SELECT * FORM user');
        $stmt = $pdo->prepare($query);
        // SQL文を実行

        //バインド 変換
        //$stmt->bindParam(':password', $password);
        $stmt->bindParam(':price_data', $price, PDO::PARAM_INT);
        $stmt->bindParam(':name_data', $name_);

        $stmt->execute(); 

        // ループして1レコードずつ取得
        /*foreach ($stmt as $row) {
            echo ($row["user_id"]);
            echo ", ";
            echo($row["name"]);
            echo ", ";
            echo($row["password"]);
            echo ", ";
            echo($row["email"]);
            echo "<BR>";
        }   */


        require_once 'select.php';


        } catch (PDDException $e) {
            require_once 'exception_tp1.php';
            echo $e->getMessage();
            exit();
        
        } 
        require_once 'select.php';

?>
