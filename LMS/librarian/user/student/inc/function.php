<?php
	if (isset($_POST["submit"])) {
		$name = $_POST["name"];
		$username = $_POST["username"];                   
		$password = $_POST["password"];
		$email = $_POST["email"];
		$phone = $_POST["phone"];
		$sem = $_POST["sem"];
		$dept = $_POST["dept"];
		$regno = $_POST["regno"];
		$address = $_POST["address"];
		$photo = "upload/avatar.jpg";
		$utype = "student";
		
		$sql_u= mysqli_query($link,"select * from std_registration where username= '$username'");
		$sql_e= mysqli_query($link,"select * from std_registration where email= '$email'");
		$sql_p= mysqli_query($link,"select * from std_registration where phone= '$phone'");
		$sql_r= mysqli_query($link,"select * from std_registration where regno= '$regno'");
        
		if(mysqli_num_rows($sql_u) > 0){
			$error_uname = "Username already exist";
		}
       
        elseif(mysqli_num_rows($sql_e) > 0){
            $error_email = "Email already exist";
        }
		elseif(mysqli_num_rows($sql_p) > 0){
            $error_phone = "Phone already registered";
        }
		elseif(mysqli_num_rows($sql_r) > 0){
            $error_reg = "This regno already registered";
        }
		elseif(strlen($username) < 6 ){
            $error_ua ="<b>Username too short !</b> <span>Your username must be more than 6 character </span>";
        }
		elseif(strlen($password) < 6 ){
            $error_pw ="<b>Password too short !</b> <span>Your password must be more than 6 character </span>";
        }
		elseif (filter_var($email, FILTER_VALIDATE_EMAIL)== false) {
				$e_msg = "<strong>Error ! </strong> <span>Email Address Not Valid </span>";
		} 
		else{
		    $vkey = md5(time().$username);
			$password = md5($password);
		    $insert = mysqli_query($link, "insert into std_registration values('','$name','$username','$password','$email','$phone','$sem','$dept','$regno','$address','$utype','$photo','pending','$vkey','no')");
			echo "<div class='alert alert-success'>
					<strong style='color:#333'>
					<br>
					<h4>
					<center> Registered successfully !</center>
					</h4>
					</strong>
					<br>
				</div>";
		}
	}
?>

