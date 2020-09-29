<?php 
     session_start();
    if (!isset($_SESSION["teacher"])) {
        ?>
            <script type="text/javascript">
                window.location="login.php";
            </script>
        <?php
    }
    $page = 'rbook';
    include 'inc/header.php';
    include 'inc/connection.php';
 ?>
 
	<!-- For Dropdown of MY PROFILE -->
	<script src="inc/js/jquery-2.2.4.min.js"></script>
	<script src="inc/js/custom.js"></script>
	
	<!--dashboard area-->
	<div class="dashboard-content">
		<div class="dashboard-header">
			<div class="container">
				<div class="row">
					<div class="right">	
					<a href="dashboard.php">Home</a>
					</div>
					
					<div class="right">
					<a href="profile.php">Profile</a>
					</div>
					
					<div class="right">
					<a href="logout.php">logout</a>
					</div>
				</div>
				<div class="st-issuedBook">
                     <?php
						
						$res5 = mysqli_query($link, "select * from t_registration where username='$_SESSION[teacher]' ");
						while($row5 = mysqli_fetch_array($res5)){
                           $name      = $row5['name'];                    
                           $username  = $row5['username'];
                           $email     = $row5['email'];
                           $phone     = $row5['phone']; 
                           $utype     = $row5['utype'];
						}
                    ?>
					<form action="" method="post" class="issue-content">
						<table class="table table-bordered table-striped">
						<?php 
							if (isset($_POST["submit"])){
								$bname = $_POST['bname'];
								$burl = $_POST['burl'];
								
								if ($bname == "" | $burl =="" ) {
									echo "<span style='color: red;'><b>Error !</b> Feild mustn't be empty</span>";
								}else{
									$sql = mysqli_query($link, "insert into request_books values('','$name','$username','$email','$utype','$bname','$burl','no') ");
									if($sql){
										echo "<span style='color: green;'><b>Success !</b> Books request send successfully.</span>";
									}
								}
								
							}
						?>
							<tr>
                                <td>
                                  <input type="text" class="form-control" name="name" value="<?php echo $name; ?>" disabled>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                  <input type="text" class="form-control" name="username" value="<?php echo $username; ?>" disabled>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                  <input type="text" class="form-control bdr" name="bname" value="" placeholder="Request book name">
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <input type="text" class="form-control" value="student" name="<?php echo $utype; ?>" disabled>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                  <input type="text" class="form-control" name="email" value="<?php echo $email; ?>" disabled>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                  <input type="text" class="form-control bdr" name="burl" value="" placeholder="Books url">
                                </td>
                            </tr>
                            
                        </table>
                        <input type="submit" name="submit" value="Send Request" class="btn">
					</form>
                     
				</div>
			</div>					
		</div>
	</div>
	