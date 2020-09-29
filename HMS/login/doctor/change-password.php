<?php
session_start();
error_reporting(0);
include('include/config.php');
include('include/checklogin.php');
check_login();
date_default_timezone_set('Asia/Kolkata');// change according timezone
$currentTime = date( 'd-m-Y h:i:s A', time () );
if(isset($_POST['submit']))
{
$sql=mysqli_query($con,"SELECT password FROM  doctors where password='".md5($_POST['cpass'])."' && id='".$_SESSION['id']."'");
$num=mysqli_fetch_array($sql);
if($num>0)
{
 $con=mysqli_query($con,"update doctors set password='".md5($_POST['npass'])."', updationDate='$currentTime' where id='".$_SESSION['id']."'");
$_SESSION['msg1']="Password Changed Successfully !!";
}
else
{
$_SESSION['msg1']="Old Password not match !!";
}
}
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Doctor  | change Password</title>
		
		<link href="http://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" rel="stylesheet" type="text/css" />
	
	    <link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="vendor/themify-icons/themify-icons.min.css">
		<link rel="stylesheet" href="assets/css/styles.css">
		<link rel="stylesheet" href="assets/css/plugins.css">
		<link rel="stylesheet" href="assets/css/themes/theme-1.css" id="skin_color" />

<script type="text/javascript">
function valid()
{
if(document.chngpwd.cpass.value=="")
{
alert("Current Password Filed is Empty !!");
document.chngpwd.cpass.focus();
return false;
}
else if(document.chngpwd.npass.value=="")
{
alert("New Password Filed is Empty !!");
document.chngpwd.npass.focus();
return false;
}
else if(document.chngpwd.cfpass.value=="")
{
alert("Confirm Password Filed is Empty !!");
document.chngpwd.cfpass.focus();
return false;
}
else if(document.chngpwd.npass.value!= document.chngpwd.cfpass.value)
{
alert("Password and Confirm Password Field do not match  !!");
document.chngpwd.cfpass.focus();
return false;
}
return true;
}
</script>


</head>
	<body>
	<div id="app">
		<div class="sidebar app-aside" id="sidebar">
				<div class="sidebar-container perfect-scrollbar">
					<nav>
					
						<div class="navbar-title">
							<span>Main Navigation</span>
						</div>
					
						<ul class="main-navigation-menu">
					
							<li>
								<a href="dashboard.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-home"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Dashboard </span>
										</div>
									</div>
								</a>
							</li>
							

							<li>
								<a href="appointment-history.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-list"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Appointment History </span>
										</div>
									</div>
								</a>
							</li>
					
							<li>
								<a href="javascript:void(0)">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-user"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Patients </span><i class="icon-arrow"></i>
										</div>
									</div>
								</a>
								<ul class="sub-menu">
									
									<li>
										<a href="add-patient.php">
											<span class="title"> Add Patient</span>
										</a>
									</li>
									<li>
										<a href="manage-patient.php">
											<span class="title"> Manage Patient </span>
										</a>
									</li>
									
								</ul>
								</li>




                             <li><a href="search.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-search"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Search </span>
										</div>
									</div>
								</a>
							</li>


						</ul>
						
					</nav>
					</div>
			</div>
<?php error_reporting(0);?>
<header class="navbar navbar-default navbar-static-top">
					<!-- start: NAVBAR HEADER -->
					<div class="navbar-header">

						<a href="#" class="sidebar-mobile-toggler pull-left hidden-md hidden-lg" class="btn btn-navbar sidebar-toggle" data-toggle-class="app-slide-off" data-toggle-target="#app" data-toggle-click-outside="#sidebar">
							<i class="ti-align-justify"></i>
						</a>

						<a class="navbar-brand" href="#">
							<h2 style="padding-top:20% ">HMS</h2>
						</a>
						
						<a href="#" class="sidebar-toggler pull-right visible-md visible-lg" data-toggle-class="
						app-sidebar-closed" data-toggle-target="#app">
							<i class="ti-align-justify"></i>
						</a>
						
						<a class="pull-right menu-toggler visible-xs-block" id="menu-toggler" data-toggle="collapse" href=".navbar-collapse">
							<span class="sr-only">Toggle navigation</span>
							<i class="ti-view-grid"></i>
						</a>
					</div>
					
					<div class="navbar-collapse collapse">
						<ul class="nav navbar-right">
					
								<li  style="padding-top:2% ">
								<h2>Hospital Management System</h2>
							</li>
						
						
							
						
							<li class="dropdown current-user">
								<a href class="dropdown-toggle" data-toggle="dropdown">
									<img src="assets/images/doctor-icon-vector-11004500.jpg" > 
									<span class="username">
									<?php $query=mysqli_query($con,"select fullname from doctorsignup where id='".$_SESSION['id']."'"); 
                               while($row=mysqli_fetch_array($query))
                             {
                                 	echo $row['fullname'];
                              }
									?> 
							<i class="ti-angle-down"></i></i></span></a>

								<ul class="dropdown-menu dropdown-dark">
									
									<li>
										<a href="edit-profile.php">
											My Profile
										</a>
									</li>
								
									<li>
										<a href="change-password.php">
											Change Password
										</a>
									</li>
									
									<li>
										<a href="logout.php">
											Log Out
										</a>
									</li>
								</ul>
							</li>


								</ul>
					
						<div class="close-handle visible-xs-block menu-toggler" data-toggle="collapse" 
						href=".navbar-collapse">
							<div class="arrow-left"></div>
							<div class="arrow-right"></div>
						</div>
						
							</div>
				
						</header>

				<div class="main-content" >
					<div class="wrap-content container" id="container">

						<section id="page-title">
							<div class="row">
								<div class="col-sm-8">
									<h1 class="mainTitle">Doctor | Change Password</h1>
																	</div>
							</div>

						</section>

						<div class="container-fluid container-fullw bg-white">
							<div class="row">
								<div class="col-md-12">
									
									<div class="row margin-top-30">
										<div class="col-lg-8 col-md-12">
											<div class="panel panel-white">

												<div class="panel-heading">
													<h5 class="panel-title">Change Password</h5>
												</div>

												<div class="panel-body">
								<p style="color:red;"><?php echo htmlentities($_SESSION['msg1']);?>
								<?php echo htmlentities($_SESSION['msg1']="");?></p>	
													<form role="form" name="chngpwd" method="post" onSubmit="return valid();">
														<div class="form-group">
															<label for="exampleInputEmail1">Current Password</label>
							
							<input type="password" name="cpass" class="form-control"  placeholder="Enter Current Password" required>
														</div>
							<br>
														<div class="form-group">
															<label for="exampleInputPassword1">New Password</label>

					<input type="password" name="npass" class="form-control"  placeholder="New Password"></div>
														<br>
                                                         <div class="form-group">
													<label for="exampleInputPassword1">Confirm Password</label>

						<input type="password" name="cfpass" class="form-control"  placeholder="Confirm Password">
														</div>
														
														<br>
														
								<button type="submit" name="submit" class="btn btn-o btn-primary">Submit</button>
								
													</form>
												</div>
											</div>
										</div>
											
											</div>
										</div>
									
								</div>
							</div>
					</div>
			</div>
	<hr>		</div>
		
		<script src="vendor/jquery/jquery.min.js"></script>
		<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
		<script src="vendor/jquery-cookie/jquery.cookie.js"></script>	
		<script src="assets/js/main.js"></script>
		<script src="assets/js/form-elements.js"></script>
          <script>
			jQuery(document).ready(function() {
				Main.init();
				FormElements.init();
			});
		</script>
	</body>
</html>
