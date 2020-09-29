<?php 
     session_start();
    if (!isset($_SESSION["username"])) {
        ?>
            <script type="text/javascript">
                window.location="login.php";
            </script>
        <?php
    }
    include 'inc/header.php';
    include 'inc/connection.php';
    $rdate = date("d/m/Y", strtotime("+30 days"));
 ?>
 <html>
 <head></head>
 <body>
	<!--dashboard area-->
	<div class="dashboard-content">
		<div class="dashboard-header">
			<div class="container">
				<div class="row">
					
						<div class="right">	
							<a href="dashboard.php">home</a>
						</div>
						
						<div class="right">
						<a href="profile.php">Profile</a>
						</div>
						
						<div class="right">
						<a href="logout.php">logout</a>
						</div>
				</div>
				<div class="issueBook">
					<div class="row">
						<div class="col-md-8">
							<div class="issue-wrapper">
								<form action="" class="form-control" method="post" name="reg">
									<table class="table">
											<h5>Issue book to a student </h5>
										<tr>
											<td>
												
												<select name="reg"  class="form-control">
												
													 <?php 
                                                        $res= mysqli_query($link, "select regno from std_registration");
                                                        while($row=mysqli_fetch_array($res)){
                                                            echo "<option>";
                                                            echo $row["regno"];
                                                            echo "</option>";
                                                        }
                                                    ?>
												</select>
											</td>
											<td>
												<input type="submit" class="btn btn-info" value="select" name="submit1">
											</td>
										</tr>
									</table>
                                    <?php 
                                    if (isset($_POST["submit1"])) {
                                       $res5 = mysqli_query($link, "select * from std_registration where regno='$_POST[reg]' ");
                                       while($row5 = mysqli_fetch_array($res5)){
                                           $name      = $row5['name'];                    
										   $username  = $row5['username'];
                                           $sem       = $row5['sem'];
                                           $dept      = $row5['dept'];
                                           $email     = $row5['email'];
                                           $phone     = $row5['phone'];
                                           $utype     = $row5['utype'];
                                           $regno     = $row5['regno'];
                                           $_SESSION["utype"]     = $utype;
                                           $_SESSION["regno"]     = $regno;
                                           $_SESSION["susername"] = $username;
                                       }
                                    ?>
									<table class="table table-bordered table-center">
                                        
                                        
                                        <tr>
                                            <td>
                                               Name : <input type="text" class="form-control" name="name" value="<?php echo $name; ?>" > 
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                               Username :<input type="text" class="form-control" name="username"  value="<?php echo $username; ?>" > 
                                            </td>
                                        </tr>
                                         <tr>
                                            <td>
                                               <input type="text" class="form-control" name="dept"  value="<?php echo $dept; ?>"> 
                                            </td>
                                        </tr>
										<tr>
                                            <td>
                                               <input type="text" class="form-control" name="sem"  value="<?php echo $sem; ?>" > 
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                               Phone :<input type="text" class="form-control" name="phone"  value="<?php echo $phone; ?>"> 
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                               Email :<input type="text" class="form-control" name="mail"  value="<?php echo $email; ?>" > 
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <select name="booksname" class="form-control">
                                                    <?php 
                                                            $res= mysqli_query($link, "select books_name from add_book");
                                                            while($row=mysqli_fetch_array($res)){
                                                                echo "<option>";
                                                                echo $row["books_name"];
                                                                echo "</option>";
                                                            }
                                                        ?>
                                                </select>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                              Issue date : <input type="text" class="form-control" name="booksissuedate"  value="<?php echo date("d/m/Y"); ?>"> 
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                              Return date : <input type="text" class="form-control" name="booksreturndate"  value="<?php echo $rdate; ?>" > 
                                            </td>
                                        </tr>
                                        
                                        <tr>
                                            <td>
                                               <input type="submit" name="submit2" class="btn btn-info" value="Issue Book"> 
                                            </td>
                                        </tr>
                                    </table>
                                  <?php
                                }

                            ?>
                                </form>
                                <?php
                                    if (isset($_POST["submit2"])) {
                                      $qty=0;
                                      $res= mysqli_query($link, "select * from add_book where books_name='$_POST[booksname]' ");
                                       while($row = mysqli_fetch_array($res)){
                                          $qty= $row["books_availability"];
                                       }
                                       if ($qty==0) {
                                          ?>
                                            <div class="alert alert-danger col-lg-6 col-lg-push-3">
                                            <strong style="">This book is not available.</strong>
                                            </div>
                                          <?php  
                                       }
                                       else{
                                          mysqli_query($link, "insert into issue_book values('','$_SESSION[utype]','$_SESSION[regno]','$_POST[name]','$_POST[sem]','$_POST[dept]','$_POST[phone]','$_POST[mail]','$_POST[booksname]','$_POST[booksissuedate]','$_POST[booksreturndate]','$_SESSION[susername]') ");
                                          mysqli_query($link, "update add_book set books_availability=books_availability-1 where books_name='$_POST[booksname]'");
                                          ?>
                                              <script type="text/javascript">
                                                  alert("books issued successfully");
                                                  window.location.href=window.location.href;
                                              </script>
                                        <?php
                                        }
                                    }
                                 ?>
							</div>
						</div>
					</div>
				</div>
			</div>					
		</div>
	</div>
</body>
	<?php 
		include 'inc/footer.php';
	 ?>
</html>