<?php
	if (isset($_POST["submit"])) {
		$name = $_POST["name"];
		$username = $_POST["username"];                   
		$password = $_POST["password"];
		$email = $_POST["email"];
		$phone = $_POST["phone"];
		$lecturer = $_POST["lecturer"];
		$idno = $_POST["idno"];
		$address = $_POST["address"];
		$photo = "upload/avatar.jpg";
		$utype = "teacher";
        
		$sql2_u= mysqli_query($link,"select * from t_registration where username= '$username'");
        $sql2_e= mysqli_query($link,"select * from t_registration where email= '$email'");
        $sql2_p= mysqli_query($link,"select * from t_registration where phone= '$phone'");
		
        if(mysqli_num_rows($sql2_u) > 0){
			$error_uname = "Username already exist";
		}elseif(mysqli_num_rows($sql2_e) > 0){
            $error_email = "Email already exist";
        }elseif(mysqli_num_rows($sql2_p) > 0){
            $error_phone = "Phone already registered";
        }elseif(strlen($username) < 6){
            $error_ua ="<b>Username too short !</b> <span>Your username must be more than 6 character </span>";
        }else{
            $vkey = md5(time().$username);
			$password = md5($password);
            $insert = mysqli_query($link, "insert into t_registration values('','$name','$username','$password','$lecturer','$email','$phone','$idno','$address','$utype','$photo','pending','$vkey','no')");
		}
	}
?>