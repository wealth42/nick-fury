<?php 
	include 'inc/connection.php';
	$id = $_GET["id"];
	$a  = date("d/m/Y");
    $fine = "50";
	
	$res4 = mysqli_query($link, "select * from t_issuebook where id=$id");
	
	while($row4=mysqli_fetch_array($res4)){
		$username = $row4["username"];
		$utype = $row4["utype"];
		$email = $row4["email"];
        $booksname = $row4["booksname"];
        $brdate = $row4["booksreturndate"];
	}
	
	if($a > $brdate){
        mysqli_query($link, "insert into finezone values('','$username','$utype','$email','$booksname','$fine')");
    }
	
	$res = mysqli_query($link, "update t_issuebook set booksreturndate='$a' where id=$id");
	$books_name="";
	$res = mysqli_query($link, "select  * from t_issuebook where id=$id");

	while($row=mysqli_fetch_array($res)){
		$books_name = $row["booksname"];
	}
	
	mysqli_query($link, "update add_book set books_availability=books_availability+1 where books_name='$books_name'");
?>

 <script type="text/javascript">
 	window.location="issued-books.php";
 </script>

