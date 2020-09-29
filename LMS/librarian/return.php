<?php 
	include 'inc/connection.php';
	$id = $_GET["id"];
	$a  = date("d/m/Y");
    $fine = "50";
   
	$res3 = mysqli_query($link, "select * from issue_book where id=$id");

	while($row3=mysqli_fetch_array($res3)){
		$username = $row3["username"];
		$utype = $row3["utype"];
		$email = $row3["email"];
        $booksname = $row3["booksname"];
        $brdate = $row3["booksreturndate"];
	}
   
	if($a > $brdate){
        mysqli_query($link, "insert into finezone values('','$username','$utype','$email','$booksname','$fine')");
    }
   
	$res2 = mysqli_query($link, "update issue_book set booksreturndate='$a' where id=$id");
	$books_name="";
	$res2 = mysqli_query($link, "select  * from issue_book where id=$id");
	
    while($row=mysqli_fetch_array($res2)){
		$books_name = $row["booksname"];
	}

	mysqli_query($link, "update add_book set books_availability=books_availability+1 where books_name='$books_name'");
?>

 <script type="text/javascript">
 	window.location="issued-books.php";
 </script>


